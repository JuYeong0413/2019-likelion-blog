from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋 # 메소드

    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'blogs': blogs, 'posts': posts})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드


def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id) # pk = primary key : 객체들의 이름표, 구분자, 데이터의 대표값

    return render(request, 'blog/detail.html', {'details': details})


# new.html 띄워주는 함수
def new(request):
    return render(request, 'blog/new.html')


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


def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = BlogPost(request.POST) # POST 방식으로 들어온 데이터를 담아줌
        if form.is_valid(): # form이 잘 입력되었는지 검사
            post = form.save(commit=False) # 모델 객체를 반환하되 저장하지 않는다. post는 Blog형 객체
            post.pub_date = timezone.now()
            post.save()
            return redirect('detail', blog.id)
    else:
        form = BlogPost() # 빈 객체의 form 탄생
        return render(request, 'blog/new.html', {'form': form})