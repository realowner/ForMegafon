from django import forms


CHOICES = (
    ('encrypt', 'Зашифровать'),
    ('decrypt', 'Расшифровать')
)

class LoanForm(forms.Form):
    loan_summ = forms.FloatField(min_value=1, required=True, label='Сумма займа')
    interest_rate = forms.FloatField(min_value=1, required=True, label='Процентная ставка')
    years = forms.FloatField(min_value=1, required=True, label='Кол-во лет')
    

class EncryptDecryptFotm(forms.Form):
    target_file = forms.FileField(required=True, label='Файл')
    encryptdecrypt = forms.ChoiceField(required=True, choices=CHOICES, label='Действие')
    
    def clean(self):
        file_exp = self.cleaned_data.get('target_file').name.split('.')[1]
        if file_exp != 'txt':
            raise forms.ValidationError('Можно загрузить только TXT файл!')
        return self.cleaned_data
    

class ProductsForm(forms.Form):
    products_num = forms.IntegerField(min_value=0, required=True, label='Количество')
    

class NumericalSpiralForm(forms.Form):
    size = forms.IntegerField(min_value=1, required=True, label='Размер спирали')
    
    def clean(self):
        if self.cleaned_data.get('size') % 2 == 0:
            raise forms.ValidationError('Размер должен быть нечетным!')
        return self.cleaned_data