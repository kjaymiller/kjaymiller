module.exports = {
  purge: {
    enabled: false,
    mode: 'all',
    content: [
      './output/**/*.html',
      './output/**/*.js',
    ],
  },
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [
    // ...
    require('tailwindcss'),
    require('autoprefixer'),
    // ...
  ],
}
