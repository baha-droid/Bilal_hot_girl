from django.shortcuts import render, get_list_or_404
from .models import Tour

def home(request):
    tours = Tour.objects.all()
    return render(request, 'tourism/home.html', {'tours': tours})

def tour_detail(request, pk):
    tour = get_list_or_404(Tour, pk=pk)
    return render(request, 'tourism/tour_detail.html', {'tour': tour})
