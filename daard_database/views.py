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
from rest_framework.permissions import IsAuthenticated


# Disease Case
class DiseaseCaseViewset(viewsets.ModelViewSet):
    serializer_class = DiseaseCaseSerializer
    queryset = DiseaseCase.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=disease']
    http_method_names = ['get', 'post', 'head']
    permission_classes = [IsAuthenticated]


class DiseaseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    serializer_class = DiseaseSerializer
    queryset = DiseaseLibrary.objects.all()

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name',]

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = '__all__'

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
                print(age)
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
            print(search_bone)
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
        search_bone = self.request.query_params.get('bone_ids')
        if q is None or search_bone is None:
            return Response({'body': '?q=<disease_name>&bone_ids=<1,2,3> needed for search'},
                            status=status.HTTP_400_BAD_REQUEST)
        search_bone = search_bone.split(',')
        search_bone = list(filter(bool, search_bone))

        # model and serializer
        bone_changes = BoneChangeBoneProxy.objects.filter(anomalies__name=q)
        bone_changes_serializer = BoneChangeBoneProxySerializer(bone_changes, many=True)
        bone_change_relations = bone_changes_serializer.data

        # fill dict with technics
        # Todo: refactor model and for loops to be more pythonic
        # all_technics = {disease["technic"]["name"]: {} for disease in bone_change_relations}
        all_technics = {"Radiography": {}, "Macroscopy": {}, "Microscopy": {}}

        # create dict of technics and bones
        for disease in bone_change_relations:
            disease_as_dict = dict(disease)
            for current_bone in disease_as_dict["bone"]:
                if str(current_bone["id"]) in search_bone:
                    all_technics[disease["technic"]["name"]][current_bone["name"]] = {
                        "id": current_bone["id"],
                        "name": current_bone["name"],
                        "values": []
                    }
        # add bone changes to bones
        for disease in bone_change_relations:
            disease_as_dict = dict(disease)
            for current_bone in disease_as_dict["bone"]:
                if str(current_bone["id"]) in search_bone:
                    all_technics[disease["technic"]["name"]][current_bone["name"]]["values"].append(disease["bone_change"])
        return Response(all_technics)


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
            bone["type"] = "selectfield" if bone["options"] else "Label"
            bone_sections[bone["section"]].append(bone)
            bone_sections[bone["section"]].append(
                {"name": f"{bone['name']}_amount",
                 "type": "selectfield",
                 "values": forms['disease']['age_class']['values']
                 })

        # build forms from choices.py
        all_forms = {}
        for step in forms:
            for objects in forms[step]:
                key_values = []
                for name, value in forms[step][objects]['values']: key_values.append({"name": name, "value": value})
                forms[step][objects]['values'] = key_values
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

        resp = requests.get(f'https://gazetteer.dainst.org/suggestions?field=nameSuggestions&queryId=3&text={q}')
        if task == "site":
            resp = requests.get(
                f'https://gazetteer.dainst.org/search.json?q={q}&fq=_exists_:prefLocation.'
                f'coordinates&limit=1000&type=&pretty=true')

        return Response(resp.json(), status=resp.status_code)


class ChronologyServiceAPI(viewsets.ViewSet):
    def list(self, request):
        q = self.request.query_params.get('q')

        if q is None:
            return Response({'body': '?q=<term> needed for search'}, status=status.HTTP_400_BAD_REQUEST)

        resp = requests.get(f'https://chronontology.dainst.org/data/period?q={q}')
        return Response(resp.json(), status=resp.status_code)
