function showmeg(){
  document.getElementById('my_store').innerHTML = 'Oops,not ready yet'
          }
function backmeg(){
  document.getElementById('my_store').innerHTML = 'My Store'
}


var weatherContainer = document.getElementById('weather');
var weather_icon = document.getElementById('weather_icon');
// var btn = document.getElementById("btn");
// if(btn){
    // btn.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', 'https://api.apixu.com/v1/current.json?key=0630cbfbf6b541768f633447180502&q=Auckland')
    ourRequest.onload = function(){
      var ourData = JSON.parse(ourRequest.responseText);
      // console.log(ourRequest.responseText)
      renderHTML(ourData);
    };
    ourRequest.send();


  // });
// }

function renderHTML(data){
  var htmlString ="";
  var location = data.location.name;
  var temp_c = data.current.temp_c;
  var conditon = data.current.condition.text;
  var icon = data.current.condition.icon;
  htmlString = "<p>" + location + "<br> " + data.location.localtime + "<br> Current: " + temp_c + "C<br>" + conditon + ".</p>";
  weatherContainer.insertAdjacentHTML('beforeend',htmlString)
  weather_icon.src = icon;

}
