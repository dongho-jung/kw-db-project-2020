<template>
  <div class="simpleLogin">
    <form>
      <img alt="DB1" src="@/assets/kw01.jpg" height="400" width="760">
      <legend>
        <h1>DB MANMAN<br>Time Planner</h1>
      </legend>

      <div class="Lbox1">
        <div class="LPad">
        </div>

        <div class="Lbox11">
          <div class="LPad">
          </div>

          <div class="LBox">ID :
          </div>

          <div class="Lbox">
            <input placeholder="Username" id="username" type="text" v-model="username" size=50 style = "text-align:center;"/>
          </div>

          <div class="LPad">
          </div>

          <div class="Lbox">
            <button id = "New Account" v-on:click="btn_NewAccount" style = "color: white; width:100pt; background-color:#8fc400">New Account</button>
          </div>
        </div>
        <div class="Lbox11">
          <div class="LPad">
          </div>

          <div class="LBox">PW :
          </div>

          <div class="Lbox">
            <input id="password" type="psassword" placeholder="Password" v-model="password" name="ID" size=50 style= "text-align:center;"/>
          </div>

          <div class="LPad">
          </div>

          <div class="Lbox">
            <button id = "Check ID" style = "color: white; width:100pt; background-color:#8fc400" v-on:click="btn_FindPW">Check IDs</button>
          </div>
        </div>

        <div class="Lbox12" style="padding:20px;">
          <div class="LPad">
          </div>

          <div class="Lbox">
            <input v-on:click="btn_Login" type="button" value="Login" style="width:140px; height:40px; background-color:#8fc400; color:white;">
          </div>
          <div class="LPad">
          </div>

          <div class="Lbox">
            <p v-on:click="loginkakao"><a href="/Newaccount"><img src="../../assets/kakao.png" style="width:140px; height:40px;"></a></p>
          </div>

          <div class="LPad">
          </div>
        </div>

      </div>
    </form>
  </div>
</template>

<script>

import axios from "axios";
export default {
  data(){
    return{
      username : '',
      password : '',
      response_ : '',
    }
  },
  name: 'Bbox33',
  //메소드는 methods 객체 안에 정의
  methods : {
    default(){
      this.$cookies.set('student_id',this.username)
    },
    loginkakao() {
      alert('Use to set data using from Kakao Data Server \n Click 카카오 계정으로 가입')
    },
    btn_Login : function() {
      let bodyFormdata = new FormData();
      bodyFormdata.append('student_id',this.username)
      bodyFormdata.append('hashed_pw',this.password)
      console.log(this.username, this.password)
      axios({
        method: 'post',
        baseURL: 'http://localhost:5000',
        url: '/login',
        data: bodyFormdata,
        headers: {'Content-Type': 'multipart/form-data' }
      })
          .then(res=> {
            console.log(res);
            this.$cookies.set("SuccessLogin",this.username)
            this.$router.push("/");
            this.$router.go()
          }, async function (error) {
              console.log('에러일 경우', error.config);
              alert('Worng ID or PW');
          })
    },

    btn_NewAccount : function (){
      this.$router.push('/NewAccount')
    },
    btn_FindPW : function (){
      this.$router.push('/Findpw')
    }
  }
}
</script>

<style>
.simpleLogin form {
  max-width: 400px;
  max-height: 100px;
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
}
a {
  text-decoration: none;
  color: black;
}
.Login_part > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}
.Login_part {
  display: grid;
  grid-template-rows: 400px 60px 60px 40px;
  grid-gap: 10px;
}
.BPad {}
.Bbox1 {}
.Bbox2 {
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.Bbox21 {}
.Bbox22 {}
.Bbox23 {}
.Bbox3 {
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.Bbox31 {}
.Bbox32 {}
.Bbox33 {}
.Bbox4 {
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 10fr;
}
.Bbox40 {
  display: grid;
  grid-template-columns: 1fr 10fr 1fr 4fr 1fr;
  grid-template-rows: 2fr 1fr 2fr;
  padding: 10px;
}
.Bbox41 {
  display: grid;
  grid-template-columns: 1fr 4fr 1fr 4fr 1fr;
}
.Bbox42 {}
.Bbox43 {}
.Bbox44 {}
#footer,
#header,
#nav,
#section {
  text-align: center;
}
#footer,
#header {
  line-height: 100px;
}
#nav,
#section {
  line-height: 240px;
}
:root {}
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: 'Alata', sans-serif;
}
.page-container {
  width: 100vw;
  height: 100vh;
  background: #eff0f2;
  display: flex;
  justify-content: center;
  align-items: center;
}
.shadow {
  -webkit-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
  -moz-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
  box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
}
/*
.shadow-light{
-webkit-box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
-moz-box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
}*/
.login-form-container {
  background: #f5f5f5;
  width: 860px;
  height: 540px;
  display: flex;
  flex-direction: row;
  box-shadow: 10px black;
  border-radius: 10px;
}
.login-form-right-side {
  width: 50%;
  border-radius: 10px 0 0 10px;
  padding: 75px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  background-image: radial-gradient(ellipse farthest-corner at 0 140%, #5d9dff 0%, #2178ff 70%, #3585ff 70%);
}
.login-form-right-side h1 {
  color: white;
  width: 100%;
  text-align: right;
  opacity: 0.9;
}
.login-form-right-side p {
  padding-top: 50px;
  font-size: 12px;
  text-align: right;
  opacity: 0.8;
}
.login-form-left-side {
  width: 50%;
  border-radius: 0 10px 10px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px;
  background: rgb(255,255,255);
  background: linear-gradient(287deg, rgba(255,255,255,1) 0%, rgba(243,244,244,1) 0%, rgba(255,255,255,1) 100%);
}
.login-form-left-side .login-top-wrap {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  width: 100%;
}
.login-form-left-side .login-top-wrap span {
  color: gray;
  font-size: 11px;
  padding-right: 20px;
}
.login-form-left-side .login-top-wrap .create-account-btn {
  background: white;
  border: 0;
  width: 85px;
  height: 35px;
  font-size: 11px;
  color: #2178ff;
  border-radius: 3px;
}
.login-input-container {
  padding-top: 120px;
  width: 300px;
}
.login-input-container .login-input-wrap {
  width: 300px;
  height: 45px;
  margin-top: 20px;
  border-radius: 2px;
  border-bottom: solid 2px #2178ff;
}
.login-input-container .login-input-wrap i {
  color: #2178ff;
  line-height: 45px;
}
.login-input-container .login-input-wrap input {
  background: none;
  border: none;
  line-height: 45px;
  padding-left: 10px;
  width: 267px;
}
.login-input-container .login-input-wrap input:focus {
  outline: none;
}
.login-btn-wrap {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.login-btn-wrap .login-btn {
  width: 95px;
  height: 35px;
  color: white;
  border: 0;
  border-radius: 4px;
  background: rgb(105,163,255);
  background: linear-gradient(162deg, rgba(105,163,255,1) 0%, rgba(43,125,254,1) 50%, rgba(43,125,254,1) 100%);
}
.login-btn-wrap a {
  margin-top: 10px;
  text-decoration: none;
  font-size: 11px;
  color: gray;
}
.Lbox1{
  display: grid;
  grid-template-columns: 800px;
  grid-template-rows: 100px 40px 80px 50px;
}
.Lbox11{
  display: grid;
  grid-template-columns: 100px 100px 250px 100px 100px;
}
.Lbox12{
  display: grid;
  grid-template-columns: 3fr 3fr 1fr 3fr 3fr;
}
.LPad{
}
.Lbox{
}
</style>
