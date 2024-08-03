from django import forms
from .models import CartItem

class quotationForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('specification',)
        widgets = {
            'specification':forms.Textarea(attrs={
                'class':'input-section',
                'placeholder':'請輸入產品規格',
            })
        }