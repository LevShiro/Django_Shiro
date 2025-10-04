document.querySelector('.input-comment').addEventListener('input', function (event) {
    this.style.height = '24px';
    this.style.height = `${this.scrollHeight}px`;
    const scrollY = window.scrollY;
    window.scrollBy(0, scrollY)
    
});
document.querySelector('.input-text-article').addEventListener('input', function () {
    this.style.height = '19px';
    this.style.height = `${this.scrollHeight}px`;
    const scrollY = window.scrollY;
    window.scrollBy(0, scrollY)
});