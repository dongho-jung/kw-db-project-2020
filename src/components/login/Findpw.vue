<template>
  <div class="simpleLogin">
    <form>
    <a href="http://localhost:3000/Findpw">
      <img src="../../assets/password.png" height = "200" width="300">
      <legend>
      <h1>Find Password</h1>
      </legend>
    </a>
    <tr>
      <div class="box21">
      * Student ID : <input v-model="student_id" type="text" name="student_id" size = 48 style = "text-align:center;"><br><br>
      </div>
      <div class="box21">
      * Name : <input v-model="Name" type="text" name="name" size = 53 style = "text-align:center;"><br><br>
      </div>
        Phone : <input type="text" name="phone" size = 55 style = "text-align:center;"><br><br>
      * Email : <input v-model="email" type="text" name="email" size = 54 style = "text-align:center;"><br><br>

      <div class="Bbox41" style="padding:10px;">
        <div class="BPad"></div>
      <input type="button" v-on:click="OK" value="OK" size=70 style = "width:100pt;height:20pt;text-align:center;">
       <div class="BPad"></div>
      <input type="button" v-on:click="Cancel" value="Cancel" size=70 style = "width:100pt;height:20pt;text-align:center;">
       <div class="BPad"></div>
      </div>

    </tr>
    </form>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<script>
import axios from "axios";
export default {
  data() {
    return {
      student_id:'',
      Name:'',
      email:''
    }
  },
  methods: {
    Check_email: function() {
      if(this.kakao_email == ''){
        alert('Empty Email!!')
      }
      let bodyFormdata = new FormData();
      bodyFormdata.append('student_id',this.student_id)
      axios({
        method: 'get',
        baseURL: 'http://localhost:5000',
        url: '/student',
        data: bodyFormdata,
        headers: {'Content-Type': 'multipart/form-data' }
      })
          .then(res=>{ //못찾으면 error 출력하도록 유도
            console.log(res);
            alert('Already Presented Email')
          }), async function (error){
        console.log(error);
        alert('You can use it')
        this.$cookies.set('CheckDuplicatedEmail')
      }
    },
    OK() {
      if (this.email=='') {
        alert('Success to Make New Account')
        this.$router.push('/login')
      } else {
        alert('')
      }
    },
    Cancel() {
      alert('Go to Login Page')
      this.$router.push('/login')
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.simpleLogin form {
  width: 600px;
  height: 500px;
  margin: auto;
  background: #fefefd;
  box-shadow: 0 10px 10px #222;
}
.simpleLogin form fieldset {
  display : grid;
  border: 0 none;
  margin: 0;
  padding: 50px;
}
.simpleLogin form fieldset input,
.simpleLogin form legend {
  font-family: Open Sans;
  font-size: 15px;
}
.simpleLogin form legend {
  background-color: #8fc400;
  border-top: 0 none;
  color: white;
  display: table-cell;
  padding: 10px 20px;
  width: auto;
}
.simpleLogin form fieldset input {
  width: 90%;
  margin: 10px 0;
  padding: 10px 5%;
  border: thin #8fc400 solid;
}
.simpleLogin input[type="submit"] {
  width: 100px;
  float: right;
  background: #8fc400;
  color: white;
  transition: 0.2s;
  border: 0;
  cursor: pointer;
}
.simpleLogin input[type="submit"]:focus,
.simpleLogin input[type="submit"]:hover,
.simpleLogin input[type="submit"]:active {
  padding: 10px 5%;
  background: #B3E226;
  outline: none;
}


.button {
  color: black;
  padding: 7px 60px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
  margin: 4px 2px;
}
.box2{
  padding:9px;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 9fr;
  grid-gap: 0px;
}
.box2n{
  padding:9px;
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}
#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
.box4{
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 10fr;
}
.box4n{
  padding:9px;
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}
</style>