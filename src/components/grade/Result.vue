<!-- > 왼쪽 화면에 선 그래프를 어떻게 구현하면 좋을까?< -->
<!-- 상단에 있는 장학 제도 누르면 나오는 페이지 -->
<template>
<div class="Schlorship_part">
    <div class="IPad">
    </div>

    <div class="Ibox1">
        <div class="Ibox">
            <h2>취득 학점</h2>
            <bar-chart></bar-chart>
        </div>

        <div class="Ibox">
            <h2>취득 평점</h2>
            <line-chart></line-chart>
        </div>
    </div>

    <div class="Ibox2">
        <div class="IboxBorder">
            <a href="/grade/result">
            <h3>학습결과</h3>
            </a>
        </div>
        <div class="Ibox2n" align="left">
            <div class="Ibox21" align="left">
            <font size="3em">- 학년 : 4 </font><br><br>
            <font size="3em">- 전공 : 48 / 60</font><br><br>
            <font size="3em">- 교양 : 120 / 140</font><br><br>  
            </div>
        </div>
        <div class="IPad">
        </div>
    </div>

    <div class="IPad">
    </div>
</div>

</template>

<script>
import BarChart from '@/components/BarChart'
import LineChart from '@/components/LineChart'
  
  export default {
    name: 'VueChartJS',
    components: {
      BarChart,
      LineChart
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
  grid-template-columns: 1fr 4fr 2fr 2fr;
  grid-template-rows: 1000px;
  grid-gap: 10px;
}
.IPad{
  
}
.Ibox{
  
}
.IboxBorder{
  border: 1px solid;
}
.IboxPad{
  padding:9px;
}
.IboxPad15{
  padding:15px;
  
}
.IboxPad15Border{
  padding:15px;
  border: 1px solid;
}
.IboxMar{
  border: 1px solid;
  margin:5px;
}
.Ibox1{
  display: grid;
  grid-template-rows: 1fr 1fr;
  grid-gap: 10px;
}
.Ibox12{
  display: grid;
  grid-template-rows: 1fr 3fr 3fr 3fr 1fr;
  grid-gap: 0px;
}
.Ibox121{
  display: grid;
  grid-template-columns: 2fr 12fr 3fr;
  grid-gap: 0px;
  border: 1px solid;
}
.Ibox125{
  display: grid;
  grid-template-columns: 6fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}
.Ibox12n{
  display: grid;
  grid-template-rows: 1fr 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}
.Ibox2{
  padding:9px;
  display: grid;
  grid-template-rows: 1fr 8fr 8fr;
  grid-gap: 0px;
}
.Ibox2n{
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