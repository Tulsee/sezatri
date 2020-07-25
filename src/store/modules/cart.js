import axios from "axios";

const state = {};
const getters = {};
const actions = {
  async addTocart({ commit }, data) {
    const JsonData = JSON.parse(JSON.stringify(data));
    const response = await axios.post("/api/v1/cart/view-set/", JsonData);
    console.log(response);
  }
};
const mutations = {};

export default {
  state,
  getters,
  actions,
  mutations
};
