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
            'width': 3,
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


// Variables globales
var click_on_motive = false;

//

function arreglo_coma_espacio(entrada){
    var salida ="";
    for (i=0; i<entrada.length; i++){
        salida=salida+entrada[i][0]+" ";
    }
    return salida     
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


    if(click_on_motive==true){$("#mostrar_motivos_de_operon").click()};

    $("#mostrar_motivos_de_operon").empty();
    $("#data_motivos").empty();

 
	var node = evt.target;		
	document.getElementById("mostrar_nombre_operon").innerHTML = node.data("name");

    fetch('/operon/'+ node.data("name"),{
        method: 'get'
        }).then(function(response) {
            return response.json();
        }).then(function(data) { 
            document.getElementById("mostrar_locus_de_operon").innerHTML = arreglo_coma_espacio(data['locus']);
            document.getElementById("mostrar_regula_de_operon").innerHTML = arreglo_coma_espacio(data['regula']);
            document.getElementById("mostrar_reguladoPor_de_operon").innerHTML = arreglo_coma_espacio(data['reguladoPor']);
            document.getElementById("mostrar_motivos_de_operon").innerHTML = data['motivos'].length;
        });        			
});


function resetFunction() {
	cy.fit();
    // Agregar que se deje de deseleccionar
    if(click_on_motive==true){$("#mostrar_motivos_de_operon").click()};
    $("#mostrar_motivos_de_operon").empty();
    $("#data_motivos").empty();
}

function dataMotivos(){

    click_on_motive=true;

    if ($("#data_motivos").html().length == 0)
    {
        var texto=("<table class=\"table\">" + 
        "<tbody><tr><td>Data</td><td>Data2</td><td>Data2</td></tr>")
        $("#data_motivos").html(texto);
    } 
    else {
    $("#mostrar_motivos_de_operon").click();
    click_on_motive=false;
    }    
}
