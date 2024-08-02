from django.urls import path

from . import views

app_name='item'

urlpatterns=[
    path('add_item_to_quotation/<int:item_id>/', views.add_item_to_quotation, name='add_to_quotation'),
    path('quotation_summary/', views.quotation_summary, name='quotation_summary'),
    path('submit_quotation/', views.submit_quotation, name='submit_quotation'),
    path('', views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
]