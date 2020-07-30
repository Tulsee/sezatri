<template>
  <div>
    <Banner :title="'Cart'" :text="'All carts Item you have added'" />
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
                <CartItem v-for="cart in carts" :key="cart.id" :carts="cart" />
              </tbody>
            </table>
            <hr />
            <div class="cart-total-price">
              <h5>Subtotal</h5>
              <h5>${{ total }}</h5>
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
                  @click.prevent="TotalCartPrice()"
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
import Banner from "../components/shared/Banner";
import { mapGetters } from "vuex";
export default {
  name: "CartPage",
  components: {
    CartItem,
    Banner
  },
  computed: {
    ...mapGetters(["carts"])
  },
  created() {},
  methods: {
    TotalCartPrice() {
      var total = 0;
      for (var i = 0; i < this.carts.length; i++) {
        total += this.carts[i].product.price * this.carts[i].quantity;
      }
      return total;
    }
  }
};
</script>
<style scoped>
.cart-total-price {
  text-align: right;
  padding-right: 50px;
  display: block;
}
</style>
