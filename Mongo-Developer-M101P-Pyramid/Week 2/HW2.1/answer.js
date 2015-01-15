 //use simple query
 db.grades.find({type:"exam",score:{$gte:65}}).sort({score:1}).limit(1)


 //use aggregate framework
db.grades.aggregate([{$project:{type:1,score:1,student_id:1}},
	{'$match':{type:"exam",score:{$gte:65},student_id:{$exists:true}}},{$sort:{score:1}},{$limit:4}])
