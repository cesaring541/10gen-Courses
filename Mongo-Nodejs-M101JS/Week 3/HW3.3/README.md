<div><h2 class="problem-header">
  Homework: Homework 3.2 (Manual Validation Version)
</h2>

<section class="problem"><div><b><i>Preface to Homework 3.2 (Manual Validation Version)</i></b><br>

There are two versions of homework 3.2. You only need to do one. This is the
version that previous students have used. It involves running a manual
validation script on your local machine in order to verify that your blog is
working, and so this version will include instructions on running that script.
<br><br><b><i>You only need to do <em>one</em> version of homework 3.2. Do not do this
    version if you've already done the MongoProc version.
</i></b>
<br><br>

If you choose to do this version, you will need to download the homework
packet, hw3-2and3-3.zip and hw_3-2validate.zip from the Download Handout link above, and unpack. hw3-2validate.zip will include a
<em>hw3-2validate.js</em> file that we will
use to verify on your local machine (port 8082) that the signup and login pages
of the blog work properly. You will not yet be building functionality for
displaying posts. Don't worry, that will come later.
<br><br><b>Making your blog accept posts</b>
<p>
In this homework you will be enhancing the blog project to insert entries into the posts collection. After this, the blog will have the basic functionality. It will allow you to add blog posts with a title, body and tags and have it be added to the posts collection properly.
</p>
<p>
We have provided the code that creates users and allows you to login (the assignment from last week). Download and unpack the files for this homework from the Download Handout link.
</p>
<p>
We have removed parts of the code that uses the Node.js driver to query MongoDB from posts.js and marked the area where you need to work for hw3.2 with "hw3.2 TODO". </p>
In a terminal: <br><br>
Linux/Mac:
<pre>cd blog/
grep -rn "hw3.2 TODO" *
</pre>
Windows:
<pre>cd blog/
find /n "hw3.2 TODO" *
</pre>
<p>You should not need to touch any other code. The database call that you are going to add will insert a new post into the posts collection.

Here is an example of valid blog post:
</p><pre>&gt; db.posts.find().pretty()
{
"_id" : ObjectId("513d396da0ee6e58987bae74"),
"title" : "Martians to use MongoDB",
"author" : "andrew",
"body" : "Representatives from the planet Mars announced today that the planet would adopt MongoDB as a planetary standard. Head Martian Flipblip said that MongoDB was the perfect tool to store the diversity of life that exists on Mars.",
"permalink" : "martians_to_use_mongodb",
"tags" : [
"martians",
"seti",
"nosql",
"worlddomination"
],
"comments" : [ ],
"date" : ISODate("2013-03-11T01:54:53.692Z")
}
</pre>


As a reminder, to run your blog you type:<br><pre>npm install
node app.js
</pre>

To play with the blog you can navigate to the following URLs:<br><pre>http://localhost:8082/
http://localhost:8082/signup
http://localhost:8082/login
http://localhost:8082/newpost
</pre>
Ok, now it’s time to validate you got the code for hw3-2 working. You can validate the blog using the validation script we've provided in the hw3-2validate directory. Just run the following commands:
<pre>cd hw3-2validate
npm install
node hw3-2validate.js
</pre>
For those who are using MongoHQ, MongoLab or want to run the webserver on a different host or port, there are some options to the validation script that can be exposed by running
<pre>node hw3-2validate.js --help</pre>
If you got it right, it will provide a validation code for you to enter into the box below. Enter just the code, no spaces. Note that your blog must be running when you run the validator.
</div>

  <section class="action"><input type="hidden" value="Homework: Homework 3.2 (Manual Validation Version)" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
