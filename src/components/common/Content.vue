<template>
  <div class="Main_part">
    <div class="ZPad"></div>
    <div class="Zbox1">
      <div class='Zbox11'>
        <div class='Zbox111'>
         <img alt="Profile" v-bind:src="kakao_profile_image" height = "100" width="160">
        </div>

        <div class='Zbox112'>
          <font size="3em" face="bold">{{kakao_name}}</font><br>
          <font size="1.5em">
            {{ id }}<br>
          {{kakao_email}}
          </font>
        </div>
      </div>
      
      <div class='Zbox12'>
        </div>

    </div>

    <div class="Zbox2">
      <div class='Zbox21'>
        <h3>ID : {{id}}</h3>
      </div>

      <div class='Zbox22'>
        <div v-for = "(my_list,idx) in My_class_list" :key="idx">
          <table border="1" bordercolor="black" width='460' height='580' align="center" font size="1em">
            <tr>
              <td width="100" style="word-break: break-all">{{my_list.index}}</td>
              <td width="100" style="word-break: break-all">{{ my_list.MON }}</td>
              <td width="100" style="word-break: break-all">{{my_list.TUE}}</td>
              <td width="100" style="word-break: break-all">{{my_list.WED}}</td>
              <td width="100" style="word-break: break-all">{{my_list.THU}}</td>
              <td width="100" style="word-break: break-all">{{my_list.FRI}}</td>
            </tr>
          </table>
        </div>
      </div>

    </div>

    <div class="Zbox3">
      <h1>Credit Polar Area Chart</h1>
       <div class="columns">
          <div class="column">
            <polar-area-chart></polar-area-chart>
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
import PolarAreaChart from '@/components/PolarAreaChart'

import axios from "axios";
export default{
  name: 'VueChartJS',
    components: {
        PolarAreaChart
  },

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
      ],
      id: this.$cookies.get('SuccessLogin'),

      kakao_name:'',
      kakao_email:'',
      kakao_profile_image:'',
      kakao_gender:'',
      kakao_birth:'',
    }
  },
  methods:{
    Make_2D_list() {
      let a = this.$cookies.isKey('SuccessLogin')
      console.log('Session ' + a)
      axios.get("http://localhost:5000/timetable")
           .then(res=>{
             let all_data = res.data
             console.log(all_data)
             for (let i = 0 ; i<all_data.length; i++){
               let name = all_data[i].name;
               console.log(name)
               for (let j= 0; j<all_data[i].period.length; j++){
                 let period = all_data[i].period[j];
                 let date = period.slice(0,3)
                 let time = period.slice(3,4)
                 console.log(date,time)
                 this.My_class_list[time][date] = name;
               }
             }
           })

      let URL = decodeURIComponent(this.$cookies.get('profile'))
      this.kakao_profile_image=URL
      let URL_ = decodeURIComponent(this.$cookies.get('name'))
      this.kakao_name=URL_
      let URL__ = decodeURIComponent(this.$cookies.get('email'))
      this.kakao_email=URL__
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
}

.Zbox42{
  background-color: white;
}

.Zbox43{
  background-color: white;
}

th{
  width: 20px;
}

#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
</style>