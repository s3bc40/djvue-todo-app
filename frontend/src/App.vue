<template>
  <div>
    <TaskList
      :tasks = 'tasks'
    ></TaskList>
  </div>
</template>

<script>
import axios from 'axios'

import TaskList from './components/TaskList'

export default {
  name: 'App',
  components: {
    TaskList
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

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
