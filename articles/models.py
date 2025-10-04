from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True,blank=True,)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,default=None)
    pic = models.ImageField(upload_to="articles/pic",blank=True,null=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    def score_likes(self):
        return len(list(self.likes.all()))
    def score_comments(self):
        return Comment.objects.filter(article_id=self.pk).count()
    def users_liked(self):
        return list(self.likes.all())

    def __str__(self):
        return self.title
class Comment(models.Model):
    class Meta:
        db_table = "comments"
    article_id = models.ForeignKey(Article,on_delete=models.CASCADE,blank=True)
    author_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.autor_id.username