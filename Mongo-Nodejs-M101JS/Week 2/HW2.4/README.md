<li id="vert-0">
    <section data-type="MongoProc" class="xmodule_display xmodule_MongoProcModule">
    <h2 class="problem-header">Homework: Homework 2.3 (MongoProc Beta Version)</h2>
<section data-ajax-url="/courses/10gen/M101JS/2015_January/modx/i4x://10gen/M101JS/mongoproc/52dd0707e2d423744501cfbe" class="mongoproc">
  <b><i>Preface to Homework 2.3 (MongoProc Beta Version)</i></b><br><br>

This version of homework 2.3 uses an experimental homework validation program.
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
in the other version of homework 2.3. Please feel free to leave feedback
(positive or negative) about your experiences on the forum, or by emailing
education@mongodb.com.
<br><br><b><i>
        You only need to do <em>one</em> version of homework 2.3. If you
        complete it with MongoProc, don't do the manual validation version.
</i></b>
<br><br>

If you choose to do this version, you will need to download one of the
following versions of the MongoProc client, which will verify on your local
machine (port 8082) that the signup and login pages of the blog work properly.
<br><br><a href="https://education.mongodb.com/mongoproc">Download MongoProc</a>
<br><br><em>Blog User Sign-up and Login</em>
<br><br>

Download hw2-3.zip from the Download Handout link and uncompress it.
<br><br>

You should see four files in the 'blog' directory: app.js, users.js, posts.js
and sessions.js. There is also a 'views' directory which contains the templates
for the project and a 'routes' directory which contains our express routes.
<br><br>

If everything is working properly, you should be able to start the blog by
typing:
<br><pre>npm install
node app.js
</pre>
<br>

Note that this requires Node.js to be correctly installed on your computer.<br>
After you run the blog, you should see the message:
<br><pre>Express server listening on port 3000
</pre>
<br>

If you goto http://localhost:3000 you should see the front page of the blog.
Here are some URLs that must work when you are done.
<br><br>

http://localhost:3000/signup<br>
http://localhost:3000/login<br>
http://localhost:3000/logout<br><br>

When you login or sign-up, the blog will redirect to
http://localhost:3000/welcome and that must work properly, welcoming the user
by username.
<br><br>

We have removed parts of the code that uses the Node.js driver to query MongoDB
from users.js and marked the area where you need to work with "TODO: hw2.3".
You should not need to touch any other code. The database calls that you are
going to add will add a new user upon sign-up and validate a login by
retrieving the right user document.
<br><br>

The blog stores its data in the blog database in two collections, users and
sessions. Here are two example docs for a username ‘sverch’ with password
‘salty’. You can insert these if you like, but you don’t need to.
<br><pre>&gt; use blog
switched to db blog
&gt; db.users.find()
{ "_id" : "sverch", "password" : "$2a$10$wl4bNB/5CqwWx4bB66PoQ.lmYvxUHigM1ehljyWQBupen3uCcldoW" }
&gt; db.sessions.find()
{ "username" : "sverch", "_id" : "8d25917b27e4dc170d32491c6247aabba7598533" }
&gt;
</pre>

Once you have the the project working, the following steps should work:
<br><pre>go to http://localhost:3000/signup
create a user
</pre>
<br>

It should redirect you to the welcome page and say: welcome username, where
username is the user you signed up with. Now:
<br><pre>    Goto http://localhost:3000/logout
    Now login http://localhost:3000/login
</pre>
<br>

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
  <div class="mongoproc-status"><div class="status ">


</div>

<div class="action">
  <section class="submission_feedback">
    You have used 0 of 3 submissions.
  </section>
</div>
</div>
</section>

</section>

  </li>
