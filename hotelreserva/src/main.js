
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
if (process.env.NODE_ENV === 'production') {
    Vue.config.devtools = false;
  }
  

app.use(router)

app.mount('#app')
