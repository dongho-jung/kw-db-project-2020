<template>
  <div class="Notice_part">
    <div class="APad">
    </div>

    <div class="Abox1">
      <div class="AboxBorder">
        <h1>자유게시판</h1>
      </div>

      <div class="Abox12">
        <div class="Abox121">
          <div class="AboxPad">
            <img alt="DB1" src="../../assets/pencil.png" height = "30" width="30">
          </div>
          <div class="AboxPad">
            <input type="text" name="Search" style = "width:360pt;height:20pt;text-align:center;">
          </div>
          <div class="AboxPad">
            <input type="button" name="Search" value="Search" style = "width:60pt;height:24pt;text-align:center;">

          </div>
        </div>
        <div class="Abox12n">
          <div class="Abox" align="left">
            <a href="http://localhost:8080/#/board/hotlist">
            <font size="5em">법과권리</font>
            </a>
          </div>
          <div class="Abox" align="left">
            <font size="3em">과제 여태 몇번 나갔나요?</font><br><br><br>
            <font size="3em">2021/11/23 15:18</font>
          </div>
          <div class="AboxPad" align="right">
            <font size="3em">Like 1 Hate 0 Comment 1</font>
          </div>
        </div>
        <div class="Abox12n">
          <div class="Abox" align="left">
            <a href="http://localhost:8080/#/board/hotlist">
            <font size="5em">미개봉 중고 팔아요</font>
            </a>
          </div>
          <div class="Abox" align="left">
            <font size="3em">학번 : 20<br>...</font><br><br>
            <font size="3em">2021/11/23 15:09</font>
          </div>
          <div class="AboxPad" align="right">
            <font size="3em">Like 126 Hate 3 Comment 3</font>
          </div>
        </div>
        <div class="Abox12n">
          <div class="Abox" align="left">
            <a href="http://localhost:8080/#/board/hotlist">
            <font size="5em">아 티모 마렵다</font>
            </a>
          </div>
          <div class="Abox" align="left">
            <font size="3em">아이언1들은 솔랭 돌리지 마라.<br>내가 나간다 아ㅋㅋㅋㅋ</font><br><br>
            <font size="3em">2021/11/23 15:01</font>
          </div>
          <div class="AboxPad" align="right">
            <font size="3em">Like 3 Hate 24 Comment 1</font>
          </div>
        </div>
        <div class="Abox125">
          <div class="APad" align="center">
          </div>
          <div class="AboxPad15" align="center">
            <font size="4em">1</font>
          </div>
          <div class="AboxPad15" align="center">
            <a href="http://localhost:8080/#/board/hotlist">
            <font size="3em">◀</font>
            </a>
          </div>
          <div class="AboxPad15" align="center">
            <a href="http://localhost:8080/#/board/hotlist">
            <font size="3em">▶</font>
            </a>
          </div>
        </div>

      </div>
    </div>

    <div class="Abox2">
      <div class="AboxBorder">
        <h2>HOT게시판</h2>
      </div>
      <div class="Abox2n">
        <div class="AboxPad15" align="left">
          <a href="http://localhost:8080/#/board/hotlist">
          <font size="2.8em">진짜 너무 한거 아니냐...</font>
          </a>
        </div>
        <div class="AboxPad15" align="right">
          <font size="2em">11/23 09:13</font>
        </div>
      </div>
      <div class="Abox2n">
        <div class="AboxPad15" align="left">
          <a href="http://localhost:8080/#/board/hotlist">
          <font size="2.8em">송라이팅1 수강생 여러분</font>
          </a>
        </div>
        <div class="AboxPad15" align="right">
          <font size="2em">11/23 01:28</font>
        </div>
      </div>
      <div class="Abox2n">
        <div class="AboxPad15" align="left">
          <a href="http://localhost:8080/#/board/hotlist">
          <font size="2.8em">오늘은 연평도 포격사건 10주기</font>
          </a>
        </div>
        <div class="AboxPad15" align="right">
          <font size="2em">11/23 01:01</font>
        </div>
      </div>
      <div class="Abox2n">
        <div class="AboxPad15" align="left">
          <a href="http://localhost:8080/#/board/hotlist">
          <font size="2.8em">짜잔</font>
          </a>
        </div>
        <div class="AboxPad15" align="right">
          <font size="2em">11/22 20:46</font>
        </div>
      </div>
      <div class="AboxPad15">
        <a href="http://localhost:8080/board/hotlist">
        <font size="2em">더보기</font>
        </a>
      </div>
      <div class="APad">
      </div>
    </div>

    <div class="APad">
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.Abutton {
  color: black;
  padding: 7px 60px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
}

a{text-decoration:none; color:black}

.Notice_part > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}

.Notice_part{
  display: grid;
  grid-template-columns: 2fr 4fr 2fr 2fr;
  grid-template-rows: 800px;
  grid-gap: 10px;
}

.APad{
  
}

.Abox{
  
}

.AboxBorder{
  border: 1px solid;
}

.AboxPad{
  padding:9px;
}

.AboxPad15{
  padding:15px;
}
.AboxPad15Border{
  padding:15px;
  border: 1px solid;
}

.AboxMar{
  border: 1px solid;
  margin:5px;
}

.Abox1{
  display: grid;
  grid-template-rows: 1fr 7fr;
  grid-gap: 10px;
}

.Abox12{
  display: grid;
  grid-template-rows: 1fr 3fr 3fr 3fr 1fr;
  grid-gap: 0px;
}

.Abox121{
  display: grid;
  grid-template-columns: 2fr 12fr 3fr;
  grid-gap: 0px;
  border: 1px solid;
}
.Abox125{
  display: grid;
  grid-template-columns: 6fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}

.Abox12n{
  display: grid;
  grid-template-rows: 1fr 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;

}

.Abox2{
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 9fr;
  grid-gap: 0px;
}

.Abox2n{
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}


#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
</style>