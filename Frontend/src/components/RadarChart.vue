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
            label: '전필 전선 교양 취득학점',
            backgroundColor: 'rgba(179, 181, 198, 0.2)',
            borderColor: 'rgba(179,181,198,1)',
            pointBackgroundColor: 'white',
            borderWidth: 3,
            pointBorderColor: '#249EBF',
            //Data to be represented on y-axis
            data: [1,3,3,0,0,3,1,0,3]
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
 