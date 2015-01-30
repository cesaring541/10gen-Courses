var mongo = require('mongodb')

mongo.connect('mongodb://localhost:27017/m101',function(err,db){
	var profile = db.collection('profile');

	var _query = {'ns':/school2/i};
	var _sort = {'millis':-1};
	var cursor = profile.find(_query);
	cursor = cursor.sort(_sort);
	cursor.nextObject(function(err,obj){
		console.log("The latency of the longest running operation to the collection " + obj.millis + " ms ");
		return db.close();
	});

});
