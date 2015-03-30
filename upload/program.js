var http = require('http');

var responses = {};

responses[process.argv[2]] = '';
responses[process.argv[3]] = '';
responses[process.argv[4]] = '';

var printAll = function(){
	console.log(responses[process.argv[2]]);
	console.log(responses[process.argv[3]]);
	console.log(responses[process.argv[4]]);
}

http.get(process.argv[2], function(response){
	var request = process.argv[2];
	response.setEncoding('utf8');
	var string = '';
	response.on("data", function(data){
		string += data;
	});
	response.on('end', function(data){
		responses[request] = string;
		if(responses[process.argv[2]] != '' && responses[process.argv[3]] != '' && responses[process.argv[4]] != ''){
			printAll();
		}
	});
});

http.get(process.argv[3], function(response){
	var request = process.argv[3];
	response.setEncoding('utf8');
	var string = '';
	response.on("data", function(data){
		string += data;
	});
	response.on('end', function(data){
		responses[request] = string;
		if(responses[0] && responses[process.argv[3]] && responses[process.argv[4]]){
			printAll();
		}
	});
});

http.get(process.argv[4], function(response){
	var request = process.argv[4];
	response.setEncoding('utf8');
	var string = '';
	response.on("data", function(data){
		string += data;
	});
	response.on('end', function(data){
		responses[request] = string;
		if(responses[0] && responses[process.argv[3]] && responses[process.argv[4]]){
			printAll();
		}
	});
});