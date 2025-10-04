from django import forms
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    pic = forms.ImageField(required=False)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-title-artice',
        'placeholder': 'Заголовок записи'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class':'input-text-article',
        'placeholder':'Текст записи'
    }))
    class Meta:
        model = Article
        fields = ["pic","title","text","author"]

class CommentForm(forms.ModelForm):
    content = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class': 'input-comment',
        'placeholder': 'Написать комментарий'
    }))
    def there_is_content(self):
        if self.cleaned_data['content'] != "":
            return True
        return False
    class Meta:
        model = Comment
        fields = ['article_id','author_id','content']
        
class ChangeArticleForm(forms.ModelForm):
    pic = forms.ImageField(required=False)
    class Meta:
        model = Article
        fields = ['pic']