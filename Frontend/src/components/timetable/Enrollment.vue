
<template>
  <div class="Enrollment_part">
    <div class="Fbox1">
      <div class="Fbox11" align="center">All class
        <div class="Fbox111">
          <table border="1" bordercolor="black" width='560' height='580' align="center">
            <tr>
              <td width="25%" style="word-break:break-all">Name</td>
              <td width="20%" style="word-break:break-all">Class Id</td>
              <td width="20%" style="word-break:break-all">Professor</td>
              <td width="15%" style="word-break:break-all">Period</td>
              <td width="15%" style="word-break:break-all">Place</td>
              <td width="5%" style="word-break:break-all">C</td>
              <td width="5%" style="word-break:break-all">●</td>
            </tr>
          </table>
        </div>
        <div class="Fbox112">
          <div style="overflow-x:auto; overflow-y:auto; height:280px;">
            <div v-for="(class_,idx) in class_list" :key="idx">
              <table border="1" bordercolor="black" width='560' height='580' text-align="center" font size="1em">
                <tr>
                  <td width="25%" style="word-break:break-all">{{class_.class_name}}</td>
                  <td width="20%" style="word-break:break-all">{{class_.class_id}}</td>
                  <td width="20%" style="word-break:break-all">{{class_.professor_name}}</td>
                  <td width="15%" style="word-break:break-all">{{class_.period}}</td>
                  <td width="15%" style="word-break:break-all">{{class_.place}}</td>
                  <td width="5%" style="word-break:break-all">{{class_.credit}}</td>
                </tr>
              </table>
            </div>
          </div>
        </div>
      </div>

    <div class="Fbox12">
      <img src="https://www.kw.ac.kr/ko/img/symbol02_08.jpg" style="width: auto; height: 130px">

    </div>

    <div class="Fbox13">
      <div class="Fbox131">
        <div class="Fbox1311">
          <font size="3em" face="bold"><p>Class ID : </p></font>
        </div>

        <div class="Fbox1312">
          <p><input v-model="search_class_id" placeholder="Class ID를 입력하시오" size=50 style = "text-align:center;"></p>
        </div>

        <div class="Fbox1313">
          <p><input type="button" v-on:click="search_class" value="Search" size=70 style = "width:60pt;height:16pt;text-align:center;"></p>
        </div>
      </div>

      <div class="Fbox132" align="center">
        <font size="3em" face="bold"><p>Search Result</p></font>
      </div>

      <div class="Fbox133">
        <table border="1" bordercolor="black" width='560' height='580' align="center" font size="1em">
          <th width="220" height="30">Name</th><th width="120">Class Id</th><th width="160">Class Professor</th><th width="100">Period</th><th width="100">Place</th><th>Credit</th>
            <tr>
              <td width="220">{{res_search_name}}</td>
              <td width="120">{{res_search_class_id}}</td>
              <td width="160">{{ res_search_class_professor }}</td>
              <td width="100">{{ res_search_period }}</td>
              <td width="100">{{res_search_place}}</td>
              <td>{{res_search_credit}}</td>
            </tr>
        </table>
      </div>

      <div class="Fbox134">
        <p><input type="button"  v-on:click="Push_to_Favorite" value="Push to Favorite" width=70 style = "width:260pt;height:20pt;text-align:center;"></p>
      </div>

    </div>
   </div>

   <div class="Fbox2">
     <div class="Fbox21">
        <div class="Fbox211">
          <hn>Select index number</hn>
          <hn>that you want to Earse</hn>
          <select @change="Remove_Favorite" v-model="selected_index">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            <option>6</option>
            <option>7</option>
            <option>8</option>
          </select>
          <p></p>
          <span>Your selected number: </span>
          <hn> {{ selected_index }}</hn>
        </div>
        <div class="Fbox212">
          <table border="1" bordercolor="black" width='560' height='580' align="center" font size="1em">
            <div v-for="(item,idx) in favorite_table" :key="idx">
                <tr>
                    <td width="100" height='30'>{{ item.index }}</td>
                    <td width="400" height='30'>{{ item.name }}</td>
                    <td width="160" height='30'>{{ item.class_id }}</td>
                    <td width="160" height='30'>{{ item.class_professor }}</td>
                    <td width="100" height='30'>{{ item.period }}</td>
                    <td width="100" height='30'>{{ item.place }}</td>
                    <td width="100" height='30'>{{ item.credit }}</td>
                </tr>
            </div>
          </table>
        </div>
     </div>

     <div class="Fbox22">
       <div class="Pad">
         <font size="5em" face="bold"><p>Course registration time: 10:00:00</p></font>
       </div>
       <div class="Fbox221">
         <font size="5em" face="bold"><p>Current Server Time: {{now}}</p></font>
       </div>
       <div class="Pad">
         <p><input type="button" v-on:click="time" value="Update current server time" width="70" style = "width:280pt; height:30pt; text-align:center;"></p>
       </div>
       <div class="Fbox222">
         <p><input type="button" v-on:click="Enrollment" value="Enrollment all" width=70 style = "width:280pt; height:30pt; text-align:center;"></p>
       </div>
     </div>
   </div>
  </div>
