<!-- > 왼쪽 화면에 선 그래프를 어떻게 구현하면 좋을까?< -->
<!-- 상단에 있는 장학 제도 누르면 나오는 페이지 -->
<template>
  <div class="Schlorship_part">
    <div class="DPad"></div>

    <div class="Dbox1">
      <!-- ><li><router-link to="/chartjs">장학제도</router-link></li>< -->

      <section class="container">
        <h1>Scholarship System</h1>
        <div class="columns">
          <div class="column">
            <line-chart2></line-chart2>
            <!--Line Chart2 example-->
          </div>
        </div>
      </section>

    </div>

    <div class="Dbox2">
      <div class="DboxBorder">
        <a href="http://localhost:8080/grade/Scholarship">
          <h3>Condition of Scholarship System </h3>
        </a>
      </div>
      <div class="Dbox2n" align="left">
        <div class="Dbox21" align="left">
          <font size="3em">- 직전학기 취득학점이 17학점 이상</font><br><br>
          <font size="3em">- 4학년은 12학점 이상</font><br><br>
          <font size="3em">- 평량평균이 3.0이상인 자</font><br><br>
          <font size="3em">[평가 기준]</font><br><br>
          <font size="3em">1) 직전학기 취득학점</font><br><br>
          <font size="3em">2) 직전학기 전체평점</font><br><br>
          <font size="3em">3) 직전학기 본인의 석차</font><br><br>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart2 from '@/components/LineChart2'

export default {
  name: 'VueChartJS2',
  components: {
    LineChart2
  },
}
</script>

<style>
ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
.button {
  color: black;
  padding: 7px 60px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
}
a{text-decoration:none; color:black}
.Schlorship_part > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}
.Schlorship_part{
  display: grid;
  grid-template-columns: 2fr 4fr 2fr 2fr;
  grid-template-rows: 800px;
  grid-gap: 10px;
}
.DPad{

}
.Dbox{

}
.DboxBorder{
  border: 1px solid;
}
.DboxPad{
  padding:9px;
}
.DboxPad15{
  padding:15px;

}
.DboxPad15Border{
  padding:15px;
  border: 1px solid;
}
.DboxMar{
  border: 1px solid;
  margin:5px;
}
.Dbox1{
  display: grid;
  grid-template-rows: 1fr 7fr;
  grid-gap: 10px;
}
.Dbox12{
  display: grid;
  grid-template-rows: 1fr 3fr 3fr 3fr 1fr;
  grid-gap: 0px;
}
.Dbox121{
  display: grid;
  grid-template-columns: 2fr 12fr 3fr;
  grid-gap: 0px;
  border: 1px solid;
}
.Dbox125{
  display: grid;
  grid-template-columns: 6fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}
.Dbox12n{
  display: grid;
  grid-template-rows: 1fr 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}
.Dbox2{
  padding:9px;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 9fr;
  grid-gap: 0px;
}
.Dbox2n{
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