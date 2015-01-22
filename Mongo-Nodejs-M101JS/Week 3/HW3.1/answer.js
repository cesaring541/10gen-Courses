var mongo = require('mongodb');

mongo.connect('mongodb://localhost:27017/school',function(err,db){
	if (err) throw err;

	_students = db.collection('students');

	_students.aggregate([
			{ '$unwind' : '$scores' },
			{'$match':{'scores.type':'homework'}},
			{"$group": {"_id": "$_id", "min": {"$min": '$scores.score'}}}
		],function(err,result){

			if (err) throw err;
			result.forEach(function(data){
				query = {'_id':data._id};
				_update = {'$scores.type':'homework','$pull':{'$score.score':data.min}};
				_students.update(query,_update,function(err,doc){
					console.dir('updated ' + doc );
				})
			});
			_students.aggregate([
						{'$unwind':'$scores'},
						{'$group':{'_id':'$_id','avg':{'$avg':'$scores.score'}}},
						{'$sort':{'avg':-1}},
						{'$limit':1}
					],function(err,result){
						console.dir("students has max avg score id :" + result.pop()._id);
						db.close();

			});
			}
	);

});
