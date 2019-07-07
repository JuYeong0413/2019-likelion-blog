from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋 # 메소드
    return render(request, 'blog/home.html', {'blogs': blogs})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드


def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id) # pk = primary key : 객체들의 이름표, 구분자, 데이터의 대표값

    return render(request, 'blog/detail.html', {'details': details})


# new.html 띄워주는 함수
def new(request):
    return render(request, 'blog/new.html', name="new")


# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        pub_date = timezone.datetime.now()
        blog = Blog(title=title, body=body, pub_date=pub_date)
        blog.save()

    # return redirect('/blog/'+str(blog.id))
    return redirect('detail', blog.id)