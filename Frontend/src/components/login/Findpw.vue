<template>
  <div class="box2">
    <a href="http://localhost:3000/Findpw">
      <img src="../../assets/password.png" height = "200" width="300">
      <h1>Check if id exists</h1>
    </a>
    <tr>
      <div class="box21">
       * Student ID : <input v-model="student_id" type="text" name="student_id" size = 48 style = "text-align:center;"><br><br><br>
      </div>
      <div class="box21">
       * Name : <input v-model="Name" type="text" name="name" size = 53 style = "text-align:center;"><br><br><br>
      </div>
       Phone : <input type="text" name="phone" size = 53 style = "text-align:center;"><br><br><br>
      * Email : <input v-model="email" type="text" name="email" size = 53 style = "text-align:center;"><br><br><br>
      <input type="button" v-on:click="OK" value="OK" size=70 style = "width:100pt;height:20pt;text-align:center;">
      <input type="button" v-on:click="Cancel" value="Cancel" size=70 style = "width:100pt;height:20pt;text-align:center;">
    </tr>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      student_id:'',
      Name:'',
      email:''
    }
  },
  methods: {
    OK() {
      if(this.email!='')
        if(this.student_id!='')
            if(this.Name!=''){
              axios.get('/student/check/id',{
                baseURL: 'http://localhost:5000',
                params: {
                  student_id: this.student_id
                }
              })
                  .then(res=>{ //못찾으면 error 출력하도록 유도
                    alert("You don't have ID")
                    console.log(res);
                    this.$cookies.set('CheckDuplicatedEmail');
                    this.$router.push('/login')
                  })
                  .catch(error =>{
                    console.log(error);
                    alert('You already have ID')
                    this.$router.push('/login')
                  })
            }
            else {
                alert('Please input Name')
                return
              }
        else {
          alert('Please input Student_id')
          return
        }
      else{
        alert('Please input Email')
        return
      }
    },
    Cancel() {
      alert('Go to Login Page')
      this.$router.push('/login')
    }
  }
}

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
  margin: 4px 2px;
}


.box2{
  padding:9px;
  display: grid;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 9fr;
  grid-gap: 0px;
}

.box2n{
  padding:9px;
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}


#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }

.box4{
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 10fr;
}

.box4n{
  padding:9px;
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-gap: 1px;
  border: 1px solid;
}
</style>