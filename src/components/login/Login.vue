<!-- 상단에 있는 로그 아웃 누르면 나오는 페이지 -->

<template>
  <div class="Login_part">
    <div class="Bbox1">
      <img alt="DB1" src="@/assets/kw01.jpg" height = "200" width="320">
      <h1>DB MANMAN<br>Time Planner</h1>
    </div>

    <div class="Bbox2">
      <div class="BPad">
      </div>
      <div class="Bbox21">
        <font size="2em" face="bold">ID : </font>
      </div>
      <div class="Bbox22">
        <input type="text" name="ID" size=50 style = "text-align:center;">
      </div>
      <div class="Bbox23"><!-- >버튼< -->
        <button id = "New Account" style = "width:80pt" v-on:click="btn_NewAccount">New Account</button>
        <!-- ><input type="button" value="New Account" size=70 style = "width:80pt;height:16pt;text-align:center;">< -->
      </div>
      <div class="BPad">
      </div>
    </div>

    <div class="Bbox3">
      <div class="BPad">
      </div>
      <div class="Bbox31">
        <font size="2em" face="bold">PW : </font>
      </div>
      <div class="Bbox32">
        <input type="text" name="ID" size=50 style = "text-align:center;">
      </div>
      <div class="Bbox33"><!-- >버튼< -->
        <button id = "Find PW" style = "width:80pt" v-on:click="btn_FindPW">Find PW</button>
        <!-- ><input type="button" value="Find PW" size=70 style = "width:80pt;height:16pt;text-align:center;">< -->
      </div>
      <div class="BPad">
      </div>
    </div>

    <div class="Bbox4">
      <div class="BPad">
      </div>
      <div class="Bbox41"><!-- >버튼< -->
        <input type="button" value="Log In" size=50 style = "width:160pt;height:47pt;text-align:center;">
      </div>
      <div class="Bbox42"><!-- >버튼< -->
        <a href="http://localhost:8080/login"><img src="../../assets/kakao.png"></a>
      </div>
      <div class="BPad">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Bbox33',
  //메소드는 methods 객체 안에 정의
  methods : {
      btn_NewAccount : function (){
        this.$router.push('/NewAccount')
      }
      ,btn_FindPW : function (){
        this.$router.push('/Findpw')
      }
  }
}
</script>

<style>
.button {
  color: black;
  padding: 7px 60px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
}
a{text-decoration:none; color:black}
.Login_part > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}
.Login_part{
  display: grid;
  grid-template-rows: 400px 60px 60px 40px;
  grid-gap: 10px;
}
.BPad{
}
.Bbox1{
}
.Bbox2{
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.Bbox21{
}
.Bbox22{
}
.Bbox23{
}
.Bbox3{
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.Bbox31{
}
.Bbox32{
}
.Bbox33{
}
.Bbox4{
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 10fr;
}
.Bbox41{
}
.Bbox42{
}
.Bbox43{
}
.Bbox44{
}
#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }


:root{


}
*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Alata', sans-serif;
}

.page-container{
    width: 100vw;
    height: 100vh;
    background: #eff0f2;
    display: flex;
    justify-content: center;
    align-items: center;

}
.shadow{
    -webkit-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
    -moz-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
    box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
}/*
.shadow-light{
    -webkit-box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
    -moz-box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
    box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);

}*/
.login-form-container{
 
    background:#f5f5f5 ;
    width:860px;
    height: 540px;
    display: flex;
    flex-direction: row;
    box-shadow: 10px black;
    border-radius: 10px;

}
.login-form-right-side{
    width: 50%; 
    border-radius: 10px 0px 0px 10px;
    padding:75px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    background-image: 
  radial-gradient(ellipse farthest-corner at 0 140%, #5d9dff 0%, #2178ff 70%, #3585ff 70%);
}
.login-form-right-side h1{
    color: white;
    width:100%;
    text-align: right;
    opacity: 0.9;

}
.login-form-right-side p{
    padding-top: 50px;
    font-size:12px;
    text-align: right;
    opacity: 0.8;
}
.login-form-left-side{
    width: 50%;
    border-radius: 0px 10px 10px 0px;
    display: flex;

    flex-direction: column;
    align-items: center;
    padding:40px;
    background: rgb(255,255,255);
background: linear-gradient(287deg, rgba(255,255,255,1) 0%, rgba(243,244,244,1) 0%, rgba(255,255,255,1) 100%);
}
.login-form-left-side .login-top-wrap{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    width:100%;
}
.login-form-left-side .login-top-wrap span{
    color: gray;
    font-size: 11px;
    padding-right:20px;

}
.login-form-left-side .login-top-wrap .create-account-btn {
    background: white;
    border:  0;
    width:85px;
    height: 35px;
    font-size: 11px;
    color: #2178ff;
    border-radius: 3px;

}
.login-input-container{
    padding-top:120px;
    width:300px;
}
.login-input-container .login-input-wrap{
    width:300px;
    height: 45px;
    margin-top: 20px;
    border-radius: 2px;
    border-bottom: solid 2px #2178ff;
   
}
.login-input-container .login-input-wrap i{
    color: #2178ff;
    line-height: 45px;
}

.login-input-container .login-input-wrap input{
    background: none;
   
    border: none;
    line-height: 45px;
    padding-left:10px;
    width:267px;
}
.login-input-container .login-input-wrap input:focus{
    outline: none;
}
.login-btn-wrap{
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;;
}
.login-btn-wrap .login-btn{
    width:95px;
    height:35px;
    color:white;
    border: 0;
    border-radius: 4px;

    background: rgb(105,163,255);
background: linear-gradient(162deg, rgba(105,163,255,1) 0%, rgba(43,125,254,1) 50%, rgba(43,125,254,1) 100%);
}
.login-btn-wrap a{
    margin-top:10px;
    text-decoration: none;
    font-size: 11px;
    color: gray;

}
</style>