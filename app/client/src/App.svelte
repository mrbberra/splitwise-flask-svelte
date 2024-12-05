<script lang="ts">
  type UserInfo = {
    firstName?: string;
    lastName?: string;
    id: string;
    email: string;
  };

  const getUserInfoPromise = async () => {
    const response = await fetch("/api/me");
    const data = await response.json();
    return data as UserInfo;
  };
</script>

{#await getUserInfoPromise()}
  <p>Loading...</p>
{:then userInfo}
  <nav class="navbar fixed-top bg-body-tertiary">
    <div class="container-fluid d-flex justify-content-space-between">
      <h3>Hi, {userInfo.firstName || userInfo.email}</h3>
      <a href="/logout">Logout</a>
    </div>
  </nav>
{:catch error}
  <p>{error.message}</p>
{/await}
