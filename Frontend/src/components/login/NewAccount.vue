<template>
  <div class="box2">
    <a href="http://localhost:3000/NewAccount">
      <img src="../../assets/time.png" height = "200" width="300">
      <h1>New Account</h1>
    </a>
    <tr>
      <img v-bind:src="kakao_profile_image">

      <div class="box21">
        * Student ID : <input v-model="student_id" type="text" name="student_id" size = 48 style = "text-align:center;"><br><br><br>
      </div>

      <div class="box21">
        * Name : <input v-model="kakao_name" type="text" name="name" size = 53 style = "text-align:center;"><br><br><br>
      </div>
      Phone : <input type="text" name="phone" size = 53 style = "text-align:center;"><br><br><br>
      Gender : <input v-model="kakao_gender" type="text" name="gender" size = 53 style = "text-align:center;"><br><br><br>
      * Email : <input v-model="kakao_email" type="text" name="email" size = 38 style = "text-align:center;"><br><br><br>
      <input v-on:click="Check_email" type="button" value="중복체크" size = 50 style = "width:80pt;height:16pt;text-align:center;"><br><br><br>
      Birth(Month,Date) : <input type="text" v-model="kakao_birth" name="birth" size = 53 style = "text-align:center;"><br><br><br>
      * PW :    <input type="text" name="PW" size = 56 maxlength=10><br><br><br>
      <div class="Bbox42"><!-- >버튼< -->
        <p v-on:click="KakaoLogin" ><a href="https://kauth.kakao.com/oauth/authorize?client_id=8d323fc0c13720cda59983912f875316&redirect_uri=http://localhost:5000/oauth&response_type=code"><img src="../../assets/kakaoNewAccount.png"></a></p>
      </div>
      <input type="button" v-on:click="OK" value="OK" size=70 style = "width:100pt;height:20pt;text-align:center;">
      <input type="button" v-on:click="Cancel" value="Cancel" size=70 style = "width:100pt;height:20pt;text-align:center;">
      <div class="Apad"><!-- >버튼< --></div>

    </tr>
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
        console.log(this.kakao_name)
        console.log('http:'+URL_[5].split(':')[1])
        this.kakao_profile_image = 'http:'+URL_[5].split(':')[1]
        this.kakao_email=URL_[2].split('=')[1]
        this.kakao_gender=URL_[3].split('=')[1]
        this.kakao_birth=URL_[4].split('=')[1]
        this.$cookies.set('profile',this.kakao_profile_image)
      }
    },
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
    OK (){
      if (this.$cookies.isKey('CheckDuplicatedEmail')==true){
        alert('Success to Make New Account')
        this.$router.push('/login')
      }
      else{
        alert('')
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 100px 100px;
  grid-gap: 10px;
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

</style>