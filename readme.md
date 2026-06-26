## Быстрый старт (Инструкция по запуску)

### 1. Подготовка виртуального окружения
Создайте изолированное окружение и активируйте его.

```powershell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.venv\Scripts\activate
```



### 2. Установка библиотек
Установите зависимости проекта строго под вашу версию PostgreSQL:
```bash
python -m pip install -r requirements.txt
```

### 3. Настройка базы данных
1. Откройте клиент PostgreSQL (pgAdmin или консоль psql) и создайте базу данных:
   ```sql
   CREATE DATABASE perevozka_db;
   ```
2. Откройте файл `DjangoProject/settings.py` и в блоке `DATABASES` пропишите ваш реальный пароль от PostgreSQL (вместо `ВАШ_ПАРОЛЬ`):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'perevozka_db',
           'USER': 'postgres',
           'PASSWORD': 'ВАШ_ПАРОЛЬ',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
   ```

### 4. Применение таблиц 
```bash
# Применяем миграции
python manage.py makemigrations
python manage.py migrate

### 5. Создание администратора
Создайте профиль администратора для работы с панелью управления:
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера
Запустите сервер разработки:
```bash
python manage.py runserver
```

После этого откройте браузер:
* Главная страница (О компании): http://127.0.0.1:8000/
* Панель администратора: http://127.0.0.1:8000/admin/