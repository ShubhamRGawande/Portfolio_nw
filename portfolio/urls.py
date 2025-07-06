from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),  # ✅ Corrected line
    path('learning/', views.learning, name='learning'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]
