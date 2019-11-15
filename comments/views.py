from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Comment
from .forms import CommentForm

"""Allows user to write comment"""
def create_comment(request, id):

    comment = get_object_or_404(Comment, pk=id) if id else None
    
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            print(form)
            comment = form.save()
            return redirect(comment_detail, comment.id)
    else:
        form = CommentForm(instance=comment)
        
    return render(request, 'product.html', {'form': form})
    
"""Returning details from the comment"""
def comment_detail(request, id):
    comments = Comment.objects.all()
    
    return render(request, "product.html", {'comments': comments})
