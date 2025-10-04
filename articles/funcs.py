def change_article_func(POST,pic,article):
    if pic:
        article.pic.delete(False)
        article.pic = pic
    article.title = POST['change_article_title']
    article.text = POST['change_article_text']
    article.save()