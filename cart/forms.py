from django import forms
from .models import QuotationItem, QuotationInfo
from captcha.fields import CaptchaField

class quotationForm(forms.ModelForm):
    class Meta:
        model = QuotationItem
        fields = ('specification','quantity','remark')
        widgets = {
            'specification':forms.TextInput(attrs={
                'class':'input-section',
                'placeholder':'請輸入產品規格',
            }),
            'quantity':forms.NumberInput(attrs={
                'class':'input-section',
                'placeholder':'請輸入產品數量',
            }),
            'remark':forms.TextInput(attrs={
                'class':'input-section',
                'placeholder':'如有需求，請輸入對產品的備註'
            })
        }
class clientInfo(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=QuotationInfo
        fields=('username', 'email', 'phonenum', 'captcha')
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'input-section',
                'placeholder':'輸入您的公司或聯絡人名稱',
            }),
            'email':forms.EmailInput(attrs={
                'class':'input-section',
                'placeholder':'example@emil.com'
            }),
            'phonenum':forms.TextInput(attrs={
                'class':'input-section',
                'placeholder':'輸入您的電話號碼'
            }),
            'captcha':forms.TextInput(attrs={
                'class':'input-section',
                'placeholder':'輸入驗證碼'
            }),
        }
