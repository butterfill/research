import sveltePreprocess from 'svelte-preprocess';

module.exports = {
  preprocess: sveltePreprocess({
    postcss: true,
    pug : true,
    stylus : true
  })
};