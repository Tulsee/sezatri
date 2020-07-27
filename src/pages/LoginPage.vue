<template>
  <section class="py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="card">
            <div class="card-header bg-dark text-white">
              <h4 style="color:#fff;"><i class="fa fa-sign-in"></i> Login</h4>
            </div>
            <div class="card-body">
              <!-- alert -->
              <form>
                <div class="form-group">
                  <label for="username">Username</label>
                  <input
                    v-model="form.username"
                    type="text"
                    class="form-control"
                  />
                </div>

                <div class="form-group">
                  <label for="password">Password</label>
                  <input
                    v-model="form.password"
                    type="password"
                    class="form-control"
                  />
                </div>

                <input
                  @click.prevent="login"
                  type="submit"
                  class="btn btn-success btn-block"
                />
                <!--  -->
              </form>
              <br />
              <h5>
                Need to create account?
                <a style="cursor:pointer; color:green;">Register here</a>
              </h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { required } from "vuelidate/lib/validators";
import { mapActions } from "vuex";
export default {
  name: "LoginPage",
  data() {
    return {
      form: {
        username: null,
        password: null
      }
    };
  },
  validations: {
    form: {
      username: { required },
      password: { required }
    }
  },
  computed: {},
  methods: {
    ...mapActions(["loginWithUsernameAndPassword"]),
    login() {
      this.loginWithUsernameAndPassword(this.form).then(response => {
        console.log(response);
        if (response.status === 200) {
          this.$router.push("/");
        } else {
          console.log(response.response.data.detail);
        }
      });
      // .catch(err => {
      //   console.log(err.response.data);
      // });
      // this.$store
      //   .dispatch("loginWithUsernameAndPassword", this.form)
      //   .then(() => {
      //     this.$router.push("/");
      //   })
      //   .catch(error => {
      //     return error;
      //   });
    }
  }
};
</script>

<style lang="scss"></style>
