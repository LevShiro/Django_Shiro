from django.shortcuts import render
from django.contrib.auth import logout
from articles.models import Article
from django.db.models import Q,F
from .funcs import distinct_articles

# Create your views here.
def home(request):
    articles = Article.objects.all()
    data = {'articles':articles}
    
    
    return render(request,"main/articles.html",data)
    


def logout_user(request):
    logout(request)
    articles = Article.objects.all()
    data = {'articles':articles}
    return render(request,"main/articles.html",data)

def article_search(request):
    query = request.GET.get('article_search','')
    if query!='':
                
                articles = Article.objects.filter(
            Q(text__contains=query) | Q(title__contains=query)
        ).all()
    else: 
        articles = Article.objects.all()
    context={
        'articles':articles
    }
    return render(request,'main/particles/articles_searching.html',context)

