<script>
  import Tailwindcss from "./Tailwindcss.svelte"
  import Intro from './units/intro.svelte'
  // import Question from './units/question.pug'
  export let name
</script>

<style lang='stylus' global>

@import './style/presentation'

main 
  padding: 1em
  max-width: 240px
  margin: 0 auto

@media (min-width: 640px) {
  main {
    max-width: 768px;
  }
}
@media (min-width: 1200px) {
  main {
    max-width: 1024px
  }
  body{
    font-size: font_size * 1.2
  }
}
@media (min-width: 1440px) {
  main {
    max-width: 1240px
  }
  body{
    font-size: font_size * 1.5
  }
}
</style>

<Tailwindcss />
<main>
  <Intro />
  <template src='./units/question.pug' lang='pug'></template>
  <p>hi</p>
  <template src='./units/red.pug' lang='pug'></template>
</main>
