// routers 속에 있음. 다른 페이지 연결

import Vue from 'vue';
import Router from 'vue-router';
import Content from '@/components/common/Content'; //메인 컴포넌트 호출
import List from '@/components/board/List'; //게시판 리스트 컴포넌트 호출
import Login from '@/components/Login';

Vue.use(Router); //vue 라우터

export default new Router({ //라우터 연결
	routes:[
		{
			path:'/'
			,name:Content
			,component:Content
		}
		,{
			path:'/board/list'
			,name:List
			,component:List
		}
		,{
			path:'/login'
			,name:Login
			,component:Login
		}
	]
})