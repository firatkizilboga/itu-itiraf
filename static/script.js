let url = `http://firatkizilboga.pythonanywhere.com/api`;

let confTitle = document.getElementById("confession-title");
let confBody = document.getElementById("confession-info");
let confDate = document.getElementById("confession-date");
let confLikes = document.getElementById("likes");
let confComments = document.getElementById("confessions");


async function getData() {
    const response = await fetch(url); // buraya api adresini yaz
    const data = await response.json(); // datayla ne yapılacaksa yap
    
    console.log(data);
    console.log(data[0].title);
    console.log(data[0].date);
    console.log(data[0].body);
    console.log(data[0].likes);
    console.log(data[0].comments);

    confTitle.innerHTML = data[1].title;
    confDate.innerHTML = data[1].date.toString().split('T')[0];
    confBody.innerHTML = data[1].body;
    confLikes.innerHTML = data[1].likes + " " + '<i class="fa-regular fa-heart"></i>';
    confComments.innerHTML = data[1].comments + " " + '<i class="fa-regular fa-comment"></i>';
    
  }
window.addEventListener("load", getData);