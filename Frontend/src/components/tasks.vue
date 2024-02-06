<template>
    <section class="vh-100 gradient-custom-2">
        <div class="container py-5 h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-md-12 col-xl-10">
      
              <div class="card mask-custom">
                <div class="card-body p-4 text-white">
      
                  <div class="text-center pt-3 pb-2">
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-todo-list/check1.webp"
                      alt="Check" width="60">
                    <h2 class="my-4 " >ToDo App</h2>
                  </div>
                  
                  <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="Type here to add task" aria-label="Recipient's username" aria-describedby="button-addon2" v-model="TaskText">
                    <button class="btn btn-success" type="button" id="button-addon2" @click="AddTask" v-if="this.editedtask == null" >Add task</button>
                    <button class="btn btn-success" type="button" id="button-addon2" @click="AddTask" v-else  >Edit</button>
                  </div>
                  
                  

                  <table class="table text-white mb-0  ">
                    <thead>
                      <tr>
                        <th scope="col">Task</th>
                        <th scope="col">Status</th>
                        <th scope="col">Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="fw-normal" v-for="task in apidata" :key="task.id" >
                      
                        <td class="align-middle">
                          <span :class="{'text-decoration-line-through':task.status == 'Done'}">{{ task.task }}</span>
                        </td>
                        <td class="align-middle">
                          <h6 class="mb-0"><span 
                            :class="{
                              'badge bg-danger':task.status == 'To Do',
                              'badge bg-warning':task.status == 'In Progress',
                              'badge bg-success':task.status == 'Done',
                            }" 
                            @click="changestatus(task.id)">{{ task.status }}</span></h6>
                        </td>
                        
                        <td class="align-middle">
                            <a href="#!" data-mdb-toggle="tooltip" title="Done" @click="done(task.id)">
                                <i class="fas fa-check-circle me-3" style="color: #256b03;"></i>
                              </a>
                              
                                
                              <a href="#!" data-mdb-toggle="tooltip" title="Edit" @click="edit(task.id)" ><i
                                  class="fas fa-pen-alt fa-lg text-dark me-3"></i></a>
                            
                            <a href="#!" data-mdb-toggle="tooltip" title="Remove" @click="deleteTask(task.id)" ><i
                                class="fas fa-trash-alt fa-lg text-warning "></i></a>
                          
                          
                        </td>
    
                      </tr>
                    </tbody>
                  </table>

                </div>
              </div>
      
            </div>
          </div>
        </div>
      </section>
</template>

<script>
import axios from 'axios';
export default {
    name:'tasks components page',
    props:['data'],
    data(){
        return{
            TaskText:'',
            apidata:'',
            editedtask :null,
            avilablestatus:['To Do','In Progress','Done'],
        }
        
    },
    
    methods:{
        listapitasks(){
           axios({
            method:'get',
            url:'http://127.0.0.1:8000',
          }).then(response => this.apidata = response.data)
        },

        AddTask(){
          
          if (this.TaskText == '') return;
          if(this.editedtask == null){
            
            axios({
              url:'http://127.0.0.1:8000/create/',
              method:'post',
              data:{
                task:this.TaskText,
                status:'To Do'
              }

            }).then(()=>this.listapitasks());
            
            this.TaskText = '';

         }
        else {
           
          axios({
            url:'http://127.0.0.1:8000/editTask/'+this.editedtask,
            method:'put',
            data:{
              task:this.TaskText
            }
          }).then(() => this.listapitasks());
            
          };
          this.editedtask = null
          this.TaskText =''

          
    } ,

    deleteTask(index){
      axios({
        method:'delete',
        url:'http://127.0.0.1:8000/editTask/'+index,

      }).then(()=>this.listapitasks());
     
    },
    edit(index) {
      axios({
        method: 'PATCH',
        url: 'http://127.0.0.1:8000/editTask/' + index,
      }).then(response => {
        this.TaskText = response.data.task;
        this.editedtask = index;
        this.button = 'edit';
      });
    },

    changestatus(index){
    axios({
      url: 'http://127.0.0.1:8000/editTask/' + index,
      method: 'patch',
    }).then(() => {
      const task = this.apidata.find(task => task.id === index);
      if (task) {
        const currentIndex = this.avilablestatus.indexOf(task.status);
        const newIndex = (currentIndex + 1) % this.avilablestatus.length;
        axios({
          url: 'http://127.0.0.1:8000/editTask/' + index,
          method: 'patch',
          data: {
            status: this.avilablestatus[newIndex]
          }
        }).then(() => this.listapitasks());
      }
    });
},



    done(index) {
      axios({
        url: 'http://127.0.0.1:8000/editTask/'+ index,
        method:'patch',
        data:{
          status:'Done'
        }
      }).then(()=> {

    const taskIndex = this.apidata.findIndex(task => task.id === index);
    if (taskIndex !== -1) {
      this.apidata[taskIndex].status = 'Done';
    }
  })

  },


  },

  mounted() {
    this.listapitasks();
  }
};
</script>

<style>
.mask-custom {
    background: rgba(24, 24, 16, 0.2) !important;
    border-radius: 2em !important;
    backdrop-filter: blur(25px) !important;
    border: 2px solid rgba(255, 255, 255, 0.05) !important;
    background-clip: padding-box !important;
    box-shadow: 10px 10px 10px rgba(46, 54, 68, 0.03) !important;
  }
  .gradient-custom-2 {
  
    background: linear-gradient(
      to right,
      rgba(126, 64, 246, 1),
      rgba(80, 139, 252, 1)
    );
  }
  .btn-custom {
    background-color: #00f7a4;
    color: #fff; 
    border-color: #256b03; /* Adjust border color to your preference */
  }
</style>