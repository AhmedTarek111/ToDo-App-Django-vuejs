import { createRouter, createWebHistory } from 'vue-router'
import taskview from '@/views/tasksview.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: taskview,
    },

  ]
})

export default router
