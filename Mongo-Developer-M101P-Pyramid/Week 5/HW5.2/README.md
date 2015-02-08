<div><b>Crunching the Zipcode dataset</b><br>
Please calculate the average population of cities in California (abbreviation CA)  and New York (NY) (taken together) with populations over 25,000.
<br><br>
For this problem, assume that a city name that appears in more than one state represents two separate cities.
<br><br>
Please round the answer to a whole number.
<br>
Hint: The answer for CT and NJ (using this data set) is 38177. <br><br>Please note:<ul><li>Different states might have the same city name.</li><li>A city might have multiple zip codes.</li></ul><br><br>

For purposes of keeping the <em>Hands On</em> shell quick, we have used a subset of the data you previously used in zips.json, not the full set. This is why there are only 200 documents (and 200 zip codes), and all of them are in New York, Connecticut, New Jersey, and California.
<br><br>
If you prefer, you may download the handout and perform your analysis on your machine with
<pre>&gt; mongoimport -d test -c zips --drop small_zips.json
</pre><br>
Once you've generated your aggregation query and found your answer, select it from the choices below.
<br><br><span><form id="inputtype_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1" class="choicegroup capa_inputtype" __biza="WJ__"><fieldset><label for="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_0"><input type="radio" checked="" value="choice_0" id="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_0" name="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1"> 44805 </label><label for="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_1"><input type="radio" value="choice_1" id="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_1" name="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1"> 55921 </label><label for="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_2"><input type="radio" value="choice_2" id="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_2" name="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1"> 67935 </label><label for="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_3"><input type="radio" value="choice_3" id="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_3" name="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1"> 71819 </label><label for="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_4"><input type="radio" value="choice_4" id="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_4" name="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1"> 82426 </label><label for="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_5"><input type="radio" value="choice_5" id="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1_choice_5" name="input_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1"> 93777 </label><span id="answer_i4x-10gen-M101P-problem-52aa454be2d4232c54a18b38_2_1"></span></fieldset></form></span></div>
