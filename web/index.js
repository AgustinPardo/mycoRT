var cy = cytoscape({
  container: document.getElementById('cy'),

//Stilo del grafo
style: [
	{
		selector: 'node', style: 
		{
			'content':'data(shared_name)', //Nombres de los nodos
        	'background-color': '#df5f5f',
        	'border-color':'black',
        	'border-width': 5,
        	'opacity': 0.8,
        }
    },
	{
        selector: 'edge', 
        style: 
        {
            'width': 6,
            'line-color': '#14a926',
            'opacity': 0.2,
            'target-arrow-color': '#14a926',
            'target-arrow-shape': 'triangle',
            'arrow-scale': 10
        },       
    },
    {
        selector: ':parent',
        style: 
        {
         	'background-opacity': 0.6,
         	'background-color': '#e38080'
        }
    }
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

//Agrego los clusters de Operones, es decir motivos
/*
var eles = cy.add([
	{ data: { id: '3873039', parent: 'b' }},
    { data: { id: 'b' } },
    { data: { id: '3873198', parent: 'b' } },
    { data: { id: '1132850', parent: 'b' } },
    { data: { id: '1132110', parent:'e' }},
    { data: { id: '3873198', parent:'e' }},
    { data: { id: 'e' } },
    { data: { id: '1132143', parent: 'e' } }
]);
*/
//Request nodos y aristas//


//cy.json( cyJson )
fetch('/red', {
	method: 'get'
}).then(function(response) {
	return response.json();
}).then(function(data) {
    cy.json(data)
    console.log(data)


/*
	data.nodos.forEach( x =>{
		var eles = cy.add(
		//Cargo nodos con el id de Operon
		{group:"nodes", data:{ id: x.rv}})});

var i = 0;
	data.aristas.forEach(y =>{		
		
		i++;
	var eles = cy.add(
		//Cargo aristas con un nuevo id..
		{group: "edges", data:{ id: i.toString() , source:y.op1 , target: y.op2 }}
	)
});

*/

//

	
//Diseño del grafo
    //var layout = cy.layout(  { name: 'breadthfirst', circle: true, spacingFactor: 4.5,directed:true});
	//layout.run();
	
}).catch(function(err) {
	console.log(err)
});
