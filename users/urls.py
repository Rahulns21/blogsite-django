from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('password-change/', views.password_change, name='password_change'),
    path('password_reset/', views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.password_reset_confirm, name='password_reset_confirm'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
