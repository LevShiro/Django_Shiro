from django.shortcuts import render,redirect
from .models import Article,Comment
from django.views.decorators.csrf import csrf_protect
from .forms import ArticleForm,CommentForm,ChangeArticleForm
from .funcs import *


# Create your views here.
@csrf_protect
def view_article(request,article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id)
    form_comment = CommentForm()
    form_change = ChangeArticleForm()
    errors = dict()
    
    #лайки
    if "unlike" in request.POST:
        article.likes.remove(request.user)
    elif "like_up" in request.POST:
        article.likes.add(request.user)
    #комментарии
    elif 'public-comment-button' in request.POST:
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid() and form_comment.there_is_content():
            instance = form_comment.save(commit=False)
            instance.author_id = request.user
            instance.article_id = Article.objects.get(id=article_id)
            form_comment.save()
            return redirect('article',article_id)
        else: errors['null_comment'] = "Чтобы оставить коментарий, надо его написать в этом поле"
    #удаление комментария
    elif 'delete-comment' in request.POST:
        delete_comment = Comment.objects.get(id = request.POST.get('delete-comment'))
        delete_comment.delete()
        return redirect('article',article_id)
    # удаление записи
    elif "delete-article" in request.POST:
        article.pic.delete(False)
        article.delete()
        return redirect('home')
    elif 'change_article' in request.POST:
        form_change = ChangeArticleForm(request.POST,request.FILES)
        if form_change.is_valid():
            change_article_func(request.POST,form_change.cleaned_data['pic'],article)
    data = {'article': article,
            'comments':comments,
            'form_comment': form_comment,
            'form_change':form_change,
            'errors':errors}
    return render(request,"articles/article.html",data)
        
def article_add(request):
    if "public_article" in request.POST:
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            
            instance = form.save()
            article_id = instance.id
            return redirect('article',article_id)
    else:
        form = ArticleForm()
    data = {'form':form}
    return render(request,"articles/article_add.html",data)
    