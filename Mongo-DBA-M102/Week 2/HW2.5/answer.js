db.products.ensureIndex({for:1});
var d = db.products.find({},{for:1});
d.forEach(function(data){
	if(data.for && (data.for.indexOf("ac3")>=0)){
		db.products.update(data,{$set:{price:2}});
	}
});
