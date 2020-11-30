<template>
  <div class="Main_part">
    <div class="ZPad"></div>
    <div class="Zbox1">
      <div class='Zbox11'>
        <div class='Zbox111'>
         <img alt="Profile" src="../../assets/profile.png" height = "100" width="160">
        </div>

        <div class='Zbox112'>
          <font size="3em" face="bold">CHOO HO SUNG</font><br>
          <font size="1.5em">
          2016722049<br>
          hosung0610@naver.com
          </font>
        </div>
      </div>
      
      <div class='Zbox12'>
        </div>

    </div>

    <div class="Zbox2">
      <div class='Zbox21'>
        <h3>ID : 2016722049</h3>
      </div>

      <div class='Zbox22'>
        <table border="1" bordercolor="black" width='460' height='580' align="center" font size="1em">
          <th></th>
          <th>Mon</th><th>Tue</th><th>Wed</th><th>Thr</th><th>Fri</th>
          <tr><td>1</td><td></td><td></td><td></td><td></td><td></td></tr>
          <tr><td>2</td><td></td><td></td><td></td><td></td><td></td></tr>
          <tr><td>3</td><td>Data<br>Structure</td><td></td><td>Algorithm</td><td></td><td>Understanding<br>of music</td></tr>
          <tr><td>4</td><td></td><td>Data<br>Structure</td><td></td><td>Algorithm</td><td>Understanding<br>of music</td></tr>
          <tr><td>5</td><td></td><td></td><td></td><td>Understanding<br>of movie</td><td></td></tr>
          <tr><td>6</td><td></td><td></td><td>Understanding<br>of movie</td><td></td><td></td></tr>
        </table>

      </div>

    </div>

    <div class="Zbox3">
      <div class='Zbox31'>
        <h3>Notice board</h3>
      </div>

      <div class='Zbox32'>
        <div class ='Zbox321'>
          <a href="http://localhost:8080/#/board/list/1">
           <p style="font-size:1em;  font-weight:bold; text-align:left; ">도서관</p>
           <p style="font-size:0.8em; text-align:left;">자료실은 언제 열고 닫나요?</p>
           <p style="font-size:0.8em; text-align:left;">2020/11/22/13:11</p>
           <p style="font-size:0.7em; text-align:right;">Like 1  Hate 1  comment 1</p>
          </a>
        </div>

        <div class ='Zbox322'>
          <a href="http://localhost:8080/#/board/list/2">
            <p style="font-size:1em; font-weight:bold; text-align:left; ">다음주가 몇주차인지 아시는 분?</p>
            <p style="font-size:0.8em; text-align:left;">ㅈㄱㄴ</p>
            <p style="font-size:0.8em; text-align:left;">2020/11/22/15:27</p>
            <p style="font-size:0.7em; text-align:right;">Like 1  Hate 2 comment 2</p>
          </a>
        </div>

        <div class ='Zbox323'>
          <a href="http://localhost:8080/#/board/list/3">
            <p style="font-size:1em; font-weight:bold; text-align:left; ">민초</p>
            <p style="font-size:0.8em; text-align:left;">민초 좋아하면 좋아요 눌러라</p>
            <p style="font-size:0.8em; text-align:left;">2020/11/22/15:54</p>
            <p style="font-size:0.7em; text-align:right;">Like 0  Hate 127  comment 2 </p>
          </a>
        </div>

        <div class ='Zbox324'>
          <a href="http://localhost:8080/#/board/list/4">
            <p style="font-size:1em; font-weight:bold; text-align:left; ">컴공 이기훈 교수님</p>
            <p style="font-size:0.8em; text-align:left;">이기훈 교수님 강의 잘하시더라. 조교님들도 좋으시고</p>
            <p style="font-size:0.8em; text-align:left;">2020/11/22/17:24</p>
            <p style="font-size:0.7em; text-align:right;">Like 324  Hate 2  comment 29</p>
          </a>
        </div>
      </div>

    </div>

    <div class="Zbox4">
      <div class='Zbox41'>
        <a href="http://www.kw.ac.kr">
         <img alt="KW01" src="../../assets/kw01.jpg" height = "190" width="320">
        </a>

      </div>

      <div class='Zbox42'>
        <a href="http://sw.kw.ac.kr">
         <img alt="KW02" src="../../assets/kw02.png" height = "190" width="320">
        </a>
        </div>

      <div class='Zbox43'>
       <a href="http://datasci.kw.ac.kr">
        <img alt="KW03" src="../../assets/kw03.png" height = "190" width="200">
      </a>
      </div>
    </div>

    <div class="ZPad"></div>
  </div>
