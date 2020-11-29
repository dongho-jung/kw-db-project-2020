<!-- > 왼쪽 화면에 선 그래프를 어떻게 구현하면 좋을까?< -->
<!-- 상단에 있는 장학 제도 누르면 나오는 페이지 -->
<template>
    <div class="Schlorship_part">
        <div class="DPad"></div>

        <div class="Dbox1">
            <!-- ><li><router-link to="/chartjs">장학제도</router-link></li>< -->
            <section class="container">
                <h1>취득 학점</h1>
                <div class="columns">
                    <div class="column">
                        <bar-chart></bar-chart><!--BarChart example-->
                    </div>
                </div>
            </section>

            <section class="container">
                <h1>취득 평점</h1>
                <div class="columns">
                    <div class="column">
                        <line-chart></line-chart><!--Line Chart example-->
                    </div>
                </div>
            </section>
        </div>

        <div class="Dbox2">
            <div class="DboxBorder">
                <a href="http://localhost:8080/grade/result">
                    <h3>학습결과</h3>
                </a>
            </div>
            <div class="Dbox2n" align="left">
                <div class="Dbox21" align="left">
                    <font size="3em">- 학년 : 4</font><br><br>
                    <font size="3em">- 전공 : 48 / 60</font><br><br>
                    <font size="3em">- 교양 : 120 / 140</font><br><br>
                </div>
            </div>
                <section class="container">
                <div class="columns">
                    <div class="column">
                        <radar-chart></radar-chart><!--RadarChart example-->

                    </div>
                </div>
                </section>
        </div>
    </div>
</template>
                        <script>
                            import BarChart from '@/components/BarChart'
                            import LineChart from '@/components/LineChart'
                            import RadarChart from '@/components/RadarChart'

                            export default {
                                name: 'VueChartJS',
                                components: {
                                    BarChart,
                                    LineChart,
                                    RadarChart
                                }
                            }
                        </script>

                        <style>
                            ul {
                                list-style-type: none;
                                padding: 0;
                            }

                            li {
                                display: inline-block;
                                margin: 0 10px;
                            }

                            a {
                                color: #42b983;
                            }

                            .button {
                                color: black;
                                padding: 7px 60px;
                                text-align: center;
                                text-decoration: none;
                                display: inline-block;
                                cursor: pointer;
                            }
                            a {
                                text-decoration: none;
                                color: black;
                            }
                            .Schlorship_part > div {
                                border-radius: 5px;
                                background-color: white;
                                padding: 1em;
                            }
                            .Schlorship_part {
                                display: grid;
                                grid-template-columns: 2fr 4fr 2fr 2fr;
                                grid-template-rows: 800px;
                                grid-gap: 10px;
                            }
                            .DPad {
                                }
                            .Dbox {
                                }
                            .DboxBorder {
                                border: 1px solid;
                            }
                            .DboxPad {
                                padding: 9px;
                            }
                            .DboxPad15 {
                                padding: 15px;

                            }
                            .DboxPad15Border {
                                padding: 15px;
                                border: 1px solid;
                            }
                            .DboxMar {
                                border: 1px solid;
                                margin: 5px;
                            }
                            .Dbox1 {
                                display: grid;
                                grid-template-rows: 1fr 7fr;
                                grid-gap: 10px;
                            }
                            .Dbox12 {
                                display: grid;
                                grid-template-rows: 1fr 3fr 3fr 3fr 1fr;
                                grid-gap: 0;
                            }
                            .Dbox121 {
                                display: grid;
                                grid-template-columns: 2fr 12fr 3fr;
                                grid-gap: 0;
                                border: 1px solid;
                            }
                            .Dbox125 {
                                display: grid;
                                grid-template-columns: 6fr 1fr 1fr 1fr;
                                grid-gap: 10px;
                                border: 1px solid;
                            }
                            .Dbox12n {
                                display: grid;
                                grid-template-rows: 1fr 2fr 1fr;
                                grid-gap: 1px;
                                border: 1px solid;
                            }
                            .Dbox2 {
                                padding: 9px;
                                display: grid;
                                grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr 9fr;
                                grid-gap: 0;
                            }
                            .Dbox2n {
                                padding: 9px;
                                display: grid;
                                grid-template-columns: 2fr 1fr;
                                grid-gap: 1px;
                                border: 1px solid;

                            }
                            #footer,
                            #header,
                            #nav,
                            #section {
                                text-align: center;
                            }
                            #footer,
                            #header {
                                line-height: 100px;
                            }
                            #nav,
                            #section {
                                line-height: 240px;
                            }
                        </style>