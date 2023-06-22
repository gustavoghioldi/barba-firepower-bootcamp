function calculate() { 
  const num1 = document.getElementById("num1").value;
  const num2 = document.getElementById("num2").value;
  const result = parseInt(num1) + parseInt(num2);
    alert(`Resultado: ${result}`);
}

function validate(bith, name, dni, gener) {
  let valid = [];
  // validaciones
  if (bith == "") {
    valid.push("dato bith no valido");
  }
  if (dni == "") {
    valid.push("dato dni no valido");
  }
  if (name == "") {
    valid.push("dato name no valido");
  }
  if (gener == null) {
    valid.push("dato gener no valido");
  }
  return valid;
}
function send() {
    // obtengo valores
  const bith = document.getElementById("bith").value;
  const name = document.getElementById("name").value;
  const dni = document.getElementById("dni").value;
  let gener = null;
  if (document.getElementById("male").checked == true) {
    gener = "male";
  }
  if (document.getElementById("female").checked == true) {
    gener = "female";
  }
  // valido los valores
  const is_valid = validate(bith, name, dni, gener);
  if (is_valid.length == 0) {
    alert(
      `nombre: ${name}, dni: ${dni}, nacimiento: ${bith}, genero: ${gener}`
    );
  } else {
    alert(is_valid);
  }
}

function change() {
  console.log("change!");
}
