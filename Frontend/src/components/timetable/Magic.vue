<template>
  <div class="Magic_part">
    <div class="EPad">
    </div>
    <div class="Ebox1">
      <div class="Ebox11" style = "padding: 10px 0px 0px 0px;">
        <h2>Time table Maker</h2>
      </div>
      <div class="Ebox112">
        <div style="overflow-x:auto; overflow-y:auto; height:280px;">
          <table border="1" bordercolor="black" width='670' height='590' text-align="center" font size="1em">
            <div v-for="(item,idx) in Time_table" :key="idx">
              <tr>
                <td width="10%" style="word-break:break-all">{{item.index}}</td>
                <td width="18%" style="word-break:break-all">{{item.first_class}}</td>
                <td width="18%" style="word-break:break-all">{{item.second_class}}</td>
                <td width="18%" style="word-break:break-all">{{item.third_class}}</td>
                <td width="18%" style="word-break:break-all">{{item.forth_class}}</td>
                <td width="18%" style="word-break:break-all">{{item.fifth_class}}</td>
                <td width="18%" style="word-break:break-all">{{item.sixth_class}}</td>
              </tr>
            </div>
          </table>
        </div>
      </div>
    </div>

    <div class="Ebox2">
      <div class="Ebox21" style = "padding: 30px 0px 0px 0px;">
        <h2>Please select all questions</h2>
      </div>
      <div class="Ebox22">
        <div class="Ebox" style = "padding: 33px 0px 0px 0px;">
          <input type="radio" name="rad1" id="DC" v-model="a" value="DC" />상관 없음
        </div>
        <div class="Ebox" style = "padding: 33px 0px 0px 0px;">
          <input type="radio" name="rad1" id="AM" v-model="b" value="AM" />이른 강의
        </div>
        <div class="Ebox" style = "padding: 33px 0px 0px 0px;">
          <input type="radio" name="rad1" id="PM" v-model="c" value="PM"/>늦은 강의
        </div>
        <div class="Ebox" style = "padding: 33px 0px 0px 0px;">
          <input type="radio" name="rad1" id="SP" v-model="d" value="SP"/>공강
        </div>
        <div class="Ebox" style = "padding: 33px 10px 0px 0px;">
          <select v-model="selected_index">
            <option>Mon</option>
            <option>Tue</option>
            <option>Wed</option>
            <option>Thr</option>
            <option>Fri</option>
          </select>
        </div>
      </div>
      <div class="Ebox24">
        <div class="Ebox" style = "padding: 33px 0px 0px 0px;">
          <input type="radio" name="rad3" id="NM" v-model="e" value="SL"/>소규모 강의
        </div>
        <div class="Ebox" style = "padding: 33px 0px 0px 0px;">
          <input type="radio" name="rad3" id="MA" v-model="f" value="LL"/>대규모 강의
        </div>
      </div>
      <div class="Ebox25">
        <div class="EPad">
        </div>
        <div class="Ebox" style = "padding: 33px 0px 0px 20px;">
          <font size="2.5em">전체 요구 학점 : </font>
        </div>
        <div class="Ebox" style = "padding: 33px 0px 0px 0px;">
          <input type="text" v-model="required" name="Search_text" style = "width: 100px; height:20px;">
        </div>
        <div class="EPad">
        </div>
      </div>
      <div class="EPad">
      </div>
      <div class="Ebox26">
        <div class="Ebox261" style = "padding: 10px 0px 0px 0px;">
          <p><input type="button" v-on:click='Make' value="Make Time Table" size=70 style = "width:80pt;height:20pt;text-align:center; padding: 0px 0px 0px 0px;"></p>
        </div>
        <div class="Ebox262" style = "padding: 10px 0px 0px 0px;">
          <p><input type="button" v-on:click='Back' value="Go Back" size=70 style = "width:80pt;height:20pt;text-align:center;"></p>
        </div>
      </div>
    </div>
    <div class="EPad">
    </div>
  </div>
</template>

<script>

//import axios from "axios";

import axios from "axios";

export default {
  data() { //전역변수라고 생각하면 편해 그리고 method에서 쓰일 수 있는 변수들을 선언할 수 있
    return {

      a: null,
      b: null,
      c: null,
      d: null,
      e: null,
      f: null,
      prefer_time: '',
      prefer_cap:'',
      selected_index: '',
      required:'',

      // for making favorite table
      Time_table: [
        {
          index: '○',
          first_class: 'MON',
          second_class: 'TUE',
          third_class: 'WED',
          forth_class: 'THR',
          fifth_class: 'FRI',
          sixth_class: 'SAT'
        },
        {index: 1, first_class: '', second_class: '', third_class: '', forth_class: '', fifth_class: '', sixth_class: ''},
        {index: 2, first_class: '', second_class: '', third_class: '', forth_class: '', fifth_class: '', sixth_class: ''},
        {index: 3, first_class: '', second_class: '', third_class: '', forth_class: '', fifth_class: '', sixth_class: ''},
        {index: 4, first_class: '', second_class: '', third_class: '', forth_class: '', fifth_class: '', sixth_class: ''},
        {index: 5, first_class: '', second_class: '', third_class: '', forth_class: '', fifth_class: '', sixth_class: ''},
        {index: 6, first_class: '', second_class: '', third_class: '', forth_class: '', fifth_class: '', sixth_class: ''},
      ],


    };
  },

  methods: { //지역 변수 + 함수들 {{선언 공간
    Make: function () {
      if (this.a==true){
        this.prefer_time=''
      }
      else if(this.b==true){
        this.prefer_time='early'
      }
      else if(this.c==true){
        this.prefer_time='late'
      }
      else if(this.d==true){
        this.prefer_time='free_'+this.selected_index
      }
      if (this.e == true){
        this.prefer_cap='small'
      }
      if(this.f==true){
        this.prefer_cap='large'
      }
      axios.get('/wizard',{
        baseURL: 'http://localhost:5000',
        params: {
          year: 2020,
          quarter: 1,
          desired_credit: this.required,
          prefer_time: this.prefer_time,
          prefer_cap: this.prefer_cap
        }
      })
          .then(res=>{ //못찾으면 error 출력하도록 유도
            console.log(res.data.data)
            alert('You can use it')




          })
          .catch(error =>{
            console.log(error)
            if (this.required==''){
              alert('Please input Required credit')
            }
          })
    },
    Back: function(){
      this.$router.push('/')
    }
  }
  ,created() {
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
  grid-template-columns: 670px;
  grid-template-rows: 60px 590px;
  grid-gap: 10px;
  border: 1px solid;
}

.Ebox11{
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
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 1fr;
  border: 1px solid;
}

.Ebox2{
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-gap: 10px;
}

.Ebox21{
  border: 1px solid;
}

.Ebox22{
  display: grid;
  grid-template-columns: 3fr 3fr 3fr 3fr 1fr;
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