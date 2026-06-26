from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from .models import BookingRequest
from .forms import BookingForm

def home_view(request):
    """Главная страница (Объединенная с О нас)"""
    return render(request, 'home.html')

def catalog_view(request):
    """Отдельная страница услуг и онлайн-записи с AJAX"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
                return JsonResponse({'success': True})
                
            return render(request, 'catalog.html', {'form': BookingForm(), 'success': True})
    else:
        form = BookingForm()
        
    return render(request, 'catalog.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def manager_dashboard(request):
    """Кастомная админка менеджера для обработки заявок"""
    requests_list = BookingRequest.objects.all().order_by('-created_at')
    
    total_count = requests_list.count()
    new_count = requests_list.filter(status='new').count()
    completed_count = requests_list.filter(status='completed').count()

    if request.method == 'POST':
        req_id = request.POST.get('request_id')
        new_status = request.POST.get('status')
        if req_id and new_status:
            booking = get_object_or_404(BookingRequest, id=req_id)
            booking.status = new_status
            booking.save()
            return redirect('manager_dashboard')

    context = {
        'requests': requests_list,
        'total_count': total_count,
        'new_count': new_count,
        'completed_count': completed_count,
    }
    return render(request, 'manager.html', context)