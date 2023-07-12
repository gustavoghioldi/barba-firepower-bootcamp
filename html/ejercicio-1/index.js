function calculator(n1, n2, op) {
  let rta = false;
  switch (op) {
    case "sumar":
      rta = n1 + n2;
      break;
    case "restar":
      rta = n1 - n2;
      break;

    case "multiplicar":
      rta = n1 * n2;
      break;

    case "dividir":
      rta = n1 / n2;
      break;

    default:
      break;
  }
  return rta;
}

const calcu = () => {
  const num_1 = parseFloat(document.getElementById("number1").value);
  const num_2 = parseFloat(document.getElementById("number2").value);
  const op = document.querySelector('input[name="calcula"]:checked').id;

  const rta = calculator(num_1, num_2, op);
  document.getElementById("rta").innerHTML = rta;
};
