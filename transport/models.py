from django.db import models
from django.contrib.auth.models import User

class BookingRequest(models.Model):
    SERVICE_CHOICES = [
        ('repair', 'Ремонт грузового автомобиля'),
        ('cargo', 'Перевозка сыпучих материалов'),
    ]
    
    STATUS_CHOICES = [
        ('new', 'Новая заявка'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пользователь")
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    service_type = models.CharField(max_length=30, choices=SERVICE_CHOICES, verbose_name="Услуга")
    booking_date = models.DateField(verbose_name="Дата записи")
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка #{self.id} — {self.client_name} ({self.get_service_type_display()})"