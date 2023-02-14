<script>
	import { fly } from 'svelte/transition';
	import plantainbeans from '../assets/images/food/plantain_beans.jpeg';
	import riceball from '../assets/images/food/riceball.jpeg';
	import tz from '../assets/images/food/tz.jpeg';
	import yamchicken from '../assets/images/food/yam_chicken.jpeg';
	import yamtilapia from '../assets/images/food/yam_tilapia.jpeg';
	import bankuokro from '../assets/images/food/IMG_0559.jpg';
	import waakye from '../assets/images/food/IMG_0560.jpg';
	import jollof from '../assets/images/food/jollof.jpeg';
	import kenkeyfish from '../assets/images/food/kenkey_fish.jpeg';
	import friedrice from '../assets/images/food/ff.jpeg';
	import fufugroundnut from '../assets/images/food/fufu.jpeg';
	import bankuTilapia from '../assets/images/food/bankutilipia.jpeg';

	let imageModal = '';
	let openModalImage = false;

	function closeModal() {
		openModalImage = false;
	}
	function openModal(src) {
		openModalImage = true;
		imageModal = src;
		// return src;
	}
</script>

<section class="food-box">
	{#if openModalImage}
		<div class="modal" in:fly={{ y: 50, duration: 300, delay: 300 }} out:fly={{ duration: 500 }}>
			<button on:click={closeModal}>x</button>
			<div class="modal-content">
				<img src={imageModal} alt="" />
			</div>
		</div>
	{/if}
	<div class="box">
		<img src={plantainbeans} alt="food-menu" on:click={(e) => openModal(plantainbeans)} />
		<br />
		<br />
		<h1>Fried Plantain & Beans</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
    <br>
	<div class="box">
		<img src={riceball} alt="food-menu" on:click={(e) => openModal(riceball)} />
		<br />
		<br />
		<h1>Rice ball & Groundnut soup</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
    <br>
	<div class="box">
		<img src={tz} alt="food-menu" on:click={(e) => openModal(tz)} />
		<br />
		<br />
		<h1>TZ</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
    <br>
	<div class="box">
		<img src={yamchicken} alt="food-menu" on:click={(e) => openModal(yamchicken)} />
		<br />
		<br />
		<h1>Fried Yaw & Chicken</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
</section>
<br />
<hr />
<br />

<section class="food-box">
	{#if openModalImage}
		<div class="modal" in:fly={{ y: 50, duration: 300, delay: 300 }} out:fly={{ duration: 500 }}>
			<button on:click={closeModal}>x</button>
			<div class="modal-content">
				<img src={imageModal} alt="" />
			</div>
		</div>
	{/if}

	<div class="box">
		<img src={yamtilapia} alt="food-menu" on:click={(e) => openModal(yamtilapia)} />
		<br />
		<br />
		<h1>Fried Yam & Tilapia</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
    <br>
	<div class="box">
		<img src={bankuokro} alt="food-menu" on:click={(e) => openModal(bankuokro)} />
		<br />
		<br />
		<h1>Banku & Okro Soup.</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
    <br>
	<div class="box">
		<img src={waakye} alt="food-menu" on:click={(e) => openModal(waakye)} />
		<br />
		<br />
		<h1>Waakye</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
    <br>
	<div class="box">
		<img src={jollof} alt="food-menu" on:click={(e) => openModal(jollof)} />
		<br />
		<br />
		<h1>Jollof & Tilapia</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
</section>
<br />
<hr />
<br />
<section class="food-box">
	{#if openModalImage}
		<div class="modal" in:fly={{ y: 50, duration: 300, delay: 300 }} out:fly={{ duration: 500 }}>
			<button on:click={closeModal}>x</button>
			<div class="modal-content">
				<img src={imageModal} alt="" />
			</div>
		</div>
	{/if}

	<div class="box">
		<img src={kenkeyfish} alt="food-menu" on:click={(e) => openModal(kenkeyfish)} />
		<br />
		<br />
		<h1>Kenkey & Fish</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div><br>
	<div class="box">
		<img src={friedrice} alt="food-menu" on:click={(e) => openModal(friedrice)} />
		<br />
		<br />
		<h1>Fried Rice & Chicken</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
    <br>
	<div class="box">
		<img src={fufugroundnut} alt="food-menu" on:click={(e) => openModal(fufugroundnut)} />
		<br />
		<br />
		<h1>Fufu & Groundnut Soup.</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
    <br>
	<div class="box">
		<img src={bankuTilapia} alt="food-menu" on:click={(e) => openModal(bankuTilapia)} />
		<br />
		<br />
		<h1>Banku & Tilapia.</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
</section>

<style lang="scss">
	.modal {
		width: 100%;
		background-color: rgba(0, 0, 0, 0.829);
		position: fixed;
		z-index: 1000;
		top: 0;
		left: 0;
		bottom: 0;
		right: 0;
		overflow: hidden;

		button {
			padding: 20px;
			border: none;
			font-size: 30px;
			background: none;
			color: white;
			float: right;
			padding-right: 30px;
			cursor: pointer;
			transition: 1s ease;
			&:hover {
				color: #ec2027;
				font-size: 40px;
			}
		}
		.modal-content {
			width: 75%;
			transition: 1s ease;
			padding: 20px;
			display: flex;
			justify-content: center;
			align-items: center;
			margin-left: 12%;
			margin-top: 5%;
			img {
				width: 75%;
				height: auto;
				border-radius: 24px;
				// max-height: 100%;
			}
		}
	}
	.food-box {
		height: inherit;
		padding: 2rem;
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		gap: 1rem;
		.box {
			h1 {
				padding-top: 2rem;
				padding-bottom: 20px;
				font-size: 20px;
			}
			p {
				font-weight: bold;
				color: rgb(169, 166, 166);
			}
			.price {
				color: #ec2027;
				border: 1px solid #ec2027;
				border-radius: 20px;
				padding-left: 12px;
				padding-right: 12px;
				padding-top: 3px;
				padding-bottom: 3px;
			}
			border-radius: 20px;
			position: relative;
			padding: 2rem;
			box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
			display: flex;
			flex-direction: column;
			justify-content: center;
			flex-wrap: wrap;
			align-items: center;
			cursor: pointer;
			transition: 1.5s ease;
			width: 250px;

			&:hover {
				background-color: #f38822;
				.price {
					color: #fff;
					border: 1px solid #fff;
					border-radius: 20px;
					padding-left: 12px;
					padding-right: 12px;
					padding-top: 3px;
					padding-bottom: 3px;
				}
				p {
					font-weight: bold;
					color: white;
				}
				h1 {
					color: white;
				}
				img {
					transform: rotate(90deg);
					border: solid 5px #f38822;
					left: 0;
				}
			}
			img {
				box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
				position: absolute;
				z-index: 1;
				top: -29px;
				left: 10px;
				width: 100px;
				height: 100px;
				border-radius: 50%;
				overflow: hidden;
				object-fit: cover;
				border: solid 5px #ec2027;
				transition: 1s ease;
				// &:hover{
				// 	transform: rotate(90deg);
				// }
			}
		}
	}
	@media (max-width: 768px) {
		.food-box {
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
		}
	}
</style>
