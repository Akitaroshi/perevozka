from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# ОБЯЗАТЕЛЬНО ИМПОРТИРУЕМ МОДЕЛЬ ЗАЯВОК:
from transport.models import BookingRequest

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            # ИСПРАВЛЕНО: редиректим на 'home' вместо 'landing'
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_view(request):
    # Достаем все заявки текущего вошедшего пользователя
    bookings = BookingRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'registration/profile.html', {'bookings': bookings})