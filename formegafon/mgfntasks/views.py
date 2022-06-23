from django.shortcuts import render

from .forms import LoanForm, EncryptDecryptFotm, ProductsForm, NumericalSpiralForm
from .addons.addon import calculate, overpayment, define_word, encode_decode


def index(request):
    return render(request, 'mgfntasks/index.html')

def loan(request):
    form = LoanForm()
    result = None
    
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            result = overpayment(form_data)
            return render(request, 'mgfntasks/loan.html', {
                'form': form,
                'form_data': form_data,
                'result': result
            })
        
    return render(request, 'mgfntasks/loan.html', {
        'form': form,
        'result': result
    })
    
def crypt(request):
    form = EncryptDecryptFotm()
    result = None
    
    if request.method == "POST":
        form = EncryptDecryptFotm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            result = encode_decode(form_data)
            return render(request, 'mgfntasks/crypt.html', {
                'form': form,
                'result': result
            })
            
    return render(request, 'mgfntasks/crypt.html', {
        'form': form,
        'result': result
    })
    
def products(request):
    form = ProductsForm()
    result = None
    
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            result = define_word(form_data['products_num'])
            return render(request, 'mgfntasks/products.html', {
                'form': form,
                'result': result,
                'products_num': form_data['products_num']
            })

    return render(request, 'mgfntasks/products.html', {
        'form': form,
        'result': result
    })
    
def spiral(request):
    form = NumericalSpiralForm()
    result = None
    
    if request.method == "POST":
        form = NumericalSpiralForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            result = calculate(form_data['size'])
            return render(request, 'mgfntasks/spiral.html', {
                'form': form,
                'result': result,
                'size': form_data['size']
            })

    return render(request, 'mgfntasks/spiral.html', {
        'form': form,
        'result': result
    })