from django.contrib import admin
from shoes.models import Manufacturer, ShoeType, ShoeColor, Shoe

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)