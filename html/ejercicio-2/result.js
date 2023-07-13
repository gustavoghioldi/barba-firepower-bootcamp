const urlParams = new URLSearchParams(window.location.search);

function calulateAge(birthdate) {
  const today = new Date();
  // A bool that represents if today's day/month precedes the birth day/month
  const one_or_zero = (today.getMonth() < birthdate.getMonth()) ||
                      (today.getMonth() === birthdate.getMonth() &&
                       today.getDate() < birthdate.getDate());
  
  // Calculate the difference in years from the date object's components
  let year_difference = today.getFullYear() - birthdate.getFullYear();
  
  // The difference in years is not enough. 
  // To get it right, subtract 1 or 0 based on if today precedes the 
  // birthdate's month/day.
  // To do this, subtract the 'one_or_zero' boolean from 'year_difference'
  // (This converts true to 1 and false to 0 under the hood.)
  const age = year_difference - one_or_zero;
  
  return age;
}
document.getElementById("name").innerHTML =  urlParams.get("name");
document.getElementById("surName").innerHTML =  urlParams.get("sur_name");
document.getElementById("dni").innerHTML =  urlParams.get("dni");
document.getElementById("gener").innerHTML =  urlParams.get("gener");
document.getElementById("bio").innerHTML =  urlParams.get("bio");

//document.getElementById("age").innerHTML =  urlParams.get("birth");
let conocimientos = [];

for (i of urlParams) {
    if (i[0] == "conocimientos") {
        conocimientos.push(i[1]);
    }
}
const bithArray  = urlParams.get("birth").split("-")
const age = calulateAge(new Date(bithArray[0], bithArray[1], bithArray[2] ));

document.getElementById("age").innerHTML = age.toString()
document.getElementById("know").innerHTML = conocimientos.toString()
