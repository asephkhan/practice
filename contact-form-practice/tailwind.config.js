/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      // 🎨 COLORS from your style guide
      colors: {
        'grey': {
          900: '#3A434A',
          500: '#A6AEB4',
        },
        'green': {
          600: '#0C7D69',
          200: '#E0F1EE',
        },
        'error': '#D92D20',
        'white': '#FFFFFF',
      },
      
      // ✍️ TYPOGRAPHY
      fontFamily: {
        // Best practice to capitalize the font name to match the actual font
        sans: ['Karla', 'sans-serif'], 
      },
      fontSize: {
        'h1': ['32px', {
          lineHeight: '100%',
          letterSpacing: '-1px',
          fontWeight: '700',
        }],
        'body-md': ['18px', {
          lineHeight: '150%',
          letterSpacing: '0px',
          fontWeight: '700',
        }],
        'body-sm': ['16px', {
          lineHeight: '150%',
          fontWeight: '400',
        }],
      },
      // SCREENS
      screens:{
        'sm': '480px',
        'md': '768px',
        'lg': '976px'
      },

      // 📏 SPACING
      spacing: {
        '5px': '5px',
        '8px': '8px',
        '10px': '10px',
        '12px': '12px',
        '16px': '16px',
        '24px': '24px',
        '25px': '25px',
        '32px': '32px',
        '40px': '40px',
        '50px': '50px',
        '100px': '100px',
        '200px': '200px',
        '300px': '300px',
        '400px': '400px',
        '500px': '500px',
        '1000px': '1000px',
      },
    },
  },
  plugins: [],
};