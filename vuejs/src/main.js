import Vue from 'vue'
import App from './App.vue'

import ApolloClient from 'apollo-boost'
import VueApollo from 'vue-apollo'
import { InMemoryCache } from "apollo-cache-inmemory";

const apolloClient = new ApolloClient({
  // You should use an absolute URL here
  uri: 'http://localhost:8000/graphql/',
  cache: new InMemoryCache({
    addTypename: true
  })
})


Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
})

new Vue({
  el: '#app',
  apolloProvider,
  render: h => h(App)
})
