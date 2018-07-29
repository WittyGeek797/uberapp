from django.contrib import admin
from .models import Customer,Driver,BookCab,TravelHistory

# Register your models here.
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(BookCab)
admin.site.register(TravelHistory)
