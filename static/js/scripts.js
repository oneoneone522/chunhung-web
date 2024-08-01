const imgs=document.querySelectorAll('.header-slider ul img');
const prev_btn = document.querySelector('control-prev');
const next_btn = document.querySelector('control-next');

let n=2;

function changeSlide(){
    for (let i=0; i<imgs.length; i++){
        imgs[i].style.display='none';
    } imgs[n].style.display='block';
}
changeSlide();

prev_btn.addEventListenr('click', (e)=>{
    if (n>0){
        n--;
    }else{
        n=imgs.length-1
    }changeSlide();
})

next_btn.addEventListenr('click', (e)=>{
    if (n<imgs.length-1){
        n++;
    }else{
        n=0
    }changeSlide();
})
document.addEventListener("DOMContentLoaded", function() {
    // 获取按钮和侧边栏元素
    var btn = document.querySelector('.btn');
    var sidebar = document.querySelector('.sidebar');

    // 添加点击事件处理程序
    btn.addEventListener('click', function() {
        // 切换 btn 的 click 类
        btn.classList.toggle('click');
        // 切换 sidebar 的 show 类
        sidebar.classList.toggle('show');
    });
});
