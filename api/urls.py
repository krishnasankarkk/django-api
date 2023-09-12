# from django.urls import path
# from .views import ReactView

# urlpatterns = [
#     path('', ReactView.as_view(), name='index'),
# ]

from django.urls import include, path
from rest_framework import routers
  
from . import views 
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
# router.register(r'user', UserView)
  
# specify URL Path for rest_framework
urlpatterns = [
    path('get-all-user', views.UserView, name="get_all_users"),
    path('create-user', views.CreateUser, name="create_user"),
    path('get-user', views.GetUser, name="get_users"),
    path('api-auth/', include('rest_framework.urls'))
]