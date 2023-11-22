from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Sum
from myapp2.models import Product


def total_in_db(request):
    # Представление для суммирования в БД
    total = Product.objects.aggregate(Sum('price'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_view(request):
    # Представление для суммирования в представлении
    products = Product.objects.all()
    total = sum(product.price for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request):
    # Представление для суммирования в модели из шаблона
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)
