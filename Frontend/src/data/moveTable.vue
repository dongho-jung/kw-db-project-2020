<template>
</template>

<script>
import tableData from './tableData';

export default{
    data() {
        retirm{
            tableData: tableData,
        }
    },

    method: {
        createTable(charId, data){
            var space = document.getElementById(charId);
            Plotly.newPlot(space, [data]);
        }
    }

    created(){
        this.createTable('graph', tableData);
    }
}

</script>
