var mongo = require('mongodb');

mongo.connect('mongodb://localhost:27017/weather',function(err,db){
	if(err) throw err;
	var query = [{'$group': {'_id':'$State','Temp':{'$max':'$Temperature'}}}]
	db.collection('data').aggregate(query,function(err,docs){

		docs.forEach(function(elem,index){
			var q = {'State':elem._id,'Temperature':elem.Temp};
			var update = {'$set':{"month_high":true}};
			db.collection('data').update(q,update,{'upsert':true},function(err,success){
				console.log('update');
			});
			if(index == docs.length-1)
				return db.close();
		});
	});

})
