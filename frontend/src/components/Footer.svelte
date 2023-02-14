<script>
	import email from '../assets/images/email.png';
	import calling from '../assets/images/calling.png';
	import location from '../assets/images/location-pin.png';

	import working from '../assets/images/discipline.png';
</script>

<footer>
	<h3>Contact Us</h3>
	<div class="container">
		<div class="box">
			<img src={email} alt="email" />
			<p>kitchenabis360@gmail.com</p>
		</div>
		<div class="box">
			<img src={calling} alt="phone" />
			<p>+1(815)905-110</p>
		</div>
		<div class="box">
			<img src={location} alt="location" />
			<p>101 W Romeo Road Romeoville,IL 60446</p>
		</div>
		<div class="box">
			<img src={working} alt="menu" />
			<p>Working days(Fridays,Saturdays & Sundays)</p>
		</div>
	</div>
	<div class="footer-below">&copy;2023 Abiskitchen.online All rights reserved.</div>
</footer>

<style lang="scss">
	footer {
		h3 {
			padding: 3rem;
			font-size: 30px;
		}
		background-color: #ec2027;
		color: white;
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		gap: 1rem;
		.container {
			display: flex;
			justify-content: center;
			align-items: center;
			gap: 2rem;
			padding-left: 12px;
			padding-right: 12px;
			.box {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;
				gap: 1rem;

				img {
					width: 50px;
					height: 50px;
				}
				a {
					color: white;
				}
			}
		}
		.footer-below {
			height: 50px;
			background-color: #aa0006;
			width: 100%;
			padding: 0;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
			font-weight: bold;
			color: white;
		}
	}
	@media (max-width: 768px) {
		.container {
			padding: 20px;
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
			.box {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;
			}
		}
	}
</style>
