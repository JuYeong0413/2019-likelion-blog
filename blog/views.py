from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋 # 메소드
    return render(request, 'blog/home.html', {'blogs': blogs})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id) # pk = primary key : 객체들의 이름표, 구분자, 데이터의 대표값

    return render(request, 'blog/detail.html', {'blog': blog_detail})