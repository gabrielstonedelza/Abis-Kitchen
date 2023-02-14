<script>
	import { fly } from 'svelte/transition';
	export let data;
	import Abis from '../assets/images/abis_market.png';
	import AbisLogo from '../assets/images/edited.png';
	import FoodList from '../components/FoodList.svelte';
	import UsCard from '../components/UsCard.svelte';
	import Footer from '../components/Footer.svelte';
	import menu from '../assets/images/open-menu.png';
	
	
</script>
<svelte:head>
	<title>Abi's | Home</title>
</svelte:head>

<section
	class="section-a"
	in:fly={{ y: 50, duration: 500, delay: 500 }}
	out:fly={{ duration: 500 }}
>
	<div class="container">
		<div class="title-logo">
			<img src={AbisLogo} alt="" />
			<!-- <h1>Abi's Kitchen</h1> -->
		</div>

		<!-- motto and foods -->
		<div class="motto-food-display">
			<div class="motto">
				<h1>Abi's Kitchen</h1>
				<p class="my-motto">Food you can't resist 😋</p>
				<a sveltekit:prefetch sveltekit:noscroll href="/menu">Our Menu</a>
			</div>
			<div class="side-img">
				<img src={Abis} alt="abis_market_side_image" />
			</div>
		</div>
		<br>
		<br>
		<FoodList data={data} />
		<br>
		<h3>Why Choose Us?</h3>
		<br>
		<UsCard />
		<Footer />
		<div class="fixed-menu">
			<a href="/menu">
				<img src={menu} alt="">
			</a>
		</div>
	</div>
</section>

<style lang="scss">
	.container {
		h3{
			text-align: center;
			padding: 2rem;
			font-size:30px;
		}
		// padding-right: 2rem;
		// padding-left: 2rem;
		padding-top: 2rem;
		
		.title-logo {
			display: flex;
			gap: 1rem;
			align-items: center;
			padding-left: 2rem;
			img {
				width: 50px;
				height: 50px;
				border-radius: 50%;
				box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
			}
		}

		.motto-food-display {
			// width: 100%;
			display: grid;
			grid-template-columns: 50% auto;
			align-items: center;
			gap: 1rem;
			.motto {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;
				h1{
					font-size:4rem;
					padding-left: 20px;
				}
				p{
					color: grey;
					font-style: italic;
					padding-bottom: 20px;
				}
				a{
					background-color:#ec2027;
					color: white;
					padding-left: 10px;
					padding-right: 10px;
					padding-top: 5px;
					padding-bottom: 5px;
					border-radius: 20px;
					cursor: pointer;
					transition: 1s ease;
					box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
					&:hover{
						background-color:#f38822;
					}
				}
			}
			.side-img {
				img {
					animation: rotation 11s infinite linear;
					max-width: 50%;
					
					// display: block;
				}
			}
		}
		.fixed-menu{
			position: fixed;
			z-index: 1;
			top: 410px;
			right: 10px;
			overflow: hidden;
			img{
				// box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
				width: 50px;
				height: 50px;
				border-radius: 50%;
			}
		}
	}

	@keyframes rotation {
	from {
		transform: rotate(0deg);
	}
	to {
		transform: rotate(359deg);
	}
}
// media query
@media (max-width: 991px){}
@media (max-width: 768px){
	.container{
		.motto-food-display{
			display: flex;
			justify-content: center;
			.motto{
				h1{
					font-size: 30px;
				}
			}
			.side-img{
				display: none;
			}
		}
	}
}
@media (max-width: 500px){
	.container{
		.motto-food-display{
			display: flex;
			justify-content: center;
			.motto{
				h1{
					font-size: 30px;
				}
			}
			.side-img{
				display: none;
			}
		}
	}
}
</style>
