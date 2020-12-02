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
            label: '2020_1',
            backgroundColor: 'rgba(0, 84, 255, 0.2)',
            borderColor: 'rgba(0, 84, 255, 0.2)',
            pointBackgroundColor: 'white',
            borderWidth: 3,
            pointBorderColor: 'rgba(0, 84, 255, 0.2)',
            data: [1,0,2,1,0,0,0,0,0]
          },
          {
            label: '2020_2',
            backgroundColor:'rgba(255, 159, 64, 0.2)',
            borderColor: 'rgba(255, 159, 64, 0.2)',
            pointBackgroundColor: 'white',
            borderWidth: 3,
            pointBorderColor: 'rgba(255, 159, 64, 0.2)',
            data: [1,1,1,0,1,0,0,0,0]
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
 