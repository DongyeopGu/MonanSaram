module.exports = {
  devServer: {
    disableHostCheck: true,
    proxy: {
       '/api' : {
        // target: 'http://172.18.0.4:8001',
        target: 'http://localhost:8000',
        changeOrigin: true,
        logLevel: 'debug',
        pathRewrite: {'^/api' : ''}     
      }    
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}