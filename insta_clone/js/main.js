/*
<script src="js/main.js"></script>를 html문서 상단에 놓는다면
html문서가 다 로드될 때까지 기다렸다가 얘를 실행해라

window.addEventListener('DOMContentLoaded', funtion(){
});
*/

const heart = document.querySelector('.heart_btn'); //자식 .sprite_outline_heart_icon을 가져오는 것보다 효율적
const header = document.querySelector('#header');
const sidebox = document.querySelector('.side_box');

heart.addEventListener('click', function(){
    heart.classList.toggle('on');
});

function resizeFunc(){
    if(pageYOffset >=10){
        //console.log(window.innerWidth); //화면의 좌우값 구하는 이너메소드
        let calcWidth = (window.innerWidth *0.5) + 160;
        console.log(calcWidth);
        sidebox.style.left = calcWidth + 'px'; //sidebox.style 스타일 접근
    }
}

function scrollFunc(){
    console.log(pageYOffset);
    if(pageYOffset>=10){
        header.classList.add('on');
        sidebox.classList.add('on');
        resizeFunc();
    }else{
        header.classList.remove('on');
        sidebox.classList.remove('on');
        sidebox.removeAttribute('style');
    }
}

window.addEventListener('scroll', scrollFunc);