<template>
    <div>
        <div class="task-header">
            {{ task.title }}
        </div>
        <div class="task-body">
            <div class="description">
                {{ task.description}}
            </div>
            <div class="info-container">
                <div>Created: {{ task.date_created }}</div>
                <div>Last Update: {{ task.date_updated }}</div>
                <div v-if="task.completed">
                    Date completed : {{ task.date_completed }}
                </div>
                <div>
                    <label for="completed">Completed?</label>
                    <input type="checkbox" id="completed" v-model="isCompleted" disabled/>
                </div>
            </div>
        </div>
        <div class="task-footer">
            <div class="task-tag" v-for="tag in task.tags" :key="tag.id">
                {{ tag.name }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Task',
    props: {
        task: {
            type: Object,
        }
    },
    computed: {
        isCompleted: {
            get() {
                return this.task.completed
            },
            set(value) {
                this.$emit('input', value)
                console.log(this.task.completed)
            }
        }
    }
}
</script>

<style lang="postcss" scoped>
    .task-header {
        @apply text-xl text-left font-semibold text-pink-500 
    }
    .description {
        @apply text-sm text-center font-normal text-black py-2
    }
    .info-container {
        @apply text-xs flex flex-row font-light text-gray-600 space-x-3 items-baseline py-4
    }
    .task-footer {
        @apply flex flex-wrap
    }
    .task-tag {
        @apply text-xs font-light text-gray-400 mr-1
    }
</style>