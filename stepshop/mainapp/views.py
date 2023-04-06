from random import sample

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products = Product.objects.all()
    return sample(list(products), 1)[0]


def get_same_products(product):
    same_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
    return same_products


def products(request, pk=None):
    title = 'продукты'

    products = Product.objects.all()  #[:2]
    categories = ProductCategory.objects.all()

    basket = get_basket(request.user)

    context = {
        'title': title,
        'products': products,
        'categories': categories,
        'links_menu': links_menu,
        'basket': basket,
    }

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_ = Product.objects.filter(category__pk=pk).order_by('price')

        context.update({'products': products_, 'category': category,})

        context = {
            'title': title,
            'products': products,
            'categories': categories,
            'category': category,
            'links_menu': links_menu,
            'basket': basket,
        }




    return render(request, 'products.html', context)


def product(request, pk):
    title = 'продукт'

    product_item = get_object_or_404(Product, pk=pk)
    category = product_item.category

    same_products = get_same_products(product_item)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'category': category,
        'same_products': same_products,

    }

    return render(request, 'product.html', context)


