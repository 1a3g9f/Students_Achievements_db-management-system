from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:pk>/edit/', views.update_student, name='update_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
    
    path('student/<int:student_id>/add_achievement/', views.add_achievement, name='add_achievement'),
    path('achievement/<int:pk>/status/<str:status>/', views.update_achievement_status, name='update_status'),
    path('add-category/', views.add_category, name='add_category'),
    path('category/edit/<int:pk>/', views.update_category, name='update_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('master-report/', views.master_report, name='master_report'),
]