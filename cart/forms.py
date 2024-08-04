from django import forms
from .models import QuotationItem, QuotationInfo

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
class clientInfo(forms.ModelForm):
    class Meta:
        model=QuotationInfo
        fields=('username', 'email', 'phonenum',)
        widgets = {
            'username':forms.TextInput(attrs={
                'placeholder':'輸入您的公司名稱',
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'example@emil.com'
            }),
            'phonenum':forms.TextInput(attrs={
                'placeholder':'輸入您的電話號碼'
            })
        }
