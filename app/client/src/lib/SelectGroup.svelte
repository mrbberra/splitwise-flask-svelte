<script lang="ts">
  export let groups: { id: string; name: string }[] = [];
  export let selectedGroup: { id: string; name: string } | undefined;

  let selectedGroupIdUnconfirmed: string;

  const confirmGroup = () => {
    selectedGroup = groups.find((group) => group.id === selectedGroupIdUnconfirmed);
  };
</script>

{#if groups.length > 0}
  <div class="container mt-5">
    <h4>First, select a Splitwise group:</h4>
    <div class="btn-group" role="group" aria-label="Group selection">
      {#each groups as group}
        <input
          type="radio"
          class="btn-check"
          name="group-select"
          id="group-{group.id}"
          autocomplete="off"
          value={group.id}
          bind:group={selectedGroupIdUnconfirmed}
        />
        <label class="btn" for="group-{group.id}">{group.name}</label>
      {/each}
    </div>
    <div>
      <button
        type="button"
        class="btn btn-primary mt-3"
        disabled={!selectedGroupIdUnconfirmed}
        on:click={confirmGroup}
      >
        Continue
      </button>
    </div>
  </div>
{/if}
