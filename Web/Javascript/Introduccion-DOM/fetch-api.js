// Fetch api es un nuevo estándar de javascript que permite hacer peticiones http de manera asíncrona. Es una mejora de XMLHttpRequest.

// Podemos obtener un archivo local o respuesta de un servidor en formato json o texto

// Utiliza como toda las API de javascript promises o async/await



// function obtenerEmpleado(){
//     // si necesitamos sacar info de una url ponemos la url ejemplo https://google.com
//     const archivo = "empleado.json"
//     fetch(archivo)
//     .then(resultado => {
//         return resultado.json();
//     })
//     .then(datos => {
//         // console.log(datos);
//         // una mejor forma es crear un destructuring
//         // el destructuring nos permite extraer múltiples elementos de un objeto/array y asignarlos a variables individuales
//         const { empleados } = datos;

//         empleados.forEach( empleados =>{
//             console.log("ID: ",empleados.id);
//             console.log("Nombre: ",empleados.nombre);
//             console.log("Puesto: ",empleados.puesto);
//         })
//     })
// }



// ahora con async/await
async function obtenerEmpleado(){
    const archivo = "empleado.json"

    // al hacer con await, se reduce el código y se hace más legible
    const resultado = await fetch(archivo);
    const datos = await resultado.json();
    console.log(datos);
}

obtenerEmpleado();