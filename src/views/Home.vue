<template>
  <div class="home row no-gutters justify-content-center">
    <div class="auto col-sm-8">
      <p>Set a timer for the blinds to open or close</p>
      <input
        v-b-tooltip.hover
        title="Input the time you want the blinds to open"
        id="timeSet"
        v-model="timeOn"
        type="time"
        min="1:00"
        max="24:00"
        placeholder="00:00"
      >
      <b-button class="manBtn" variant="warning" size="md" @click="setTime('open')">Set Open Time</b-button>
      <p>Open time setting: {{currentTimeOn}}</p>
      <input
        v-b-tooltip.hover.left
        title="Input the time you want the blinds to Close"
        id="timeSet"
        v-model="timeOff"
        type="time"
        min="1:00"
        max="24:00"
        placeholder="00:00"
      >
      <b-button class="manBtn" variant="warning" size="md" @click="setTime('close')">Set Close Time</b-button>
      <p>Close time setting: {{currentTimeOff}}</p>
    </div>
    <br>
    <div class="auto col">
      <b-button
        class="manBtn"
        variant="primary"
        size="md"
        @click="blinds('open')"
      >Open</b-button>
      <b-button
        class="manBtn"
        variant="primary"
        size="md"
        @click="blinds('close')"
      >Close</b-button>
      <br>
      <p>current state: {{currentState}}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      timeOn: "",
      timeOff: "",
      currentState: "",
      currentTimeOn: "",
      currentTimeOff: ""
    };
  },
  methods: {
    blinds(direction) {
      axios
        .post("/blinds-manual", { control: direction })
        .then(Response => {
          this.currentState = Response.data;
          console.log('The response data is: ' + Response.data)
        })
        .catch(error => {
          console.log(error);
        });
    },
    setTime(direction) {
      if(direction == 'close'){
        var time = this.timeOff;
      axios
        .post("/blinds-auto", {
          setTime: time,
          command: direction
        })
        .then(Response => {
          this.currentTimeOff = Response.data;
        })
        .catch(error => {
          console.log(error);
        });
      }
      if(direction == 'open'){
        var time = this.timeOn;
      axios
        .post("/blinds-auto", {
          setTime: time,
          command: direction
        })
        .then(Response => {
          this.currentTimeOn = Response.data;
        })
        .catch(error => {
          console.log(error);
        });
      }
    }
  }
};
</script>

<style>
#timeSet {
  padding: 5px;
  border-radius: 5px;
  font-size: 1.5rem;
  margin: 15px;
}
p {
  font-size: 1.25rem;
  padding: 10px;
}
.auto {
  background: rgb(182, 189, 197);
  border: 1px solid black;
  padding-top: 20px;
}
.manBtn{
  margin: 5px;
  border-radius: 0 !important;
  border: 1px solid black !important;
}

</style>

