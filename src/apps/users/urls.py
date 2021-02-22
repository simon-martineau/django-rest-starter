from django.urls import path, include
from rest_framework import routers

from apps.users import views


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)

app_name = 'users'  # TODO: is this necessary?
urlpatterns = [
    path('register', views.RegisterUserView.as_view(), name='register'),
    path('', include(router.urls))
]
