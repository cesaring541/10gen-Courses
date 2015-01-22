<div><h2 class="problem-header">
  Homework: Homework 3.1
</h2>

<section class="problem"><div>Download the students.json file from the Download Handout link and import it into your local Mongo instance with this command:

<pre>$ mongoimport -d school -c students &lt; students.json
</pre>

<p>
This dataset holds the same type of data as last week's grade collection, but it's modeled differently. You might want to start by inspecting it in the Mongo shell.
</p><p>
Write a program in the language of your choice that will remove the lowest <em>homework</em> score for each student. Since there is a single document for each student containing an array of scores, you will need to update the scores array and remove the homework. </p>

<p>Remember, just remove a homework score. Don't remove a quiz or an exam!
</p><p>
Hint/spoiler: With the new schema, this problem is a lot harder and that is sort of the point. One way is to find the lowest homework in code and then update the scores array with the low homework pruned.
</p><p>
To confirm you are on the right track, here are some queries to run after you process the data with the correct answer shown:
</p><p>

Let us count the number of students we have:
</p>
<pre>&gt; use school
&gt; db.students.count()
200
</pre>

Let's see what Tamika Schildgen's record looks like:
<pre>&gt; db.students.find( { _id : 137 } ).pretty( )
{
	"_id" : 137,
	"name" : "Tamika Schildgen",
	"scores" : [
		{
			"type" : "exam",
			"score" : 4.433956226109692
		},
		{
			"type" : "quiz",
			"score" : 65.50313785402548
		},
		{
			"type" : "homework",
			"score" : 89.5950384993947
		}
	]
}
</pre>
<p>
To verify that you have completed this task correctly, provide the identity (in the form of their _id) of the student with the highest average in the class with following query that uses the aggregation framework. The answer will appear in the _id field of the resulting document.
</p>
<pre>&gt; db.students.aggregate( { '$unwind' : '$scores' } , { '$group' : { '_id' : '$_id' , 'average' : { $avg : '$scores.score' } } } , { '$sort' : { 'average' : -1 } } , { '$limit' : 1 } )
</pre>
</div>

  <section class="action"><input type="hidden" value="Homework: Homework 3.1" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
