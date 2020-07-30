<template>
  <tr>
    <td>
      <div class="media">
        <div class="d-flex">
          <img :src="carts.product.thumbnail" alt="" class="thumbnail" />
        </div>
        <div class="media-body">
          <p>{{ carts.product.name }}</p>
        </div>
      </div>
    </td>
    <td>
      <h5>${{ carts.product.price }}</h5>
    </td>
    <td>
      <div class="product_count">
        <input
          disabled
          name="qty"
          maxlength="12"
          :value="carts.quantity"
          class="input-text qty"
        />
        <button
          @click="addProduct()"
          class="increase items-count"
          type="button"
        >
          <i class="lnr lnr-chevron-up"></i>
        </button>
        <button
          @click="removeProduct()"
          class="reduced items-count"
          type="button"
        >
          <i class="lnr lnr-chevron-down"></i>
        </button>
      </div>
    </td>
    <td>
      <h5>${{ ProductTotalPrice }}</h5>
    </td>
  </tr>
</template>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "cartItem",
  props: {
    carts: {
      required: true,
      type: Object
    }
  },
  data() {
    return {
      cartDetail: {
        product: this.carts.product.id,
        quantity: null,
        customer: null,
        checkout: false
      }
    };
  },
  computed: {
    ...mapGetters(["authUser"]),
    ProductTotalPrice() {
      const pTotal = this.carts.product.price * this.carts.quantity;
      return pTotal;
    }
  },
  methods: {
    ...mapActions(["addTocart", "cart"]),
    addProduct() {
      this.cartDetail.quantity = 1;
      this.cartDetail.customer = this.authUser.id;
      this.addTocart(this.cartDetail);
    },
    removeProduct() {
      this.cartDetail.quantity = -1;
      this.cartDetail.customer = this.authUser.id;
      this.addTocart(this.cartDetail).then(() => {
        this.cart(this.authUser.id);
      });
    }
  }
};
</script>
<style scoped>
.thumbnail {
  width: 150px;
  height: 110px;
}
.quantity {
  display: inline-block;
  font-weight: 700;
  padding-right: 10px;
}

.chg-quantity {
  width: 12px;
  cursor: pointer;
  display: block;
  margin-top: 5px;
  transition: 0.1s;
}

.chg-quantity:hover {
  opacity: 0.6;
}
</style>
