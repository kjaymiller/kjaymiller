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
   fontFamily: {
      display: ['Gilroy', 'sans-serif'],
      body: ['Graphik', 'sans-serif'],
    },
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
