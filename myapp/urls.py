from .import views
from django.urls import path
from .views import ReportView
urlpatterns=[
    path('home/',views.home,name='home'),
    path('download/',views.download, name='download'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    path('bugreport/', ReportView.as_view(), name='report')

]