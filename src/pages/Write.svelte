<!-- svelet는 자바스크립트 파일 맨 위에 -->
<script>
  import { getDatabase, ref, push } from "firebase/database";
  import Nav from "../components/Nav.svelte";
  import {
    getStorage,
    ref as refImage,
    uploadBytes,
    getDownloadURL,
  } from "firebase/storage";
  import MyPage from "./MyPage.svelte";

  let title;
  let price;
  let description;
  let place;
  let files;

  const storage = getStorage();
  const db = getDatabase();

  function writeUserData(imgUrl) {
    push(ref(db, "items/"), {
      title,
      price,
      description,
      place,
      insertAt: new Date().getTime(),
      imgUrl,
    });
    alert("글쓰기 완료");
    window.location.hash = "/"; //글쓰기 완료 후 홈으로 이동
  }

  const uploadFile = async () => {
    const file = files[0];
    const name = file.name;
    const imgRef = refImage(storage, name);
    await uploadBytes(imgRef, file);
    const url = await getDownloadURL(imgRef);
    return url;
  };

  const handleSubmit = async () => {
    const url = await uploadFile(); //업로드 파일된 URL을 받고
    writeUserData(url); //user데이터 업데이트
  };
</script>

<form id="write-form" on:submit|preventDefault={handleSubmit}>
  <!-- DB ID 값과 동일하게 하는 것이 좋음 -->
  <div>
    <label for="image">이미지</label>
    <input type="file" bind:files id="image" name="image" />
  </div>
  <div>
    <label for="title">제목</label>
    <input type="text" id="title" name="title" bind:value={title} />
  </div>
  <div>
    <label for="price">가격</label>
    <input type="number" id="price" name="price" bind:value={price} />
  </div>
  <div>
    <label for="description">설명</label>
    <input
      type="text"
      id="description"
      name="description"
      bind:value={description}
    />
  </div>
  <div>
    <label for="place">장소</label>
    <input type="text" id="place" name="place" bind:value={place} />
  </div>
  <div>
    <button class="write-button" type="submit"> 글쓰기 완료!</button>
  </div>
</form>

<Nav location="write" />

<style>
  .write-button {
    background-color: rgb(49, 65, 59);
    margin-top: 10px;
    border-radius: 10px;
    padding: 5px 12px 5px 12px;
    color: white;
    cursor: pointer;
  }
</style>
