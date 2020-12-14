/* eslint-disable */

const routes = [
  {
    path: '/', component: () => import('layouts/Layout.vue'),
      children: [
        { path: '', component: () => import('pages/GetNip.vue') }
      ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
