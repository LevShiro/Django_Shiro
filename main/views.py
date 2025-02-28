from django.shortcuts import render
from django.contrib.auth import logout
from articles.models import Article
# Create your views here.
def home(request):
    articles = Article.objects.order_by('date')[:10]
    
    data = {'articles':articles,
            }
    return render(request,"main/articles.html",data)


def logout_user(request):
    logout(request)
    articles = Article.objects.order_by('date')[:10]
    data = {'articles':articles,
            }
    return render(request,"main/articles.html",data)