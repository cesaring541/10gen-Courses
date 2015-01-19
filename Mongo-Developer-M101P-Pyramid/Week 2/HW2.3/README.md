<div><em>Blog User Sign-up and Login</em><p>
Download hw2-3.zip or hw2-3.tar and unpack.
</p><p>
You should see three files at the highest level: <i>blog.py</i>, <i>userDAO.py</i> and <i>sessionDAO.py</i>. There is also a views directory which contains the templates for the project.
</p><p>
The project roughly follows the model/view/controller paradigm. <i>userDAO</i> and <i>sessionDAO.py</i> comprise the model. <i>blog.py</i> is the controller.  The templates comprise the view.
</p><p>
If everything is working properly, you should be able to start the blog by typing:
</p><pre>python blog.py
</pre><p>
Note that this project requires the following python modules be installed on your computer: cgi, hmac, re, datetime, random, json, sys, string, hashlib, bson, urllib, urllib2, random, re, pymongo, and bottle. A typical Python installation will already have most of these installed except <i>pymongo</i> and <i>bottle</i>.
</p><p>
If you have python-setuptools installed, the command "easy_install" makes this simple.  Any other missing packages will show up when <i>validate.py</i> is run, and can be installed in a similar fashion.
</p><pre>$ easy_install pymongo bottle
</pre><p>
If you goto <a href="http://localhost:8082/">http://localhost:8082</a> you should see a message “this is a placeholder for the blog”
</p><p>
Here are some URLs that must work when you are done.
</p><pre>http://localhost:8082/signup
http://localhost:8082/login
http://localhost:8082/logout
</pre><p>
When you login or sign-up, the blog will redirect to
http://localhost:8082/welcome
and that must work properly, welcoming the user by username
</p><p>
We have removed two pymongo statements from userDAO.py and marked the area where you need to work with XXX. You should not need to touch any other code.  The pymongo statements that you are going to add will add a new user upon sign-up and validate a login by retrieving the right user document.
</p><p>
The blog stores its data in the blog database in two collections, <i>users</i> and <i>sessions</i>.  Here are two example docs for a username ‘erlichson’ with password ‘fubar’. You can insert these if you like, but you don’t need to.
</p><pre>&gt; db.users.find()
{ "_id" : "erlichson", "password" : "d3caddd3699ef6f990d4d53337ed645a3804fac56207d1b0fa44544db1d6c5de,YCRvW" }
&gt;
&gt; db.sessions.find()
{ "_id" : "wwBfyRDgywSqeFKeQMPqVHPizaWqdlQJ", "username" : "erlichson" }&gt;
</pre><p>
Once you have the the project working, the following steps should work:
</p><ul><li>go to http://localhost:8082/signup</li><li>create a user</li></ul>
It should redirect you to the welcome page and say: welcome username, where username is the user you signed up with.  Now
<ul><li>Goto http://localhost:8082/logout</li><li>Now login http://localhost:8082/login.</li></ul><br><p>
Ok, now it’s time to validate you got it all working.
</p>
<p>
There was one additional program that should have been downloaded in the project called <i>validate.py</i>.
</p>
<pre>python validate.py
</pre>
<p>
For those who are using MongoHQ, MongoLab or want to run the webserver on a different host or port, there are some options to the validation script that can be exposed by running
</p>
<pre>python validate.py -help
</pre>
<p>
If you got it right, it will provide a validation code for you to enter into the box below. Enter just the code, no spaces. Note that your blog must be running when you run the validator.
</p></div>
