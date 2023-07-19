<template>
  <div>
    <VideoUploader @video-uploaded="handleVideoUploaded" />
    <SubtitleEditor :videoName="videoName" @subtitles-updated="handleSubtitlesUpdated" />
    <video ref="videoPlayer" :src="videoUrl" controls></video>
    <div v-for="(subtitle, index) in subtitles" :key="index">
      <p>{{ subtitle.text }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import VideoUploader from "./components/VideoUploader.vue";
import SubtitleEditor from "./components/SubtitleEditor.vue";

export default {
  components: {
    VideoUploader,
    SubtitleEditor,
  },
  data() {
    return {
      video: null,
      videoUrl: null,
      videoName: "",
      subtitles: [],
    };
  },
  methods: {
    handleVideoUploaded(videoData) {
      this.video = videoData.file;
      this.videoName = videoData.name;
      this.videoUrl = URL.createObjectURL(this.video);
      this.getSubtitles();
    },
    handleSubtitlesUpdated(videoName, subtitles) {
      this.videoName = videoName;
      this.subtitles = subtitles;
      this.saveSubtitles();
    },
    getSubtitles() {
      axios
        .get(`http://127.0.0.1:8000/api/get_subtitles/${this.videoName}/`)
        .then((response) => {
          this.subtitles = response.data.subtitles;
        });
    },
    saveSubtitles() {
      const data = {
        videoId: this.videoName,
        subtitles: this.subtitles,
      };
      axios.post("http://127.0.0.1:8000/api/save_subtitles/", data);
    },
  },
};
</script>

<style>
textarea {
  width: 100%;
  height: 80px;
}
</style>
