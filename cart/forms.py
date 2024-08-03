from django import forms
from .models import QuotationItem

class quotationForm(forms.ModelForm):
    class Meta:
        model = QuotationItem
        fields = ('specification','quantity',)
        widgets = {
            'specification':forms.TextInput(attrs={
                'class':'input-section',
                'placeholder':'請輸入產品規格',
            }),
            'quantity':forms.NumberInput(attrs={
                'class':'input-section',
                'placeholder':'請輸入產品數量',
            })
        }