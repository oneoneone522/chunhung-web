from django import forms

class QuotationForm(forms.Form):
    specification=forms.CharField(label="規格", max_length=225)
    quatity=forms.IntegerField(label="數量",min_value=1)