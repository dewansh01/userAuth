from django.urls import path
from authApp import views

app_name = 'authApp'
urlpatterns = [
path('create/',views.createUserView.as_view(),name='create'),
path('token/',views.createTokenView.as_view(),name='token'),
path('me/',views.ManageUserView.as_view(),name='me')
]
