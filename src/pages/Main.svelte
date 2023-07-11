<script>
  let hour = new Date().getHours();
  let min = new Date().getMinutes();
</script>

<header>
  <div class="info-bar">
    <div class="info-bar__time">{hour}:{min}</div>
    <div class="info-bar__icons">
      <!-- 구글에서 검색한 이미지 svg 파일 적용 alt 뒤에는 원래 뭐였는지 그냥 표시하는 용어 -->
      <img src="assets/chart-bar.svg" alt="chartbar" />
      <img src="assets/wifi-bar.svg" alt="wifi" />
      <img src="assets/battery-bar.svg" alt="battery" />
    </div>
  </div>
  <div class="menu-bar">
    <div class="menu-bar__location">
      <!-- 텍스트부분은 div으로 주고, 이미지는 하단 svg 파일 적용 -->
      <div>역삼1동</div>
      <!-- 세로로 폰트가 세워져서 div로 감싸주고, 중앙배열을 위해 class 화시켜줌 -->
      <div class="menu-bar__location-icons">
        <img src="assets/down-bar.svg" alt="down" />
      </div>
    </div>
    <!-- 메뉴 아이콘들 구글에서 검색한 이미지 svg 파일 적용 -->
    <div class="menu-bar__icons">
      <img src="assets/glass-bar.svg" alt="glass" />
      <img src="assets/menu-bar.svg" alt="menu" />
      <img src="assets/alarm-bar.svg" alt="alarm" />
    </div>
  </div>
</header>

<!-- main 영역 -->
<main>
  <!-- java script로 만들어줄거임 index.js-->
  <a class="write-btn" href="#/write">+글쓰기</a>
</main>

<!-- footer 영역 -->
<footer>
  <!-- footer 안에 div로 한번 감싸준다. -->
  <div class="footer-block">
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/home.svg" alt="home" />
      </div>
      <div class="footer-icons__desc">홈</div>
    </div>
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
    <div class="footer-icons">
      <div class="footer-icons__img">
        <img src="assets/user.svg" alt="" />
      </div>
      <div class="footer-icons__desc">나의 당근</div>
    </div>
  </div>
</footer>
<div class="media-info-msg">화면 사이즈를 줄여주세요.</div>

<style>
  .info-bar__time {
    color: black;
  }
</style>
