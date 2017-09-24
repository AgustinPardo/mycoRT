var cy = cytoscape({
  container: document.getElementById('cy')
});

//Request//
fetch('/red', {
	method: 'get'
}).then(function(response) {
	return response.json();
}).then(function(data) {
	
	data.nodos.forEach( x =>{
		console.log(x.rv)
		var eles = cy.add([
		{group:"nodes", data:{ id: x.rv}}])});

	data.aristas.forEach(y =>{		
	var eles = cy.add([
			{group: "edges", data:{ id: "s", source:y.op1 , target: y.op2 }}])}
		);

	var layout = cy.layout( { name: 'grid'} );
	layout.run();
	
}).catch(function(err) {
	console.log(err)
});






