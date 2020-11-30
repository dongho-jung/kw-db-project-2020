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
          <div v-for = "(my_list,idx) in My_class_list" :key="idx">
            <table border="1" bordercolor="black" width='460' height='580' align="center" font size="1em">
              <tr>
                <td width="100" style="word-break: break-all">aaa</td>
                <td width="100" style="word-break: break-all">aaaaaaaa</td>
                <td width="100" style="word-break: break-all">aaaaaa</td>
                <td width="100" style="word-break: break-all">aaaaaa</td>
                <td width="100" style="word-break: break-all">aaaaa</td>
                <td width="100" style="word-break: break-all">aaaaaaa</td>
              </tr>
            </table>
          </div>

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

import axios from "axios";

export default{
  data(){
    return{
      My_class_list: [
        {index: '',MON:'Mon',TUE:'Tue',WED:'Wed',THU:'Thr',FRI:'Fri'},
        {index: 1,MON:'',TUE:'',WED:'',THU:'',FRI:''},
        {index: 2,MON:'',TUE:'',WED:'',THU:'',FRI:''},
        {index: 3,MON:'',TUE:'',WED:'',THU:'',FRI:''},
        {index: 4,MON:'',TUE:'',WED:'',THU:'',FRI:''},
        {index: 5,MON:'',TUE:'',WED:'',THU:'',FRI:''},
        {index: 6,MON:'',TUE:'',WED:'',THU:'',FRI:''}
      ]
    }
  },
  methods:{
    Make_2D_list() {
      axios.get("http://127.0.0.1:5000/timetable", {withCredentials: true})
           .then(res=>{
             let all_data = res.data

             console.log('start')

             for (let i = 0 ; i<all_data.length; i++){
               let name = all_data[i].name;
               for (let j= 0; j<all_data[i].period; j++){
                 let period = all_data[i].period[j];
                 let date = period.slice(3)
                 let time = period.slice(-1)
                 this.My_class_list[time][date] = name;
               }
             }

           })
    }
  },
  created() {
    this.Make_2D_list();
  }
}

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