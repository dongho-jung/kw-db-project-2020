// 전체적으로 설계하는 부분
<template>
  <div id="app">
    <!-- 추가된 헤더 컴포넌트 사용 -->
    <Header />
    
    <Content/>
	
    <!-- 추가된 풋터 컴포넌트 사용 -->
    <Footer />
  </div>
</template>

<script>
import Header from './components/common/Header'; //import 헤더 추가
import Content from './components/common/Content'; 
import Footer from './components/common/Footer'; //import 풋터 추가

export default {
  name: 'App',
  components: {
    Header          //헤더 컴포넌트 추가
    ,Content
    ,Footer         //풋터 컴포넌트 추가
    
  }
}
</script>

<style>
html,body{padding:0; margin:0;}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin:0; padding:0;
}
</style>