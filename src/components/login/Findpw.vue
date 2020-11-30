<template>
  <div class="box2">
    <a href="http://localhost:8080/Findpw">
      <img src="../../assets/password.png" height = "200" width="300">
      <h1>Find Password</h1>
    </a>
      <tr>
        <div class="box21">
        Student ID : <input type="text" name="student_id" size = 48 style = "text-align:center;"><br><br><br>
        </div>
        <div class="box21">
        Name : <input type="text" name="name" size = 53 style = "text-align:center;"><br><br><br>
        </div>
        Phone : <input type="text" name="phone" size = 53 style = "text-align:center;"><br><br><br>
        Email : <input type="text" name="email" size = 38 style = "text-align:center;">
                <input type="button" value="중복체크" size = 50 style = "width:80pt;height:16pt;text-align:center;"><br><br><br>
                <input type="button" value="OK" size=70 style = "width:100pt;height:20pt;text-align:center;">
                <input type="button" value="Cancel" size=70 style = "width:100pt;height:20pt;text-align:center;">
      </tr>
  </div>
</template>

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