</template>

<script>

import axios from "axios";

export default {
  data() { //전역변수라고 생각하면 편해 그리고 method에서 쓰일 수 있는 변수들을 선언할 수 있
    return {

      // for first_api
      class_list: [],
      all_data:[],

      // value_of_class_id_that_user_want_to_search
      search_class_id: null,

      // after searching_class_id
      res_search_name: null,
      res_search_class_id: null,
      res_search_class_professor: null,
      res_search_period: null,
      res_search_place: null,
      res_search_credit: null,

      // for making favorite table
      favorite_table: [
        {index: 'Index',name:'Name',class_id: 'Class Id',class_professor: 'Class Professor',period: 'Period',place: 'Place',credit: 'Credit'},
        {index: 1, name: '',class_id:'',class_professor:'',period:'',place:'',credit:''},
        {index: 2, name: '',class_id:'',class_professor:'',period:'',place:'',credit:''},
        {index: 3, name: '',class_id:'',class_professor:'',period:'',place:'',credit:''},
        {index: 4, name: '',class_id:'',class_professor:'',period:'',place:'',credit:''},
        {index: 5, name: '',class_id:'',class_professor:'',period:'',place:'',credit:''},
        {index: 6, name: '',class_id:'',class_professor:'',period:'',place:'',credit:''},
        {index: 7, name: '',class_id:'',class_professor:'',period:'',place:'',credit:''},
        {index: 8, name: '',class_id:'',class_professor:'',period:'',place:'',credit:''}
      ],

      // selected number for earasing
      selected_index: '',

      // for server time(current time)
      now : "00:00:00",

      // My Class List
    };
  },

  methods: { //지역 변수 + 함수들 {{선언 공간
    // Server time
    time: function(){
      let date = new Date();

      this.now = date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();

    },
    // 1. All class 를 보여줄 때 전체 ==> 전체 수강 시간표를 좌측 상단 Table에 가져오는 것
    //     api = http://0.0.0.0/timetable?get
    Set_all_class_list() {
        axios
        .get("http://localhost:5000/class")
            .then(res => {
              this.all_data = res.data;
              console.log(this.all_data)
              for (let i =0 ; i<this.all_data.length; i++){
                if (this.all_data[i].year == '2020' && this.all_data[i].quarter=='2'){
                  this.class_list.push(this.all_data[i]);
                }
              }
              console.log(this.class_list);
            })
            .catch(err => {
              console.log(err);
            });
    },

    // 2. 우측 상단 Search button ==> 학정번호 일치하는 것을 찾는 것
    search_class: function(){
      let want_value = this.search_class_id;
      for (let i = 0; i<this.class_list.length; i++) {
        if (this.class_list[i].class_id == want_value) {
          this.res_search_name = this.class_list[i].class_name;
          this.res_search_class_id = this.class_list[i].class_id;
          this.res_search_class_professor = this.class_list[i].professor_name;
          this.res_search_period = this.class_list[i].period;
          this.res_search_place = this.class_list[i].place;
          this.res_search_credit = this.class_list[i].credit;
          return
        }
      }
      alert('Fail to find')
    },

    // 3. Push 버튼을 누르면 좌측 하단 Table에 마지막 index에 추가시키기
    // api = x / front 자체처리 / Table값이 다 채워져 있으면 예외처리 ( Max index : 8 )
    Push_to_Favorite: function () {
      let check_count = 1;
      let check_full = 1;
      for(let i=0; i<this.favorite_table.length;i++){
        if(this.favorite_table[i].class_id!=''){
           check_full = check_full+1;
        }
      }
      if (check_full == 9){
        alert('FULL')
        return
      }

      for(let i=0; i<this.favorite_table.length;i++) {
        if (this.favorite_table[i].class_id == this.search_class_id) {
          alert('class_id "' + this.favorite_table[i].class_id + '" is already pushed in your Favorite!!')
          break;
        }
        if (this.favorite_table[i].class_id == '') {
          check_count = check_count + 1;
          this.favorite_table[i].name = this.res_search_name;
          this.favorite_table[i].class_id = this.res_search_class_id;
          this.favorite_table[i].class_professor = this.res_search_class_professor;
          this.favorite_table[i].period = this.res_search_period;
          this.favorite_table[i].place = this.res_search_place;
          this.favorite_table[i].credit = this.res_search_credit;
          alert('Success to push in "' + i + '" index');
          break;
        }
      }
    },

    // 4. 삭제 버튼을 누르면 해당 index에 있는 data 삭제
    Remove_Favorite() {
      for (let i = 0; i < this.favorite_table.length; i++) {
        if (this.favorite_table[i].index == this.selected_index) {
          if (this.favorite_table[i].class_id == '' ){
            alert('Fail to erase: already empty')
            return
          }
          else
          {
            this.favorite_table[i].name = '';
            this.favorite_table[i].class_id = '';
            this.favorite_table[i].class_professor = '';
            this.favorite_table[i].period = '';
            this.favorite_table[i].place = '';
            this.favorite_table[i].credit = '';
          }
          alert('Success to erase index '+ this.selected_index)
          return
        }
      }
    },
    // 5. 수강신청 이라는 button ==> index 차례대로 되어있는 값이
    //      예외처리 : if 기존 database에 class_id가 중복 되는지 확인
    //                  if 중복:
    //                    if 학점이 C+이 이상일 경우:
    //                          수강 가능
    //                    else 수강 불가능
    //                  else:
    //                     database frontent에 삽입
    //                특정 서버시간이 완료될때 버튼 활성화 (x)
    //                선후수 과목 중 a를 들어야만 a'을 들을 수 있는 기능
    //                21학점이 넘는지안넘는
    //
    Enrollment: function (){
      for (let i=1; i<this.favorite_table.length; i++){
        if (this.favorite_table[i].class_id!=''){
          let favorite_class_id = this.favorite_table[i].class_id
          let bodyFormdata = new FormData();
          bodyFormdata.append('class_ids',favorite_class_id)
          console.log(this.username, this.password)
          axios({
            method: 'post',
            baseURL: 'http://localhost:5000',
            url: '/enroll',
            data: bodyFormdata,
            headers: {'Content-Type': 'multipart/form-data' }
          })
              .then(res=> {
                console.log(res);
                this.$cookies.set("SuccessLogin")
                this.$router.push("/");
                this.$router.go()
              }, async function (error) {
                console.log('에러일 경우', error.config);
                alert('Worng ID or PW');
              })
          alert('Success to enrollment' + favorite_class_id)
        }
      }
    }
  },
  created() {
    this.Set_all_class_list();
  }
};

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
  text-align:center;
  width: 100%;
  height: 100%;
}

