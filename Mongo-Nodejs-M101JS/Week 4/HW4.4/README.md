<section data-type="Problem" class="xmodule_display xmodule_CapaModule">
    <section data-url="/courses/10gen/M101JS/2015_January/modx/i4x://10gen/M101JS/problem/52e93d6be2d42365b944fce0" data-problem-id="i4x://10gen/M101JS/problem/52e93d6be2d42365b944fce0" class="problems-wrapper" id="problem_i4x-10gen-M101JS-problem-52e93d6be2d42365b944fce0" progress="done"><div><h2 class="problem-header">
  Homework: Homework 4.3 (Manual Validation Version)
</h2>

<section class="problem"><div><b><i>Preface to Homework 4.3 (Manual Validation Version)</i></b><br>

There are two versions of homework 4.3. You only need to do one. This is the
version that previous students have used. It involves running a manual
validation script on your local machine in order to verify that your blog is
working, and so this version will include instructions on running that script.
<br><br><b><i>You only need to do <em>one</em> version of homework 4.3. Do not do this
    version if you've already done the MongoProc version.
</i></b>
<br><br>

If you choose to do this version, you will need to download the homework
packet, hw4-3.zip, from the Download Handout link above, and unpack.
This will include a <em>hw4-3_validate.js</em> file in the validate/ directory
that we will use to verify on your local machine (port 8082) that the blog post
software is working properly.
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
Once you have added the indexes to make those pages fast, run the following commands to validate your project just like in previous homeworks.
</p>
<pre>cd validate
npm install
node hw4-3_validate.js
</pre>
For those who are using MongoHQ or MongoLab, or just want to run MongoDB on a different host and port, there are some options to the validation script that can be exposed by running:
<pre>node hw4-3_validate.js --help
</pre>
<p>If you got it right, it will provide a validation code for you to enter into the box below. Enter just the code, no spaces. </p>
<p>Note that your blog does NOT need to be running when you run the validator, but your database server does. </p></div>

  <section class="action"><input type="hidden" value="Homework: Homework 4.3 (Manual Validation Version)" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div></section>

</section>
