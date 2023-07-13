const calcular = function () {
    n1 = parseInt(document.getElementById("n1").value);
    n2 = parseInt(document.getElementById("n2").value);
    n3 = parseInt(document.getElementById("n3").value);

    let rta = [];
    for (i = n1; n2>i; i=i+n3) {
        rta.push(i);
    }

    document.write(rta);
}