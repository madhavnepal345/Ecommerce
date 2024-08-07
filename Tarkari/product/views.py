from django.shortcuts import render,redirect
from .forms import ProductForm

def create_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form=ProductForm()
    return render(request,'create_product.html',{'form':form})
