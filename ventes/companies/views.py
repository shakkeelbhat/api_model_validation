from django.shortcuts import render
from companies.serializers import CompanySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from companies.models import Company
from django.core.paginator import Paginator




class CUDApiView(APIView):
    def post(self,request):
        try:
            data = request.data
            try:
                serializer = CompanySerializer(data=data)
            except Exception as e:
                return Response({'message':"Error while serializing"},status=status.HTTP_400_BAD_REQUEST)
            if not serializer.is_valid():
                return Response({'message':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer.save()
            return Response({'data':serializer.data,'message':'Record added'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message':"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
class GetCompanyByIDApiView(APIView):
    def get(self,request,id):
        try:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)#no data argument to be passed
            #no is_valid() to do
            return Response(serializer.data)
        
        except Exception as e:
            return Response({'message':"Record of that ID doesn't exist"},status=status.HTTP_400_BAD_REQUEST)
            

class GetAllCompaniesApiView(APIView):
    def get(self,request) :
        try:
            comps = Company.objects.all().order_by('company_name')
            page_number =  request.GET.get('page',1)
            page_size = 2
            paginator = Paginator(comps,page_size)
            
            serializer = CompanySerializer(paginator.page(page_number),many=True)
            #no is_valid() to do
            return Response(serializer.data)
        except Exception as e:
            return Response({'message':"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
 



