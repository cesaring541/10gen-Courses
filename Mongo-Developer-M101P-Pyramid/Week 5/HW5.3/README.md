<div><h2 class="problem-header">
  Homework: Homework 5.3 (Hands On)
</h2>

<section class="problem"><div><b>Who's the easiest grader on campus?</b><br>
A set of grades are loaded into the <em>grades</em> collection.
<br><br>
The documents look like this:
<pre>{
	"_id" : ObjectId("50b59cd75bed76f46522c392"),
	"student_id" : 10,
	"class_id" : 5,
	"scores" : [
		{
			"type" : "exam",
			"score" : 69.17634380939022
		},
		{
			"type" : "quiz",
			"score" : 61.20182926719762
		},
		{
			"type" : "homework",
			"score" : 73.3293624199466
		},
		{
			"type" : "homework",
			"score" : 15.206314042622903
		},
		{
			"type" : "homework",
			"score" : 36.75297723087603
		},
		{
			"type" : "homework",
			"score" : 64.42913107330241
		}
	]
}
</pre>
There are documents for each student (student_id) across a variety of classes (class_id). Note that not all students in the same class have the same exact number of assessments. Some students have three homework assignments, etc.
<br><br>
Your task is to calculate the class with the best average student performance. This involves calculating an average for each student in each class of all non-quiz assessments and then averaging those numbers to get a class average. To be clear, each student's average includes only exams and homework grades. <b>Don't include their quiz scores in the calculation.</b>
<br><br>
What is the class_id which has the highest average student perfomance?
<br><br>Hint/Strategy: You need to group twice to solve this problem. You must figure out the GPA that each student has achieved in a class and then average those numbers to get  a class average. After that, you just need to sort. The class with the lowest average is the class with class_id=2. Those students achieved a class average of 37.6
<br><br>
If you prefer, you may download the handout and perform your analysis on your machine with
<pre>&gt; mongoimport -d test -c grades --drop grades.json
</pre><br>
Below, choose the class_id with the highest average student average.
<span><form id="inputtype_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1" class="choicegroup capa_inputtype" __biza="WJ__"><div class="indicator_container"><span id="status_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1" style="display:inline-block;" class="unanswered"></span></div><fieldset><label for="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_0"><input type="radio" value="choice_0" id="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_0" name="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1"> 8 </label><label for="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_1"><input type="radio" value="choice_1" id="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_1" name="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1"> 9 </label><label for="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_2"><input type="radio" value="choice_2" id="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_2" name="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1"> 1 </label><label for="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_3"><input type="radio" value="choice_3" id="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_3" name="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1"> 5 </label><label for="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_4"><input type="radio" value="choice_4" id="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_4" name="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1"> 7 </label><label for="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_5"><input type="radio" value="choice_5" id="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_5" name="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1"> 0 </label><label for="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_6"><input type="radio" value="choice_6" id="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1_choice_6" name="input_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1"> 6 </label><span id="answer_i4x-10gen-M101P-problem-52aa45e5e2d4232c54a18b3b_2_1"></span></fieldset></form></span></div>

  </section></div>
