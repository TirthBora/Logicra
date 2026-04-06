import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

export const graphAPI = {
  generate: (projectPath) => api.post('/graph/', { project_path: projectPath }),
}

export const cloneAPI = {
  detect: (data) => api.post('/clone/', data),
}

export const explainAPI = {
  code: (data) => api.post('/explain/', data),
}

export const errorAPI = {
  translate: (data) => api.post('/error/', data),
}

export default api

