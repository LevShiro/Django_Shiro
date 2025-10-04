const articles = document.getElementsByClassName('article')

let arr_articles = Array.from(articles)


arr_articles.sort((a,b)=>
    ((Number(a.getElementsByClassName('score_likes')[0].innerHTML) + Number(a.getElementsByClassName('score_comments')[0].innerHTML))-
    (Number(b.getElementsByClassName('score_likes')[0].innerHTML) + Number(b.getElementsByClassName('score_comments')[0].innerHTML))
))

arr_articles.forEach(function(element,i) {
    element.style.order = -i;
})


