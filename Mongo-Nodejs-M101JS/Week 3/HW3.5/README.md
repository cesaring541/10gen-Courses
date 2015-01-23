<div><h2 class="problem-header">
  Homework: Homework 3.3 (Manual Validation Version)
</h2>

<section class="problem"><div><b><i>Preface to Homework 3.3 (Manual Validation Version)</i></b><br>

There are two versions of homework 3.3. You only need to do one. This is the
version that previous students have used. It involves running a manual
validation script on your local machine in order to verify that your blog is
working, and so this version will include instructions on running that script.
<br><br><b><i>You only need to do <em>one</em> version of homework 3.3. Do not do this
    version if you've already done the MongoProc version.
</i></b>
<br><br>

If you choose to do this version, you will need to download the homework
packet, hw3-2and3-3.zip from the Download Handout link above, and unpack. You
will also need the hw3-3validate.zip. This will include a
<em>hw3-3validate.js</em> file that we will use to
verify on your local machine (port 8082) that the signup and login pages of the
blog work properly. You will not yet be building functionality for displaying
posts. Don't worry, that will come later.
<br><br><b>Making your blog accept comments</b>
<p>
In this homework  you will add code to your blog so that it accepts comments. Download and unpack the files for this homework from the Download Handout link. You will also be using the same code as you downloaded for homework 3.2.<br><br>
We have removed parts of the code that uses the Node.js driver to query MongoDB from posts.js and marked the area where you need to work for HW 3.3 with "hw3.3 TODO".
</p>

In a terminal: <br><br>
Linux/Mac:
<pre>cd blog/
grep -rn "hw3.3 TODO" *
</pre>
Windows:
<pre>cd blog/
find /n "hw3.3 TODO" *
</pre>

<p>
You should not need to touch any other code. The database call that you are going to add will add a new comment to a given post.
</p>

<p>
This assignment has fairly little code, but it's a little more subtle than the previous assignment because you are going to be manipulating an array within the Mongo document.  For the sake of clarity, here is a document out of the posts collection from a working project that also has comments.
</p>

<pre>{
"_id" : ObjectId("513d396da0ee6e58987bae74"),
"author" : "andrew",
"body" : "Representatives from the planet Mars announced today that the planet would adopt MongoDB as a planetary standard. Head Martian Flipblip said that MongoDB was the perfect tool to store the diversity of life that exists on Mars.",
"comments" : [
{
"author" : "Larry Ellison",
"body" : "While I am deeply disappointed that Mars won't be standardizing on a relational database, I understand their desire to adopt a more modern technology for the red planet.",
"email" : "larry@oracle.com"
},
{
"author" : "Salvatore Sanfilippo",
"body" : "This make no sense to me. Redis would have worked fine."
}
],
"date" : ISODate("2013-03-11T01:54:53.692Z"),
"permalink" : "martians_to_use_mongodb",
"tags" : [
"martians",
"seti",
"nosql",
"worlddomination"
],
"title" : "Martians to use MongoDB"
}
</pre>

<p>
Note that you add comments in this blog from the blog post detail page, which appears at

</p><pre>http://localhost:8082/post/post_slug
</pre>

where post_slug is the permalink. For the sake of eliminating doubt, the permalink for the example blog post above is <pre>http://localhost:8082/post/martians_to_use_mongodb</pre>



<p>
You will run <code>hw3-3validate.js</code> to check your work, much like the last homework. <code>hw3-3validate.js</code> will run through, check to make sure it can add blog comments and will print out a 3.3 validation code that you should enter below.
</p>

Once again, you can validate the blog using the validation script we've provided in the 'hw3-3validate' directory. Just run the following commands:

<pre>cd hw3-3validate
npm install
node hw3-3validate.js
</pre>

For those who are using MongoHQ, MongoLab or want to run the webserver on a different host or port,
there are some options to the validation script that can be exposed by running

<pre>node hw3-3validate.js --help
</pre>

If you got it right, it will provide a validation code for you to enter into the box below. Enter just the code, no spaces. Note that your blog must be running when you run the validator.
</div>

  <section class="action"><input type="hidden" value="Homework: Homework 3.3 (Manual Validation Version)" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
