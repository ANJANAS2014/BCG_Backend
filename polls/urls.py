from django.urls import path

from . import views

urlpatterns = [
    path('viewData/', views.viewData, name='viewData'),
    path('chartData/', views.chartData, name='chartData'),
    path('updateData/', views.updateData, name='updateData')

]
