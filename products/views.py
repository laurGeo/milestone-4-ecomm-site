from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product
from comments.models import Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
 
    return render(request, "products.html", {"products": products})
    
def view_specific_product(request, id):
    comment_form = CommentForm()
    comments = Comment.objects.all()
    product = get_object_or_404(Product, pk=id)
    
    return render(request, 'product.html', {"product":product, "comments":comments,"comment_form": comment_form})
    
def index(request):
    return render(request, "index.html")