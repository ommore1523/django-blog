from django.shortcuts import render ,get_object_or_404  
from django.http import HttpResponse
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.views.generic.edit import  CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin

from .models import Posts



#extract a list of objects from db
class PostListview(ListView):
    model = Posts
    template_name='blogapp/home.html'
    context_object_name='posts'
    paginate_by = 2
    ordering = [ '-date_posted']

class UserPostListview(ListView):
    model = Posts
    template_name='blogapp/user_posts.html'
    context_object_name='posts'
    paginate_by = 2
    ordering = [ '-date_posted']

    def get_queryset(self):
        user=get_object_or_404(User ,username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Posts
    template_name='blogapp/post_detail.html'

class PostCreateview(LoginRequiredMixin ,CreateView):
    model = Posts
    template_name="blogapp/post_create.html"
    fields=['title','content']
    

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateview(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model = Posts
    template_name="blogapp/post_create.html"
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)   

    def test_func(self):
        post=self.get_object()
        print(post,"\n")
        if self.request.user   == post.author :
             return True
        else:
             False     

class PostDeleteview(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Posts
    success_url="/blog"
    template_name='blogapp/post_delete.html'

    def test_func(self):
        post=self.get_object()
        print(post,"\n")
        if self.request.user   == post.author :
             return True
        else:
             False 

def about(request):
     return render(request,'blogapp/about.html')