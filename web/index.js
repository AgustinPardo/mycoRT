var cy = cytoscape({
  container: document.getElementById('cy'),

// initial viewport state:
// No funciona!
  //zoom: 50,
  //pan: { x: 1600, y: 1300 },
 

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
            'curve-style': 'bezier',
            'width': 3,
            'target-arrow-shape': 'triangle',
            'line-color': '#9dbaea',
            'target-arrow-color': '#9dbaea',
            'opacity':0.4          
        },       
    },
]
});


// Para hacer un boton (En construccion!!)
/*
cy.on('tap', 'node', function(evt){
	  var node = evt.target;
	  console.log( 'tapped ' + node.id() ); // Verificar node.tipoDeMotivo
	  document.getElementById("pruebita").innerHTML = node.id()
	});
*/

fetch('/red', {
	method: 'get'
}).then(function(response) {
	return response.json();
}).then(function(data) {
    cy.json(data)
    console.log(data)

}).catch(function(err) {
	console.log(err)
});
