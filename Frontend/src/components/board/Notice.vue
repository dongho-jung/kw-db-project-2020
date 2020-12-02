<!--&lt;!&ndash;<template>&ndash;&gt;-->
<!--&lt;!&ndash;  <div class="List_part">&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="CPad">&ndash;&gt;-->
<!--&lt;!&ndash;    </div>&ndash;&gt;-->
<!--&lt;!&ndash;    <div class="Cbox1">&ndash;&gt;-->
<!--&lt;!&ndash;      <div class="CboxBorder">&ndash;&gt;-->
<!--&lt;!&ndash;        <h1>READ NOTICE</h1>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->
<!--&lt;!&ndash;      <div class="Cbox12">&ndash;&gt;-->
<!--&lt;!&ndash;        <div class="Cbox121">&ndash;&gt;-->
<!--&lt;!&ndash;            <select v-model='year' name="subject" style="width:100px;height:50px;" >&ndash;&gt;-->
<!--&lt;!&ndash;              <option value="">YEAR</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2020</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2019</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2018</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2017</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2016</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2015</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2014</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2013</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2012</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2011</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2010</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2009</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2008</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2007</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2006</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2005</option>&ndash;&gt;-->
<!--&lt;!&ndash;            </select>&ndash;&gt;-->
<!--&lt;!&ndash;            <select v-model='quarter' name="subject" style="width:100px;height:50px;" align="right">&ndash;&gt;-->
<!--&lt;!&ndash;              <option value="">QUARTER</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>1</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>2</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>3</option>&ndash;&gt;-->
<!--&lt;!&ndash;              <option>4</option>&ndash;&gt;-->
<!--&lt;!&ndash;            </select>&ndash;&gt;-->
<!--&lt;!&ndash;          <div class="Fbox134"><br>&ndash;&gt;-->
<!--&lt;!&ndash;            <p><input type="button"  v-on:click="Search_Notice" value="Search Notice" width=70 style = "width:260pt;height:20pt;text-align:center;"></p>&ndash;&gt;-->
<!--&lt;!&ndash;          </div>&ndash;&gt;-->
<!--&lt;!&ndash;        </div>&ndash;&gt;-->

<!--&lt;!&ndash;        </div>&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->
<!--&lt;!&ndash;    </div>&ndash;&gt;-->
<!--<template>-->
<!--  <div class="List_part22">-->
<!--    <div class="ZPad">-->
<!--    </div>-->

<!--    <div class="Zbox1">-->
<!--      <div class="ZboxBorder" style='padding: 10px 0px 10px 0px;'>-->
<!--        <h1>READ NOTICE</h1>-->
<!--      </div>-->
<!--      <div class="Zbox12">-->
<!--        <div class="Zbox121" style='padding: 10px 0px 10px 10px;'>-->
<!--          <div class="Zbox">-->
<!--            <select v-model='year' name="subject" style="width:100px;height:40px;align:center" >-->
<!--              <option value="">YEAR</option>-->
<!--              <option>2020</option>-->
<!--              <option>2019</option>-->
<!--              <option>2018</option>-->
<!--              <option>2017</option>-->
<!--              <option>2016</option>-->
<!--              <option>2015</option>-->
<!--              <option>2014</option>-->
<!--              <option>2013</option>-->
<!--              <option>2012</option>-->
<!--              <option>2011</option>-->
<!--              <option>2010</option>-->
<!--              <option>2009</option>-->
<!--              <option>2008</option>-->
<!--              <option>2007</option>-->
<!--              <option>2006</option>-->
<!--              <option>2005</option>-->
<!--            </select>-->
<!--          </div>-->

<!--          <div class="Zbox">-->
<!--            <select v-model='quarter' name="subject" style="width:100px;height:40px;" align="right">-->
<!--              <option value="">QUARTER</option>-->
<!--              <option>1</option>-->
<!--              <option>2</option>-->
<!--              <option>3</option>-->
<!--              <option>4</option>-->
<!--            </select>-->
<!--          </div>-->

<!--          <div class="ZPad"></div>-->

<!--          <div class="Zbox13">-->
<!--            <div style="overflow-x:auto; overflow-y:auto;">-->
<!--              <table border="1" bordercolor="black" align="center" font size="1em">-->
<!--                <tr height='200' align="left">-->
<!--                  <td>-->
<!--                    <font size="5em">Title: </font><br><br>-->
<!--                    <font size="4em">Writer_ID:</font><br>-->
<!--                    <font size="4em">Date: </font><br>-->
<!--                    <font size="4em">LIKE: </font><br><br>-->
<!--                    <font size="3em">Content: </font>-->
<!--                  </td>-->
<!--                </tr>-->

<!--              </table>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->


<!--          <div class='Zbox' style="padding: 5px 10px 0px 0px;">-->
<!--            <input type="button"  v-on:click="Search_Notice" value="Search Notice" style="width:160px;height:30px;text-align:center;">-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->



<!--  <div v-for="(each_post,idx) in post" :key="idx">-->
<!--    <div class="Cbox12n">-->
<!--      <font size="5em">Post number: {{idx+1}}</font>-->
<!--      <div class="Cbox" align="left">-->
<!--        <font size="5em">Title: {{each_post[2]}}</font><br><br>-->
<!--        <font size="4em">Writer_ID: {{each_post[0]}}</font><br>-->
<!--        <font size="4em">Date: {{year}}/{{quarter}}</font><br>-->
<!--        <font size="4em">LIKE: {{each_post[4]}} HITS: {{each_post[3]}}</font><br><br>-->
<!--        <font size="3em">Content: {{each_post[1]}}</font>-->
<!--      </div>-->
<!--    </div>-->

