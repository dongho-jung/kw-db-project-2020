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
        labels: ['2016.1', '2016.2', '2017.1', '2017.2','2019.1', '2019.2', '2020.1', '2020.2'],
        datasets: [
          {
            label: 'My Credit',
            fill:false,
            lineTension: 0,
            borderColor:'#4472C4',
            pointBackgroundColor: '#4472C4',
            borderWidth: 5,
            pointBorderColor: '#4472C4',
            data: [3.5, 3.4, 4.1, 3.6, 4.2, 4.21, 4.41, 3.8]
          },
          {
            label: 'Quarter Scholarship',
            fill:false,
            lineTension: 0,
            borderColor:'#ED7D31',
            pointBackgroundColor: '#ED7D31',
            borderWidth: 5,
            pointBorderColor: '#ED7D31',
            data: [3.8, 3.9, 4.0, 3.8, 3.9, 3.7, 3.8, 4.0]
          },
          {
            label: 'Half Scholarship',
            fill:false,
            lineTension: 0,
            borderColor:'#A5A5A5',
            pointBackgroundColor: '#A5A5A5',
            borderWidth: 5,
            pointBorderColor: '#A5A5A5',
            data: [4.2, 4.1, 4.2, 4.1, 4.1, 4, 3.9, 4.15]
          },
          {
            label: 'Full Scholarship',
            fill:false,
            lineTension: 0,
            borderColor:'#FFC000',
            pointBackgroundColor: '#FFC000',
            borderWidth: 5,
            pointBorderColor: '#FFC000',
            data: [4.5, 4.4, 4.3, 4.3, 4.4, 4.3, 4.2, 4.3]
          },
        ]
      },
      //Chart.js options that controls the appearance of the chart
      options: {
        scales: {
          yAxes: [{
            ticks: {
              min:2,
              max:4.5,
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
    this.renderChart(this.datacollection, this.options)
  }
}
</script>