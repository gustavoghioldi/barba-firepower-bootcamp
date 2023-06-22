function f1 () {
    let arr = ["1", 1, true, null, 1.2,  [1, 2, 2, [1, 1]]]
    document.write(`largo ${arr.length}<br>`);
    arr.push("allgo");
    document.write(`largo ${arr.length}<br>`);
    arr.pop()
    arr.pop()
    document.write(`largo ${arr.length}<br>`);
    document.write(`posicion 3: ${arr[3]}<br>`);
    document.write(`posicion 0: ${arr[0]}<br>`);
    document.write(`posicion 4: ${arr[4]}<br>`);

    for (const index in arr) {
        console.log(arr[index]);
    }

    // let i = 0
    // while (i < arr.length) {
    //     console.log(arr[i]);
    //     i++;
    // }

    // for (let index = 0; index < arr.length; index++) {
    //     const element = arr[index];
    //     console.log(element);
    // }

    // esto necesito que lo entiendan si o si
    const matrix = [[1, 0, 0], [1, 1, 0], [0,0,0]]
    for (const key in matrix) {
        console.log(matrix[key]);
        for (const keyInternal in matrix[key]) {
            console.log(matrix[key][keyInternal]);
        }
        
    }
}

function f2 () {
    let arr = [1, 2, 3, 2, 3, 3, 3, 3, 1, 1, 1, 0, 0, 0,0 ];
    arr.shift(); // elimina el primer elemento
    arr.unshift(100); //inserta en la posicion 0
    document.write(arr+"<br>"); 
    arr[1] = "HOLA";
    document.write(arr+"<br>"); 
    //delete arr[1];
    document.write(arr+"<br>"); 
    document.write(arr.length+"<br>"); 
    document.write(arr.sort()+"<br>"); 
    document.write(arr.reverse()+"<br>"); 
    document.write(arr.splice(1,4)+"<br>"); // cambia el vector
    document.write(arr.slice(1,4)+"<br>"); // devuelve el valor (que es otro vector) sin cambiar el vector 
    document.write(arr.join("-")+"<br>");
    document.write(arr.concat(1, 2, 3, 3, 4, 4,4 ,44, 4, 4, 4)+"<br>");
}
f1();
f2();
