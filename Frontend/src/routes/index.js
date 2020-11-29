// routers 속에 있음. 다른 페이지 연결

import Vue from 'vue';
import VueRouter from 'vue-router';
import Content from '@/components/common/Content'; 
import List from '@/components/board/List';
import List2 from '@/components/board/List2';
import Hotlist from '@/components/board/Hotlist';
import Login from '@/components/login/Login';
import Notice from '@/components/board/Notice'; 
import Result from '@/components/grade/Result';
import Schlorship from '@/components/grade/Scholarship';
import Prereq from '@/components/timetable/Prereq';
import Magic from '@/components/timetable/Magic';
import Enrollment from '@/components/timetable/Enrollment';
import Webtoon from "@/components/MyTest/webtoon";

Vue.use(VueRouter); //vue 라우터

var routes = [
	{
		path:'/'
		,name: Content
		,component:Content
	},
	{
		path:'/Test/webtoon'
		,name: Webtoon
		,component: Webtoon
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
		path:"/grade/schlorship"
		,name: Schlorship
		,component:Schlorship
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
]

const router = new VueRouter({
	mode:'history',
	routes
});

export default router