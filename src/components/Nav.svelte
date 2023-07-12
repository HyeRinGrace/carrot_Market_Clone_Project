<!-- 모듈화 해서 컴포넌트로 다른곳도 사용할 수 있게 만듬 -->
<script>
  export let location;

  const moveToHome = () => {
    window.location.hash = "/"; //# 해시를 쓰고 있어서 hash를 써준다.
  };

  const moveToMyPage = () => {
    window.location.hash = "/my";
  };
</script>

<!-- footer 영역 -->
<footer>
  <!-- footer 안에 div로 한번 감싸준다. -->
  <div class="footer-block">
    <button class="footer-icons" on:click={moveToHome}>
      <div class="footer-icons__img">
        {#if location === "home"}
          <img src="assets/home.svg" alt="" />
        {:else}
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
            />
          </svg>
        {/if}
      </div>
      <div class="footer-icons__desc">홈</div>
    </button>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/document.svg" alt="" />
      </div>
      <div class="footer-icons__desc">동네생활</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/location.svg" alt="" />
      </div>
      <div class="footer-icons__desc">내 근처</div>
    </div>
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/communication.svg" alt="" />
      </div>
      <div class="footer-icons__desc">채팅</div>
    </div>
    <button class="footer-icons" on:click={moveToMyPage}>
      <div class="footer-icons__img">
        {#if location === "my"}
          <img src="assets/user2.svg" alt="" />
        {:else}
          <img src="assets/user.svg" alt="" />
        {/if}
      </div>
      <div class="footer-icons__desc">나의 당근</div>
    </button>
  </div>
</footer>
