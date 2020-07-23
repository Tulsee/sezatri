<template>
  <div>
    <div class="single-product">
      <div class="product-img">
        <img class="card-img category-image" :src="product.thumbnail" alt />
        <div class="p_icon">
          <router-link :to="`/productdetail/${product.id}`">
            <i class="ti-eye"></i>
          </router-link>
          <a href="#">
            <i class="ti-heart"></i>
          </a>
          <a href="#">
            <i class="ti-shopping-cart"></i>
          </a>
        </div>
      </div>
      <div class="product-btm">
        <a href="#" class="d-block">
          <h4>{{product.name}}</h4>
        </a>
        <div class="mt-3">
          <span class="mr-4">${{product.price}}</span>
          <del>$35.00</del>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductItem",
  props: {
    product: {
      required: true,
      type: Object
    }
  }
};
</script>

<style scoped>
.category-image {
  height: 261px !important;
}
</style>