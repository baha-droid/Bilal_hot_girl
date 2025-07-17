from django.contrib import admin
from .models import Tour

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'start_date', 'end_date', 'price')
