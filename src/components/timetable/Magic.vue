<!-- 상단에 있는 시간표 마법사 누르면 나오는 페이지 -->
<template>
  <div class="Magic_part">
    <div class="Pad">
    </div>
    <div class="Ebox1">
      <div class="Ebox11">
        <div class="Ebox111">
        </div>
        <div class="Ebox112">
          <font size="3em" face="bold"><p>1 / 6</p></font>
        </div>
        <div class="Ebox113">
          <p><input type="button" value="←" size=70 style = "width:60pt;height:20pt;text-align:center;"></p>
        </div>
        <div class="Ebox114">
          <p><input type="button" value="→" size=70 style = "width:60pt;height:20pt;text-align:center;"></p>
        </div>
      </div>
      <div class="Ebox12">
        <table border="1" bordercolor="black" width='460' height='580' align="center" font size="1em">
          <th width="40"></th>
          <th height='20'>Mon</th><th>Tue</th><th>Wed</th><th>Thr</th><th>Fri</th>
          <tr><td>1</td><td></td><td></td><td></td><td></td><td></td></tr>
          <tr><td>2</td><td></td><td></td><td></td><td></td><td></td></tr>
          <tr><td>3</td><td>Data<br>Structure</td><td></td><td>Algorithm</td><td></td><td>Understanding<br>of music</td></tr>
          <tr><td>4</td><td></td><td>Data<br>Structure</td><td></td><td>Algorithm</td><td>Understanding<br>of music</td></tr>
          <tr><td>5</td><td></td><td></td><td></td><td>Understanding<br>of movie</td><td></td></tr>
          <tr><td>6</td><td></td><td></td><td>Understanding<br>of movie</td><td></td><td></td></tr>
        </table>
      </div>
    </div>

    <div class="Ebox2">
      <div class="Ebox21">
        <h3>모두 체크한 뒤 시간표 생성을 눌러주세요</h3>
      </div>
      <div class="Ebox22">
        <input type="radio" name="chk_info1" value="오전">오전
        <input type="radio" name="chk_info2" value="오후">오후
        <input type="radio" name="chk_info3" value="공강">공강
      </div>
      <div class="Ebox23">
        <input type="radio" name="chk_info1" value="교양">교양
        <input type="radio" name="chk_info2" value="전공">전공
      </div>
      <div class="Ebox24">
        <input type="radio" name="chk_info1" value="소규모 강의">소규모 강의
        <input type="radio" name="chk_info2" value="대규모 강의">대규모 강의
      </div>
      <div class="Ebox25">
        <div class="Ebox251">
          <p><input type="button" value="시간표생성" size=70 style = "width:60pt;height:20pt;text-align:center;"></p>
        </div>
        <div class="Ebox252">
          <p><input type="button" value="돌아가기" size=70 style = "width:60pt;height:20pt;text-align:center;"></p>
        </div>
      </div>
    </div>
    <div class="Pad">
    </div>
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
table {
  text-align:center;
  width: 100%;
  height: 100%;
}
a{text-decoration:none; color:black}
.Magic_part > div {
  border-radius: 5px;
  background-color: white;
  border: 1px solid;
  padding: 1em;
}
.Magic_part{
  display: grid;
  grid-template-columns: 1fr 2fr 2fr 1fr;
  grid-template-rows: 700px;
  grid-gap: 10px;
  border: 1px solid;
}
.Pad{
  border: 1px solid;
}
.Ebox1{
  display: grid;
  grid-template-rows: 1fr 10fr;
  grid-gap: 10px;
  border: 1px solid;
}
.Ebox11{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}
.Ebox111{
  border: 1px solid;
}
.Ebox112{
  border: 1px solid;
}
.Ebox113{
  border: 1px solid;
}
.Ebox114{
  border: 1px solid;
}
.Ebox12{
  border: 1px solid;
}
.Ebox2{
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}
.Ebox21{
  border: 1px solid;
}
.Ebox22{
  border: 1px solid;
}
.Ebox23{
  border: 1px solid;
}
.Ebox24{
  border: 1px solid;
}
.Ebox25{
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}
.Ebox251{
  border: 1px solid;
}
.Ebox252{
  border: 1px solid;
}
</style>