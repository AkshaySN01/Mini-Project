from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Users, Posts
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import Post, Edit_user, UserCreation, CommentForm

# Create your views here.
#login view
def log_in(request):
    obj=Users.objects.all()
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user=request.user
            id=current_user.id
            return redirect('home',pk=id)
    return render(request,'login.html')

#sign_in views
def registration(request):
    obj=Users()
    form=UserCreation(request.POST or None, request.FILES or None, instance=obj)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'registration_page.html',{'form':form})

#current_user profile view
def home_page(request,pk):
    if request.user.is_authenticated:
        obj=Users.objects.get(id=pk)
        p=Posts.objects.all()
        if obj.photo:
            pic = obj.photo.url
        else:
            pic = '/static/blank.webp'
        return render(request,'home_page.html',{'x':obj,'p':p,'pic':pic})
    else:
        return redirect('login')

#Add Posts view
def posts(request,pk):
    form=Post(request.POST or None, request.FILES or None)
    if form.is_valid():
        photo=form.cleaned_data.get('photo')
        caption=form.cleaned_data.get('caption')
        obj=Posts.objects.create(username=Users.objects.get(id=pk),photo=photo,caption=caption)
        obj.save()
        return redirect('home',pk=pk)
    return render(request,'posts.html',{'form':form})

#edit profile view
def edit_profile(request,pk):
    obj=Users.objects.get(id=pk)
    form=Edit_user(request.POST or None, request.FILES or None, instance=obj)
    if request.method=='POST':
         if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('login')
    return render(request,'edit.html',{'form':form})

#account delete view
def delete_acc(request,pk):
    obj=request.user
    obj.delete()
    return redirect('login')

#Register likes
def LikeView(request,post_id):
    if request.user.is_authenticated:
        post=Posts.objects.get(id=post_id)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        pk=request.user.id
    return redirect('feed',pk=pk)

#Add Comment view
def comment_view(request,post_id,pk): 
    post=Posts.objects.get(id=post_id)
    obj=Users.objects.get(id=pk)
    postss=Posts.objects.all().order_by('?')
    form=CommentForm()
    if request.method == 'POST':
        form=CommentForm(request.POST or None)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post= post
            comment.user= request.user
            comment.save()
    return redirect('feed',pk=pk)

#show feed view
def feed(request,pk):
    if request.user.is_authenticated:
        obj=Users.objects.get(id=pk)
        postss=Posts.objects.all().order_by('?')
        form=CommentForm()
        return render(request, 'feed.html', {'pk':pk,'cmnt_form':form,'posts': postss,'x':obj,})
    else:
        return redirect('login')

#logout view
def log_out(request):
    logout(request)
    return redirect('login')