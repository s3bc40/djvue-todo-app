<template>
    <div>
        <div class="task-list">
            <div class="task-container" v-for="task in tasks" :key="task.id">
                <task-content 
                :task="task"
                ></task-content>
            </div>
        </div>
    </div>
</template>

<script>
import Task from './Task'

export default {
    name: 'ListTask',
    components: {
        'task-content': Task,
    },
    props: {
        tasks: {
            type: Array,
            required: true,
            default: () => {
                return []
            }
        }
    }
}
</script>

<style lang="postcss" scoped>
    .task-list {
        @apply flex flex-col
    }
    .task-container {
        @apply my-6 p-4 mx-auto w-1/2 rounded-md shadow-md border border-gray-300
    }
</style>