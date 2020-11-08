from django.urls import path
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from django.views.generic import RedirectView



class BaniList(APIView):
    def get(self, request,*args, **kwargs):
        with open('data/bani.json', encoding='utf-8') as f:
            json_data = json.load(f)

        return Response(json_data)

class BaniDetail(APIView):
    def get(self, request, id, *args, **kwargs):
        with open(f'data/{id}.json', encoding='utf-8') as f:
            json_data = json.load(f)

        return Response(json_data)



urlpatterns = [
    path('',  RedirectView.as_view(url='banis/')),
    path('banis/', BaniList.as_view()),
    path('banis/<id>/', BaniDetail.as_view()),
    

]
