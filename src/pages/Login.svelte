<script>
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
  import { user$ } from "../store";

  const provider = new GoogleAuthProvider();
  const auth = getAuth();

  const loginWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
      const user = result.user;
      user$.set(user);
      localStorage.setItem("token", token);
    } catch (error) {
      console.error(error);
    }
  };
</script>

<div>
  <!-- {#if $user$}
    <div>{$user$?.displayName}로그인됨</div> -->
  <!--$ 표시를 해줘야 그 안에 있는 값을 보여줄 수 있다. -->
  <div>로그인하기</div>
  <button class="login-btn" on:click={loginWithGoogle}>
    <img
      class="google-img"
      src="https://cdn-icons-png.flaticon.com/512/2991/2991148.png"
      alt=""
    />
    <div>Google로 시작하기</div>
  </button>
</div>

<style>
  .login-btn {
    width: 200px;
    height: 30px;
    border: 1px solid gray;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    border-radius: 3px;
  }

  .google-img {
    width: 20px;
  }
</style>
