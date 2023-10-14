from django.urls import path,include
from companies import views
urlpatterns = [
    path('action/',views.CUDApiView.as_view()),
    path('company/<id:int>',views.GetCompanyByIDApiView.as_view()),
    path('allcompanies/',views.GetAllCompaniesApiView.as_view()),

]
