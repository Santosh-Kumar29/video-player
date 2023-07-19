<template>
  <div>
    <textarea v-model="subtitleText" placeholder="Add subtitles..."></textarea>
    <button @click="addSubtitle">Add Subtitle</button>
    <div v-for="(subtitle, index) in subtitles" :key="index">
      <p>{{ subtitle.text }}</p>
      <button @click="removeSubtitle(index)">Remove</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["videoName"],
  data() {
    return {
      subtitleText: "",
      subtitles: [],
    };
  },
  methods: {
    addSubtitle() {
      const currentTime = this.$refs.videoPlayer.currentTime;
      const newSubtitle = {
        text: this.subtitleText,
        time: currentTime.toFixed(2),
      };
      this.subtitles.push(newSubtitle);
      this.subtitleText = "";
      this.$emit("subtitles-updated", this.videoName, this.subtitles);
    },
    removeSubtitle(index) {
      this.subtitles.splice(index, 1);
      this.$emit("subtitles-updated", this.videoName, this.subtitles);
    },
  },
};
</script>
