from django.urls import path
from . import views
urlpatterns = [
    path("<int:article_id>",views.view_article,name="article"),
    path("add_article",views.article_add,name="add_article")
]