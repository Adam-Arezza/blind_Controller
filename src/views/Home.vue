<template>
  <div class="home">
    <b-container fluid>
      <p>Set a time for the blinds to open or close</p>
      <b-row align-h="center" align-v="start">
        <input
          v-b-tooltip.hover
          title="Input the time you want the blinds to open"
          id="timeSetOpen"
          v-model="timeOn"
          type="time"
          min="1:00"
          max="24:00"
          placeholder="00:00"
        >
        <b-button class="manBtn" variant="warning" size="sm" @click="setTime('open')">Set Open Time</b-button>
      </b-row>
      <b-row align-h="center" align-v="start">
        <input
          v-b-tooltip.hover.left
          title="Input the time you want the blinds to Close"
          id="timeSetClose"
          v-model="timeOff"
          type="time"
          min="1:00"
          max="24:00"
          placeholder="00:00"
        >
        <b-button
          class="manBtn"
          variant="warning"
          size="sm"
          @click="setTime('close')"
        >Set Close Time</b-button>
      </b-row>
      <h3>Manual Controls</h3>
      <b-row align-h="center">
          <b-button class="manBtn" variant="primary" size="md" @click="blinds('open')">Open</b-button>
          <b-button class="manBtn" variant="primary" size="md" @click="blinds('close')">Close</b-button>
      </b-row>
        <p>Blinds are currently:</p>
        <p>{{currentState}}</p>
    </b-container>
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
          console.log("The response data is: " + Response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
    setTime(direction) {
      if (direction == "close") {
        var time = this.timeOff;
        axios
          .post("/blinds-auto", {
            setTime: time,
            command: direction
          })
          .then(Response => {
            this.currentTimeOff = Response.data;
            console.log(this.currentTimeOff)
          })
          .catch(error => {
            console.log(error);
          });
          return alert('Blinds will close at: ' + this.currentTimeOff)
      }
      if (direction == "open") {
        var time = this.timeOn;
        axios
          .post("/blinds-auto", {
            setTime: time,
            command: direction
          })
          .then(Response => {
            this.currentTimeOn = Response.data;
            console.log(this.currentTimeOn)
          })
          .catch(error => {
            console.log(error);
          });
          return alert('Blinds will open at: ' + this.currentTimeOn)
      }
    }
  }
};
</script>

<style>
#timeSetOpen,
#timeSetClose {
  border-radius: 5px;
  font-size: 1.5rem;
  margin: 15px;
}
.btn {
  margin: 15px;
}
.auto {
  background: rgb(182, 189, 197);
  border: 1px solid black;
  padding-top: 20px;
}
.home p {
  text-align: center;
  font-size: 1.5em;
}
.home h3 {
  text-align: center;
}
</style>

