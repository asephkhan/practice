/** @type {import('tailwindcss').Config} */
export default {
  content: [
        "./*.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'neutral': {
          900: '#163A34',
          600: '#395852',
          300: '#D0DCD9',
          200: '#E0E6E3',
          100: '#F6F5F1',
          0: '#FFFFFF'
        },
        'orange': {
          500: '#FE9F6B'
        },
        'teal': {
          500: '#49ac9b'
        },
        'indigo': {
          500: '#697ddb'
        }
      }
    },
  },
  plugins: [],
}

