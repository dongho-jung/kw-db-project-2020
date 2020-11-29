<template>
	<header>
		<h1><router-link to="/"><img alt="Vue logo" src="../../assets/KWLOGO.jpg" width="80">
		</router-link></h1>
		<div class="menuWrap">
			<ul class="menu">
        <li><router-link to="/test/webtoon">Test_Webtoon</router-link></li>
				<li><router-link to="/board/list2">호에엥</router-link></li>
				<li><router-link to="/board/notice">과목별 공지사항</router-link></li>
				<li><router-link to="/board/list">게시판 바로가기</router-link></li>
				<li><router-link to="/grade/result">학습 결과</router-link></li>
				<li><router-link to="/grade/schlorship">장학 제도</router-link></li>
				<li><router-link to="/timetable/prereq">선후수과목 확인</router-link></li>
				<li><router-link to="/timetable/magic">시간표 마법사</router-link></li>
				<li><router-link to="/timetable/enrollment">수강 신청</router-link></li>
				<li><router-link to="/login">로그아웃</router-link></li>
				
			</ul>
		</div>
		
	</header>
</template>

<script>
export default {
	
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
header h1{position:absolute; top:0; left:100px;}
header ul.menu:after{display:block; clear:both; content:'';}
header ul.menu{position:absolute; top:20px; right:50px;}
header ul.menu li{float:left; padding:10px 20px; list-style:none;}

a{text-decoration:none; color:#333;}
</style>