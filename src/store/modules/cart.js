import axios from "axios";

const state = {
  carts: []
};
const getters = {
  carts: state => state.carts
};
const actions = {
  async addTocart({ commit }, data) {
    const JsonData = JSON.parse(JSON.stringify(data));
    const response = await axios.post("/api/v1/cart/view-set/", JsonData);
    console.log(response);
    return response;
  },
  async cart({ commit }, data) {
    // const JsonData = JSON.parse(JSON.stringify(data));
    // console.log(JsonData);
    // const authUser = getters.authUser.id;
    if (data !== "null") {
      const response = await axios.get(`/api/v1/cart/cartdetial/${data}`);
      console.log(response.data);
      commit("setCarts", response.data);
      return response;
    }
  }
};
const mutations = {
  setCarts: (state, carts) => {
    console.log(carts);
    state.carts = carts;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
