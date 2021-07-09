module.exports = {
  purge: {
    enabled: true,
    mode: 'all',
    content: [
      'output/**/*.html',
      'output/**/*.js',
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
