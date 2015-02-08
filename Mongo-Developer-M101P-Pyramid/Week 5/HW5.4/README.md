<div><h2 class="problem-header">
  Homework: Homework 5.4
</h2>

<section class="problem"><div><b>Removing Rural Residents</b><br>
In this problem you will calculate the number of people who live in a zip code in the US where the city starts with a digit. We will take that to mean they don't really live in a city.  Once again, you will be using the zip code collection, which you will find in the 'handouts' link in this page. Import it into your mongod using the following command from the command line:<br><pre>&gt; mongoimport -d test -c zips --drop zips.json
</pre><br>
If you imported it correctly, you can go to the <em>test</em> database in the mongo shell and conform that<br><pre>&gt; db.zips.count()
</pre><br>
yields 29,467 documents.
<br><br>
The project operator can extract the first digit from any field. For example, to extract the first digit from the city field, you could write this query:
<pre>db.zips.aggregate([
    {$project:
     {
	first_char: {$substr : ["$city",0,1]},
     }
   }
])
</pre>
Using the aggregation framework, calculate the sum total of people who are living in a zip code where the city starts with a digit. Choose the answer below.
<br><br><i>Note that you will need to probably change your projection to send more info through than just that first character. Also, you will need a filtering step to get rid of all documents where the city does not start with a digital (0-9).</i><span><form id="inputtype_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1" class="choicegroup capa_inputtype" __biza="WJ__"><fieldset><label for="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_0"><input type="radio" checked="" value="choice_0" id="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_0" name="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1"> 298015 </label><label for="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_1"><input type="radio" value="choice_1" id="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_1" name="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1"> 345232 </label><label for="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_2"><input type="radio" value="choice_2" id="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_2" name="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1"> 245987 </label><label for="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_3"><input type="radio" value="choice_3" id="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_3" name="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1"> 312893 </label><label for="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_4"><input type="radio" value="choice_4" id="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_4" name="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1"> 158249 </label><label for="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_5"><input type="radio" value="choice_5" id="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1_choice_5" name="input_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1"> 543282 </label><span id="answer_i4x-10gen-M101P-problem-52aa4639e2d4232c54a18b3e_2_1"></span></fieldset></form></span></div>

  </section></div>
