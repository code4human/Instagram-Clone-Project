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
const hidden_menu = document.querySelector('.hidden_menu');

/*
heart.addEventListener('click', function(){
    //heart.classList.toggle('on');  //delegationFunc로 이동
});
*/

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

        //제이쿼리 ajax 통신
        let pk = elem.getAttribute('name');
        $.ajax({
            type: 'POST', 
            url: 'data/like.json', //통신 가능한 url. json데이터를 통해 받을 것이므로 data라는 폴더 생성.
            data: {pk}, //primary key를 통해 넘버링을 찍고, 유저들이 가지고 있는 pk을 통해 갱신을 통해 고유번호를 찍는 등
                        // data: {pk} 였는데 pk is not defined이어서 그냥 숫자 data: {37}로 바꿈
                        // Unexpected token '}'이어서 data: 37로 바꿈
                        //pk를 변수로 받아옴
            dataType: 'json', //내가 보낸 애가 어떤 타입으로 들어올건지
            success: function(response){ //통신이 완료되면 response객체를 받아옴. data/like.json에 있는 데이터
                let likeCount = document.querySelector('#like-count-37'); //#like-count37에 좋아요라는 글자를 넣을 것. 백엔드에서는 pk를 받아서 변수처리 한다. document.querySelector('#like-count37-' +pk)이렇게 작업을 원래 하지만 우리는 데이터가 없으니.
                likeCount.innerHTML = '좋아요' + response.like_count + '개';
            },
            
            error: function(request, status, error){ //ajax통신 에러 났을 때 처리. request, staus 매개변수를 받는다.
                alert('로그인이 필요합니다.');
                window.location.replace('https://www.naver.com'); //백 딴에서는 다시 회원가입 창으로 돌아가게 하기 위해 window.location.replace('accounts/login') 이런식으로 받음. 우리는 넘어갈 곳이 없으니 
            }
            
        });

    }else if(elem.matches('[data-name="bookmark"]')){
        console.log('북마크');

        //pk값을 받아오는 법
        let pk = elem.getAttribute('name');
        $.ajax({
            type:'POST',
            url: 'data/bookmark.json',
            data: {pk},
            dataType: 'json',
            success: function(response){
                let bookmarkCount = document.querySelector('#bookmark-count-'+pk); 
                bookmarkCount.innerHTML = '북마크' + response.bookmark_count + '개'; //돌아오는 response에다 
            },
            
            error: function(request, status, error){ //ajax통신 에러 났을 때 처리. request, staus 매개변수를 받는다.
                alert('로그인이 필요합니다.');
                window.location.replace('https://www.naver.com'); //백 딴에서는 다시 회원가입 창으로 돌아가게 하기 위해 window.location.replace('accounts/login') 이런식으로 받음. 우리는 넘어갈 곳이 없으니 
            }
            
        });
    }else if(elem.matches('[data-name="comment"]')){ //comment는 게시 버튼을 누르고 달리게 됨. <div class="upload_btn m_text"
        let comment = document.querySelector('#add-comment-post-37 > input[type=text]').value; //#add-comment-post-37 안에 있는 input의 타입이 text인 친구의 value값(input에 쓴 글자들)을 가져온다. #add-comment-post-37은 input위에 <div class="comment_field" 에 넣어준다.
        console.log(comment);

        if(comment.length > 140){
            alert('댓글은 최대 140자 입력 가능합니다. 현재 글자수 : ' + comment.length);
            return;
        }

        $.ajax({
            type: 'POST',
            url: './comment.html', //댓글은 DOM을 하나하나씩 쏘는 것이므로, 데이터타입을 html로 받는다.
            data: {'pk': 37,
                    'content': comment,},
            dataType: 'html',
            success: function(data){
                document.querySelector('#comment-list-ajax-post-37').insertAdjacentHTML('afterbegin',data); //글자가 찍힐 곳을 정해야 한다. 댓글창 class="comment"에 삽입.  insertAdjacentHTML은 html문서에 태그 등 삽입
            }, 
            error: function(request, status, error){ 
                alert('문제가 발생했습니다.');
                window.location.replace('https://www.naver.com'); 
            }
        });

        document.querySelector('#add-comment-post-37 > input[type=text]').value='' //게시를 클릭하고 댓글 업로드 되면 input창에 있는 내용은 지우기
    }else if(elem.matches('[data-name="comment-delete"]')){
        $.ajax({
            type: 'POST',
            url: 'data/delete.json',
            data: {
                'pk':37,
                //통신으로 개발하면 csrf토큰이라는 걸 받게 된다. 이건 장고에서 보안을 위해 암호화시키는 방법이다. 그 부분은 생략하겠다.
            },
            dataType:'json',
            success:function(response){
                if(response.status){ //delete.json에서 status를 1로 지정함. 나중에 백엔드 딴에서 0, 1이냐에 따라 삭제여부를 설정가능
                    let comt = document.querySelector('.comment-detail');
                    comt.remove();
                }
            },
            error: function(request, status, error){ 
                alert('문제가 발생했습니다.');
                window.location.replace('https://www.naver.com'); 
            }
        });
    }else if(elem.matches('[data-name="follow"]')){
        $.ajax({
            type:'POST',
            url: 'data/follow.json',
            data: {
                'pk':37,
            },
            dataType:'json',
            success: function(response){
                if(response.status){
                    document.querySelector('input.follow').value="팔로잉";  //follow가 붙은 input찾음
                }else{
                    document.querySelector('input.follow').value="팔로워";
                }
                //value값을 바꿔주는 이유는 input태그의 submit이라는 태그를 활용할 것이기 때문.
                //submit은 버튼인데 value값에 따라 글자가 바뀐다.
            },
            error: function(request, status, error){ 
                alert('문제가 발생했습니다.');
                window.location.replace('https://www.naver.com'); 
            }
        })
    }



    else if(elem.matches('[data-name="share"]')){
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
    if(matchMedia('screen and (max-width : 1000px)').matches){
        hidden_menu.style.display = "block"; //css @media screen and (max-width:1000px)일 때 side_box가 none이므로 맞춰줌
        
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
    }else{
        hidden_menu.removeAttribute('style');
    }
}

