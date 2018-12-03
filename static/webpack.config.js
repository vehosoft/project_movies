const path = require('path');

module.exports = {
  // This is the "main" file which should include all other modules
  entry: __dirname + '/management/main.js',
  // Where should the compiled file go?
  output: {
        // To the `dist` folder
        path: __dirname + '/management',
        // With the filename `build.js` so it's dist/build.js
        filename: 'app.js'
  },
    module: {
        rules: [
            {
                // vue-loader config to load `.vue` files or single file components.
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        // https://vue-loader.vuejs.org/guide/scoped-css.html#mixing-local-and-global-styles
                        css: ['vue-style-loader', {
                            loader: 'css-loader',
                        }],
                    },
                    cacheBusting: true,
                },
            },
        ],
    }
}