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

function descargarUltimosPedidos(){
    return new Promise( resolve => {
        console.log('Descargando pedidos');

        setTimeout( () =>{
            resolve('Los pedidos fueron descargados');
        }, 3000);
    })
}

async function app(){
    try{
        // esto no es optimo, ya que se ejecutan en serie
     /*    const resultado = await descargarClientes();
        console.log(resultado);

        const resultado2 = await descargarUltimosPedidos();
        console.log(resultado2); */
        // Promise.all nos permite ejecutar multiples promesas al mismo tiempo
        const resultado = await Promise.all([descargarClientes(), descargarUltimosPedidos()]);
        console.log(resultado[0]);
        console.log(resultado[1]);
    

    }catch(error){
        console.log(error);
    }
}

app();