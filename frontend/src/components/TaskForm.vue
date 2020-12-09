<template>
    <div>
        <div class="form-header">{{ form_title }}</div>
        <div class="form-content">
            <!-- Title -->
            <div>
                <label class="form-label" for="title">Title: </label>
                <input 
                    type="text" 
                    id="title" 
                    v-model="task.title"
                    placeholder="Insert title here"
                    required
                >
            </div>
            <!-- Description -->
            <div>
                <label class="form-label" for="description">Description: </label>
                <textarea
                    id="description"
                    placeholder="Insert details here"
                    v-model="task.description"
                ></textarea>
            </div>
            <!-- Due Date -->
            <div>
                <label class="form-label" for="due_date">Due Date: </label>
                <input
                    type="date"
                    id="due_date"
                    name="due_date"
                    v-model="task.due_date" 
                >
            </div>
            <!-- Priority -->
            <div>
                <label class="form-label" for="priority">Priority: </label>
                <select
                    id="priority"
                    name="priority"
                    v-model="task.priority" 
                >
                    <option value=""></option>
                    <option value="1">Not important</option>
                    <option value="2">Important</option>
                    <option value="3">Urgent</option>
                </select>
            </div>
            <!-- Completed -->
            <div>
                <label class="form-label" for="completed">Completed : </label>
                <input
                    type="checkbox"
                    id="completed"
                    name="completed"
                    v-model="task.completed" 
                >
            </div>
            <!-- Tags -->
            <div>
                <div class="form-label">Select tags: </div> 
                <div v-for="tag in tags" :key="tag.id">
                    <div v-if="tag.visibility">
                        <input 
                            type="checkbox" 
                            :id="tag.id" 
                            :value="tag.id" 
                            v-model="tags_selected"
                        >
                        <label class="pl-2" :for="tag.id">{{ tag.name }}</label>
                    </div>
                </div>
            </div>
        </div>
        <div class="form-footer">
            <button v-if="isEmpty" @click="addTask">Add</button>
            <button v-else @click="updateTask">Update</button>
        </div>
    </div>
</template>

<script>
// IMPORT UTILITIES
import axios from 'axios'

export default {
    name: 'TaskForm',
    props: {
        form_title: {
            type: String,
            required: true
        },
        taskModel: {
            type: Object,
            default: () => {
                return {}
            }
        }
    },
    data () {
        return {
            tags: [],
            tags_selected: [],
            task: this.taskModel
        }
    },
    mounted () {
        axios
            .get('http://127.0.0.1:8000/api/tags/')
            .then( (response) => {
                console.log(response.data)
                this.tags = response.data
            })

    },
    methods: {
        isEmpty() {
            return Object.keys(this.task).length === 0
        },
        addTask() { 
            this.task.tags = this.tags_selected
            console.log(this.task)      
            axios
                .post('http://127.0.0.1:8000/api/tasks/', 
                    this.task)
                .then( (response) => {
                    console.log(response);
                })
                .catch( (error) => {
                    console.log(error);
                });
        },
    }
}
</script>

<style lang="postcss" scoped>
    .form-header {
        @apply
            p-2
            m-2
            text-3xl
            text-pink-500
            font-bold
    }
    .form-content {
        @apply
            md:grid-cols-3
            grid
            grid-cols-2
            gap-4
            justify-items-center
            p-2
            m-2
    }
    .form-label {
        @apply
            text-lg
    }
    input, textarea {
        @apply
            p-2
            border-2
            border-opacity-40
            border-solid
            border-gray-300
            rounded-sm
    }
    textarea {
        vertical-align: top;
        resize: none;
    }
    .form-footer {
        @apply
            p-2
            m-2
    }
    .form-footer>button {
        @apply
            focus:outline-none
            hover:bg-pink-800
            block
            p-2
            rounded-xl 
            bg-pink-400 
            text-white 
            font-bold 
            transition-colors
    }
</style>