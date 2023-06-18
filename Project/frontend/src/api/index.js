import axios from 'axios';

const axiosInstance = axios.create({
    baseURL : process.env.VUE_APP_BACKEND_URL
});

function registerUser(data) {
    return axiosInstance.post('api/accounts/signup/', data);
}

function loginUser(data) {
    return axiosInstance.post('api/accounts/login/', data);
}

function getUserInfo(token) {
    return axiosInstance.get('api/accounts/user/', {
        headers : {
            'Authorization' : `token ${token}`
        }
    })
}

function updateUsernameInfo(data, token) {
    return axiosInstance.put('api/accounts/user/', data, {
        headers : {
            'Authorization' : `token ${token}`
        }
    })
}

function deleteUserInfo(token) {
    return axiosInstance.delete('api/accounts/user/', {
        headers : {
            'Authorization' : `token ${token}`
        }
    })
}

function updatePassword(data, token) {
    return axiosInstance.put('api/accounts/user/pw_update/', data, {
        headers : {
            'Authorization' : `token ${token}`
        }
    })
}

function findPassword(data) {
    return axiosInstance.put('api/accounts/pw_change/', data)
}

function getArticles() {
    return axiosInstance.get('api/articles/')
}

export { registerUser, loginUser, getUserInfo, updateUsernameInfo, deleteUserInfo, updatePassword, findPassword, getArticles };