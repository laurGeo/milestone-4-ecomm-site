from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_cart(request):
    return render(request, "cart.html")
    
def make_bid(request, id):
    """Making bid"""
    return redirect(reverse('index'))
    
"""Add specific item to cart using id"""
def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 1)
    request.session['cart'] = cart
    
    return redirect(reverse('index'))

def adjust_cart(request,id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    """ Can only remove if greater than 0"""
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))
    
"""Deleting item from cart"""
def delete_from_cart(request,id):
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))