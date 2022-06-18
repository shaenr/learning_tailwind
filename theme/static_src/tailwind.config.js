const colors = require('tailwindcss/colors')

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        colors: {
            transparent: 'transparent',
            current: 'currentColor',
            blue: colors.indigo,
            purple: colors.violet,
            gray: colors.gray,
            black: colors.black,
            green: colors.emerald,
            red: colors.rose,
            pink: colors.fuchsia,
            white: colors.white,
        },
        extend: {},
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
