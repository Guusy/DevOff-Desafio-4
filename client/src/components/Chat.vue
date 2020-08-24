<template>
  <div>
    <div class="chat">
      <div
        v-for="userMessage in chat"
        :key="userMessage.message"
        class="chat-message-container"
        v-bind:class="{ 'chat-message-container--self': isMe(userMessage.user) }"
      >
        <div class="chat-message" v-bind:class="{ 'chat-message--self': isMe(userMessage.user) }">
          <div v-if="!isMe(userMessage.user)" class="message-name">{{ userMessage.user.name}}</div>
          <div class="message-content">{{userMessage.message}}</div>
        </div>
      </div>
    </div>
    <form v-on:submit.prevent="sendMessage">
      <input type="text" name="message" placeholder="Mensaje" v-model="message" />
      <button type="submit">Ingresar</button>
    </form>
  </div>
</template>

<script>
export default {
  methods: {
    sendMessage: function() {
      this.$socket.emit("send_message", this.message);
      this.message = "";
    },
    isMe: function(user) {
      return user.name === this.user;
    }
  },
  sockets: {
    new_message_on_chat: function(chat) {
      this.chat = chat;
    }
  },
  data: () => {
    return {
      message: "",
      chat: []
    };
  },
  props: {
    user: String
  }
};
</script>

<style scoped>
.chat-message-container {
    display: flex;
}
.chat-message-container--self{
    justify-content: flex-end;
}
.message-name {
  font-weight: bold;
  font-size: 14px;
}
.message-content {
  font-size: 12px;
}
.chat {
  background-color: white;
  padding: 1em;
  min-height: 200px;
  border: 0.5px solid black;
}
.chat-message {
  margin-top: 0.2em;
  border-radius: 5px;
  padding: 0.3em;
  background-color: lightgray;
}
.chat-message--self {
  background-color: aquamarine;
}
</style>