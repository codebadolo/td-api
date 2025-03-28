from django.urls import path
from .views import  user_signup, user_logout, user_profile , LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
]
