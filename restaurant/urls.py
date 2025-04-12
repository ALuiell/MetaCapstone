from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

from .views import say_hello

urlpatterns = [
    path('hello/', say_hello, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
