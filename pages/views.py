from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
 template_name = 'pages/about.html'

 def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
    "title": "About us - Online Store",
    "subtitle": "About us",
    "description": "This is an about page ...",
    "author": "Developed by: Samuel Deossa",
    })
    return context
 
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact Us - Online Store",
            "subtitle": "Contact Information",
            "email": "contact@onlinestore.fake",
            "address": "1234 Fake Street, Medellín, Colombia",
            "phone": "+57 300 000 0000",
        })
        return context

class Product:
    products = [
    {"id":"1", "name":"TV", "description":"Best TV", "price":"150 USD"},
    {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":"120 USD"},
    {"id":"3", "name":"Glasses", "description":"Best Glasses", "price":"70 USD"},
    {"id":"4", "name":"Chromecast", "description":"Best Chromecast", "price":"90 USD"},
    {"id":"5", "name":"Laptop", "description":"Best Laptop", "price":"200 USD"},
    {"id":"6", "name":"Headphones", "description":"Best Headphones", "price":"50 USD"},
    {"id":"7", "name":"Smartwatch", "description":"Best Smartwatch", "price":"80 USD"},
    {"id":"8", "name":"Camera", "description":"Best Camera", "price":"300 USD"},
    {"id":"9", "name":"Speaker", "description":"Best Speaker", "price":"120 USD"},
    {"id":"10", "name":"Tablet", "description":"Best Tablet", "price":"150 USD"},
    
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        if not id.isdigit() or int(id) < 1 or int(id) > len(Product.products):
            return HttpResponseRedirect(reverse('home'))
        
        product = Product.products[int(id)-1]
        viewData = {
            "title": product["name"] + " - Online Store",
            "subtitle": product["name"] + " - Product information",
            "product": product,
            "price_value": int(product["price"].split()[0])  # Solo el número
        }
        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Price is required.")
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {"title": "Create product", "form": form}
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return render(request, 'products/success.html', {"title": "Product Created"})
        else:
            viewData = {"title": "Create product", "form": form}
            return render(request, self.template_name, viewData)