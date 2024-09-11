import django.conf
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings



# Create your views here.
@login_required( login_url = '/login')
def home(request):
    posts = Post.objects.all()
    
        
    poste = Post.objects.all().order_by('-created_at')
    
    # Get the latest post
    latest_post = poste.first() if poste.exists() else None
    
    context = {
        'poste': poste,
        'latest_post_id': latest_post.id if latest_post else None,
    }
    
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')
        
        
        if post_id:
            post = get_object_or_404(Post, id=post_id)
            
            # Check if the post belongs to the user or the user has permission to delete
            if post and (post.author == request.user or request.user.has_perm('main.delete_post')):
                post.delete()
                messages.success(request, 'Post deleted successfully.')
                return redirect('/home')
            else:
                messages.error(request, 'You are not authorized to delete this post.')
                return redirect('/home')

        elif user_id:
            user = get_object_or_404(User, id=user_id)
            
            if user and (user == request.user or request.user.is_staff):
                try:
                    group = get_object_or_404(Group, name='default')
                    group.user_set.remove(user)
                    messages.success(request, 'User deleted successfully.')
                    return redirect('/home')
                except:
                    pass
                try:
                    group = get_object_or_404(Group, name='mod')
                    group.user_set.remove(user)
                    messages.success(request, 'User deleted successfully.')
                    return redirect('/home')
                except:
                    pass
              
                
            else:
                messages.error(request, 'You are not authorized to delete this user.')
                return redirect('/home')
                
        
    
    
    return render(request, 'main/home.html', {'posts' : posts}) 

@login_required( login_url = '/login')
@permission_required ('main.add_post', login_url = '/login', raise_exception = True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
            
    else:
        form = PostForm()
        
    return render(request, 'main/create_post.html', {'form': form})

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
            
    else:
        form = RegisterForm()
        
    return render(request, 'registration/sign_up.html', {'form': form})

