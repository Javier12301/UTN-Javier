// Asyn y Await

// Podemos crear una función por ejemlo que nos permita crear descargar clientes, y nuestro sistema seguira funcionando hasta que se descarguen todos los clientes.

// Función para simular la descarga de clientes
function descargarClientes(){
    // Devolvemos una nueva promesa
    return new Promise( resolve => {
        // Imprimimos un mensaje en la consola
        console.log('Descargando clientes...');
        
        // Usamos setTimeout para simular la demora en la descarga de clientes
        setTimeout( () =>{
            // Resolvemos la promesa después de 5 segundos
            resolve('Los clientes fueron descargados');
        }, 5000); // 5 segundos
    });
}

// Función asíncrona para manejar la descarga de clientes
async function app(){
    try{
        // Esperamos a que se resuelva la promesa de descargarClientes
        const resultado = await descargarClientes();
        // Imprimimos el resultado en la consola
        console.log(resultado);
    }catch(error){
        // Si hay un error, lo capturamos y lo imprimimos en la consola
        console.log(error);
    }
}

// Función para contar segundos
function contarSegundos(numero){
    // Recorremos desde 0 hasta el número dado
    for(let i = 0; i < numero; i++){
        // Imprimimos el número actual en la consola
        console.log(i);
    }
}

// Llamamos a la función asíncrona app
app();
// Llamamos a la función contarSegundos
contarSegundos(5);
