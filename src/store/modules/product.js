import axios from 'axios'

const state = {
  products: [],
  product: {}
};
const getters = {
  products: (state) => state.products,
  product: (state) => state.product
};
const actions = {
  async fetchProducts({
    commit
  }) {
    const response = await axios.get('/api/v1/product/');
    commit('setProducts', response.data)
  },
  async fetchFilterProduct({
    commit
  }, name) {
    const response = await axios.get(`/api/v1/product/?category=${name}`);
    commit('setProducts', response.data)
  },
  async fetchProductById({
    commit
  }, id) {
    const response = await axios.get(`/api/v1/product/${id}`);
    commit('setProduct', response.data)
  }
};
const mutations = {
  setProducts: (state, products) => {
    state.products = products;
  },
  setProduct: (state, product) => {
    state.product = product
  }
};


export default {
  state,
  getters,
  actions,
  mutations
}
