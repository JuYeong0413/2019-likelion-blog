from django.shortcuts import render
from .models import Portfolio
import pdb

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects.order_by('-id')
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})