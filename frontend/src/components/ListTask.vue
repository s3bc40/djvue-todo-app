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
// IMPORT COMPONENTS
import Task from './Task'

// APPLICATION
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
        @apply 
            flex 
            flex-col 
            w-2/3 
            mx-auto
    }
    .task-container {
        @apply 
            relative 
            my-6 
            p-4 
            container
            mx-auto 
            rounded-md 
            shadow-md 
            border 
            border-gray-300
    }
</style>