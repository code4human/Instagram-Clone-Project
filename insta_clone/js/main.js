/*
<script src="js/main.js"></script>를 html문서 상단에 놓는다면
html문서가 다 로드될 때까지 기다렸다가 얘를 실행해라

window.addEventListener('DOMContentLoaded', funtion(){
});
*/

//const heart = document.querySelector('.heart_btn'); //자식 .sprite_outline_heart_icon을 가져오는 것보다 효율적
const header = document.querySelector('#header');
const sidebox = document.querySelector('.side_box');
const variableWidth = document.querySelectorAll('.contents_box .contents'); //.contents_box안에 있는 .contents
const delegation = document.querySelector('.contents_box');

heart.addEventListener('click', function(){
    //heart.classList.toggle('on');  //delegationFunc로 이동
});

function delegationFunc(e){ //event객체를 받음
    //console.log(e.target);
    let elem = e.target;
    console.log(elem);

    //잘못 클릭시
    //data-name이 없으면
    while(!elem.getAttribute('data-name')){
        elem = elem.parentNode; //요소의 부모노드를 찾는다. 있을 때까지 찾아 올라간다.
        if(elem.nodeName === 'BODY'){ //무한으로 올라가면 안된다. 찾아 올라가다가 BODY를 만난다면
            elem = null;  //멈추게 하기 위해 null을 넣는다.
            return; // 그리고 함수를 끝낸다.
        }
    }

    if(elem.matches('[data-name="heartbeat"]')){
        //클릭한 엘리먼트의 대상의 데이터네임 속성이 heartbeat를 가지고 있으면 실행
        console.log('하트');
    }else if(elem.matches('[data-name="bookmark"]')){
        console.log('북마크');
    }else if(elem.matches('[data-name="share"]')){
        console.log('공유');
    }else if(elem.matches('[data-name="more"]')){
        console.log('더보기');
    }
    elem.classList.toggle('on');
}

function resizeFunc(){
    console.log('resize!!')
    if(pageYOffset >=10){
        //console.log(window.innerWidth); //화면의 좌우값 구하는 이너메소드
        let calcWidth = (window.innerWidth *0.5) + 160;
        console.log(calcWidth);
        sidebox.style.left = calcWidth + 'px'; //sidebox.style 스타일 접근
    }
    if(matchMedia('screen and (max-width : 800px)').matches){  //스크린 좌우가 800px이하로 내려가면 실행
        //variableWidth.style.width = window.innerWidth -20 + 'px'; 을 querySelectorAll('.contents_box .contents')로 잡아서  배열로 
        for(let i=0; i<variableWidth.length; i++){
            variableWidth[i].style.width = window.innerWidth -20 + 'px';
        }
        
    }else{
        //variableWidth.removeAttribute('style');
        for(let i=0; i<variableWidth.length; i++){
            //variableWidth[i].removeAttribute('style');
            if(window.innerWidth > 600){
                variableWidth[i].removeAttribute('style');
            }
        }
    }

    
}

function scrollFunc(){
    console.log(pageYOffset);
    if(pageYOffset>=10){
        header.classList.add('on');

        if(sidebox){ //다른 html 만들 때 sidebox없어서 오류 뜨는거 방지 
            sidebox.classList.add('on');
        }
        resizeFunc();
    }else{
        header.classList.remove('on');

        if(sidebox){
            sidebox.classList.remove('on');
            sidebox.removeAttribute('style');
        }
    }
}

//새로고침이 될 때마다 그대로의 위치가 아니라 스크롤이 맨 위로 올라가도록
setTimeout(function(){ //setTimeout은 타이머
    scrollTo(0,0); //0.01초 만에 스크롤 위치가 0.0으로 돌아가라.
},100);


//.contents_box가 다른 문서에 없을 경우 대비
if(delegation){
    delegation.addEventListener('click', delegationFunc);
}

window.addEventListener('resize', resizeFunc);
window.addEventListener('scroll', scrollFunc);
