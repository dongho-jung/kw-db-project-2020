<template>
  <div class="simpleLogin">
    <form>
    <a href="http://localhost:3000/NewAccount">
      <legend>
      <h1>New Account</h1>
      </legend>
      <input type="text" name="student_id" size = 48 style = "width:100pt;height:100pt;text-align:center;">
    </a>
    <tr>
      <img v-bind:src="kakao_profile_image">
      <div class="box21">
        * Student ID : <input v-model="student_id" type="text" name="student_id" size = 48 style = "text-align:center;"><br><br>
      </div>

      <div class="box21">
        * Name : <input v-model="kakao_name" type="text" name="name" size = 53 style = "text-align:center;"><br><br>
      </div>
      Phone : <input type="text" name="phone" size = 55 style = "text-align:center;"><br><br>
      Gender : <input v-model="kakao_gender" type="text" name="gender" size = 54 style = "text-align:center;"><br><br>
      * Email : <input v-model="kakao_email" type="text" name="email" size = 38 style = "text-align:center;">
      <input v-on:click="Check_email" type="button" value="중복체크" size = 50 style = "width:80pt;height:16pt;text-align:center;"><br><br>
      Birth(M,D) : <input type="text" v-model="kakao_birth" name="birth" size = 53 style = "text-align:center;"><br><br>
      * PW :    <input type="text" name="PW" size = 56 maxlength=10><br><br>
      <input type="button" v-on:click="OK" value="OK" size=70 style = "width:100pt;height:20pt;text-align:center;">
      <input type="button" v-on:click="Cancel" value="Cancel" size=70 style = "width:100pt;height:20pt;text-align:center;">
       <div class="Bbox42"><!-- >버튼< -->
        <p v-on:click="KakaoLogin" ><a href="https://kauth.kakao.com/oauth/authorize?client_id=8d323fc0c13720cda59983912f875316&redirect_uri=http://localhost:5000/oauth&response_type=code"><img src="../../assets/kakaoNewAccount.png"></a></p>
      </div>
      <div class="Apad"><!-- >버튼< --></div>

    </tr>
    </form>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.simpleLogin form {
  width: 1000px;
  height: 1000px;
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
  padding:10px;
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