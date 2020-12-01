<template>
  <div>
      <button class="button-add">
        <i class="far fa-plus-square"></i>
        Add a Task
      </button>
      <list-task
        :tasks = 'tasks'
        v-if="tasks.length > 0"
      ></list-task>
      <div class="no-task" v-else>No tasks available</div>
    </div>
</template>

<script>
// IMPORT UTILITIES
import axios from 'axios'

// IMPORT COMPONENTS
import ListTask from './components/ListTask'

// APPLICATION
export default {
  name: 'App',
  components: {
    'list-task': ListTask,
  },
  data () {
    return {
      tasks: []
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
      fixed 
      p-2 
      rounded-xl 
      bg-pink-400 
      text-white 
      font-bold 
      top-2 
      right-0
      sm:right-2
      md:right-4
      lg:right-12
      transition-colors
      hover:bg-pink-800
      focus:outline-none
  }

</style>
