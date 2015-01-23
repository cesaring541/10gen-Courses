<section data-ajax-url="/courses/10gen/M101JS/2015_January/modx/i4x://10gen/M101JS/mongoproc/52e6c595e2d423298bce84a4" class="mongoproc">
  <b><i>Preface to Homework 3.3 (MongoProc Beta Version)</i></b><br><br>

This version of homework 3.3 uses an experimental homework validation program.
Previously, we've used manual validation scripts to verify homework answers.
Every term, a number of students have had issues setting up the script.
This version of the MongoProc validation program is an attempt to work
around these issues.
<br><br>

If you have any difficulty using MongoProc, here are
<a target="_blank" href="http://www.youtube.com/playlist?list=PL4RCxklHWZ9vb8rR55iKEffkY-5GhCGvC"><b>2 video lectures</b></a>
showing how to set it up.
<br><br>

Furthermore, you still have the option of using the manual validation scripts
in the other version of homework 3.3. Please feel free to leave feedback
(positive or negative) about your experiences on the forum, or by emailing
education@mongodb.com.
<br><br><b><i>
        You only need to do <em>one</em> version of homework 3.3. If you
        complete it with MongoProc, don't do the manual validation version.
</i></b>
<br><br>

If you choose to do this version, you will need to download one of the
following versions of the MongoProc client, which will verify on your local
machine (port 8082) that the signup and login pages of the blog work properly.
<br><br><a href="https://education.mongodb.com/mongoproc">Download MongoProc</a>
<br><br><b>Making your blog accept comments</b>
<p>
In this homework  you will add code to your blog so that it accepts comments. Download and unpack the files for this homework from the Download Handout link. You will be using the same code as you downloaded for homework 3.2, along with the changes you made.<br><br>
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

As a reminder, to run your blog, go into the blog directory and type:<br><pre>npm install
node app.js
</pre>

<p>
Note that you add comments in this blog from the blog post detail page, which appears at

</p><pre>http://localhost:8082/post/post_slug
</pre>

where post_slug is the permalink. For the sake of eliminating doubt, the permalink for the example blog post above is <pre>http://localhost:8082/post/martians_to_use_mongodb</pre>



Ok, now it’s time to validate you got it all working.
<br><br>

From the top of this page, there was one additional program that should have
been downloaded: <i>mongoProc</i>.
<br><br>

With it, you can test your code and look at the Feedback section. When it says
"user creation successful" and "user login successful", you can
<em>Turn in</em> your assignment.
<br><br>

You will see a message below about your number of submissions, but you must
submit this assignment using MongoProc.


</section>
