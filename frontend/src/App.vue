<template>
  <div>
    <list-task
      :tasks = 'tasks'
       v-if="tasks.length > 0"
    ></list-task>
    <div class="no-task" v-else>No tasks available</div>
  </div>
</template>

<script>
import axios from 'axios'

import ListTask from './components/ListTask'

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
</style>
