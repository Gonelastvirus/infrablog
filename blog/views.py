from django.shortcuts import render, get_object_or_404,  redirect
from .models import Post, RedHatPost, vmwarepost,Comment  # Assuming you have separate models
from django.contrib import messages
def post_list(request):
    query = request.GET.get('q')
    
    aix_posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query) if query else Post.objects.all().order_by('-created_at')
    redhat_posts = RedHatPost.objects.filter(title__icontains=query) | RedHatPost.objects.filter(content__icontains=query) if query else RedHatPost.objects.all().order_by('-created_at')
    vmware_posts = vmwarepost.objects.filter(title__icontains=query) | vmwarepost.objects.filter(content__icontains=query) if query else vmwarepost.objects.all().order_by('-created_at')
    latest_aix_posts = Post.objects.all().order_by('-created_at')[:5]
    latest_redhat_posts = RedHatPost.objects.all().order_by('-created_at')[:5]
    latest_vmware_posts = vmwarepost.objects.all().order_by('-created_at')[:5]

    
    return render(request, 'blog/post_list.html', {
        'aix_posts': aix_posts,
        'redhat_posts': redhat_posts,
        'vmware_posts': vmware_posts,
        'query': query,
        'latest_aix_posts': latest_aix_posts,
        'latest_redhat_posts': latest_redhat_posts,
        'latest_vmware_posts': latest_vmware_posts,
    })

# def aix_post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     return render(request, 'blog/post_detail.html', {'post': post})

# def redhat_post_detail(request, pk):
#     post = get_object_or_404(RedHatPost, pk=pk)
#     return render(request, 'blog/redhat_post_detail.html', {'post': post})

# def vmware_post_detail(request, pk):
#     post = get_object_or_404(vmwarepost, pk=pk)
#     return render(request, 'blog/vmware.html', {'post': post})

# AIX Post Detail + Comment Handling
def aix_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')  # Retrieve all comments for this post

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')

        if name and email and content:
            Comment.objects.create(post=post, name=name, email=email, content=content)
            messages.success(request, "Your comment has been posted!")
            return redirect('aix_post_detail', pk=pk)  # Reload page after submission
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

# RedHat Post Detail + Comment Handling
def redhat_post_detail(request, pk):
    post = get_object_or_404(RedHatPost, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')

        if name and email and content:
            Comment.objects.create(post=post, name=name, email=email, content=content)
            messages.success(request, "Your comment has been posted!")
            return redirect('redhat_post_detail', pk=pk)
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'blog/redhat_post_detail.html', {'post': post, 'comments': comments})

# VMware Post Detail + Comment Handling
def vmware_post_detail(request, pk):
    post = get_object_or_404(vmwarepost, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')

        if name and email and content:
            Comment.objects.create(post=post, name=name, email=email, content=content)
            messages.success(request, "Your comment has been posted!")
            return redirect('vmware_post_detail', pk=pk)
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'blog/vmware_post_detail.html', {'post': post, 'comments': comments})
