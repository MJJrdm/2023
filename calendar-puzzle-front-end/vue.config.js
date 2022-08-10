const { defineConfig } = require('@vue/cli-service')
const { DefinePlugin } = require('webpack')
module.exports = defineConfig({
  configureWebpack: {
    plugins: [
      new DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV)
      })
    ]
  },
  transpileDependencies: true,
  publicPath: './',
  assetsDir: 'static',
  devServer: {
    // port: port,
    // open: true,
    // overlay: {
    //   warnings: false,
    //   errors: true
    // },
    proxy: {
      '/api': {
        target: 'http://43.138.208.115:8006/',
        pathRewrite: {'^/api' : ''}
      }
    }
  },
})
