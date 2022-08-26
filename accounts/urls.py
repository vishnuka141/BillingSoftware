from django.urls import path
from accounts import views
urlpatterns = [
   path('signin',views.SigninView.as_view(),name='login'),
   path('user/home',views.user_home,name='userhome'),
   path('signout',views.signout,name='logout'),
]