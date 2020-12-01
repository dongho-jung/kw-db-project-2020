<template>
  <div class="simpleLogin">
    <form>
      <div class="JBox" style="align:center;padding : 10px;">
        <a href="http://localhost:3000/NewAccount">
          <img alt="DB1" src="@/assets/time.png" height="200" width="270">
        </a>
      </div>
      <legend>
        <h1>New Account</h1>
      </legend>

        <br><img v-bind:src="kakao_profile_image" height="200" width="270"><br>
<!--      <br><input type="text" name="student_id" size = 48 style = "width:200pt;height:200pt;text-align:center;"><br><br>-->
      <div class="Jbox1" >
        <div class="JPad">
        </div>

        <div class="Jbox11">
          <div class="JPad">
          </div>

          <div class="JBox">* Student ID :
          </div>

          <div class="JBox">
            <input v-model="student_id" type="text" name="student_id" size = 50 style = "text-align:center; ">
          </div>

          <div class="JBox">
          </div>

          <div class="JPad">
          </div>
        </div>

        <div class="Jbox11">
          <div class="JPad">
          </div>

          <div class="JBox">* Name :
          </div>

          <div class="JBox">
            <input v-model="kakao_name" type="text" name="name" size = 50 style = "text-align:center;">
          </div>

          <div class="JBox">
          </div>

          <div class="JPad">
          </div>
        </div>

        <div class="Jbox11">
          <div class="JPad">
          </div>

          <div class="JBox">Phone :
          </div>

          <div class="JBox">
            <input type="text" name="phone" size = 50 style = "text-align:center;">
          </div>

          <div class="JBox">
          </div>

          <div class="JPad">
          </div>
        </div>

        <div class="Jbox11">
          <div class="JPad">
          </div>

          <div class="JBox">Gender :
          </div>

          <div class="JBox">
            <input v-model="kakao_gender" type="text" name="gender" size = 50 style = "text-align:center;">
          </div>

          <div class="JBox">
          </div>

          <div class="JPad">
          </div>
        </div>

        <div class="Jbox11">
          <div class="JPad">
          </div>

          <div class="JBox">* Email :
          </div>

          <div class="JBox">
            <input v-model="kakao_email" type="text" name="email" size = 50 style = "text-align:center;">
          </div>

          <div class="JBox">
            <input v-on:click="Check_email" type="button" value="중복체크" size = 50 style = "color: white; background-color:#8fc400; width:80pt;height:16pt;text-align:center;">
          </div>

          <div class="JPad">
          </div>
        </div>

        <div class="Jbox11">
          <div class="JPad">
          </div>

          <div class="JBox">Birth(MMDD) :
          </div>

          <div class="JBox">
            <input type="text" v-model="kakao_birth" name="birth" size = 50 style = "text-align:center;">
          </div>

          <div class="JBox">
          </div>

          <div class="JPad">
          </div>
        </div>

        <div class="Jbox11">
          <div class="JPad">
          </div>

          <div class="JBox">* PW :
          </div>

          <div class="JBox">
            <input v-model="PW" type="text" name="PW" size = 50 maxlength=10>
          </div>

          <div class="JBox">
          </div>

          <div class="JPad">
          </div>
        </div>

        <div class="Jbox12" style="padding:20px;">
          <div class="JPad">
          </div>

          <div class="JBox">
            <input type="button" v-on:click="OK" value="OK" size=70 style = "color: white; background-color:#8fc400; width:100pt;height:25pt;text-align:center;">
          </div>

          <div class="JBox">
            <input type="button" v-on:click="Cancel" value="Cancel" size=70 style = "color: white; background-color:#8fc400; width:100pt;height:25pt;text-align:center;">
          </div>

          <div class="JBox">
            <p v-on:click="KakaoLogin" ><a href="https://kauth.kakao.com/oauth/authorize?client_id=8d323fc0c13720cda59983912f875316&redirect_uri=http://localhost:5000/oauth&response_type=code">
              <img src="../../assets/kakaoNewAccount.png" height="30"></a></p>
          </div>

          <div class="JPad">
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
    return {
      kakao_name:'',
      kakao_email:'',
      kakao_profile_image:'',
      kakao_gender:'',
      kakao_birth:'',

      student_id:'',
      PW:''
    }
  },
  methods:{
    default_(){
      if (this.$cookies.isKey('kakaoURL')==true){
        let URL = decodeURIComponent(this.$cookies.get('kakaoURL'))
        let URL_ = URL.split('&')
        this.kakao_name=URL_[1].split('=')[1]
        console.log(URL_)
        console.log(this.kakao_name)
        this.kakao_profile_image = 'http:'+URL_[5].split(':')[1]
        this.kakao_email=URL_[2].split('=')[1]
        this.kakao_gender=URL_[3].split('=')[1]
        this.kakao_birth=URL_[4].split('=')[1]
        this.$cookies.set('profile',this.kakao_profile_image)
        this.$cookies.set('name',this.kakao_name)
        this.$cookies.set('email',this.kakao_email)
      }
    },
    Check_email: function() {
      if(this.kakao_email == ''){
        alert('Empty Email!!')
      }
      let bodyFormdata = new FormData();
      bodyFormdata.append('email',this.kakao_email)
      axios.get('/student/check/email',{
        baseURL: 'http://localhost:5000',
        params: {
          email: this.kakao_email
        }
      })
      .then(res=>{ //못찾으면 error 출력하도록 유도
        alert('You can use it')
        console.log(res);
        this.$cookies.set('CheckDuplicatedEmail');
      })
      .catch(error =>{
        console.log(error);
        alert('Already Presented Email')
      })
    },
    OK (){
      if (this.$cookies.isKey('CheckDuplicatedEmail')==true){
        if(this.student_id!='')
          if(this.kakao_name!='')
            if(this.PW!=''){
              alert('Success to Make New Account')
              this.$router.push('/login')
            }
            else alert('Please input PW')
          else alert('Please input Name')
        else alert('Please input Student_id')
      }
      else{
        alert('Check email first')
      }
    },
    Cancel(){
      alert('Go to Login Page')
      this.$router.push('/login')
    },
    KakaoLogin:function () {
      let URL = window.location.href
      this.$cookies.set('kakaoURL',URL)
      console.log(URL)
      this.$router.go()
    }
  },
  created() {
    this.$router.go(1)
    this.default_()
  }
}
</script>

<style>
.simpleLogin form {
  min-width: 760px;
  min-height: 1000px;
  margin: auto;
  background: #fefefd;
  box-shadow: 0 10px 10px #222;
}
.simpleLogin form fieldset {
  display : grid;
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
#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
.Jbox1{
  display: grid;
  grid-template-columns: 800px;
  grid-template-rows: 20px 40px 40px 40px 40px 40px 40px 40px 50px;
}
.Jbox11{
  display: grid;
  grid-template-columns: 50px 150px 400px 150px 50px;
}
.Jbox12{
  display: grid;
  grid-template-columns: 2fr 3fr 3fr 3fr 2fr;
}
.JPad{
}
.JBox{
}
</style>