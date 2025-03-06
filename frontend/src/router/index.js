import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/LoginView.vue'
import EmailInput from '../pages/EmailInput.vue'
import LoginView from "@/pages/LoginView.vue";
import VerifyView from "@/pages/VerifyView.vue";

const routes = [
  {
    path: '/',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/email',
    name: 'EmailInput',
    component: EmailInput
  },
  {
    path: '/verify/:email',
    name: 'VerifyView',
    component: VerifyView
  }
]
// import TimeTable from '@/components/TimeTable.vue'
// import MyReservation from '@/views/MyReservation.vue'
// import RoomDetails from '@/views/RoomDetails.vue'
// import RoomManagement from '@/views/RoomManagement.vue'
// import Index from '@/Index.vue'


// const routes = [
//   { path: '/', name: 'Index', component: Index },
//   { path: '/room/:id', name: 'RoomDetails', component: RoomDetails, props: true },
//   { path: '/my-reservation', name: 'MyReservation', component: MyReservation },
// >>>>>>> main
// ]

const router = createRouter({
  history: createWebHistory(),
<<<<<<< frontend-dev-for-login-module
  routes
})

export default router
=======
  routes,
})

export default router
