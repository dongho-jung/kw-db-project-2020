<template>
  <div class="Login_part">
    <div class="Bbox1">
      <img alt="DB1" src="@/assets/kw01.jpg" height = "200" width="320">
      <h1>DB MANMAN<br>Time Planner</h1>
    </div>

    <div class="Bbox2">
      <div class="BPad">
      </div>
      <div class="Bbox21">
        <font size="2em" face="bold">ID : </font>
      </div>
      <div class="Bbox22">
        <input type="text" name="ID" size=50 style = "text-align:center;">
      </div>
      <div class="Bbox23">
        <input type="button" value="New Account" size=70 style = "width:80pt;height:16pt;text-align:center;">
      </div>
      <div class="BPad">
      </div>
    </div>

    <div class="Bbox3">
      <div class="BPad">
      </div>
      <div class="Bbox31">
        <font size="2em" face="bold">PW : </font>
      </div>
      <div class="Bbox32">
        <input type="text" name="ID" size=50 style = "text-align:center;">
      </div>
      <div class="Bbox33">
        <input type="button" value="Find PW" size=70 style = "width:80pt;height:16pt;text-align:center;">
      </div>
      <div class="BPad">
      </div>
    </div>

    <div class="Bbox4">
      <div class="BPad">
      </div>
      <div class="Bbox41">
        <input type="button" value="Log In" size=70 style = "width:100pt;height:18pt;text-align:center;">
      </div>
      <div class="Bbox42">
        <input type="button" value="KAKAO Log In" size=70 style = "width:100pt;height:18pt;text-align:center;background-color:yellow;">
      </div>
      <div class="BPad">
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style>
.button {
  color: black;
  padding: 7px 60px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
}

a{text-decoration:none; color:black}

.Login_part > div {
  border-radius: 5px;
  background-color: white;
  padding: 1em;
}

.Login_part{
  display: grid;
  grid-template-rows: 400px 60px 60px 40px;
  grid-gap: 10px;
}
.BPad{
}

.Bbox1{
}

.Bbox2{
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.Bbox21{
}
.Bbox22{
}
.Bbox23{
}

.Bbox3{
  display: grid;
  grid-template-columns: 5fr 1fr 3fr 1fr 5fr;
}
.Bbox31{
}
.Bbox32{
}
.Bbox33{
}

.Bbox4{
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 10fr;
}
.Bbox41{
}
.Bbox42{
}
.Bbox43{
}
.Bbox44{
}

#header, #nav, #section, #footer { text-align:center; }
#header, #footer { line-height:100px; }
#nav, #section { line-height:240px; }
</style>