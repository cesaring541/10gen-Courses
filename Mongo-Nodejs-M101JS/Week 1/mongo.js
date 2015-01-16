var mongo = require('mongodb');
var express = require('express'),
	app = express(),
	cons = require('consolidate'),
	MongoClient = require('mongodb').MongoClient,
	Server = require('mongodb').Server;

var mongo = new MongoClient(new Server('localhost',27017,{native_parser:true}));
var db = mongo.db('students');

app.engine('html',cons.swig);
app.set('view engine','html');
app.set('views',__dirname + '/views');

app.get('/',function(req,res){
	db.collection('grades').findOne({},function(err,doc){
		if(err) throw err;
		res.send(doc);
	});
	// res.send("Hello");
});

app.get('/:name',function(req,res){
	console.log(req.params);
	var name = req.params.name;
	res.render('name',{'name':name});
});
app.get('*',function(req,res){
	res.send("page not found");
});
// app.listen(8000);
// 	console.log('server run at 0.0.0.0:8000');
mongo.open(function(err,mongoclient){
	if(err) throw err;
	app.listen(8000);
	console.log('server run at 0.0.0.0:8000');
});

// mongo.connect('mongodb://127.0.0.1:27017/students',function(err,db){
// 	if(err)
// 		throw err;
// 	db.collection('grades').find({},function(err,doc){
// 		if (err) throw err;
// 		debugger;
// 		db.close();
// 	});

// 	console.dir("start");
// });
