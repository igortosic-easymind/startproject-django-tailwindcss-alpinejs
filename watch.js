const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['static/src/js/main.js'],
  bundle: true,
  outfile: 'static/dist/main.js',
  sourcemap: true, // Enable source maps in watch mode
  watch: {
    onRebuild(error, result) {
      if (error) console.error('watch build failed:', error);
      else console.log('watch build succeeded:', result);
    },
  },
}).catch(() => process.exit(1));

console.log('watching...');
