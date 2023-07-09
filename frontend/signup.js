// form을 가져온다.
const form = document.querySelector("#signup-form");

// password 확인
const checkPassword = () =>{
    const formData = new FormData(form);
    const password1 = formData.get("password");
    const password2 = formData.get("password2");

    if(password1 === password2){
        return true;
    }else return false;
};


const handleSubmit = async(event) => {
    event.preventDefault(); // 리다이렉트 되는것을 막아줌
    const formData = new FormData(form); //const formData는 form data 안에 있는 form
    const sha256Password = sha256(formData.get('password')); //암호화 시키기
    
    // formdata를 가져와서 password값을 가져와서 암호화 후 서버로 전송
    formData.set('password',sha256Password);
    const div = document.querySelector("#info");// 비밀번호 불일치 시, div html id 값 불러와 컬러값과 텍스트 출력되도록


    //Data를 보내기 전에 password확인이 일치한지 추가
    if(checkPassword()){
        const res = await fetch('/signup',{
            method: "post",
            body : formData,
        });
        const data = await res.json();
        if(data === "200"){
            // div.innerText = "회원가입에 성공했습니다."; //비밀번호 일치하지 않다는 문구 뜨고 일치했을 떄, 없애주기위해
            // div.style.color = "blue";
            alert("회원 가입에 성공했습니다.");
            window.location.pathname = "/login.html"; // login시 로그인 페이지로 이동
        }
    }else{
        div.innerText = "비밀번호가 일치하지 않습니다.";
        div.style.color = "red";
    }

    const res = await fetch('/signup',{ 
        method:"post",
        body: formData,
    });
};


//event가 발생했을 때, handleSubmit 함수를 호출하겠다.
form.addEventListener("submit",handleSubmit);