<template>
  <div class="Magic_part">
    <div class="EPad">
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
      <div class="Ebox21" style = "padding: 10px 0px 0px 0px;">
        <h3>Please select all questions</h3>
      </div>
      <div class="Ebox22">
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="radio" name="rad1" id="AM" v-model="filter" value="AM" />이른 강의
        </div>
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="radio" name="rad1" id="PM" v-model="filter" value="PM"/>늦은 강의
        </div>
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="radio" name="rad1" id="SP" v-model="filter" value="SP"/>공강
        </div>
        <div class="Ebox" style = "padding: 27px 10px 0px 0px;">
          <select @change="Remove_Favorite" v-model="selected_index">
            <option>Mon</option>
            <option>Tue</option>
            <option>Wed</option>
            <option>Thr</option>
            <option>Fri</option>
          </select>
        </div>
      </div>
      <div class="Ebox23">
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="radio" name="rad2" id="NM" v-model="filter" value="NM"/>교양
        </div>
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="radio" name="rad2" id="MA" v-model="filter" value="MA"/>전공
        </div>
      </div>
      <div class="Ebox24">
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="radio" name="rad3" id="NM" v-model="filter" value="SL"/>소규모 강의
        </div>
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="radio" name="rad3" id="MA" v-model="filter" value="LL"/>대규모 강의
        </div>
      </div>
      <div class="Ebox25">
        <div class="Ebox" style = "padding: 27px 0px 0px 20px;">
          <font size="2.5em">최소 전공 학점 : </font>
        </div>
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="text" name="Search_text" style = "width: 80px; height:20px;">
        </div>
        <div class="Ebox" style = "padding: 27px 0px 0px 20px;">
          <font size="2.5em">최소 교양 학점 : </font>
        </div>
        <div class="Ebox" style = "padding: 27px 0px 0px 0px;">
          <input type="text" name="Search_text" style = "width: 80px; height:20px;">
        </div>
        <div class="EPad">
        </div>
        <div class="EPad">
        </div>
        <div class="Ebox" style = "padding: 10px 0px 0px 20px;">
          <font size="2.5em">전체 요구 학점 : </font>
        </div>
        <div class="Ebox" style = "padding: 10px 0px 0px 0px;">
          <input type="text" name="Search_text" style = "width: 80px; height:20px;">
        </div>
      </div>
      <div class="EPad">
      </div>
      <div class="Ebox26">
        <div class="Ebox261" style = "padding: 10px 0px 0px 0px;">
          <p><input type="button" value="시간표생성" size=70 style = "width:80pt;height:20pt;text-align:center; padding: 0px 0px 0px 0px;"></p>
        </div>
        <div class="Ebox262" style = "padding: 10px 0px 0px 0px;">
          <p><input type="button" value="돌아가기" size=70 style = "width:80pt;height:20pt;text-align:center;"></p>
        </div>
      </div>
    </div>
    <div class="EPad">
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

.EPad{
  border: 1px solid res;
}

.Ebox{
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
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-gap: 10px;
}

.Ebox21{
  border: 1px solid;
}

.Ebox22{
  display: grid;
  grid-template-columns: 3fr 3fr 3fr 1fr;
  border: 1px solid;
}

.Ebox23{
  display: grid;
  grid-template-columns: 1fr 1fr;
  border: 1px solid;
}

.Ebox24{
  display: grid;
  grid-template-columns: 1fr 1fr;
  border: 1px solid;
}

.Ebox25{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  border: 1px solid;
}

.Ebox26{
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 10px;
}

.Ebox261{
}

.Ebox262{
}

</style>