from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('add-project/', views.add_project, name='add_project'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),
]