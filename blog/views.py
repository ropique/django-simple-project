from django.shortcuts import render, get_object_or_404
from itsdangerous import Serializer
from yaml import serialize
from .models import Post
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.decorators import login_required




# Create your views here.
def blog(request):
   
    context = {
        'posts': Post.objects.all()

    }
    
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post    
    template_name = 'blog/post_detail.html'

# @login_required
class PostCreateView(CreateView):
    model = Post    
    fields = ['title', 'content', 'category']
    template_name = 'blog/add_post.html'     

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   

def about(request):
    return render(request, 'blog/about.html', {'title': 'QA engineering'})

def search_res(request):
    if request.method == "GET":
        searched = request.GET['s']

        # searched = request.GET.get('searched', None)
        # searched = request.GET.get("searched")

        venues = Post.objects.filter(Q(title__contains = searched)|Q(content__contains = searched)|Q(category__contains = searched))




        return render(request, 'blog/search_res.html', {'s': searched, 'venues': venues})

    else:
        return render(request, 'blog/search_res.html')

# class PostList(APIView):
#     def get(self, request):
#         Post1 = Post.objects.all()
#         serializer = PostSerializer(Post1, many = True)
#         return Response(serializer.data)    
        

#     def post(self):
#         pass    
@api_view(['GET', 'POST'])
def PostList(request):
    if request.method == 'GET':
        Post1 = Post.objects.all()
        serializer = PostSerializer(Post1, many = True)
        
        return Response(serializer.data, status = status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PostSerializer(data = request.data,  many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


        

@api_view(['GET', 'DELETE', 'PUT'])
def post_detail(request, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        
        return Response(status = status.HTTP_404_NOT_FOUND)  
          

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    if request.method == 'PUT':  
        serializer = PostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_308_PERMANENT_REDIRECT)    
    if request.method == 'DELETE':   
        post.delete() 
        return Response(status = status.HTTP_204_NO_CONTENT)

        
