<template>
  <div class="simpleLogin">
    <form>
        <div class="JBox" style="align:center;padding : 10px;">
            <a href="http://localhost:3000/NewAccount">
            <img alt="DB1" src="@/assets/NewAccount.png" height="200" width="270">
            </a>
        </div>
      <legend>
        <h1>New Account</h1>
      </legend>
      
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
                <input v-on:click="Check_email" type="button" value="중복체크" size = 50 style = "width:80pt;height:16pt;text-align:center;">
            </div>

            <div class="JPad">
            </div>
        </div>

        <div class="Jbox11">
            <div class="JPad">
            </div>

            <div class="JBox">Birth(YYMMDD) :
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
                <input type="text" name="PW" size = 50 maxlength=10>
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
                <input type="button" v-on:click="OK" value="OK" size=70 style = "width:100pt;height:20pt;text-align:center;">
            </div>

            <div class="JBox">
                <input type="button" v-on:click="Cancel" value="Cancel" size=70 style = "width:100pt;height:20pt;text-align:center;">
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
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.simpleLogin form {
  min-width: 760px;
  min-height: 650px;
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