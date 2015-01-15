var _data = db.grades.aggregate([{$match:{$and:[{type:'homework'}]}},
	{'$group':{'_id':'$student_id', 'min_score':{$min:'$score'}}}]);

_data.forEach(function(data){
	db.grades.remove({student_id:data._id,score:data.min_score})}
});

var _answer = db.grades.aggregate({'$group':{'_id':'$student_id', 'average':
	{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1});
print(_answer._id);
