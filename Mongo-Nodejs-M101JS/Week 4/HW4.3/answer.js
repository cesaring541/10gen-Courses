var mongo = require('mongodb')

mongo.connect('mongodb://localhost:27017/blog',function(err,db){
	if(err) throw err;
	var _data = [
			{"date":-1},
			{"permalink":1},
			{"tags":1},
			{"tags":1,"date":-1},
		];
	var callback = function(err,info){
		console.log('create index ' + info);
		_data.pop();
		if(_data.length == 0){
			db.close();
		}
	};
	db.collection('posts',function(err,doc){
		if(err) throw err;
		for(var _index in _data){
			doc.ensureIndex(_data[_index],callback);
		}
		// doc.ensureIndex({"date":-1},callback);
		// doc.ensureIndex("permalink",callback);
		// doc.ensureIndex("tags",callback);
		// doc.ensureIndex({"tags":1,"date":-1},callback);

	});

})
