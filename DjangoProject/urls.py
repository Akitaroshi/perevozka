from django.contrib import admin
from django.urls import path
# Импортируем все наши функции, включая payment_view
from transport.views import home_view, catalog_view, manager_dashboard, calculator_view, payment_view
from users.views import register_view, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),                               # Главная
    path('catalog/', catalog_view, name='catalog'),                 # Услуги и запись
    path('calculator/', calculator_view, name='calculator'),       # Конструктор стоимости
    path('manager/', manager_dashboard, name='manager_dashboard'), # Панель менеджера
    
    # ВОТ ЭТОТ ПУТЬ ОБЯЗАТЕЛЬНО ДОЛЖЕН БЫТЬ ТУТ:
    path('payment/<int:booking_id>/', payment_view, name='payment'),
    
    # Авторизация и профиль
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
]