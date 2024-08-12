<div class="Footer-Svg">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="Orange" fill-opacity="1" d="M0,160L48,144C96,128,192,96,288,96C384,96,480,128,576,170.7C672,213,768,267,864,256C960,245,1056,171,1152,154.7C1248,139,1344,181,1392,202.7L1440,224L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>

</div>




<footer>
    <div class="footer-col about">
        <h4>About us</h4>
        <p style="color: black;font-size: 20px;">I am a skilled web developer specializing in Python full stack development. With expertise in both front-end and back-end technologies, I create responsive, high-quality web applications tailored to client needs. Let’s collaborate to build exceptional digital solutions together.</p>
    </div>
    <div class="footer-col services">
        <h4 style="margin-left: 120px;">Services</h4>
        <ul style="margin-left: 120px;">
            <li><a href="#">Frontend</a></li>
            <li><a href="#">Backend</a></li>
            <li><a href="#">SEO</a></li>
            <li><a href="#">Domain</a></li>
            <li><a href="#">Hosting</a></li>
           
        </ul>
    </div>
    <div class="footer-col company">
        <h4>Company</h4>
        <ul>
            <li><a href="#">About</a></li>
            <li><a href="#">Legal</a></li>
            <li><a href="#">Contact us</a></li>
        </ul>
    </div>
    <div class="footer-col follow">
        <h4>Follow us</h4>
        <div class="links">
            <a href="#"><i class="fab fa-linkedin-in"></i></a>
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
        </div>
    </div>
    <div class="line">
        <p style="font-size: 20px;color:#000;">Copyright © 2024 Codestation. All Rights Reserved.</p>
    </div>
</footer>

<style>
footer {
    display: flex;
    flex-wrap: wrap;
    background-color:Orange;
    padding: 40px 5%;
    color: black;
    margin-top:400px;
}

.footer-col {
    flex: 1;
    min-width: 200px;
    margin-bottom: 20px;
}

.footer-col h4 {
    margin-bottom: 20px;
    font-weight: bold;
    font-size: 23px;
    color: rgb(156, 47, 14);
    text-transform: capitalize;
    position: relative;

}

.footer-col h4::before {
    content: '';
    position: absolute;
    left: 0;
    bottom: -6px;
    background-color:green;
    height: 2px;
    width: 90px;
}

ul {
    list-style: none;
    padding: 0;
}

ul li {
    margin-bottom: 8px;
}

ul li a {
    display: block;
    font-size: 23px;
    text-transform: capitalize;
    color: black;
    text-decoration: none;
    transition: 0.4s;
    font-family: "Lora";
}

ul li a:hover {
    color: #27c0ac;
    padding-left: 2px;
}

.links a {
    display: inline-block;
    height: 50px;
    width: 45px;
    color: black;
    background-color: rgba(40, 130, 214, 0.8);
    margin: 0 10px 10px 0;
    text-align: center;
    line-height: 44px;
    border-radius: 50%;
    transition: 0.4s;
}

.links a:hover {
    color: white;
    background-color: green;
}

.line {
    text-align: center;
    font-size: 14px;
    margin-top: 20px;
}

.Footer-Svg{
margin-top: 200px;
position: absolute;


}



@media (max-width: 740px) {
    .footer-col {
        width: 100%;
        text-align: center;
    }

    .footer-col h4::before {
        display: none;
    }
}

@media (max-width: 555px) {
    footer {
        padding: 20px 2%;
    }

    .footer-col h4 {
        font-size: 18px;
    }

    ul li a {
        font-size: 16px;
    }

    .line {
        font-size: 12px;
    }
}



</style>



