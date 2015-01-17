var mongoclient = require('mongodb');

mongoclient.connect('mongodb://localhost:27017/weather',function(err,db){
	if(err) throw err;

	var query = {"Wind Direction":{'$lt':360,'$gt':180}};
	var options = {'sort':[['Temperature',1]]};
	var projection = {'State':1};
	db.collection('data').find(query,projection,options,function(err,docs){
		if(err) throw err;
		var count = false;
		docs.each(function(err,doc){
			if(err) throw err;
			if(!count){
				console.log('result is ' + doc.State);
				count = true;
			}
			if(doc == null){
				return db.close();
			}
		});

	});
});
