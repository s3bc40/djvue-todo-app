<template>
    <div>
        <input type="checkbox" id="completed" v-model="isCompleted" disabled/>
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
            </div>
        </div>
        <div class="task-footer">
            <div class="tag-list">
                <div class="tag" v-for="tag in task.tags" :key="tag.id">
                    {{ tag.name }}
                </div>
            </div>
            <div class="task-button">
                <button class="button-update">
                    <i class="far fa-edit"></i>
                </button>
                <button class="button-delete">
                    <i class="far fa-trash-alt"></i>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
// APPLICATION
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
    #completed {
        @apply 
            absolute 
            top-2 
            right-2
    }
    .task-header {
        @apply 
            text-xl 
            text-left 
            text-pink-500 
            font-semibold 
    }
    .description {
        @apply 
            text-sm 
            text-center 
            font-normal 
            text-black py-2
    }
    .info-container {
        @apply 
            flex-row 
            flex 
            py-4
            text-xs 
            text-gray-600 
            font-light 
            space-x-3 
            items-baseline 
    }
    .task-footer {
        @apply 
            relative
    }
    .tag-list {
        @apply 
            flex 
            flex-wrap
    }
    .tag {
        @apply 
            p-1 
            text-xs 
            text-white mr-1
            bg-pink-300 
            rounded-sm 
    }
    .task-button {
        @apply 
            sm:absolute 
            block 
            space-x-1 
            top-0 
            right-0
    }
    .task-button > button {
        @apply
            hover:text-gray-500
            focus:outline-none
            p-1
            rounded-md
            transition-colors
            opacity-40
            text-black
            text-sm
    }
</style>