<template >
   
    <body class="body">
        <div class="container text-center">

            <tasks :data="data"/>
        </div>
    </body>
</template>

<script>
import axios from 'axios'
import tasks from '@/components/tasks.vue'
import {datatasks} from '@/temp-data'
export default {
    name: 'Tasks View page ',
    components:{
        tasks,
    },
    data(){
        return{
            data:datatasks
        }
    },
}
</script>

<style>
body {

    background: linear-gradient(
    to right,
    rgba(126, 64, 246, 1),
    rgba(80, 139, 252, 1)
    );
    }


</style>