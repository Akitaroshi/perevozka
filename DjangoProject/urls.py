from django.contrib import admin
from django.urls import path
from transport.views import home_view, catalog_view, manager_dashboard
from users.views import register_view, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),                               # Главная + О компании
    path('catalog/', catalog_view, name='catalog'),                 # Отдельная страница услуг и записи
    path('manager/', manager_dashboard, name='manager_dashboard'), # Панель менеджера
    
    # Авторизация и профиль
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
]