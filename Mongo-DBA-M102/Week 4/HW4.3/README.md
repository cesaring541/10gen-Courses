<div><h2 class="problem-header">
  Homework: Homework 4.3
</h2>

<section class="problem"><div><p>Now add two more members to the set.  Use the 2/ and 3/ directories we created in homework 4.1.  Run those two mongod’s on ports 27002 and 27003 respectively (the exact numbers could be different).</p><p>Remember to use the same replica set name as you used for the first member.</p><p>You will need to add these two new members to your replica set, which will initially have only one member. In the shell running on the first member, you can see your replica set status with</p><pre>&gt; rs.status()
</pre><p>Initially it will have just that first member. Connecting to the other members will involve using </p><pre>rs.add()</pre>. For example,<pre>&gt; rs.add("localhost:27002")
</pre><p>You'll know it's added when you see an </p><pre>{ "ok" : 1 }</pre> document. <p>Your machine may or may not be OK with 'localhost'. If it isn't, try using the name in the "members.name" field in the document you get by calling rs.status() (but remember to use the correct port!).</p><p>Once a secondary has spun up, you can connect to it with a new mongo shell instance. Use </p><pre>rs.slaveOk()</pre> to let the shell know you're OK with (potentially) stale data, and run some queries. You can also insert data on your primary and then read it out on your secondary.


Once the servers have sync'd with the primary and are caught up, run (on your primary):

<pre>&gt; homework.c()
</pre>

and enter the result below.<span><section class="textbox" id="textbox_i4x-10gen-M102-problem-538256818bb48b1135b71679_2_1"><div class="codeinput"><textarea id="input_i4x-10gen-M102-problem-538256818bb48b1135b71679_2_1" name="input_i4x-10gen-M102-problem-538256818bb48b1135b71679_2_1" cols="50" rows="4" style="display: none;">5</textarea><div class="CodeMirror cm-s-default CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 6.00006px; left: 22px;"><textarea style="position: absolute; padding: 0px; width: 1px; height: 1em; outline: medium none; font-size: 4px;" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 21px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="true"><div class="CodeMirror-sizer" style="margin-left: 21px; min-height: 26px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: medium none;"><div class="CodeMirror-measure"><pre><span>5</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div style="position: relative;"><div style="position: absolute; left: -21px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 12px;">1</div></div><pre>5</pre></div></div><div class="CodeMirror-cursor" style="left: 0px; top: 1px; height: 16px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 26px;"></div><div class="CodeMirror-gutters" style="height: 268px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 20px;"></div></div></div></div></div><div class="grader-status"><span id="status_i4x-10gen-M102-problem-538256818bb48b1135b71679_2_1" class="correct">Correct</span><p class="debug"></p></div><span id="answer_i4x-10gen-M102-problem-538256818bb48b1135b71679_2_1"></span><div class="external-grader-message">

  </div><script>
    // Note: We need to make the area follow the CodeMirror for this to work.
    $(function(){
      var cm = CodeMirror.fromTextArea(document.getElementById("input_i4x-10gen-M102-problem-538256818bb48b1135b71679_2_1"), {
        lineNumbers: true,
        mode: "python",
        matchBrackets: true,
        lineWrapping: true,
        indentUnit: "4",
        tabSize: "4",
        indentWithTabs: false,
        extraKeys: {
            "Tab": function(cm) {
                cm.replaceSelection("    ", "end");
            }
        },
        smartIndent: false
      });
    });
  </script></section></span></div>

  <section class="action"><input type="hidden" value="Homework: Homework 4.3" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
