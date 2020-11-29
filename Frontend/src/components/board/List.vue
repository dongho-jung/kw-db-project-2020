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
            <img alt="DB1" src="../../assets/Search.png" height = "30" width="30">
          </div>
          <div class="AboxPad">
            <input type="text" name="Search_text" style = "width: 460px; height:24px;">
          </div>
          <div class="AboxPad">
            <button class="Abutton" id="Search_btn" v-on:click="connect_url('/')">Search</button>
          </div>
        </div>
      </div>

      <div v-for="(user, idx) in users" :key="idx">
        <div class="Abox1n">
          <div class="Abox" align="left" style="padding:3px 0px 0px 5px;">
            <a href="/board/hotlist">
              <font size="5em">{{user.first_name}}</font>
            </a>

          </div>
          <div class="Abox" align="left" style="padding:0px 0px 0px 10px;">
            <font size="3em">{{user.last_name}}</font><br><br><br>
            <font size="3em">{{user.email}}</font>
          </div>
          <div class="AboxPad" align="right">
            <font size="3em">{{user.id}}</font>
          </div>
        </div>
      </div>

      <div class="Abox13">
        <div class="APad" align="center">
        </div>
        <div class="AboxPad15" align="center">
          <font size="4em">1</font>
        </div>
        <div class="AboxPad15" align="center">
          <a href="/board/hotlist">
            <font size="3em">◀</font>
          </a>
        </div>
        <div class="AboxPad15" align="center">
          <a href="/board/hotlist">
            <font size="3em">▶</font>
          </a>
        </div>
      </div>

      <div class="Abox14">
        <div class="AboxPad">
          <img alt="DB1" src="../../assets/pencil.png" height = "30" width="30">
        </div>
        <div class="Abox1211">
          <div class="AboxPad">
            <font size="3em">Title</font>
          </div>
          <div class="AboxPad">
            <input type="text" name="Title" style = "width:360pt;height:20pt;text-align:left;">
          </div>
          <div class="AboxPad">
            <font size="3em">Content</font>
          </div>
          <div class="AboxPad">
            <input type="text" name="Contents" style = "width:360pt;height:60pt;text-align:left;">
          </div>
        </div>
        <div class="AboxPad">
          <input type="button" name="UPload" value="Upload" style = "width:60pt;height:24pt;text-align:center;">
        </div>
      </div>

    </div>

    <div class="Abox2">
      <div class="AboxBorder">
        <h2>HOT게시판</h2>
      </div>
      <div class="Abox2n">
        <div class="AboxPad15" align="left">
          <a href="/board/hotlist">
            <font size="2.8em">진짜 너무 한거 아니냐...</font>
          </a>
        </div>
        <div class="AboxPad15" align="right">
          <font size="2em">11/23 09:13</font>
        </div>
      </div>
      <div class="Abox2n">
        <div class="AboxPad15" align="left">
          <a href="/board/hotlist">
            <font size="2.8em">송라이팅1 수강생 여러분</font>
          </a>
        </div>
        <div class="AboxPad15" align="right">
          <font size="2em">11/23 01:28</font>
        </div>
      </div>
      <div class="Abox2n">
        <div class="AboxPad15" align="left">
          <a href="/board/hotlist">
            <font size="2.8em">오늘은 연평도 포격사건 10주기</font>
          </a>
        </div>
        <div class="AboxPad15" align="right">
          <font size="2em">11/23 01:01</font>
        </div>
      </div>
      <div class="Abox2n">
        <div class="AboxPad15" align="left">
          <a href="/board/hotlist">
            <font size="2.8em">짜잔</font>
          </a>
        </div>
        <div class="AboxPad15" align="right">
          <font size="2em">11/22 20:46</font>
        </div>
      </div>
      <div class="AboxPad15">
        <a href="/board/hotlist">
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
import axios from "axios";

export default {
  data() {
    return {
      users: null,
      totalPage: null,
      pageNum: 1
    };
  },
  methods: {
    fetchData(pageNum) {
      axios
          .get("https://reqres.in/api/users?page=" + pageNum)
          .then(res => {
            this.users = res.data.data;
            this.totalPage = res.data.total_pages;
          })
          .catch(err => {
            console.log(err);
          });
    },
    created() { // 바로 실행할꺼
      this.fetchData(this.pageNum);
    },
    connect_url(url) {
      this.$router.push('/board/list' + url)
    }
  }

  // Search function

  // Upload function

  // Paginf function

  // Connect link
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
  grid-template-rows: 1fr;
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
  grid-template-rows: 100px 60px 200px 200px 200px 200px 200px 200px 60px 160px ;
  grid-gap: 0px;
}

.Abox1n{
  display: grid;
  grid-template-rows: 1fr 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}

.Abox12{
  display: grid;
  grid-template-rows: 1fr 3fr 3fr 3fr 1fr;
}

.Abox13{
  display: grid;
  grid-template-columns: 6fr 1fr 1fr 1fr;
  grid-gap: 10px;
  border: 1px solid;
}

.Abox14{
  display: grid;
  grid-template-columns: 2fr 12fr 3fr;
  grid-gap: 0px;
  border: 1px solid;
}

.Abox121{
  display: grid;
  grid-template-columns: 2fr 12fr 3fr;
  grid-gap: 0px;
  border: 1px solid;
}

.Abox1211{
  display: grid;
  grid-template-rows: 1fr 3fr;
  grid-template-columns: 1fr 10fr;
  grid-gap: 0px;
}
.Abox123{
  display: grid;
  grid-template-columns: 6fr 1fr 1fr 1fr;
  grid-gap: 10px;
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