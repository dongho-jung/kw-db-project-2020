<template>
	<header>
      <div class="menuWrap">
        <ul v-if="success_login === true" class="menu">
          <h1>
            <router-link to="/">
              <img alt="Vue logo" src="../../assets/KWLOGO.jpg" width="80">
            </router-link>
          </h1>
          <li><router-link to="/board/list2">Author</router-link></li>
          <li><router-link to="/board/notice">Notice</router-link></li>
          <li><router-link to="/board/list">List</router-link></li>
          <li><router-link to="/grade/result">Result of Degree</router-link></li>
          <li><router-link to="/grade/schlorship">Scholorship</router-link></li>
          <li><router-link to="/timetable/prereq">Prereq</router-link></li>
          <li><router-link to="/timetable/magic">Magic</router-link></li>
          <li><router-link to="/timetable/enrollment">Enrollment</router-link></li>
          <li v-on:click="logout"><router-link to="/login">Log Out</router-link></li>
        </ul>
        <u1 v-else>
        </u1>
      </div>

	</header>
</template>

<script>
export default {
  data(){
    return {
      success_login: ''
    }
  },
  methods:{
    deleteCookie: function(name) {
      var date = new Date();
      document.cookie = name + "= " + "; expires=" + date.toUTCString() + "; path=/";
    },
    logout: function (){
      this.deleteCookie('SuccessLogin')
      this.$router.go()
    },
    A() {
      let a = this.$cookies.isKey('SuccessLogin')
      if (a == true){
        this.success_login = a;
        console.log('aaa')
      }
    }
  },
  created() {
    this.A();
  }
}

</script>
<!-- 
h1 : 마크 위치
ul.menu:after : ?
ul.menu : 메뉴 위치
ul.menu li : 패딩 크기

a : text color
 -->
<style scoped>
header{width:100%; text-align:center; position:relative; height:120px; border-bottom:1px solid #35495e}
header h1{position:absolute; top:10%; left:1%;}
header ul.menu:after{display:block; clear:both; content:'';}
header ul.menu{position:absolute; top:20px; right:50px;}
header ul.menu li{float:left; padding:10px 20px; list-style:none;}

a{text-decoration:none; color:#333;}
</style>
