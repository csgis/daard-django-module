from rest_framework.views import APIView
from .models import Bone
from rest_framework.response import Response
from rest_framework import serializers
import requests
import json
from .serializers import BoneSerializer

class SuggestServiceAPI(APIView):
    def get(self,request):
        q = self.request.query_params.get('q')
        resp = requests.get('https://gazetteer.dainst.org/suggestions?field=nameSuggestions&queryId=3&text='+q)
        return Response(resp.json(), status=resp.status_code)

class SiteServiceAPI(APIView):
    def get(self,request):
        q = self.request.query_params.get('q')
        resp = requests.get('https://gazetteer.dainst.org/search.json?q='+q+'&fq=_exists_:prefLocation.coordinates&limit=1000&type=&pretty=true')
        return Response(resp.json(), status=resp.status_code)

