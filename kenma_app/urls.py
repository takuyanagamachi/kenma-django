from django.urls import path
from . import views

app_name = 'kenma_app'
urlpatterns = [
   path('', views.IndexViews.as_view(), name='index'),
   path('company', views.CompanyViews.as_view(), name='company'),
   path('service/', views.ServiceViews.as_view(), name='service'),
   path('service/saikenma/', views.SaikenmaViews.as_view(), name='saikenma'),
   path('service/saidanki/', views.SaidankiViews.as_view(), name='saidanki'),
   path('service/sinba/', views.SinbaViews.as_view(), name='sinba'),
   path('service/sizai/', views.SizaiViews.as_view(), name='sizai'),
   path('contact/', views.ContactView.as_view(), name='contact'),
   path('contact/done/', views.DoneViews.as_view(), name='done'),
]