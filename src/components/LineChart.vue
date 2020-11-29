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
              label: 'Data One',
              //backgroundColor: '#f87979',
              pointBackgroundColor: 'blue',
              borderWidth: 5,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: [3.5, 4.2, 4.3, 3.7, 4.2, 3.9]
            }
          ]
        },
        //Chart.js options that controls the appearance of the chart
        options: {
          scales: {
            yAxes: [{
              ticks: {
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
          responsive: false,
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