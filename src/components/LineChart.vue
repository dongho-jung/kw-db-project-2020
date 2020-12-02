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
              label: 'Grade Acquired',
              fill:false,
              lineTension: 0,
              borderColor:'#4472C4',
              pointBackgroundColor: '#4472C4',
              borderWidth: 5,
              pointBorderColor: '#4472C4',
              data: [3.5, 3.4, 3.9, 3.6, 4.2, 4.3, 4.41, 3.8]
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