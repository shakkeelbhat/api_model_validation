from rest_framework import serializers
from companies.models import Company



class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'#['company_name','email_id','company_code','strength','website']