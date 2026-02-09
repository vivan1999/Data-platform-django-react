// AXIOS setup
import axios from "axios"

const baseURL = "http://127.0.0.1:8000/"

const api = axios.create({
    baseURL: import.meta.env.URL ? import.meta.env.URL: baseURL // for production applications enviornment variable
})

api.interceptors.request.use((config)=>{
    const token = localStorage.getItem("access")
    if(token){
        config.headers.Authorization = `JWT ${token}`
    }
    return config
},
(error)=>{
    return Promise.reject(error)
});

export default api;