a{text-decoration:none; color:black}

.Enrollment_part > div {
  border-radius: 5px;
  background-color: white;
  border: 1px solid;
  padding: 1em;
}

.Enrollment_part{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 400px 400px;
  grid-gap: 10px;
}

.Fbox1{
  display: grid;
  grid-template-columns: 5fr 1fr 5fr;
  grid-template-rows: 350px;
  grid-gap: 20px;
}

.Fbox11{
  display: grid;
  grid-template-rows: 3fr 7fr;
  grid-gap: 10px;
}

.Fbox111{
  border: 1px solid;
}

.Fbox112{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
  border: 1px solid;
}

.Fbox12{

  display: grid;
  grid-template-rows: 2fr 1fr 1fr 2fr;
  grid-gap: 20px;
  border: 1px none;
}

.Fbox13{
  display: grid;
  grid-template-rows: 1fr 1fr 3fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}

.Fbox131{
  display: grid;
  grid-template-columns: 1fr 3fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}

.Fbox1311{
  border: 1px solid;
}

.Fbox1312{
  border: 1px solid;
}

.Fbox1313{
  border: 1px solid;
}

.Fbox132{
  border: 1px solid;
}

.Fbox133{
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
  border: 1px solid;
}

.Fbox134{
  border: 1px solid;
}

.Fbox2{
  display: grid;
  grid-template-columns: 7fr 3fr;
  grid-template-rows: 350px;
  grid-gap: 20px;
}

.Fbox21{
  display: grid;
  grid-template-columns: 1fr 10fr;
  grid-gap: 10px;
  border: 1px solid;
}

.Fbox211{
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-gap: 1px;
  border: 1px solid;

}

.Fbox2111{
  border: 1px solid;
}

.Fbox2112{
  border: 1px solid;
}

.Fbox2113{
  border: 1px solid;
}

.Fbox2114{
  border: 1px solid;
}

.Fbox2115{
  border: 1px solid;
}

.Fbox2116{
  border: 1px solid;
}

.Fbox2117{
  border: 1px solid;
}

.Fbox2118{
  border: 1px solid;
}

.Fbox212{
  border: 1px solid;
}

.Fbox213{
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}

.Fbox2131{
  border: 1px solid;
}

.Fbox2132{
  border: 1px solid;
}

.Fbox2133{
  border: 1px solid;
}

.Fbox2134{
  border: 1px solid;
}

.Fbox2135{
  border: 1px solid;
}

.Fbox2136{
  border: 1px solid;
}

.Fbox2137{
  border: 1px solid;
}

.Fbox2138{
  border: 1px solid;
}
.Fbox212{
  border: 1px solid;
}

.Fbox22{
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}

.Fbox221{
  border: 1px solid;

}

.Fbox222{
  border: 1px solid;
}

.Fbox223{
  border: 1px solid;
}


.Pad{
  border: 1px solid;
}

#wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>