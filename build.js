const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['static/js/main.js'],
  bundle: true,
  outfile: 'static/dist/main.js',
  minify: true,
  sourcemap: process.env.NODE_ENV === 'development', // Enable source maps in development mode
}).catch(() => process.exit(1));
