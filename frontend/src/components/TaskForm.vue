<template>
    <div id="form">
        <h1>{{ form_title }}</h1>

        <label for="title">Title: </label>
        <input type="text" id="title" v-model="title" placeholder="Insert title here">
        
        <label for="description">Description: </label>
        <textarea 
            id="description" 
            v-model="description" 
            placeholder="Insert details here"
        ></textarea>

        <p>Select tags: </p> 
        <div v-for="tag in tags" :key="tag.id">
            <div v-if="tag.visibility">
                <input type="radio" id="tag" value="tags.name" v-model="tags_selected">
                <label for="tags.name">{{ tag.name }}</label>
            </div>
        </div>

        <button type="submit">Submit form</button>
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

</style>