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
            'curve-style': 'bezier',
            'width': 3,
            'target-arrow-shape': 'triangle',
            'line-color': '#9dbaea',
            'target-arrow-color': '#9dbaea',
            'opacity':0.1          
        },       
    },
]
});

// Para hacer un boton (En construccion!!)

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
		var node = evt.target;
		console.log('tapped ' + node.id());
		console.log(node.data);
		document.getElementById("mostrar_nombre_operon").innerHTML = node.data("name")
});

function resetFunction() {
	cy.fit();
}