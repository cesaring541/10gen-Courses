<div>Add a new product to the products collection of this form:
<pre>{
	"_id" : "ac9",
	"name" : "AC9 Phone",
	"brand" : "ACME",
	"type" : "phone",
	"price" : 333,
	"warranty_years" : 0.25,
	"available" : true
}
</pre>
Note: in general because of the automatic line continuation in the shell, you can cut/paste in the above and shouldn't have to type it all out.  Just enclose it in the proper statement(s) to get it added.

Next, load into a shell variable the object corresponding to
<pre>_id : ObjectId("507d95d5719dbef170f15c00")
</pre>
<ul><li>Then change <code>term_years</code> to 3 for that document. (And save that to the database.)</li><li>Then change <code>over_rate</code> for <code>sms</code> in <code>limits</code> to 0.01 from 0.  Save that too.</li></ul>
At the shell prompt type:
<pre>homework.b()
</pre>
What is the output?</div>
