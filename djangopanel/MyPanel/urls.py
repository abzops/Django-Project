from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('add-project/', views.add_project, name='add_project'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('projects/get/<int:project_id>/', views.get_project, name='get_project'),
    path('projects/update/<int:project_id>/', views.update_project, name='update_project'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)