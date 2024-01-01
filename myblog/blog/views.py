from django.shortcuts import render
from django.shortcuts import get_object_or_404  # вернутьобъект или 404

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(reqest, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(reqest, 'blog/post/detail.html', {'post': post})
