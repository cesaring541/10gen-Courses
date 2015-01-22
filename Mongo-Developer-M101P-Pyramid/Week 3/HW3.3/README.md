<div><h2 class="problem-header">
  Homework: Homework 3.3
</h2>

<section class="problem"><div><b>Making your blog accept comments</b><p>
In this homework  you will add code to your blog so that it accepts comments. You will be using the same code as you downloaded for HW 3.2.
</p><p>
Once again, the area where you need to work is marked with an XXX in the blogPostDAO.py file. There are one location. You don't need to figure out how to retrieve comments for this homework because the code you did in 3.2 already pulls the entire blog post (unless you specifically projected to eliminate the comments) and we gave you the code that pulls them out of the JSON document.
</p><p>
This assignment has fairly little code, but it's a little more subtle than the previous assignment because you are going to be manipulating an array within the Mongo document.  For the sake of clarity, here is a document out of the posts collection from a working project.
</p><pre>{
	"_id" : ObjectId("509df76fbcf1bf5b27b4a23e"),
	"author" : "erlichson",
	"body" : "This is a blog entry",
	"comments" : [
		{
			"body" : "This is my comment",
			"author" : "Andrew Erlichson"
		},
		{
			"body" : "Give me liberty or give me death.",
			"author" : "Patrick Henry"
		}
	],
	"date" : ISODate("2012-11-10T06:42:55.733Z"),
	"permalink" : "This_is_a_blog_post_title",
	"tags" : [
		"cycling",
		"running",
		"swimming"
	],
	"title" : "This is a blog post title"
}
</pre><p>
Note that you add comments in this blog from the blog post detail page, which appears at
</p><pre>http://localhost:8082/post/post_slug
</pre>
where post_slug is the permalink. For the sake of eliminating doubt, the permalink for the example blog post above is http://localhost:8082/post/This_is_a_blog_post_title
<p>
You will run validation.py to check your work, much like the last problem. Validation.py will run through and check the requirements of HW 3.2 and then will check to make sure it can add blog comments, as required by this problem, HW 3.3. It checks the web output as well as the database documents.
</p><pre>python validate.py
</pre><p>
Once you have the validation code, please copy and paste in the box below, no spaces.
</p></div>

  <section class="action"><input type="hidden" value="Homework: Homework 3.3" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
