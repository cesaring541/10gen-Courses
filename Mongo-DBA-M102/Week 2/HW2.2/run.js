load('../HW2.1/homework2.js');
var data = {
	"_id" : "ac9",
	"name" : "AC9 Phone",
	"brand" : "ACME",
	"type" : "phone",
	"price" : 333,
	"warranty_years" : 0.25,
	"available" : true
};

db.products.insert(data);

var _item = { _id : ObjectId("507d95d5719dbef170f15c00") };
db.products.update(_item,{$inc:{'term_years':1},$set:{"limits.sms.over_rate":0.01}},true);
homework.b()
