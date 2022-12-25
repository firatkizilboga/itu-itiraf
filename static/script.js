let url = `http://localhost:8000/api/confessions`;

/*
let confTitle = document.getElementById("confession-title");
let confBody = document.getElementById("confession-info");
let confDate = document.getElementById("confession-date");
let confLikes = document.getElementById("likes");
let confComments = document.getElementById("confessions");
*/

async function getData() {
  const response = await fetch(url); // buraya api adresini yaz
  const data = await response.json(); // datayla ne yapılacaksa yap

  console.log(data);
  console.log(data.length);
  /*
  confTitle.innerHTML = data[1].title;
  confDate.innerHTML = data[1].date.toString().split('T')[0];
  confBody.innerHTML = data[1].body;
  confLikes.innerHTML = data[1].likes + " " + '<i class="fa-regular fa-heart"></i>';
  confComments.innerHTML = data[1].comments + " " + '<i class="fa-regular fa-comment"></i>';
  */

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

function createConfessionDiv(confTitle, confDate, confBody, confLikes, confComments) {
    // Creating a div element
  var divElement = document.createElement("Div");
  divElement.id = "divID";

  // Styling it
  
  divElement.style.backgroundColor = "#f5f8fe";
  divElement.style.border = "1px solid #062a54";
  divElement.style.borderRadius = "10px";
  divElement.style.padding = "10px";
  divElement.style.height = "160px";
  divElement.style.width = "310px";
  divElement.style.position = "relative";
  divElement.style.margin = "50px";


  //Adding Title
  var confTitlee = document.createElement("H3");
  confTitlee.innerHTML = confTitle;
  divElement.appendChild(confTitlee);

  //Adding Date
  var confDatee = document.createElement("P");
  confDatee.innerHTML = confDate;
  divElement.appendChild(confDatee);

    confDatee.style.marginLeft = "16rem";
    confDatee.style.fontWeight = "lighter";

  //adding header div

  var confHeader = document.createElement("Div");
  confHeader.appendChild(confTitlee);
  confHeader.appendChild(confDatee);
  divElement.appendChild(confHeader);

  confHeader.style.display = "flex";
  confHeader.style.borderBottom = "1px solid #062a54";
  

  // Adding a paragraph to it
  var confInfo = document.createElement("P");
  var confInfoTextext = document.createTextNode(confBody);
  confInfo.appendChild(confInfoTextext);
  divElement.appendChild(confInfo);

  confInfo.style.fontWeight =  "normal";
  confInfo.style.paddingLeft = "15px";

  //Adding like and comment button
  var likeButton = document.createElement("Button");
  likeButton.innerHTML = confLikes + " " + `<i class="fa-regular fa-heart"></i>`;
  divElement.appendChild(likeButton);

  likeButton.style.width = "60px";
  likeButton.style.height = "30px";
  likeButton.style.border = "1px solid #062a54"
  likeButton.style.borderRadius = "10px";
  likeButton.style.backgroundColor = "#fbfbfd";
  likeButton.style.color = "#25292f";
  likeButton.style.marginRight = "4px";
  likeButton.style.transition = "0.4s";

  var commentButton = document.createElement("Button");
  commentButton.innerHTML = confComments + " " + `<i class="fa-regular fa-comment"></i>`;
  divElement.appendChild(commentButton);

  commentButton.style.width = "60px";
  commentButton.style.height = "30px";
  commentButton.style.border = "1px solid #062a54"
  commentButton.style.borderRadius = "10px";
  commentButton.style.backgroundColor = "#fbfbfd";
  commentButton.style.color = "#25292f";
  commentButton.style.marginRight = "4px";
  commentButton.style.transition = "0.4s";

  var instaButton = document.createElement("Button");
  instaButton.innerHTML = `<i class="fa-brands fa-instagram"></i>`;
  divElement.appendChild(instaButton);

  instaButton.style.width = "60px";
  instaButton.style.height = "30px";
  instaButton.style.border = "1px solid #062a54"
  instaButton.style.borderRadius = "10px";
  instaButton.style.backgroundColor = "#fbfbfd";
  instaButton.style.color = "#25292f";
  instaButton.style.marginRight = "4px";
  instaButton.style.transition = "0.4s";
  instaButton.style.float = "right";

  //bottom div

  var bottomDiv = document.createElement("Div");
  bottomDiv.appendChild(likeButton);
  bottomDiv.appendChild(commentButton);
  bottomDiv.appendChild(instaButton);
  divElement.appendChild(bottomDiv);

  bottomDiv.style.borderTop = "1px solid #062a54";
  bottomDiv.style.position = "relative";
  bottomDiv.style.marginTop = "50px";
  bottomDiv.style.padding = "10px";
  
  // Appending the div element to body
  document.getElementById("main").appendChild(divElement);
}
