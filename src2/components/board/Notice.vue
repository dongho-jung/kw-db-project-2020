<template>
  <div class="List_part">
    <div class="CPad">
    </div>

    <div class="Cbox1">
      <div class="CboxBorder">
        <h1>과목 : 데이터베이스</h1>
      </div>

      <div class="Cbox12">
        <div class="Cbox121">
            <a href="http://localhost:8080/#/board/notice">
            <img alt="DB1" src="@/assets/notice.png" height = "50" width="50">
            </a>
            <select name="subject" style="width:100px;height:50px;" align="right">
              <option value="">과목선택</option> 
              <option value="">데이터베이스</option>
              <option value="">운영체제</option>
              <option value="">데이터통신</option>
              <option value="">알고리즘</option>
            </select>
        </div>
        <div class="Cbox12n">
          <div class="Cbox" align="left">
            <a href="http://localhost:8080/#/board/notice">
            <font size="5em">글쓴이</font>
            </a>
          </div>
          <div class="Cbox" align="left">
            <font size="4em">10/05 12:15</font><br>
            <font size="3em">중간고사 실시 안내 </font><br><br>
            <font size="3em">중간고사 시험 날짜 : 10월 31일 10:00</font>
          </div>
        </div>
        <div class="Cbox12n">
          <div class="Cbox" align="left">
            <a href="http://localhost:8080/#/board/notice">
            <font size="5em">글쓴이</font>
            </a>
          </div>
          <div class="Cbox" align="left">
            <font size="4em">10/25 22:05</font><br>
            <font size="3em">23차 과제 제안서</font><br><br>
             <font size="3em">23차 과제 제안서입니다. 제출 기한은 11월 3일입니다.</font>
          </div>
        </div>
        <div class="Cbox12n">
          <div class="Cbox" align="left">
            <a href="http://localhost:8080/#/board/notice">
            <font size="5em">글쓴이</font>
            </a>
          </div>
          <div class="Cbox" align="left">
            <font size="4em">10/29 15:30</font><br>
            <font size="3em">24차 과제 제안서</font><br><br>
            <font size="3em">24차 과제 제안서입니다. 제출 기한은 11월 4일입니다.</font>
          </div>
        </div>
      </div>
    </div>

    <div class="Cbox2">
      <div class="CboxBorder">
        <a href="http://localhost:8080/#/board/notice">
        <h1>중간고사 실시 안내</h1>
        </a>
        <div class="CboxPad" align="right">
            <font size="3em">10/05 12:15</font>
        </div>
      
     
      <div class="Cbox21" align="left">
        <font size="3em">중간고사 시험 날짜 : 10월 31일 10:00</font><br><br>
        <font size="3em">중간고사 시험 장소 : 한울관 B101</font><br><br>
        <font size="3em">중간고사 시험 범위 : P.11 ~ P.2547</font><br><br>  
          <div class=Cboxpad align="center">
            <h3>[주의]</h3><br>
          </div>
        <font size="3em">- 마스크를 착용해야 시험 응시가 가능합니다.</font><br><br>
        <font size="3em">- 위생을 위해 옆자리와 한 칸 띄어 앉아주세요.</font><br><br>
        <font size="3em">- 시험 시작 후 30분동안 퇴실이 불가능합니다.</font><br><br>
        <font size="3em">- 화장실이 급하신 분들은 미리 해결해주세요.</font><br><br>
      </div>
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
.List_part > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}
.List_part{
  display: grid;
  grid-template-columns: 2fr 4fr 2fr 2fr;
  grid-template-rows: 800px;
  grid-gap: 10px;
}
.CPad{
  
}
.Cbox{
  
}
.CboxBorder{
  border: 1px solid;
}
.CboxPad{
  padding:9px;
}
.CboxPad15{
  padding:15px;
  
}
.CboxPad15Border{
  padding:15px;
  border: 1px solid;
}
.CboxMar{
  border: 1px solid;
  margin:5px;
}
.Cbox1{
  display: grid;
  grid-template-rows: 1fr 7fr;
  grid-gap: 10px;
}
.Cbox12{
  display: grid;
  grid-template-rows: 1fr 3fr 3fr 3fr 1fr;
  grid-gap: 0px;
}
.Cbox121{
  display: grid;
  grid-template-columns: 2fr 12fr 3fr;
  grid-gap: 0px;
  border: 1px solid;
}
.Cbox125{
  display: grid;
  grid-template-columns: 6fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}
.Cbox12n{
  display: grid;
  grid-template-rows: 1fr 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}
.Cbox2{
  padding:9px;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 9fr;
  grid-gap: 0px;
}
.Cbox2n{
  padding:9px;
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
  
}
#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
</style>