</template>

<script>
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.button {
  color: black;
  padding: 7px 60px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
}
table, th, td {
  border: 1px solid #bcbcbc;
}
table {
  width: 100%;
  height: 100%;
}
.jb-th-1{
  width:40px;
}
a{text-decoration:none; color:black}
.Main_part > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}
.Main_part{
  display: grid;
  grid-template-columns: 2fr 4fr 8fr 8fr 6fr 2fr;
  grid-template-rows: 700px;
  grid-gap: 10px;
}
.ZPad{
  
}
.Zbox1{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 250px 350px;
  grid-gap: 50px;
}
.Zbox11{
  background-color: white;
  border: 1px solid;
  grid-template-columns: 1fr;
  grid-template-rows: 10px 10px 10px 10px;
  grid-gap: 10px;
}
.Zbox111{
  padding: 10px 0px;
}
.Zbox112{
  padding: 0px 0px;
  
}
.Zbox12{
  background-color: white;
}
.Zbox2{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 60px 580px;
  grid-gap: 20px;
}
.Zbox21{
  text-align: center;
  background-color: white;
  border: 1px solid;
  padding: 0px 0px;
}
.Zbox22{
  background-color: white;
  border: 1px solid;
}
.Zbox3{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 60px 580px;
  grid-gap: 20px;
}
.Zbox31{
  text-align: center;
  background-color: white;
  border: 1px solid;
  padding: 0px 0px 0px 0px;
}
.Zbox32{
  background-color: white;
  border: 1px solid;
  grid-template-columns: 1fr;
  grid-template-rows: 95px 95px 95px 95px 95px;
}
.Zbox321{
  background-color: white;
  border: 1px solid;
  grid-template-columns: 1fr 1fr;
  height:25%;
}
.Zbox322{
  background-color: white;
  border: 1px solid;
  height:25%;
}
.Zbox323{
  background-color: white;
  border: 1px solid;
  height:25%;
}
.Zbox324{
  background-color: white;
  border: 1px solid;
  height:24%;
}
.Zbox326{
  background-color: white;
  border: 1px solid;
}
.Zbox4{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 200px 200px 200px;
  grid-gap: 20px;
}
.Zbox41{
  background-color: white;
  border: 1px solid;
}
.Zbox42{
  background-color: white;
  border: 1px solid;
}
.Zbox43{
  background-color: white;
  border: 1px solid
}
th{
  width: 20px;
}
#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
</style>

<!-- >
<template>
  <div class="content">
    <div class="box1">
       <a href="http://localhost:8080/#/login">
      <img alt="DB1" src="../../assets/time.png" height = "200" width="320">
      <h1>DB MANMAN<br>Time Planner</h1>
      </a>
    </div>

    <div class="box2">
      <div class="Pad">
      </div>
      <div class="box21">
        <font size="2em" face="bold">ID : </font>
      </div>
      <div class="box22">
        <input type="text" name="ID" size=50 style = "text-align:center;">
      </div>
      <div class="box23">
        <input type="button" value="New Account" size=70 style = "width:80pt;height:16pt;text-align:center;">
      </div>
      <div class="Pad">
      </div>
    </div>

    <div class="box3">
      <div class="Pad">
      </div>
      <div class="box31">
        <font size="2em" face="bold">PW : </font>
      </div>
      <div class="box32">
        <input type="text" name="ID" size=50 style = "text-align:center;">
      </div>
      <div class="box33">
        <input type="button" value="Find PW" size=70 style = "width:80pt;height:16pt;text-align:center;">
        
      </div>
      <div class="Pad">
      </div>
    </div>

    <div class="box4">
      <div class="Pad">
      </div>
      <div class="box41">
        <input type="button" value="Log In" size=70 style = "width:100pt;height:18pt;text-align:center;">
      </div>
      <div class="box42">
        <input type="button" value="KAKAO Log In" size=70 style = "width:100pt;height:18pt;text-align:center;background-color:yellow;">
      </div>
      <div class="Pad">
      </div>
    </div>
  </div>
</template>

<script>

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

.content > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}

.content{
  display: grid;
  grid-template-rows: 400px 60px 60px 40px;
  grid-gap: 10px;
}
.Pad{
}

.box1{
}

.box2{
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.box21{
}
.box22{
}
.box23{
}

.box3{
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.box31{
}
.box32{
}
.box33{
}

.box4{
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 10fr;
}
.box41{
}
.box42{
}
.box43{
}
.box44{
}

#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
</style>
< -->


