<script>
  //Importing Bubble class from the vue-chartjs wrapper
  import {Bubble} from 'vue-chartjs'
  //Exporting this so it can be used in other components
  export default{
    extends: Bubble,
    data () {
      return {
        datacollection: {
          //Data to be represented on x-axis
          labels: ['2016.1', '2016.2', '2019.1', '2019.2', '2020.1', '2020.2'],
          datasets: [
             {
              label: '2016,1',
              backgroundColor: '#f87979',
              pointBackgroundColor: 'white',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              data: [ {x: 100, y: 0, r: 10}]
            },
            {
              label: '2016.2',
              backgroundColor: '#f87979',
              pointBackgroundColor: 'white',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              //Data to be represented on y-axis
              data: [{x: 100, y: 1, r: 10}]
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
