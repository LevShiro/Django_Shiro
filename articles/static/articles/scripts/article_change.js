const change_block = document.getElementsByClassName('article_change_block')[0]
const article_block = document.getElementsByClassName('article-view')[0]

const button_viewChange = document.getElementById('article_change_button')
const button_viewArticle = document.getElementById('button_cancel_change_article')


button_viewArticle.addEventListener('click',function () {
    change_block.style.display = "none"
    article_block.style.display="flex"
})

button_viewChange.addEventListener('click',function () {
    change_block.style.display = "flex"
    article_block.style.display="none"
})
