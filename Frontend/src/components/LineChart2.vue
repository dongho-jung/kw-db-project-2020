
<script>
//Importing Line class from the vue-chartjs wrapper
import {Line} from 'vue-chartjs'
//Exporting this so it can be used in other components
export default {
  extends: Line,
  data () {
    return {
      datacollection: {
//Data to be represented on x-axis
        labels: ['2016.1', '2016.2', '2019.1', '2019.2', '2020.1', '2020.2'],
        datasets: [
          {
            label: '본인 학점',
            fill:false,
            lineTension: 0,
            borderColor:'#4472C4',
            pointBackgroundColor: '#4472C4',
            borderWidth: 5,
            pointBorderColor: '#4472C4',
            data: [3.5, 4.2, 4.3, 3.7, 4.2, 3.9]
          },
          {
            label: '쿼터 장학금',
            fill:false,
            lineTension: 0,
            borderColor:'#ED7D31',
            pointBackgroundColor: '#ED7D31',
            borderWidth: 5,
            pointBorderColor: '#ED7D31',
            data: [4, 3.9, 4, 3.8, 3.9, 3.7]
          },
          {
            label: '하프 장학금',
            fill:false,
            lineTension: 0,
            borderColor:'#A5A5A5',
            pointBackgroundColor: '#A5A5A5',
            borderWidth: 5,
            pointBorderColor: '#A5A5A5',
            data: [4.2, 4.1, 4.2, 4.1, 4.1, 4]
          },
          {
            label: '풀 장학금',
            fill:false,
            lineTension: 0,
            borderColor:'#FFC000',
            pointBackgroundColor: '#FFC000',
            borderWidth: 5,
            pointBorderColor: '#FFC000',
            data: [4.5, 4.3, 4.5, 4.4, 4.4, 4.3]
          },
        ]
      },
//Chart.js options that controls the appearance of the chart
      options: {
        scales: {
          yAxes: [{
            ticks: {
              min:3,
              max:4.6,
              beginAtZero: true
            },
            gridLines: {
              display: true
            }
          }],
          xAxes: [ {
            gridLines: {
              display: false
            }
          }]
        },
        legend: {
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  mounted () {
//renderChart function renders the chart with the datacollection and options object.





  },
  created(){
    this.renderChart(this.datacollection, this.options)
  }
}
</script>