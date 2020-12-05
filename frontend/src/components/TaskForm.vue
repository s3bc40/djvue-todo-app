<template>
    <div id="form">
        <div class="form-header">{{ form_title }}</div>
        <div class="form-content">
            <div>
                <label class="form-label" for="title">Title: </label>
                <input type="text" id="title" v-model="title" placeholder="Insert title here">
            </div>

            <div>
                <label class="form-label" for="description">Description: </label>
                <textarea
                    id="description"
                    v-model="description" 
                    placeholder="Insert details here"
                ></textarea>
            </div>

            <div>
                <div class="form-label">Select tags: </div> 
                <div v-for="tag in tags" :key="tag.id">
                    <div v-if="tag.visibility">
                        <input type="radio" id="tag" value="tags.name" v-model="tags_selected">
                        <label for="tags.name">{{ tag.name }}</label>
                    </div>
                </div>
            </div>
        </div>
        <div class="form-footer">
            <button type="submit">Submit form</button>
        </div>
    </div>
</template>

<script>
// IMPORT UTILITIES
import axios from 'axios'

export default {
    name: 'TaskForm',
    data () {
        return {
            tags: [],
            tags_selected: []
        }
    },
    props: {
        form_title: {
            type: String,
            required: true
        } 
    },
    mounted () {
        axios.get('http://127.0.0.1:8000/api/tags/')
            .then( (response) => {
                console.log(response.data)
                this.tags = response.data
            })
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