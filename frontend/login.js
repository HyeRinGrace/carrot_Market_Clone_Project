// form을 가져온다.
const form = document.querySelector("#login-form");

const handleSubmit = async(event) => {
    event.preventDefault(); // 리다이렉트 되는것을 막아줌
    const formData = new FormData(form); //const formData는 form data 안에 있는 form
    const sha256Password = sha256(formData.get('password')); //암호화 시키기
    // formdata를 가져와서 password값을 가져와서 암호화 후 서버로 전송
    formData.set('password',sha256Password);

    const res = await fetch('/login',{
        method: "post",
        body : formData,
    });
    const data = await res.json(); //요청을 받아서
    accessToken = data.access_token;
    window.localStorage.setItem('token',accessToken); // 로컬스토리지 이용
    // window.sessionStorage.setItem("token",accessToken); //세션 스토리지 이용

    alert("로그인되었습니다.");
    window.location.pathname = "/";

    //window.location.pathname = "/"; //root로 보내주기

    // const btn = document.createElement("button");
    // btn.innerText = "상품 가져오기";
    // btn.addEventListener("click", async()=>{
    //     const res = await fetch("/items",{
    //         headers:{
    //             Authorization : `Bearer${accessToken}`, // 서버가 받아서 응답해줄거임
    //         },
    //     });
    //     const data = await res.json();
    //     console.log(data);
    
    // })
    // infoDiv.appendChild(btn);
};


//event가 발생했을 때, handleSubmit 함수를 호출하겠다.
form.addEventListener("submit",handleSubmit);