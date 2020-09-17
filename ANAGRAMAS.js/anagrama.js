
//ejercicio 2 del Test

let cadena=' java script es un lenguaje de programación. La versión mas reciente de javascript es del año 2016. Javascript es un lenguaje de interpretado que corre en el navegador';

function contarOcurrencias(cadena, subcadena){
let contadorOcurrencias = 0;
let posición = 0;

while((posición = cadena.toLowerCase(subcadena, posición)) !== -1){
++contadorOcurrencias;

posición += subcadena.length;
}
return  contadorOcurrencias;
}

console.log(contarOcurrencias(cadena, 'Javascript'))
