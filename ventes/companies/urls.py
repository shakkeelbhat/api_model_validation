from django.urls import path




from companies import views
urlpatterns = [
    path('action/',views.CUDApiView.as_view()),
    path('company/<int:id>/',views.GetCompanyByIDApiView.as_view()),
    path('allcompanies/',views.GetAllCompaniesApiView.as_view()),

]
