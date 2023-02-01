from django.contrib import admin
from .models import *

admin.site.register(Farmer)
admin.site.register(Customer)
admin.site.register(Crop)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Cart)