function scrollFunc(){
    let scrollHeight = pageYOffset + window.innerHeight; //어느정도 스크롤 됐는지
    let documentHeight = document.body.scrollHeight; //전체 도큐멘트의 높이값. document의 body로 접근해야함 
    console.log('scrollHeight : ' + scrollHeight);
    console.log('documentHeight :' + documentHeight);

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

    if(scrollHeight >= documentHeight){
        let page = document.querySelector('#page').value; //#page의 밸류값을 받는다.
        //page는 ajax통신이 얼만큼 되고 남아있는 페이지의 개수가 몇개인지 설정
        //어느 정도 도달하면 더이상 무한 스크롤 되지 않게 하기 위해.
        //callMorePostAjax 함수를 만든다.
        document.querySelector('#page').value = parseInt(page) + 1;

        callMorePostAjax(page);

        if( page > 5 ){ //callMorePostAjax 함수도 끝내기 위해 callMorePostAjax 함수에도 넣어준다.
            return;
        }
    }
}

function callMorePostAjax(page){

    if( page > 5 ){ 
        return;
    }

    $.ajax({
        type: 'POST',
        url: './post.html',
        data:{
            'page':page,
        },
        dataType: 'html',
        success: addMorePostAjax,
        error: function(request, status, error){ 
            alert('문제가 발생했습니다.');
            window.location.replace('https://www.naver.com'); 
        }
    })
}

function addMorePostAjax(data){
    //돌아오는 html을 어디에 뿌려줄지 설정 
    //뿌려주는 위치는 contents_box 안에 article로 하나씩 넣어주면 된다.
    //contents_box는 맨 위 글로벌 변수로 delegation으로 받아놓음
    delegation.insertAdjacentHTML('beforeend', data);
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
