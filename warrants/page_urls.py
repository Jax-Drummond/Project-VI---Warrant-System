# warrants/urls.py
from django.urls import path
from . import views  # These are your Template views

urlpatterns = [

    path('', views.dashboard_view, name='dashboard'),

    # The Officer List Page (The Empty Shell)
    # path('officers/', views.officer_frontend_list, name='officer-list'),

    # The Create Warrant Page
    path('warrants/', views.warrants_view, name='warrant-list'),
    path('warrants/create/', views.warrant_create_view, name='warrant-create'),
    path('warrants/<int:pk>/', views.warrant_detail_view, name='warrant-detail'),
    path('warrants/<int:pk>/edit/', views.warrant_edit_view, name='warrant-edit'),
    path('officers/', views.officer_list_view, name='officer-list'),
    path('crimes/', views.crime_list_view, name='crime-list'),
    path('citizens/', views.citizen_list_view, name='citizen-list'),
    path('citizens/create/', views.citizen_create_view, name='citizen-create'),
    path('citizens/<int:pk>/', views.citizen_detail_view, name='citizen-detail'),
    path('citizens/<int:pk>/edit/', views.citizen_edit_view, name='citizen-edit'),
    path('plates/', views.plate_list_view, name='plate-list'),
    path('plates/create/', views.plate_create_view, name='plate-create'),
    path('plates/<str:pk>/', views.plate_detail_view, name='plate-detail'),
    path('plates/<str:pk>/edit/', views.plate_edit_view, name='plate-edit'),
]