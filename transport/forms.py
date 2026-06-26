from django import forms
from transport.models import BookingRequest # Изменено на transport

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['client_name', 'phone', 'service_type', 'booking_date', 'comment']
        widgets = {
            'client_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3.5 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-950 dark:text-white rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 transition',
                'placeholder': 'Иван Иванов',
                'required': 'required'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3.5 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-950 dark:text-white rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 transition',
                'placeholder': '+7 (999) 123-45-67',
                'required': 'required'
            }),
            'service_type': forms.Select(attrs={
                'class': 'w-full px-4 py-3.5 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-950 dark:text-white rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 transition',
                'required': 'required'
            }),
            'booking_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3.5 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-950 dark:text-white rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 transition',
                'required': 'required'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3.5 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-950 dark:text-white rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 transition h-28',
                'placeholder': 'Комментарий',
            }),
        }