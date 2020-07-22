import axios from 'axios'
// import jwt from 'jsonwebtoken'


// function checkTokenValidity(token) {
//   if (token) {
//     const decodedToken = jwt.decode(token)

//     return decodedToken && (decodedToken.exp * 1000) > new Date().getTime()
//   }
//   return false
// }

const state = {
  user: null
};
const getters = {
  user: (state) => state.user
};
const actions = {
  loginWithUsernameAndPassword({
    commit
  }, formData) {
    const data = JSON.parse(JSON.stringify(formData))
    return axios.post('/api/v1/user/login/', data).then((response) => {
      const user = response.data
      localStorage.setItem('user-jwt', user.access)
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
