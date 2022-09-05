import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/worldmap',
    name: 'Worldmap',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "WorldmapView" ,webpackpreFatch:true */ '../views/WorldmapView.vue')
  },
  {
    path: '/select',
    name: 'Select',
    component: () => import(/* webpackChunkName: "SelectView", webpackpreFatch:true */ '../views/SelectView.vue')
  },
  {
    path: '/result',
    name: 'Result',
    component: () => import(/* webpackChunkName: "ResultView", webpackpreFatch:true */ '../views/ResultView.vue')
  },
  {
    path: '/language',
    name: 'Language',
    component: () => import(/* webpackChunkName: "LanguageView", webpackpreFatch:true */ '../views/LanguageView.vue')
  },
  {
    path: '/weather',
    name: 'Weather',
    component: () => import(/* webpackChunkName: "WeatherView", webpackpreFatch:true */ '../views/WeatherView.vue')
  },
  {
    path: '/user',
    name: 'User',
    component: () => import(/* webpackChunkName: "UserView", webpackpreFatch:true */ '../views/UserView.vue')
  },
  {
    path: '/detailresult',
    name: 'detailresult',
    component: () => import(/* webpackChunkName: "DetailResultView", webpackpreFatch:true */ '../views/DetailResultView.vue')
  },
  {
    path: '/alluniv',
    name: 'alluniv',
    component: () => import(/* webpackChunkName: "AllUnivView", webpackpreFatch:true */ '../views/AllUnivView.vue')
  },
  {
    path: '/plot',
    name: 'plot',
    component: () => import(/* webpackChunkName: "AllUnivView", webpackpreFatch:true */ '../views/PlotView.vue')
  },
  {
    path: '/intro',
    name: 'intro',
    component: () => import(/* webpackChunkName: "WorldmapView", webpackpreFatch:true */ '../views/IntroTeamView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
