<script>
	import { fly } from 'svelte/transition';
	import Specials from '../../components/SpecialDishes.svelte';
	import Regular from '../../components/Regular.svelte';
	import back from '../../assets/images/left-arrow.png';
</script>

<div class="container" in:fly={{ y: 50, duration: 500, delay: 500 }} out:fly={{ duration: 500 }}>
	<h1>Special Menu</h1>
	<p>
		Pick from our special and regular menus.
	</p>
	<div class="special-container">
		<Specials />
		<br />
	</div>
	<div class="regular-container">
		<h1>Regular Menu</h1>
		<Regular />
	</div>
	<div class="fixed-menu">
		<a href="/">
			<img src={back} alt="" />
		</a>
	</div>
</div>

<style lang="scss">
	.container {
		max-width: 1200px;
		margin: 0 auto;
        h1{
            text-align: center;
            padding: 20px;
        }
        p{
            text-align: center;
            color: gray;
            padding-bottom: 20px;
        }
        .special-container{
            padding-bottom: 20px;
        }

		.fixed-menu {
			position: fixed;
			z-index: 1;
			top: 410px;
			right: 10px;
			overflow: hidden;
			img {
				// box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
				width: 50px;
				height: 50px;
				border-radius: 50%;
			}
		}
	}
</style>
