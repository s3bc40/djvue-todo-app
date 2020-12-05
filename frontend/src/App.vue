<template>
  <div>
      <button class="button-add" @click="showModal = !showModal">
        <i class="far fa-plus-square"></i>
        Add Task
      </button>
      <list-task
        :tasks = 'tasks'
        v-if="tasks.length > 0"
      ></list-task>
      <div class="no-task" v-else>No tasks available</div>
      <div class="modal" v-if="showModal">
        <div class="modal-container">
          <button class="absolute top-2 right-2" @click="showModal = false">
            <i class="far fa-window-close fa-2x"></i>
          </button>
          <add-form
            form_title="Add a task"
          ></add-form>
        </div>
      </div>
  </div>
</template>

<script>
// IMPORT UTILITIES
import axios from 'axios'

// IMPORT COMPONENTS
import ListTask from './components/ListTask'
import TaskForm from './components/TaskForm'

// APPLICATION
export default {
  name: 'App',
  components: {
    'list-task': ListTask,
    'add-form' : TaskForm,
  },
  data () {
    return {
      tasks: [],
      showModal: false,
    }
  },
  mounted () {
    axios.get('http://localhost:8000/api/tasks')
      .then( (response) => {
        console.log(response.data)
        this.tasks = response.data
      })
  }
}
</script>

<style lang="postcss">
  .no-task {
    @apply text-6xl text-center text-pink-600
  }
  body {
    @apply font-sans
  }
  .button-add {
    @apply 
      md:fixed
      md:mt-0
      md:top-2
      md:right-2
      hover:bg-pink-800
      focus:outline-none
      block
      p-2
      mt-2
      mx-auto
      rounded-xl 
      bg-pink-400 
      text-white 
      font-bold 
      transition-colors
  }
  .modal {
    @apply
      z-10
      fixed
      left-0
      top-0
      w-full
      h-full
      overflow-auto
      bg-gray-800
      bg-opacity-80
  }
  .modal-container {
    @apply
      relative
      container
      mx-auto
      rounded-md
      bg-white
      p-6
  }
</style>
