<script lang="ts">
  const handleSubmit = async (e: SubmitEvent) => {
    const formData = new FormData(e.target as HTMLFormElement);
    const response = await fetch("/api/upload", {
      method: "POST",
      body: formData,
    });
  };
</script>

<form method="POST" enctype="multipart/form-data" on:submit|preventDefault={handleSubmit}>
  <div class="input-group mb-3">
    <input type="file" class="form-control" id="file-submission" />
  </div>
  <input class="btn btn-submit btn-primary" type="submit" value="Upload" />
</form>
