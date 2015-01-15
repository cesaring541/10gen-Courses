<div><h2 class="problem-header">
  Homework: Homework 2.1
</h2>

<section class="problem"><div>In this problem, you will be using a collection of student scores that is similar to what we used in the lessons. Please download grades.json from the Download Handout link and import it into your local mongo database as follows:
<pre>mongoimport -d students -c grades &lt; grades.json
</pre>
The dataset contains 4 scores for 200 students.
<p>
First, let’s confirm your data is intact; the number of documents should be 800.
</p>
<pre>&gt; use students
&gt; db.grades.count()
800
</pre>
<p>
This next query, which uses the aggregation framework that we have not taught yet, will tell you the <em>student_id</em> with the highest average score:
</p>

<pre>&gt; db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})
</pre>
<b><i>Note:  Aggregation requires <a target="_blank" href="http://www.mongodb.org/downloads">mongodb 2.2</a> or above.</i></b>

<p>
The answer, deep in the resulting document, should be <em>student_id</em> 164 with an average of approximately 89.3.
</p>

Now it’s your turn to analyze the data set. Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest.
<p>What is the <em>student_id</em> of the lowest exam score above 65?</p></div>

  </div>
