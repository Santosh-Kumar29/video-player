<template>
  <div>
    <input type="file" @change="onFileChange" />
    <video ref="videoPlayer" :src="videoUrl" controls></video>
  </div>
</template>

<script>
export default {
  data() {
    return {
      video: null,
      videoUrl: null,
    };
  },
  methods: {
    onFileChange(event) {
      this.video = event.target.files[0];
      this.videoUrl = URL.createObjectURL(this.video);
    },
  },
};
</script>
