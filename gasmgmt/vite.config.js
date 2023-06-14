import { resolve } from 'path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
    base: '/gasmgmt/',
    plugins: [react()],
    build: {
        outDir: "../forum_app/wwwroot/gasmgmt",
        emptyOutDir: true,
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                app1: resolve(__dirname, 'app1/index1.html'),
                app2: resolve(__dirname, 'app2/index2.html'),
            },
        },
    }
})
