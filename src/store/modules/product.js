import axios from 'axios'

const state = {
  products: [],
  product: {},
  newProduct: [],
  featureProduct: []
};
const getters = {
  products: (state) => state.products,
  product: (state) => state.product,
  newProduct: (state) => state.newProduct,
  featureProduct: (state) => state.featureProduct
};
const actions = {
  async fetchProducts({
    commit
  }) {
    const response = await axios.get('/api/v1/product/all/');
    commit('setProducts', response.data)
  },
  async fetchFilterProduct({
    commit
  }, name) {
    const response = await axios.get(`/api/v1/product/all/?category=${name}`);
    commit('setProducts', response.data)
  },
  async fetchProductById({
    commit
  }, id) {
    const response = await axios.get(`/api/v1/product/all/${id}/`);
    commit('setProduct', response.data)
  },
  async fetchNewProduct({
    commit
  }) {
    const response = await axios.get('/api/v1/product/newproduct/');
    commit('setNewProducts', response.data)
    commit('setFeatureProducts', response.data.featureProduct)
    console.log(response.data.featureProduct)
  },
  async fetchFeatureProduct({
    commit
  }) {
    const response = await axios.get('/api/v1/product/featureproduct/');
    commit('setFeatureProducts', response.data)
  }
};
const mutations = {
  setProducts: (state, products) => {
    state.products = products;
  },
  setProduct: (state, product) => {
    state.product = product
  },
  setNewProducts: (state, newPrd) => {
    state.newProduct = newPrd
  },
  setFeatureProducts: (state, featurePrd) => {
    state.featureProduct = featurePrd
  }
};


export default {
  state,
  getters,
  actions,
  mutations
}
