<template>
  <div>
    <form v-if="!logged" v-on:submit.prevent="enterChat">
      <input type="text" name="name" placeholder="Ingresa tu nickname" v-model="nickname" />
      <button type="submit">Ingresar</button>
    </form>
    <div v-if="logged" class="chat-container">
      <div class="connected-users-container">
        <div>

        </div>
        Usuarios conectados
        <div v-for="user in currentUsers" :key="user.name">{{user.name}}</div>
      </div>
      <Chat v-bind="{user: nickname}" />
    </div>
  </div>
</template>

<script>
import Chat from "./Chat.vue";

export default {
  name: "Login",
  components: {
    Chat
  },
  sockets: {
    connect: function() {
      console.log("socket connected");
    },
    current_users: function(room) {
      console.log("current_users", room);
      this.currentUsers = Object.keys(room).map(userId => room[userId]);
    }
  },
  data() {
    return {
      currentUsers: [],
      logged: false,
      nickname: ""
    };
  },
  methods: {
    enterChat: function() {
      this.$socket.emit("connect_room", this.nickname);
      this.logged = true;
    }
  },
  props: {
    msg: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.chat-container {
  display: flex;
  background-color: violet;
  padding: 1em;
}
.connected-users-container{
  padding: 0.5em;
  margin-right: 0.5em;
  background-color: white;
  border: 0.5px solid black;
  border-radius: 5px;
}
</style>
