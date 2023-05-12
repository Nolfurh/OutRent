from django.contrib import admin
from .models import Dwelling, DwellingRentStatus, ReviewDwelling, ReviewRenter

admin.site.register(Dwelling)
admin.site.register(DwellingRentStatus)
admin.site.register(ReviewDwelling)
admin.site.register(ReviewRenter)
