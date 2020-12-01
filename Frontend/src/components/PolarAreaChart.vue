<script>
//Importing Bubble class from the vue-chartjs wrapper
import {PolarArea} from 'vue-chartjs'
import axios from "axios";
axios.defaults.withCredentials = true
//Exporting this so it can be used in other components
export default{
  extends: PolarArea,
  watch:{
    charData(){
      this.$data._chart.update()
    }
  },
  data () {
    return {
      sixteen_f : '',
      sixteen_s : '',

      seventeen_f : '',
      seventeen_s : '',

      eightteen_f : '',
      eightteen_s : '',

      nineteen_f : '',
      nineteen_s : '',

      twenty_f : '',
      twenty_s : '',

      datacollection: {
        //Data to be represented on x-axis
        labels: ['2016.1', '2016.2', '2017.1', '2017.2', '2018.1', '2018.2', '2019.1', '2019.2', '2020.1', '2020.2'],
        datasets: [{
          label: '# of Votes',
          data: [ this.sixteen_f, this.sixteen_s, this.seventeen_f, this.seventeen_s, this.eightteen_f,
            this.eightteen_s, this.nineteen_f, this.nineteen_s,  this.twenty_f, this.twenty_s],
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
  methods: {
    set_api() {
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2016',
          quarter: '1'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.sixteen_f = temp
            console.log(this.sixteen_f)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2016',
          quarter: '2'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.sixteen_f = temp
            console.log(this.sixteen_f)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2017',
          quarter: '1'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.seventeen_f = temp
            console.log(this.seventeen_f)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2017',
          quarter: '2'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.seventeen_s = temp
            console.log(this.seventeen_s)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2018',
          quarter: '1'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.eightteen_f = temp
            console.log(this.eightteen_f)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2018',
          quarter: '2'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.eightteen_s = temp
            console.log(this.eightteen_s)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2019',
          quarter: '1'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.nineteen_f = temp
            console.log(this.nineteen_f)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2019',
          quarter: '2'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.nineteen_s = temp
            console.log(this.nineteen_s)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2020',
          quarter: '1'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.twenty_f = temp
            console.log(this.twenty_f)
          })
      axios.get('/grade',{
        baseURL: 'http://localhost:5000',
        params: {
          year: '2020',
          quarter: '2'
        }
      })
          .then(res=>{
            console.log(res.data)
            let temp = 0;
            for(let i = 0; i<res.data.length;i++){
              temp = temp + parseInt(res.data[i][1],10);
            }
            this.twenty_s = temp
            console.log(this.twenty_s)
          })
    }
  },
   mounted () {
    this.set_api()
    //renderChart function renders the chart with the datacollection and options object.
    this.renderChart(this.datacollection, this.options)
    this.set_api()
  },
  created(){
    this.set_api()
  }
}
</script>