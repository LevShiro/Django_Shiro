document.querySelector('.input-comment').addEventListener('input', function () {
    this.style.height = '16px';
    this.style.height = `${this.scrollHeight}px`;
});
document.querySelector('.input-text-article').addEventListener('input', function () {
    this.style.height = '19px';
    this.style.height = `${this.scrollHeight}px`;
});