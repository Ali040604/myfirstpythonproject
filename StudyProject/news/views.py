from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comment
from .forms import CommentForm


def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.save()
            return redirect('home')
    else:
        form = CommentForm()
        comment = Comment.objects.all()
        return render(request, 'news/add.html', {'form': form, 'comment':comment})

