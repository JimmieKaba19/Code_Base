// change the navbar on scroll down

window.addEventListener('scroll', () => {
    document.querySelector('nav').classList.toggle('window-scroll', window.scrollY > 100 )
})


//show and hide the answers to the frequently asked questions
const faqs = document.querySelectorAll('.faq');

faqs.forEach(faq => {
    faq.addEventListener('click', () => {
        faq.classList.toggle('open');

        //change the icon to a minus when one clicks the question
        const icon = faq.querySelector('.faq__icon i');
        if(icon.className === "uil uil-plus"){
            icon.className = "uil uil-minus";
        }
        else{
            icon.className = "uil uil-plus";
        }
    })
})

//will show and hide the options in the menu if clicked in smaller devices
const menu = document.querySelector('.nav__menu');
const menuBtn = document.querySelector('#open-menu-btn');
const closeBtn = document.querySelector('#close-menu-btn');

menuBtn.addEventListener('click', () => {
    menu.style.display = 'flex';
   closeBtn.style.display = 'inline-block';
   menuBtn.style.display = 'none';
})

//close the navbar
const closeNav = () => {
    menu.style.display = 'none';
    closeBtn.style.display = 'none';
    menuBtn.style.display = 'inline-block';
}

closeBtn.addEventListener('click', closeNav)