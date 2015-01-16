<div>We will use the pcat.products collection from week 1.  So start with that; if not already set up, import it:
<pre>mongoimport --db pcat -c products &lt; products.json
</pre>
You can find <a href="/static/10gen_2015_M102_January/handouts/products.3eb7cd1a9633.json">products.json</a> from the Download Handouts link.
In the shell, if you type:
<pre>db.products.count()
</pre>

should return 11.
<p>
Next, download <a href="/static/10gen_2015_M102_January/handouts/homework2.a51ae9e0ff0e.js">homework2.js</a> from the Download Handouts link.  Run the shell with this script:</p>
<pre>mongo --shell pcat homework2.js
</pre>

First, make a mini-backup of the collection before we start modifying it.  In the shell:

<pre>b = db.products_bak; db.products.find().forEach( function(o){ b.insert(o) } )
 // check it worked:
b.count()
// should print 11
</pre>

If you have any issues you can restore from "products_bak"; or, you can re-import with mongoimport.  (You would perhaps need in that situation to empty the collection first or drop it; see the --drop option on mongoimport --help.)

At the shell "&gt;" prompt type:
<pre>homework.a()
</pre>

What is the output? (The above will check that products_bak is populated.)<br></div>
