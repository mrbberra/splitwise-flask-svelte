<script lang="ts">
  import SelectGroup from "./lib/SelectGroup.svelte";

  type Group = {
    id: string;
    name: string;
  };
  type UserInfo = {
    firstName?: string;
    lastName?: string;
    id: string;
    email: string;
    groups: Group[];
  };

  const getUserInfoPromise = async () => {
    const response = await fetch("/api/me");
    const data = await response.json();
    return data as UserInfo;
  };

  let selectedGroup: Group;
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
  {#if !selectedGroup}
    <SelectGroup groups={userInfo.groups} bind:selectedGroup />
  {:else}
    <p>Selected group: {selectedGroup.name}</p>
  {/if}
{:catch error}
  <p>{error.message}</p>
{/await}
