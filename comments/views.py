from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Comment
from .forms import CommentForm

"""Allows user to write comment"""
def create_comment(request, id):
# //TODO: https://tutorial.djangogirls.org/en/django_forms/
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        print(comment_form.is_valid())
        if comment_form.is_valid():
            comment_form.save()
            return redirect('view_specific_product', id=id)
        else:
            comment_form = CommentForm()
        
        args = {'comment_form': comment_form}
        return redirect(reverse('index'), args)
    
"""Returning details from the comment"""
def comment_detail(request, id):
    comments = Comment.objects.all()
    
    return render(request, "product.html", {"comments": comments})
