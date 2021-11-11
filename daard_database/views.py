from .serializers import DiseaseLibrary, BoneChangeBoneProxySerializer, \
    BoneSerializer, DiseaseCaseSerializer, DiseaseSerializer
from django.db.models import Q
from .models import DiseaseCase, BoneChangeBoneProxy, Bone
from rest_framework.response import Response
import requests
from rest_framework import status
from .choices import forms
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.generic import TemplateView
import logging
logger = logging.getLogger("geonode")
from slugify import slugify

class BonesImageView(TemplateView):
    template_name = 'daard_bones.html'

# Disease Case
class DiseaseCaseViewset(viewsets.ModelViewSet):
    serializer_class = DiseaseCaseSerializer
    queryset = DiseaseCase.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=disease']
    http_method_names = ['get', 'post', 'head']
    permission_classes = [IsAuthenticatedOrReadOnly]


class DiseaseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    serializer_class = DiseaseSerializer
    queryset = DiseaseLibrary.objects.all()


    def get_queryset(self):
        queryset = DiseaseLibrary.objects.all()
        search_bones = self.request.query_params.get('bone__name__in')
        search_technics = self.request.query_params.get('technic__name__in')
        search_age = self.request.query_params.get('search_age')

        # Filter by Bone
        # http://localhost:8000/api/disease-search/?bone__name__in=Right%20Ribs,Splanchnocranium
        if search_bones is not None:
            search_bones.strip()
            search_bones = search_bones.split(',')
            q = Q()
            for bone in search_bones:
                q = q | Q(anomalies__bone__name__contains=bone)
            queryset = queryset.filter(q)

        # Filter by Bone
        # http://localhost:8000/api/disease-search/?bone__name__in=Left&technic__name__in=Micro
        if search_technics is not None:
            search_technics.strip()
            search_technics = search_technics.split(',')
            q = Q()
            for technic in search_technics:
                q = q | Q(anomalies__technic__name__contains=technic)
            queryset = queryset.filter(q)

        # Filter by Age
        # http://127.0.0.1:8000/api/disease-search/?search_age=subadults,adults&fields=id,name,adults,subadults
        if search_age is not None:
            search_age.strip()
            search_age = search_age.split(',')

            q = Q()
            for age in search_age:
                term = {age.lower(): True}
                q = q | Q(**term)
            queryset = queryset.filter(q)

        # return the filtered queryset
        return queryset


class BoneChangeBoneProxyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    serializer_class = BoneChangeBoneProxySerializer

    def get_queryset(self):
        queryset = BoneChangeBoneProxy.objects.all()
        search_bone = self.request.query_params.get('bone__id__in')

        # Filter by Bone
        # http://localhost:8000/api/bone-change-to-bones/?bone__id__in=1,2
        if search_bone is not None:
            search_bone = search_bone.rstrip(',')
            search_bone = search_bone.split(',')
            q = Q()
            q = Q(bone__pk__in=search_bone)
            queryset = queryset.filter(q)
        return queryset

    def get_bone(self):
        return


class ChangeSearchViewSet(viewsets.ViewSet):
    # http://localhost:8000/api/daard/bone-change-search/?q=Dwarfismus&bone_ids=27,24
    def list(self, request):
        # url parameter
        q = self.request.query_params.get('q')
        if not q.isdecimal():
            return Response({})
        search_bone = self.request.query_params.get('bone_ids')
        if q is None or search_bone is None:
            return Response({'body': '?q=<disease_name>&bone_ids=<1,2,3> needed for search'},
                            status=status.HTTP_400_BAD_REQUEST)
        search_bone = search_bone.split(',')
        search_bone = list(filter(bool, search_bone))

        # model and serializer
        bone_changes = BoneChangeBoneProxy.objects.filter(anomalies__id=q)
        bone_changes_serializer = BoneChangeBoneProxySerializer(bone_changes, many=True)
        bone_change_relations = bone_changes_serializer.data

        # fill dict with technics
        # Todo: refactor model and for loops to be more pythonic
        all_technics = {disease["technic"]["name"]: {} for disease in bone_change_relations}
        # all_technics = {"Radiography": {}, "Macroscopy": {}, "Microscopy": {}}

        # create dict of technics and bones
        for disease in bone_change_relations:
            disease_as_dict = dict(disease)
            for current_bone in disease_as_dict["bone"]:
                if str(current_bone["id"]) in search_bone:
                    all_technics[disease["technic"]["name"]][current_bone["id"]] = {
                        "id": current_bone["id"],
                        "name": slugify(current_bone["name"]),
                        "name_complete": f'{current_bone["name"]} ({current_bone["section"]})',
                        "section": current_bone["section"],
                        "options": []
                    }

        # add bone changes to bones
        for disease in bone_change_relations:
            disease_as_dict = dict(disease)
            for current_bone in disease_as_dict["bone"]:
                if str(current_bone["id"]) in search_bone:
                    all_technics[disease["technic"]["name"]][current_bone["id"]]["options"].append(disease["bone_change"])

        if (any(technic for technic in all_technics.values())):
            all_technics = {k: v for (k, v) in all_technics.items() if v}
            return Response(all_technics)
        else:
            return Response({})



