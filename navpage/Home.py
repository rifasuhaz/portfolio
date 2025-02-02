import streamlit as st # type: ignore
import streamlit.components.v1 as components # type: ignore

components.html(
    """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Triodion&display=swap" rel="stylesheet"><style>
        .driver__container{
            width: 100%;
            display:flex;
        }
        .driver_img {
            background: black;
            width: 100%;
            display: grid;
            grid-auto-flow:dense;
            grid-template-columns: repeat(4, 25%)
            /* backface-visibility: hidden; */
        }
        .driver_img img{ 
            margin-bottom: -64px;
            width: 100%;
            height: 400px;
            filter: grayscale(100%); 
            transition: transform 0.5s;
        }
        .driver_img .text {
            transition: .5s ease;
            position: relative;
            bottom:2%;
            text-align:center;
            color: rgb(255, 255, 255);
            background-color: black;
            font-size: 18px;
            font-weight: 10;
            font-family: "Montserrat", serif;
            padding: 15px 20px;
            opacity: 0;
        }
        .driver_img img:hover{
            filter: grayscale(0);
            cursor: pointer;
            transform: scale(0.85);
            position: relative;
            z-index: 0;  
        }
        .driver_img .image:hover .text{
            opacity: 1; 
        }
    </style>
    <div class="driver_container">
        <div class="driver_img">
            <span class="image"><img src="app/static/1.png"><div class="text"><b>Al Fahidi, Dubai</b></div></span>
            <span class="image"><img src="app/static/2.png"><div class="text"><b>Cala Bona, Blanes</b></div></span>
            <span class="image"><img src="app/static/4.png"><div class="text"><b>Venezia</b></div></span>
            <span class="image"><img src="app/static/5.png"><div class="text"><b>Königssee</b></div></span>
            <span class="image"><img src="app/static/13.png"><div class="text"><b>Frankfurt</b></div></span>
            <span class="image"><img src="app/static/8.jpg"><div class="text"><b>Jelly Fishes</b></div></span>
            <span class="image"><img src="app/static/10.jpg"><div class="text"><b>Barcelona</b></div></span>
            <span class="image"><img src="app/static/11.jpg"><div class="text"><b>Milano</b></div></span>
            <span class="image"><img src="app/static/12.jpg"><div class="text"><b>Creek, Dubai</b></div></span>
            <span class="image"><img src="app/static/6.png"><div class="text"><b>OP81</b></div></span>
            <span class="image"><img src="app/static/7.png"><div class="text"><b>Amsterdam</b></div></span>
            <span class="image"><img src="app/static/3.png"><div class="text"><b>Venezia</b></div></span>
        </div>
    </div>
    """,height=400, scrolling=True
)


st.header("Rifa Suhaz")
st.text("Hello there :)")

