from django.shortcuts import render, get_list_or_404
from django.utils import timezone
from.models import post

# Create your views here.
def post_list(request):
    posts = post.objects.filter(published_date__lte=timezone.now ()).order_by('published_date')
    return render(request, 'blogtask/post_list.html', {'posts': posts})

def post_details(request,pk):
    post = get_list_or_404(post, pk=pk)
    return render(request, 'blogtask/post_details.html', {'post': post})
