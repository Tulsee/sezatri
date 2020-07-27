import Vue from "vue";
import VueRouter from "vue-router";
import HomePage from "@/pages/HomePage";
import CategoryPage from "@/pages/CategoryPage";
import ProductDetail from "@/pages/ProductDetailPage";
import LoginPage from "@/pages/LoginPage";
import RegisterPage from "@/pages/RegisterPage";
import CartPage from "@/pages/Cart";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage
  },
  {
    path: "/login",
    name: "Login",
    component: LoginPage
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterPage
  },
  {
    path: "/category",
    name: "CategoryPage",
    component: CategoryPage
  },
  {
    path: "/cart",
    name: "CartPage",
    component: CartPage
  },
  {
    path: "/productdetail/:id",
    name: "ProductDetail",
    component: ProductDetail
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
