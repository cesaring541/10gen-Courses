<div id="seq_content"><section data-type="None" class="xmodule_display xmodule_VerticalModule">
    <ol class="vert-mod">
  <li id="vert-0">
    <section data-type="Problem" class="xmodule_display xmodule_CapaModule">
    <section data-url="/courses/10gen/M101P/2015_January/modx/i4x://10gen/M101P/problem/52cf2a25e2d423570a05b92e" data-problem-id="i4x://10gen/M101P/problem/52cf2a25e2d423570a05b92e" class="problems-wrapper" id="problem_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e" progress="done"><div><h2 class="problem-header">
  Homework: Homework 4.4
</h2>

<section class="problem"><div><p>In this problem you will analyze a profile log taken from a mongoDB instance. To start, please download sysprofile.json from Download Handout link and import it with the following command:</p><pre>mongoimport -d m101 -c profile &lt; sysprofile.json
</pre><p>Now query the profile data, looking for all queries to the <i>students</i> collection in the database <i>school2</i>, sorted in order of decreasing latency. What is the latency of the longest running operation to the collection, in milliseconds?</p><span><form id="inputtype_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1" class="choicegroup capa_inputtype" __biza="WJ__"><fieldset><label for="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_0"><input type="radio" value="choice_0" id="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_0" name="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1"> 19776550 </label><label for="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_1"><input type="radio" value="choice_1" id="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_1" name="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1"> 10000000 </label><label for="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_2"><input type="radio" value="choice_2" id="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_2" name="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1"> 5580001 </label><label for="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_3"><input type="radio" checked="" value="choice_3" id="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_3" name="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1"> 15820 </label><label for="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_4"><input type="radio" value="choice_4" id="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1_choice_4" name="input_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1"> 2350 </label><span id="answer_i4x-10gen-M101P-problem-52cf2a25e2d423570a05b92e_2_1"></span></fieldset></form></span></div>

  <section class="action"><input type="hidden" value="Homework: Homework 4.4" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div></section>

</section>

  </li>
</ol>

</section>
</div>
