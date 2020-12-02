<!-- 상단에 있는 장학 제도 누르면 나오는 페이지 -->
<template>
    <div class="Schlorship_part">
        <div class="DboxPad"></div>
        <div class="Dbox1">
            <section class="container">
                <h1>Credits acquired</h1>
                <div class="columns">
                    <div class="column">
                        <bar-chart></bar-chart>
                    </div>
                </div>
            </section>
        </div>
        
        <div class="Dbox2">
            <section class="container">
                <h1>Grade acquired</h1>
                <div class="columns">
                    <div class="column">
                        <line-chart></line-chart>
                    </div>
                </div>
            </section>
        </div>
        <div class="Dbox3">
            <div class="DboxBorder">
                <a href="http://localhost:8080/grade/result">
                    <h3>Result of Degree</h3>
                </a>
            </div>
            <div class="Dbox2n" align="left">
                <div class="Dbox21" align="left">
                    <font size="3em">- grade : 4</font><br><br>
                    <font size="3em">- Magor : 63</font><br><br>
                    <font size="3em">- General subject : 78</font><br><br>
                </div>
            </div>
            
        </div>
                                
                <div class="columns">
                    <div class="column">
                    <radar-chart1></radar-chart1>
                    </div>
                </div>

                <!-- >                
                <div class="columns">
                </div>
                < -->

                <div class="columns">
                    <div class="column">
                    <radar-chart2></radar-chart2>
                    </div>
                </div>

                <div class="columns">
                    <div class="column">
                    <radar-chart3></radar-chart3>
                    </div>
                </div>

                <div class="columns">
                    <div class="column">
                    <radar-chart4></radar-chart4>
                    </div>
                </div>

    </div>
</template>
                       
<script>
import BarChart from '@/components/BarChart'
import LineChart from '@/components/LineChart'
import RadarChart1 from '@/components/radarchart/RadarChart1'
import RadarChart2 from '@/components/radarchart/RadarChart2'
import RadarChart3 from '@/components/radarchart/RadarChart3'
import RadarChart4 from '@/components/radarchart/RadarChart4'

export default {
name: 'VueChartJS',
    components: {
         BarChart,
        LineChart,
        RadarChart1,
        RadarChart2,
        RadarChart3,
        RadarChart4
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
                            .DPad {}
                            .Dbox {}
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