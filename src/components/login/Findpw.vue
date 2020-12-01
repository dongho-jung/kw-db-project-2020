<template>
  <div class="simpleLogin">
    <form>
        <div class="KBox" style="align:center;padding : 10px;">
            <a href="http://localhost:3000/Findpw">
            <img alt="DB1" src="@/assets/password.png" height="200" width="270">
            </a>
        </div>
      <legend>
        <h1>Find Password</h1>
      </legend>
      
      <div class="Kbox1" >
        <div class="KPad">
        </div>

        <div class="Kbox11">
            <div class="KPad">
            </div>

            <div class="Kbox">* Student ID : 
            </div>

            <div class="Kbox">
                <input v-model="student_id" type="text" name="student_id" size = 50 style = "text-align:center;">
            </div>

            <div class="Kbox">
            </div>

            <div class="KPad">
            </div>
        </div>

        <div class="Kbox11">
            <div class="KPad">
            </div>

            <div class="Kbox">* Name : 
            </div>

            <div class="Kbox">
                <input v-model="Name" type="text" name="name" size = 50 style = "text-align:center;">
            </div>

            <div class="Kbox">
            </div>

            <div class="KPad">
            </div>
        </div>

        <div class="Kbox11">
            <div class="KPad">
            </div>

            <div class="Kbox">Phone :
            </div>

            <div class="Kbox">
                <input type="text" name="phone" size = 50 style = "text-align:center;">
            </div>

            <div class="Kbox">
            </div>

            <div class="KPad">
            </div>
        </div>

        <div class="Kbox11">
            <div class="KPad">
            </div>

            <div class="Kbox">* Email : 
            </div>

            <div class="Kbox">
                <input v-model="email" type="text" name="email" size = 50 style = "text-align:center;">
            </div>

            <div class="KPad">
            </div>

            <div class="KPad">
            </div>
        </div>

        <div class="Kbox12" style="padding:20px;">
            <div class="KPad">
            </div>

            <div class="Kbox">
                <input type="button" v-on:click="OK" value="OK" size=70 style = "width:100pt; height:25pt; text-align:center; color: white; background-color:#8fc400">
            </div>

            <div class="KPad">
            </div>

            <div class="Kbox">
                <input type="button" v-on:click="Cancel" value="Cancel" size=70 style = "width:100pt; height:25pt; text-align:center; color: white; background-color:#8fc400">
            </div>

            <div class="KPad">
            </div>
        </div>

      </div>
    
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

.Kbox1{
    display: grid;
    grid-template-columns: 800px;
    grid-template-rows: 60px 50px 50px 50px 50px 50px;
}

.Kbox11{
    display: grid;
    grid-template-columns: 100px 100px 400px 150px 50px;
}

.Kbox12{
    display: grid;
    grid-template-columns: 3fr 3fr 1fr 3fr 3fr;
}

.KPad{
}

.Kbox{
}

</style>