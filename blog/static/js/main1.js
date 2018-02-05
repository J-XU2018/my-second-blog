function showmeg(){
  document.getElementById('my_store').innerHTML = 'Oops,not ready yet'
          }
function backmeg(){
  document.getElementById('my_store').innerHTML = 'My Store'
}

// or u can just put the script to the botton of base.html
var pageCounter = 1;
var animalContainer = document.getElementById('animal_info');
var btn = document.getElementById("btn");
if(btn){
    btn.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-'+ pageCounter +'.json')
    ourRequest.onload = function(){
      var ourData = JSON.parse(ourRequest.responseText);
      renderHTML(ourData);
    };
    ourRequest.send();
    pageCounter += 1;
    if(pageCounter > 4){
        animalContainer.innerHTML = '';
        pageCounter = 1;
      };

  });
}

function renderHTML(data){
  var htmlString ="";
  for (i = 0; i < data.length; i++){
    htmlString += "<p>" + data[i].name + "is a " + data[i].species + "."
      + "like to eat ";
      for (ii = 0; ii < data[i].foods.likes.length; ii++){
        if (ii ==0 ){
          htmlString += data[i].foods.likes[ii];
        }
        else{
          htmlString += " and " + data[i].foods.likes[ii];
        }
      }

  }
  htmlString += ".</p>";
  animalContainer.insertAdjacentHTML('beforeend',htmlString)
}
