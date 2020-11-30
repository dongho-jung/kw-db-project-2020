 // routers 속에 있음. 다른 페이지 연결
import Vue from 'vue';
import VueRouter from 'vue-router';
import Content from '@/components/common/Content';
import List from '@/components/board/List';
import List2 from '@/components/board/List2';
import Hotlist from '@/components/board/Hotlist';
import Login from '@/components/login/Login';
import NewAccount from '@/components/login/NewAccount';
import Findpw from '@/components/login/Findpw';
import Notice from '@/components/board/Notice';
import Result from '@/components/grade/Result';
import Scholarship from '@/components/grade/Scholarship';
import Prereq from '@/components/timetable/Prereq';
import Magic from '@/components/timetable/Magic';
import Enrollment from '@/components/timetable/Enrollment';

import VueChartJS from '@/components/VueChartJS';
Vue.use(VueRouter); //vue 라우터

var routes = [
	{
		path:'/'
		,name: Content
		,component:Content
	}
	,{
		path:"/board/list"
		,name: List
		,component:List
	}
	,{
		path:"/board/list2"
		,name: List2
		,component:List2
	}
	,{
		path:"/board/hotlist"
		,name: Hotlist
		,component:Hotlist
	}
	,{
		path:"/Login"
		,name: Login
		,component:Login
	}
	,{
		path:"/Findpw"
		,name: Findpw
		,component:Findpw
	}
	,{
		path:"/NewAccount"
		,name: NewAccount
		,component:NewAccount
	}
	,{
		path:"/board/notice"
		,name: Notice
		,component:Notice
	}

	,{
		path:"/grade/result"
		,name: Result
		,component: Result
	}
	,{
		path:"/grade/scholarship"
		,name: Scholarship
		,component:Scholarship
	}
	,{
		path:"/timetable/prereq"
		,name: Prereq
		,component:Prereq
	}
	,{
		path:"/timetable/magic"
		,name: Magic
		,component:Magic
	}
	,{
		path:"/timetable/enrollment"
		,name: Enrollment
		,component:Enrollment
	}
	,{
		path:'/chartjs'
		,name: VueChartJS
		,component:VueChartJS
	}
]

const router = new VueRouter({
	mode:'history',
	routes
});

export default router
