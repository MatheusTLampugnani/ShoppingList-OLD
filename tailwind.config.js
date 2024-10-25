/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      margin: {
        '14': '56px',
      },
      padding: {
        '50': '50px',
      }

    },
  },
  plugins: [],
}

