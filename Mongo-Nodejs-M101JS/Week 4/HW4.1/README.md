<div>Suppose you have a collection with the following indexes:
<pre>&gt; db.products.getIndexes()
[
	{
		"v" : 1,
		"key" : {
			"_id" : 1
		},
		"ns" : "store.products",
		"name" : "_id_"
	},
	{
		"v" : 1,
		"key" : {
			"sku" : 1
		},
                "unique" : true,
		"ns" : "store.products",
		"name" : "sku_1"
	},
	{
		"v" : 1,
		"key" : {
			"price" : -1
		},
		"ns" : "store.products",
		"name" : "price_-1"
	},
	{
		"v" : 1,
		"key" : {
			"description" : 1
		},
		"ns" : "store.products",
		"name" : "description_1"
	},
	{
		"v" : 1,
		"key" : {
			"category" : 1,
			"brand" : 1
		},
		"ns" : "store.products",
		"name" : "category_1_brand_1"
	},
	{
		"v" : 1,
		"key" : {
			"reviews.author" : 1
		},
		"ns" : "store.products",
		"name" : "reviews.author_1"
	}
</pre>
Which of the following queries can utilize an index. Check all that apply.<span><form id="inputtype_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1" class="choicegroup capa_inputtype" __biza="WJ__"><fieldset><label for="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1_choice_0"><input type="checkbox" value="choice_0" id="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1_choice_0" name="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1[]"> db.products.find({'brand':"GE"}) </label><label for="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1_choice_1"><input type="checkbox" checked="" value="choice_1" id="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1_choice_1" name="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1[]"> db.products.find({'brand':"GE"}).sort({price:1}) </label><label for="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1_choice_2"><input type="checkbox" checked="" value="choice_2" id="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1_choice_2" name="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1[]"> db.products.find({$and:[{price:{$gt:30}},{price:{$lt:50}}]}).sort({brand:1}) </label><label for="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1_choice_3"><input type="checkbox" value="choice_3" id="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1_choice_3" name="input_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1[]"> db.products.find({brand:'GE'}).sort({category:1, brand:-1}).explain() </label><span id="answer_i4x-10gen-M101P-problem-52aa2fbbe2d4232c54a18acb_2_1"></span></fieldset></form></span></div>
