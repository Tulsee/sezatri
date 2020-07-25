<template>
  <div>
    <div class="single-product">
      <div class="product-img">
        <img class="card-img category-image" :src="Product.thumbnail" alt />
        <div class="p_icon">
          <router-link :to="`/productdetail/${Product.id}`">
            <i class="ti-eye"></i>
          </router-link>
          <a href="#">
            <i class="ti-heart"></i>
          </a>
          <a style="cursor:pointer;">
            <i
              @click.prevent="addProduct(Product.id)"
              class="ti-shopping-cart"
            ></i>
          </a>
        </div>
      </div>
      <div class="product-btm">
        <a href="#" class="d-block">
          <h4>{{ Product.name }}</h4>
        </a>
        <div class="mt-3">
          <span class="mr-4">${{ Product.price }}</span>
          <del>$35.00</del>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "ProductItem",
  props: {
    Product: {
      required: true,
      type: Object
    }
  },
  data() {
    return {
      cartDetail: {
        product: null,
        quantity: null,
        customer: null,
        checkout: false
      }
    };
  },
  computed: {
    ...mapGetters(["authUser"])
  },
  methods: {
    ...mapActions(["addTocart"]),
    addProduct(productId) {
      this.cartDetail.product = productId;
      this.cartDetail.quantity = 1;
      this.cartDetail.checkout = false;
      this.cartDetail.customer = this.authUser.id;
      console.log(this.cartDetail);
      this.addTocart(this.cartDetail);
    }
  }
};
</script>

<style scoped>
.category-image {
  height: 261px !important;
}
</style>
