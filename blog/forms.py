from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): # 모델을 기반으로 한 입력 공간을 만들어주기 위해 forms.ModelForm
    class Meta:
        model = Blog # Blog 모델을 기반으로 한 입력공간을 만들 건데
        fields = ['title', 'body'] # 그 중에서 title, body를 입력받을 수 있는 공간을 만들겠다.

    # email = forms.EmailField()
    # files = forms.FileField()
    # url = forms.URLField()
    # words = forms.CharField(max_length=200)
    # max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])