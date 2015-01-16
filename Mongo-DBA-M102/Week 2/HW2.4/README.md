<div>Create an index on the field <code>for</code>.

You might want to first run the following to get some context on what is present in that field in the documents of our collection:
<pre>db.products.find({},{for:1})
</pre>

After creating the index, query products that work with an "ac3" phone; that is, "ac3" is present in the product's "for" field.
<ul><li>Q1: How many are there?</li><li>Q2: Run an explain plan on the above query.  How many records were scanned? </li><li>Q3: Was an index used?</li></ul></div>
