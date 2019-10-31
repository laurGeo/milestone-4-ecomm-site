from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Comment
from .forms import CommentForm

def create_comment(request, pk=None):

    post = get_object_or_404(Comment, pk=pk) if pk else None
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            comment = form.save()

    return render(request, 'product.html', {'form': comment_form})