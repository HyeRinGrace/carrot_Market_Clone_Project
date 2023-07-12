<script>
  import { getDatabase, ref, onValue } from "firebase/database";
  import Nav from "../components/Nav.svelte";
  import { onMount } from "svelte";
  import MyPage from "./MyPage.svelte";

  let hour = new Date().getHours();
  let min = new Date().getMinutes();

  $: items = [];
  const calcTime = (timestamp) => {
    const curTime = new Date().getTime() - 9 * 60 * 60 * 1000;
    const time = new Date(curTime - timestamp);
    const hour = time.getHours();
    const minute = time.getMinutes();
    const second = time.getSeconds();

    if (hour > 0) return `${hour}시간 전`;
    else if (minute > 0) return `${minute}분 전`;
    else if (second > 0) return `${second}초 전`;
    else if (second == 0) "방금 전";
  };

  const db = getDatabase();
  const itmesRef = ref(db, "items/");

  onMount(() => {
    // onmount화면이 보여질때마다 실행되게끔 만듬
    onValue(itmesRef, (snapshot) => {
      //onvlaue 실시간으로 값을 가져옴
      const data = snapshot.val();
      items = Object.values(data).reverse(); //reverse 하면 시간순으로 정렬해줌
    });
  });
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

{#each items as item}
  <div class="item-list">
    <div class="itme-list__img" />
    <img alt={item.title} src={item.imgUrl} />
    <div class="item-list__info">
      <div class="item-list__info-title">{item.title}</div>
      <div class="item-list__info-meta">
        {item.place}
        {calcTime(item.insertAt)}
      </div>
      <div class="item-list__info-price">{item.price}</div>
      <div class="item-list__info-description">{item.description}</div>
    </div>
  </div>
{/each}

<Nav location="home" />

<div class="media-info-msg">화면 사이즈를 줄여주세요.</div>

<style>
  .info-bar__time {
    color: black;
  }
</style>
