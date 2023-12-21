from django.contrib import admin
from .models import *

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display=['name','level','Type','description']

@admin.register(Consultancy)
class ConsultancyAdmin(admin.ModelAdmin):
    list_display=['name','level','Type','description']

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display=['name','level','description']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=['first_name','financial_goal','level','income','expense','asset','loan']
    