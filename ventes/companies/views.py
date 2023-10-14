from django.shortcuts import render
from companies.serializers import CompanySerializer
from rest_framework.views import APIView


class CUDApiView(APIView):
    def post(self,request):
        pass

class GetCompanyByIDApiView(APIView):
    def get(self,request,id):
        pass

class GetAllCompaniesApiView(APIView):
    def get(self,request) :
        pass