class FormularConfig(viewsets.ViewSet):
    def list(self, request):

        # Read Bones from Model
        bones = Bone.objects.filter(parent=None).prefetch_related("options").all()
        bone_serializer = BoneSerializer(bones, many=True)
        all_bones = bone_serializer.data
        bone_sections = {}

        for bone in all_bones:
            bone_sections[bone["section"]] = []

        for bone in all_bones:
            bone = dict(bone)
            bone["name_complete"] =  f"{bone['name']} ({bone['section']})"
            bone["type"] = "selectfield" if bone["options"] else "Label"
            bone["svgid"] = bone["svgid"] if bone["svgid"] else ""
            bone_sections[bone["section"]].append(bone)

            bone_sections[bone["section"]].append(
                {"name": f"{bone['name']}_amount",
                 "id": bone["id"],
                 "section": bone["section"],
                 "type": "selectfield",
                 "options": [
                     {"name":">75%","value":">75%"},
                     {"name":"<75%","value":"<75%"},
                     {"name":"absent","value":"ABSENT"},
                     {"name":"unknown","value":"UNKNOWN"}
                 ]
                 })

        # build forms from choices.py
        all_forms = {}
        for step in forms:
            for objects in forms[step]:
                key_values = []

                if "values" in forms[step][objects]:
                    forms[step][objects]['options'] = forms[step][objects].pop("values")
                    forms[step][objects]['options'] = [{"name": i[0], "value": i[1]} for i in forms[step][objects]['options']]
                if step != "general":
                    all_forms[step] = forms[step]

        # all_forms["inventory"] = all_bones
        all_forms["inventory"] = bone_sections

        # allow reduction of output based on key
        filter_by_key = self.request.query_params.get('filter_by_key')
        if filter_by_key is not None:
            all_forms = all_forms.get(filter_by_key)

        return Response(
            all_forms
            # + all_bones
        )


class SiteServiceAPI(viewsets.ViewSet):
    def list(self, request):
        q = self.request.query_params.get('q')
        task = self.request.query_params.get('task')

        if q is None or task is None:
            return Response({'body': '?q=<term> needed for search; &task=<suggestion|site> needed for search'},
                            status=status.HTTP_400_BAD_REQUEST)

        if task != "site":
            external_api_response = requests.get(f'https://gazetteer.dainst.org/suggestions?field=nameSuggestions&queryId=2&lang=en&text={q}')
        else:
            external_api_response = requests.get(
                f'https://gazetteer.dainst.org/search.json?q={q}&fq=_exists_:prefLocation.'
                f'coordinates&limit=1&type=&pretty=true')

        external_api_response_json = external_api_response.json()
        if task == "site":
            if not external_api_response_json["result"]:
                return Response(external_api_response_json, status=external_api_response.status_code)

            site = external_api_response_json["result"][0]
            prefName = site["prefName"]

            # set preName to english if present
            if "name" in site.keys():
                all_names_in_langauges = {c_lang["language"]: (c_lang) for c_lang in site["names"]}
                if "eng" in all_names_in_langauges:
                    prefName = all_names_in_langauges["eng"]
                else:
                    prefName = site["prefName"]

            return_arr = {"values": []}
            return_arr["values"].append({
                "site": prefName,
                "names": site["names"] if "names" in site.keys() else [],
                "position": site["prefLocation"]["coordinates"],
                "gazId": site["gazId"],
                "gaz_link": site["@id"],
                "types": site["types"]
            })

            external_api_response_json = return_arr

        return Response(external_api_response_json, status=external_api_response.status_code)


class ChronologyServiceAPI(viewsets.ViewSet):
    def list(self, request):
        q = self.request.query_params.get('q')

        if q is None:
            return Response({'body': '?q=<term> needed for search'}, status=status.HTTP_400_BAD_REQUEST)
        return_arr = {"values": set()}
        external_api_response = requests.get(f'https://chronontology.dainst.org/data/period?q={q}&size=500')
        external_api_response_json = external_api_response.json()
        for res in external_api_response_json["results"]:
            if "en" in res["resource"]["names"]:
                english_terms = ", ".join(res["resource"]["names"]["en"])
                return_arr["values"].add(english_terms)
        return_arr["values"] = sorted(return_arr["values"])
        return Response(return_arr, status=external_api_response.status_code)
