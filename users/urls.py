from django.urls import path
from .views import users_view, user_update_view


urlpatterns = [
    path('', users_view, name='users-view'),
    path('update/<int:pk>/', user_update_view, name='user-update-view'),
]
