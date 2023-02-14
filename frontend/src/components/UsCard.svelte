<script>
    import bowl from "../assets/images/rice.png"
    import quality from "../assets/images/quality.png"
    import customer from "../assets/images/customer.png"
</script>

<div class="why-us">
    <div class="box">
        <img src={bowl} alt="">
        <h2>Serve Healthy Food</h2>
        <p>Your health matters to us.</p>
    </div>
    <div class="box">
        <img src={quality} alt="">
        <h2>Quality Food</h2>
        <p>Giving you the best you can't resist.</p>
    </div>
    <div class="box">
        <img src={customer} alt="">
        <h2>Excellent Customer Service</h2>
        <p>Offering 24/7 customer service.</p>
    </div>
</div>

<style lang="scss">
    .why-us{
        // width: 30%;
		height: inherit;
		padding: 3rem;
		display: flex;
        flex-wrap: wrap;
		justify-content: center;
        align-items: center;
		gap: 1rem;

        .box{
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

            img{
                width: 150px;
                height: 150px;
                padding: 2rem;
            }
        }
    }
    @media (max-width: 768px){
        .why-us{
            .box{
                h2{
                    font-size:18px;
                }
                p{
                    color: rgba(163, 160, 160, 0.879);
                }
                width: 300px;
            }
        }
    }

</style>