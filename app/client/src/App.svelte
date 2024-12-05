<script lang="ts">
  import SelectGroup from "./lib/components/SelectGroup.svelte";
  import FileUploader from "./lib/components/FileUploader.svelte";
  import type { UserInfo, Group } from "./lib/types";

  const getUserInfoPromise = async () => {
    const response = await fetch("/api/me");
    const data = await response.json();
    return data as UserInfo;
  };

  let selectedGroup: Group;
  let uploadedFile: File;
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
  {:else if !uploadedFile}
    <FileUploader />
  {/if}
{:catch error}
  <p>{error.message}</p>
{/await}
