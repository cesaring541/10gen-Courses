<div>Download the file <a href="/static/10gen_2015_M102_January/handouts/products.3eb7cd1a9633.json">products.json</a> from education.mongodb.com.
Take a look at its content.<br><br>
Now, import its contents into MongoDB, into a database called "pcat" and a collection called "products".  Use the mongoimport utility to do this.<br><br>
When done, run this query in the mongo shell:
<pre>db.products.find({type:"case"}).count()
</pre>
What's the result?<span></span></div>
