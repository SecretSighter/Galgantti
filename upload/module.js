module.exports = function(dir, extension, callback){
	var fs = require('fs');
	var path = require('path');

	fs.readdir(dir, function(err, data){
		if(err){
			return callback(err);			
		} else {
			buf = data;
			var lastData = [];
			//console.log(buf);
			for(var i = 0; i < buf.length; i++){
				//console.log(path.extname(buf[i]));
				if(path.extname(buf[i]) == '.'+extension){
					console.log(buf[i]);
					lastData.push(buf[i]);
				}
			}
			callback(null, lastData);

		}

	});
};

