<div><p>Install MongoDB on your computer and run it on the standard port.</p><p>Download the hw1-1.zip from Download Handout link and uncompress the file.</p><p>Change directory into hw1</p><p>Use mongorestore to restore the dump into your running mongod. Do this by opening a terminal window (mac) or cmd window (windows) and navigating to the directory so that the dump directory is directly beneath you. Now type:
</p><pre>mongorestore dump
</pre><p>Note you will need to have your path setup correctly to find mongorestore.</p><p>
Now, using the Mongo shell, perform a <code>findOne</code> on the collection called <code>hw1_1</code> in the database <code>m101</code>. That will return one document. Please provide the value corresponding to the "answer" key (without the surrounding quotes) from the document returned.
</p></div>
