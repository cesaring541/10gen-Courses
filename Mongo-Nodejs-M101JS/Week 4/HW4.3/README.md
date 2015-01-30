<div id="seq_content"><section data-type="None" class="xmodule_display xmodule_VerticalModule">
    <ol class="vert-mod">
  <li id="vert-0">
    <section data-type="MongoProc" class="xmodule_display xmodule_MongoProcModule">
    <h2 class="problem-header">Homework: Homework 4.3 (MongoProc Beta Version)</h2>
<section data-ajax-url="/courses/10gen/M101JS/2015_January/modx/i4x://10gen/M101JS/mongoproc/52e93ecde2d42365b944fce2" class="mongoproc">
  <b><i>Preface to Homework 4.3 (MongoProc Beta Version)</i></b><br><br>

This version of homework 4.3 uses an experimental homework validation program.
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
in the other version of homework 4.3. Please feel free to leave feedback
(positive or negative) about your experiences on the forum, or by emailing
education@mongodb.com.
<br><br><b><i>
        You only need to do <em>one</em> version of homework 4.3. If you
        complete it with MongoProc, don't do the manual validation version.
</i></b>
<br><br>

If you choose to do this version, you will need to download one of the
following versions of the MongoProc client, which will verify on your local
machine (port 8082) that the signup and login pages of the blog work properly.
<br><br><a href="https://education.mongodb.com/mongoproc">Download MongoProc</a>
<br><br><b>Making the Blog fast</b>
<p>To get started, please download hw4-3.zip from the Download Handout link and unpack file to your computer. This assignment requires Mongo 2.2 or above. </p>

<p>In this homework assignment you will be adding some indexes to the post collection to make the blog fast.</p>

<p>We have provided the full code for the blog application and you don't need to make any changes, or even run the blog. But you can, for fun.</p>

<p>We are also providing a patriotic (if you are an American) data set for the blog. There are 1000 entries with lots of comments and tags. You must load this dataset to complete the problem.</p>
<pre># from the mongo shell
use blog
db.posts.drop()
# from the a mac or PC terminal window
mongoimport -d blog -c posts &lt; posts.json
</pre>
<p>
The blog has been enhanced so that it can also display the top 10 most recent posts by tag. There are hyperlinks from the post tags to the page that displays the 10 most recent blog entries for that tag. (run the blog and it will be obvious)
</p><p>
Your assignment is to make the following blog pages fast:
</p>
<ul><li>The blog home page</li><li>The page that displays blog posts by tag (http://localhost:8082/tag/whatever)</li><li>The page that displays a blog entry by permalink (http://localhost:8082/post/permalink)</li></ul><p>By fast, we mean that indexes should be in place to satisfy these queries such that we only need to scan the number of documents we are going to return.
</p><p>
To figure out what queries you need to optimize,  you can read the code in posts.js and see what queries it is doing to return the data needed for the relevant pages. Isolate those queries and use explain to explore.
</p><p>
Once you have added the indexes to make those pages fast, just validate your work with MongoProc.
</p>
  <div class="mongoproc-status"><div class="status ">


</div>


</div>
</section>

</section>

  </li>
</ol>

</section>
</div>
