module.exports = {
    mode: 'jit',
    content: [
      './output/**/*.html',
      './output/**/*.js',
    ],
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
  ],
}

