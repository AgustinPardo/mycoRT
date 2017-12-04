var cy = cytoscape({
  container: document.getElementById('cy'),
//Estilo del grafo
style: [
	{
		selector: 'node', style: 
		{
			//'content':'data(shared_name)', //Nombres de los nodos
        	'background-color': '#df5f5f',
        	'border-color':'black',
            'width':30,
            'height':30,
        	'border-width': 5,
        	'opacity': 0.8,
        }
    },
	{
        selector: 'edge', style: 
        {
            //'curve-style': 'bezier',
            'width': 20,
            'target-arrow-shape': 'triangle',
            'line-color': '#9dbaea',
            'target-arrow-color': '#9dbaea',
            'opacity': 0.1          
        }
    },
    {	// Nodo seleccionado
       selector: 'node:selected', style:
       {
        'background-color': '#df5f5f',        
        'opacity': 0.5,
        'width':80,
        'height':80
    	}
    },
    {	
       selector: 'edge:selected', style:
       {
        'background-color': '#9dbaea',        
        'opacity': 1,
        'width': 10
    	}
    }	
]
});

// function arreglo_coma_espacio(entrada){
//     var salida ="";
//     for (i=0; i<entrada.length; i++){
//         salida=salida+entrada[i][0]+" ";
//     }
//     return salida     
// }

function pintarNodos(target,color){

    var nodos=target;
    var entradaCy='';
    var relleno=''

    if (nodos.length>0) {

        for (var i = 0; i < nodos.length; i++) {
            var nodo=nodos[i];
            relleno='node[name="'+nodo+'"]';
            entradaCy=relleno+','+entradaCy;               
        }

        console.log(relleno);
        console.log(entradaCy);
        entradaCy = entradaCy.substring(0, entradaCy.length - 1)
        
        cy.$(entradaCy).style({'background-color': color,        
                                            'opacity': 0.5,
                                            'width':80,
                                            'height':80});
    }  
}

fetch('/red', {
	method: 'get'
    }).then(function(response) {
	   return response.json();
    }).then(function(data) {
        cy.json(data)
	   cy.fit()
    }).catch(function(err) {
	   console.log(err)
});

cy.on('tap', 'node', function(evt){

    $('.collapse').collapse("hide");

	var node = evt.target;	
  
	document.getElementById("mostrar_nombre_operon").innerHTML = node.data("name");

    fetch('/operon/'+ node.data("name"),{
        method: 'get'
        }).then(function(response) {
            return response.json();
        }).then(function(data) { 
            document.getElementById("mostrar_locus_de_operon").innerHTML = data['locus'].length;
            document.getElementById("mostrar_regula_de_operon").innerHTML = data['regula'].length;
            document.getElementById("mostrar_reguladoPor_de_operon").innerHTML = data['reguladoPor'].length;
            document.getElementById("mostrar_motivos_de_operon").innerHTML = data['motivos'].length;
           
            //Resetear los colores.
            // Pinto los operones regolados Por
            pintarNodos(data["reguladoPor"],"yellow")
            pintarNodos(data["regula"],"green")           

            // Tabla locus
            var data_tabla_locus=data["locus"]
            $( document ).ready(function() {
            $('#tabla_locus').DataTable( {
                destroy:true,
                data: data_tabla_locus,
                columns: [
                    { title: "locus" },                              
                        ]
                });
            });

            // Tabla Regula
            var data_tabla_regula=data["regula"]
            $( document ).ready(function() {
            $('#tabla_regula').DataTable( {
                destroy:true,
                data: data_tabla_regula,
                columns: [
                    { title: "Regula" },                              
                        ]
                });
            });

            // Tabla Regulado por

            var data_tabla_reguladoPor=data["reguladoPor"]
            $( document ).ready(function() {
            $('#tabla_reguladoPor').DataTable( {
                destroy:true,
                data: data_tabla_reguladoPor,
                columns: [
                    { title: "Regulado por" },                              
                        ]
                });
            });

            // Tabla motivos
            var data_tabla_motivos=data["motivos"]
            $( document ).ready(function() {
            $('#tabla_motivos').DataTable( {
                destroy:true,
                data: data_tabla_motivos,
                columns: [
                    { title: "A" },
                    { title: "B" },
                    { title: "C" },
                    { title: "Typo" },
                    { title: "Id" }           
                        ]
                });
            });
        });        			
});


function resetFunction() {
	cy.fit();
 
}

