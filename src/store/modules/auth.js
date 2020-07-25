import axios from 'axios'
// import {
//   encryptToken,
//   decryptToken
// } from '../../helpers/token'
import jwt from 'jsonwebtoken'


function checkTokenValidity(token) {
  if (token) {
    const decodedToken = jwt.decode(token)

    return decodedToken && (decodedToken.exp * 1000) > new Date().getTime()
  }
  return false
}

const state = {
  user: null
};
const getters = {
  user: (state) => state.user,
  authUser(state) {
    return state.user || null
  }
};
const actions = {
  loginWithUsernameAndPassword({
    commit
  }, formData) {
    const data = JSON.parse(JSON.stringify(formData))
    return axios.post('/api/v1/user/login/', data).then((response) => {
      const user = response.data
      // var token = encryptToken(user.access)
      // console.log(user)
      localStorage.setItem('user-jwt', user.token)
      commit('setAuthUser', user)
      return response
    }).catch((error) => {
      // console.log(error.response.data)
      return error
    })
  },
  registerUser({
    commit
  }, formData) {
    const data = JSON.parse(JSON.stringify(formData))
    return axios.post('/api/v1/user/register/', data)
    //   .then((response) => {
    //     return response
    //   }).catch((error) => {
    //     return error
    //   })
  },
  getAuthUser({
    commit,
    getters
  }) {
    const authUser = getters.authUser
    const token = localStorage.getItem('user-jwt')
    // const token = decryptToken(data)
    var formData = {
      token: token
    }
    const data = JSON.parse(JSON.stringify(formData))
    const isTokenValid = checkTokenValidity(token)
    console.log(isTokenValid)
    if (authUser && isTokenValid) {
      return Promise.resolve(authUser)
    } else if (isTokenValid) {
      console.log(token)
      return axios.post(`/api/v1/user/getuser/`, data)
        .then(response => {
          console.log(token)
          const user = response.data
          commit('setAuthUser', user)
          return response
        })
    }
  }
};
const mutations = {
  setAuthUser: (state, user) => {
    state.user = user;
  }
}


export default {
  state,
  getters,
  actions,
  mutations
}
