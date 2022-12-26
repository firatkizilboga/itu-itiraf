let url = `http://firatkizilboga.pythonanywhere.com/api/confessions`;

async function getData() {
  const response = await fetch(url); // buraya api adresini yaz
  const data = await response.json(); // datayla ne yapılacaksa yap

  console.log(data);
  console.log(data.length);

  for(let i = 0; i < data.length; i++ )
  {
    var confTitle = data[i].title;
    var confDate = data[i].date.toString().split('T')[0];
    var confBody = data[i].body;
    var confLikes = data[i].likes;
    var confComments = data[i].comments;

    createConfessionDiv(confTitle, confDate, confBody, confLikes, confComments);
  }
  
}
window.addEventListener("load", getData);

function createConfessionDiv(confTitle, confDate, confBody, confImg ,confLikes, confComments) {
  // Creating a div element
  var divElement = document.createElement("Div");
  divElement.id = "divID";

  // Styling it
  divElement.classList.add("home-confession")

  //Adding Title
  var confTitlee = document.createElement("H3");
  confTitlee.innerHTML = confTitle;
  divElement.appendChild(confTitlee);

  //Adding Date
  var confDatee = document.createElement("P");
  confDatee.innerHTML = confDate;
  divElement.appendChild(confDatee);
  confDatee.classList.add("confession-date");
    
  //adding header div
  var confHeader = document.createElement("Div");
  confHeader.appendChild(confTitlee);
  confHeader.appendChild(confDatee);
  divElement.appendChild(confHeader);
  confHeader.classList.add("confession-header");
  
  // Adding a paragraph to it
  var confInfo = document.createElement("P");
  var confInfoTextext = document.createTextNode(confBody);
  confInfo.appendChild(confInfoTextext);
  divElement.appendChild(confInfo);
  confInfo.classList.add("confession-info");

  //create an image tag if img is not null
  if(confImg != null)
  {
    var confImg = document.createElement("img");
    confImg.src = confImg;
    divElement.appendChild(confImg);
    confImg.classList.add("confession-img");
  }

  //Adding like, comment and insta button
  var likeButton = document.createElement("Button");
  likeButton.innerHTML = confLikes + " " + `<i class="fa-regular fa-heart"></i>`;
  divElement.appendChild(likeButton);
  likeButton.classList.add("btn-conf");
  
  var commentButton = document.createElement("Button");
  commentButton.innerHTML = confComments + " " + `<i class="fa-regular fa-comment"></i>`;
  divElement.appendChild(commentButton);
  commentButton.classList.add("btn-conf")
  
  var instaButton = document.createElement("Button");
  instaButton.innerHTML = `<i class="fa-brands fa-instagram"></i>`;
  divElement.appendChild(instaButton);
  instaButton.classList.add("btn-conf");
  instaButton.setAttribute('id', 'conf-contact');
  
  //bottom div
  var bottomDiv = document.createElement("Div");
  bottomDiv.appendChild(likeButton);
  bottomDiv.appendChild(commentButton);
  bottomDiv.appendChild(instaButton);
  divElement.appendChild(bottomDiv);
  bottomDiv.classList.add("confession-bottom")
  
  // Appending the div element to body
  document.getElementById("main").appendChild(divElement);
}
