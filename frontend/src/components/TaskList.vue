<template>
    <div>
        <div class="task-list" v-if="tasks.length > 0">
            <div class="task-container" v-for="task in tasks" :key="task.id">
                <div class="task-header">
                    {{ task.title }}
                </div>
                <div class="task-body">
                    {{ task.description}}
                </div>
                <div class="task-footer">
                    <div class="task-tag" v-for="tag in task.tags" :key="tag.id">
                        {{ tag.name }}
                    </div>
                </div>
            </div>
        </div>
        <h1 v-else>No tasks available</h1>
    </div>
</template>

<script>
export default {
    name: 'TaskList',
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
    .task-header {
        @apply text-xl text-left font-semibold text-pink-500 
    }
    .task-body {
        @apply text-sm text-center font-normal text-black py-2
    }
    .task-footer {
        @apply flex flex-wrap
    }
    .task-tag {
        @apply text-xs font-light text-gray-400 mr-1
    }

</style>