from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory

links_menu = [
    {'href': 'index', 'name': 'Главная', 'route': ''},
    {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
    {'href': 'about', 'name': 'О нас', 'route': 'about/'},
    {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
]

def products(request):
    title = 'продукты'

    products = Product.objects.all()  #[:2]
    categories = ProductCategory.objects.all()

    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'products': products,
        'categories': categories,
        'links_menu': links_menu,
        'basket': basket,
    }

    return render(request, 'products.html', context)


def product(request, pk):
    title = 'продукт'

    product_item = get_object_or_404(Product, pk=pk)
    category = product_item.category

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'category': category,
        # 'basket':
    }

    return render(request, 'product.html', context)