<template>
  <div class="List_part22">
    <div class="ZPad">
    </div>

    <div class="Zbox1">
      <div class="ZboxBorder" style='padding: 10px 0px 10px 0px;'>
        <h1>READ NOTICE</h1>
      </div>
      <div class="Zbox12">
        <div class="Zbox121" style='padding: 10px 0px 10px 10px;'>
          <div class="Zbox">
            <select v-model='year' name="subject" style="width:100px;height:40px;align:center" >
              <option value="">YEAR</option>
              <option>2020</option>
              <option>2019</option>
              <option>2018</option>
              <option>2017</option>
              <option>2016</option>
              <option>2015</option>
              <option>2014</option>
              <option>2013</option>
              <option>2012</option>
              <option>2011</option>
              <option>2010</option>
              <option>2009</option>
              <option>2008</option>
              <option>2007</option>
              <option>2006</option>
              <option>2005</option>
            </select>
          </div>

          <div class="Zbox">
            <select v-model='quarter' name="subject" style="width:100px;height:40px;" align="right">
              <option value="">QUARTER</option>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
            </select>
          </div>

          <div class="ZPad"></div>


          <div class='Zbox' style="padding: 5px 10px 0px 0px;">
            <input type="button"  v-on:click="Search_Notice" value="Search Notice" style="width:160px;height:30px;text-align:center;">
          </div>
        </div>
      </div>

      <div class="Zbox13">
        <div style="overflow-x:auto; overflow-y:auto;">
          <table border="0" bordercolor="black" align="center" font size="1em">
            <div v-for="(each_post,idx) in post" :key="idx">
              <tr height='200' align="left" width="500">
                <td>
                  <font size="3em">Post_ID: {{idx+1}}</font><br>
                  <font size="5em">Title: {{each_post[2]}}</font><br><br>
                  <font size="4em">Writer_ID: {{each_post[0]}}</font><br>
                  <font size="4em">Date: {{year}}/{{quarter}}</font><br>
                  <font size="4em">LIKE: {{each_post[4]}} HITS: {{each_post[3]}}</font><br><br>
                  <font size="3em">Content:{{each_post[1]}}</font>
                </td>
              </tr>
            </div>
          </table>
        </div>
      </div>

    </div>

    <div class="Zbox2">
      <div class="ZboxBorder">
        <h1>Notice of Midterm Exam</h1>
        <div class="ZboxPad" align="right">
            <font size="3em">Notice Date: 12/02</font>
        </div>
      <div class="Zbox21" align="left">
        <font size="3em">Date of MidtemExam : 10/ 31 10:00</font><br><br>
        <font size="3em">Place of MidtermExam : Hanyoul B101</font><br><br>
        <font size="3em">Midterm Exam Range : P.11 ~ P.2547</font><br><br>
          <div class=Zboxpad align="center">
            <h3>[WARNNING]</h3><br>
          </div>
        <font size="3em">-You must wear a mask to take the test.</font><br><br>
        <font size="3em">-For hygiene, please sit one space away from the seat next to you.</font><br><br>
        <font size="3em">-You cannot leave the room for 30 minutes after starting the test.</font><br><br>
        <font size="3em">-If you are in a hurry to restroom, please fix it in advance.</font><br><br>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios";
export default {
  data(){
    return{
      year : '',
      quarter : '',

      post: []

    }
  },
  methods:{
    Search_Notice: function () {
      axios.get('/post',{
        baseURL: 'http://localhost:5000',
        params: {
          year: this.year,
          quarter: this.quarter
        }
      })
          .then(res=>{ //못찾으면 error 출력하도록 유도
            console.log(res.data);
            alert('You can find "'+ res.data.length+ '" post')
            this.post = res.data


          })
          .catch(error =>{
            console.log(this.year,this.quarter)
            console.log(error);
          })``
    }
  },
  created() {
    this.Search_Notice()
  },
}


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
.List_part22 > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}
.List_part22{
  display: grid;
  grid-template-columns: 2fr 4fr 2fr 2fr;
  grid-template-rows: 1000px;
  grid-gap: 10px;
}
.ZPad{

}
.Zbox{

}
.ZboxBorder{
}
.ZboxPad{
  padding:9px;
}
.ZboxPad15{
  padding:15px;

}
.ZboxPad15Border{
  padding:15px;
  border: 1px solid;
}
.ZboxMar{
  border: 1px solid;
  margin:5px;
}
.Zbox1{
  display: grid;
  grid-template-rows: 70px 50px 800px;
  grid-gap: 10px;
}
.Zbox12{
  display: grid;
  grid-template-rows: 1fr;
  grid-gap: 0px;
}
.Zbox13{
  display: grid;
  grid-template-rows: 800px;
}
.Zbox121{
  display: grid;
  grid-template-columns: 2fr 2fr 4fr 3fr;
  grid-gap: 0px;
}
.Zbox125{
  display: grid;
  grid-template-columns: 6fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}
.Zbox12n{
  display: grid;
  grid-template-rows: 1fr 2fr 1fr;
  grid-gap: 1px;
}
.Zbox2{
  padding:9px;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 9fr;
  grid-gap: 0px;
}
.Zbox2n{
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
