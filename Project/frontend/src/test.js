import axios from 'axios';

// const apiKey = 'RGAPI-865e4515-a5c0-424c-bc62-62c0d9a4440f';

const baseURL = 'http://kr.api.riotgames.com';

const axiosInstance = axios.create({
    baseURL : baseURL
});

const response = await axiosInstance.get('/lol/platform/v3/champion-rotations');

// console.log(response);