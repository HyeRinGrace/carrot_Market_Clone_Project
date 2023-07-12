<script>
  import Nav from "../components/Nav.svelte";
  import { user$ } from "../store";

  const logout = () => {
    // 유저정보를 비워주고 로컬스토리지를 비워주고
    user$.set(null);
    localStorage.removeItem("token");
  };
</script>

<div>나의 당근</div>
<button on:click={logout}>로그아웃</button>

<Nav location="my" />

<style>
  button {
    cursor: pointer;
    margin: 10px;
    border: 1px solid rgb(0, 0, 0, 0.3);
  }
</style>
