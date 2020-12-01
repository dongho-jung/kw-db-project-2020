<script>
//Importing Bubble class from the vue-chartjs wrapper
import {PolarArea} from 'vue-chartjs'
//Exporting this so it can be used in other components
export default{
  extends: PolarArea,
  data () {
    return {
      datacollection: {
        //Data to be represented on x-axis
        labels: ['2016.1', '2016.2', '2017.1', '2017.2', '2018.1', '2018.2', '2019.1', '2019.2', '2020.1', '2020.2'],
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3, 6, 9, 18, 12],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(107, 102, 255, 0.2)',
            'rgba(255, 0, 221, 0.2)',
            'rgba(0, 84, 255, 0.2)',
            'rgba(255, 167, 167, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(107, 102, 255, 0.2)',
            'rgba(255, 0, 221, 0.2)',
            'rgba(0, 84, 255, 0.2)',
            'rgba(255, 167, 167, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderWidth: 1
        }]
      },
      //Chart.js options that controls the appearance of the chart
    }
  },
  mounted () {
    //renderChart function renders the chart with the datacollection and options object.
    this.renderChart(this.datacollection, this.options)
  }
}
</script>