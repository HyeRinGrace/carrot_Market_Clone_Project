const form = document.getElementById("write-form");//와 이거 쿼리 셀렉터로 줘서 안됐음
// getElementById으로 주니깐 바로 된다...


const handleSubmitForm = async(event) => {
    event.preventDefault();

    //body 변수 선언 FormDate(form)
    const body = new FormData(form);
    // 시간값을 넣어주는 소스 코드
    // fotm 데이터를 보낼때 세계시간 기준으로 보냄
    body.append('insertAt',new Date().getTime());
    // 에러처리
    try{
        const res = await fetch('/items',{
        method:'POST',
        body,
    });
    const data = await res.json();
    if(data === '200') window.location.pathname ="/";
    }catch(e){
        console.error(e);
    }

};

form.addEventListener("submit", handleSubmitForm);

