from django.contrib import admin
from .models import QuotationInfo, QuotationItem

class QuotationItemInline(admin.TabularInline):
    model = QuotationItem
    extra = 1 

@admin.register(QuotationInfo)
class QuotationInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phonenum', 'date_added')
    inlines = [QuotationItemInline]  # 將內聯添加到 QuotationInfo admin
