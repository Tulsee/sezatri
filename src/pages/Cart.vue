<template>
  <div>
    <section class="banner_area">
      <div class="banner_inner d-flex align-items-center">
        <div class="container">
          <div
            class="banner_content d-md-flex justify-content-between align-items-center"
          >
            <div class="mb-3 mb-md-0">
              <h2>Cart</h2>
              <p>Very us move be blessed multiply night</p>
            </div>
            <div class="page_link">
              <a href="index.html">Home</a>
              <a href="cart.html">Cart</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="cart_area">
      <div class="container">
        <div class="cart_inner" style="background:#fff;">
          <div class="table-responsive">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Product</th>
                  <th scope="col">Price</th>
                  <th scope="col">Quantity</th>
                  <th scope="col">Total</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <CartItem />
                </tr>
              </tbody>
            </table>
            <hr />
            <div class="cart-total-price">
              <h5>Subtotal</h5>
              <h5>$2160.00</h5>
            </div>
            <hr />
            <div
              class="out_button_area"
              style="float:right; margin-right:50px;"
            >
              <div class="checkout_btn_inner">
                <a class="genric-btn primary circle" href="#"
                  >Continue Shopping</a
                >
                <a
                  @click.prevent="hello"
                  class="genric-btn danger circle"
                  style="margin-left:3px;"
                  >Proceed to checkout</a
                >
              </div>
              <br />
            </div>
            <br />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import CartItem from "../components/cart/cartItem";
// import { mapGetters, mapActions } from "vuex";
export default {
  name: "CartPage",
  components: {
    CartItem
  },
  computed: {},
  created() {},
  methods: {}
};
</script>
<style scoped>
.cart-total-price {
  text-align: right;
  padding-right: 50px;
  display: block;
}
</style>
