from django.urls import path
from settings import views
urlpatterns = [
  path('profile/view/',views.profile,name='profile'),

]