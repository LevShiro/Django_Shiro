def distinct_articles(articles):
    arr_articles = []
    for article in articles:
        arr_articles.append(article)
    for article in arr_articles:
        if arr_articles.count(article)>1:
            arr_articles.remove(article)
    return arr_articles