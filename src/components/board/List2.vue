<template>
	<div>
		<h2>게시판 리스트</h2>
		<a href="javascript:;" @click="getList">GET 방식 데이터 접근</a>
	
        <div class="box" v-for="(user, idx) in users" :key="idx">
            <h2>{{user.first_name}}</h2>
            <img :src="`${user.avatar}`" alt />
        </div>
        <Paging :totalPage="totalPage" />
    </div>

</template>

<script>
export default {
	methods:{
		getList() {
			this.$axios.get("https://reqres.in/api/users?page=2")
			.then(res => {
                this.users = res.data.data;
                this.totalPage = res.data.total_pages;
            })
            .catch(err => {
                console.log(err);
            });
		}
	}
}
</script>

<style scoped>
</style>