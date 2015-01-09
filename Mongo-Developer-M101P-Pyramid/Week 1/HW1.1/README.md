<div>Install MongoDB on your computer and run it on the standard port.

<p>
Download the HW1-1 from the Download Handout link and uncompress it.
</p>
Use mongorestore to restore the dump into your running mongod. Do this by opening a terminal window (mac) or cmd window (windows) and navigating to the directory so that you are in the parent directory of the dump directory (if you used the default extraction method, it should be hw1/). Now type
<pre>mongorestore dump
</pre>
<p>
Note you will need to have your path setup correctly to find mongorestore.
</p>
<p>
Next, go into the Mongo shell, perform a findOne on the collection called <em>hw1</em> in the database <em>m101</em>. That will return one document. Please provide the value corresponding to the "answer" key from the document returned.
</p></div>
