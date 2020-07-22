<template>
  <section class="py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="card">
            <div class="card-header bg-dark text-white">
              <h4 style="color:#fff;">
                <i class="fa fa-user-plus"></i> Register
              </h4>
            </div>
            <div class="card-body">
              <!-- alert -->
              <form action="{% url 'register' %}" method="POST">
                <!-- <div class="form-group">
                  <label for="first_name">First Name</label>
                  <input type="text" name="first_name" class="form-control" required />
                </div>-->
                <!-- <div class="form-group">
                  <label for="last_name">Last Name</label>
                  <input type="text" name="last_name" class="form-control" required />
                </div>-->
                <div class="form-group">
                  <label for="username">Username</label>
                  <input v-model="form.username" type="text" class="form-control" />
                </div>
                <div class="form-group">
                  <label for="email">Email</label>
                  <input v-model="form.email" type="email" class="form-control" />
                </div>
                <div class="form-group">
                  <label for="password2">Password</label>
                  <input v-model="form.password" type="password" class="form-control" />
                </div>
                <!-- <div class="form-group">
                  <label for="password">Confirm Password</label>
                  <input type="password" name="password2" class="form-control" required />
                </div>-->
                <input @click.prevent="register" type="submit" class="btn btn-success btn-block" />
              </form>
              <br />
              <h5>
                Already have an account?
                <a style="cursor:pointer; color:green;">Login Now</a>
              </h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import { mapActions } from "vuex";
export default {
  name: "RegisterPage",
  data() {
    return {
      form: {
        username: null,
        email: null,
        password: null
      }
    };
  },
  computed: {},
  methods: {
    ...mapActions(["registerUser"]),
    register() {
      this.registerUser(this.form)
        .then(response => {
          console.log("response " + response);
        })
        .catch(err => {
          console.log("error " + err.response.data);
        });
    }
  }
};
</script>
<style lang="less" scoped>
</style>