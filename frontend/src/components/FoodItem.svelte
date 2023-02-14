<script>
	import { fly } from 'svelte/transition';
	
	import egusiyam from "../assets/images/food/egusi_yam.jpeg"
	import egusi from "../assets/images/food/egusi.jpeg"

	import goatsoup from "../assets/images/food/goat_meat.jpeg"

	import okrosoup from "../assets/images/food/okro_soup.jpeg"
	
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
		<img
			src={goatsoup}
			alt="food-menu"
			on:click={(e) => openModal(goatsoup)}
		/>
		<br />
		<br />
		<h1>Goat Soup.</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
	<div class="box">
		<img
			src={okrosoup}
			alt="food-menu"
			on:click={(e) => openModal(okrosoup)}
		/>
		<br />
		<br />
		<h1>Okro Soup.</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
	<div class="box">
		<img
			src={egusi}
			alt="food-menu"
			on:click={(e) => openModal(egusi)}
		/>
		<br />
		<br />
		<h1>Egusi</h1>
		<p>Local</p>
		<p class="price">$20</p>
	</div>
	<div class="box">
		<img
			src={egusiyam}
			alt="food-menu"
			on:click={(e) => openModal(egusiyam)}
		/>
		<br />
		<br />
		<h1>Egusi with Yam</h1>
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
		justify-content: center;
		gap: 1rem;
		.box {
			h1 {
				padding-top: 2rem;
				padding-bottom: 20px;
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
			width: 400px;

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
</style>
