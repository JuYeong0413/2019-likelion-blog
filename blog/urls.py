from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    # path converter : 여러 객체들을 다루는, 계층적인 url을 자동생성할 때 유리함
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]