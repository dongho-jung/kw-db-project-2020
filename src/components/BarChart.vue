<script>
//Importing Bar class from the vue-chartjs wrapper
import {Bar} from 'vue-chartjs'
//Exporting this so it can be used in other components
export default {
  extends: Bar,
  data() {
    return {
      datacollection: {
        //Data to be represented on x-axis
        labels: ['2016.1', '2016.2', '2017.1', '2017.2','2019.1', '2019.2', '2020.1', '2020.2'],
        datasets: [
          {
            label: 'ME(전선)',
            backgroundColor: 'orange',
            pointBackgroundColor: 'white',
            borderWidth: 1,
            pointBorderColor: '#249EBF',
            //Data to be represented on y-axis
            data: [0,0,6,6,9,6,6,3]
          },
          {
            label: 'MR(전필)',
            backgroundColor: 'yellow',
            pointBackgroundColor: 'white',
            borderWidth: 1,
            pointBorderColor: '#249EBF',
            //Data to be represented on y-axis
            data: [0,0,6,6,3,6,3,3]
          },
          {
            label: 'GR(교양)',
            backgroundColor: 'green',
            pointBackgroundColor: 'white',
            borderWidth: 1,
            pointBorderColor: '#249EBF',
            //Data to be represented on y-axis
            data: [21, 21, 9, 6, 6, 6, 3, 6]
          }
        ]
      },
      //Chart.js options that controls the appearance of the chart
      options: {
        scales: {
          yAxes: [{
            stacked:true,
            ticks: {
              beginAtZero: true
            },
            gridLines: {
              display: true
            }
          }],
          xAxes: [ {
            stacked:true,
            gridLines: {
              display: false
            }
          }]
        },
        legend: {
            display: true
          },
        responsive: false,
        maintainAspectRatio: false
      }
    }
  },
  mounted() {
    //renderChart function renders the chart with the datacollection and options object.
    this.renderChart(this.datacollection, this.options)
  }
}
</script>
 