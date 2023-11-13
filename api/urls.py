from django.urls import include, path
from rest_framework import routers
  
from . import views 
  
# specify URL Path for rest_framework
urlpatterns = [
    path('', views.home, name="home"),
    path('get-all-user', views.UserView, name="get_all_users"),
    path('create-user', views.CreateUser, name="create_user"),
    # path('get-user', views.GetUser, name="get_users"),
    path('api-auth/', include('rest_framework.urls'))
]