<script>
//Importing Bar class from the vue-chartjs wrapper
import {Radar} from 'vue-chartjs'
//Exporting this so it can be used in other components
export default {
  extends: Radar,
  data() {
    return {
      datacollection: {
        //Data to be represented on x-axis
        labels: ['A+','A0','B+','B0','C+','C0','D+','D0','F'],
        datasets: [
          {
            label: '2017_1',
            backgroundColor: 'rgba(255, 0, 221, 0.2)',
            borderColor: 'rgba(255, 0, 221, 0.2)',
            pointBackgroundColor: 'white',
            borderWidth: 5,
            pointBorderColor: 'rgba(255, 0, 221, 0.2)',
            data: [2,2,2,1,0,1,0,1]
          },
          {
            label: '2017_2',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 0.2)',
            pointBackgroundColor: 'white',
            borderWidth: 5,
            pointBorderColor: 'rgba(54, 162, 235, 0.2)',
            data: [1,2,1,1,0,0,0,0]
          }
        ]
      },
      //Chart.js options that controls the appearance of the chart
      options: {
        legend: {
            display: true
          },
        responsive: true,
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
 