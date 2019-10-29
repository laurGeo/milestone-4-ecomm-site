from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    paginator = Paginator(products, 3) # Show 3 contacts per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
 
    return render(request, "products.html", {"products": products})
    return render(request, "products.html", {"products": products})