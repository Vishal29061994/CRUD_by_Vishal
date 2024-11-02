from django.contrib import admin
from .models import Vidyarthi

# Register your models here.
@admin.register(Vidyarthi)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','Course','city')    
