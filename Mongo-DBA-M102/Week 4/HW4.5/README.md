<div><h2 class="problem-header">
  Homework: Homework 4.5
</h2>

<section class="problem"><div><p>Note our replica set now has an even number of members, and that is not a best practice.  However, to keep the homework from getting too long we’ll leave it at that for now, and instead do one more exercise below involving the <i>oplog</i>.  </p><p><i>To get the right answer on this problem, you must perform the homework questions in order. Otherwise, your oplog may look different than we expect.</i></p><p>Go to the secondary in the replica set. The shell should say SECONDARY at the prompt if you've done everything correctly.</p><p>Switch to the <em>local</em> database and then look at the oplog:</p><pre>&gt; db.oplog.rs.find()
</pre><p>If you get a blank result, you are not on the right database.</p><p>Note: as the local database doesn’t replicate, it will let you query it without entering “rs.slaveOk()” first.</p><p>Next look at the stats on the oplog to get a feel for its size:</p><pre>&gt; db.oplog.rs.stats()
</pre><p>What result does this expression give when evaluated?</p><pre>db.oplog.rs.find().sort({$natural:1}).limit(1).next().o.msg[0]
</pre><span><section class="textbox" id="textbox_i4x-10gen-M102-problem-53825eb48bb48b1135b7167e_2_1"><div class="codeinput"><textarea id="input_i4x-10gen-M102-problem-53825eb48bb48b1135b7167e_2_1" name="input_i4x-10gen-M102-problem-53825eb48bb48b1135b7167e_2_1" cols="50" rows="4" style="display: none;">R</textarea><div class="CodeMirror cm-s-default CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 6px; left: 22px;"><textarea style="position: absolute; padding: 0px; width: 1px; height: 1em; outline: medium none; font-size: 4px;" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 21px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="true"><div class="CodeMirror-sizer" style="margin-left: 21px; min-height: 26px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: medium none;"><div class="CodeMirror-measure"><pre><span>R</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div style="position: relative;"><div style="position: absolute; left: -21px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 12px;">1</div></div><pre>R</pre></div></div><div class="CodeMirror-cursor" style="left: 0px; top: 1px; height: 16px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 26px;"></div><div class="CodeMirror-gutters" style="height: 268px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 20px;"></div></div></div></div></div><div class="grader-status"><span id="status_i4x-10gen-M102-problem-53825eb48bb48b1135b7167e_2_1" class="correct">Correct</span><p class="debug"></p></div><span id="answer_i4x-10gen-M102-problem-53825eb48bb48b1135b7167e_2_1"></span><div class="external-grader-message">

  </div><script>
    // Note: We need to make the area follow the CodeMirror for this to work.
    $(function(){
      var cm = CodeMirror.fromTextArea(document.getElementById("input_i4x-10gen-M102-problem-53825eb48bb48b1135b7167e_2_1"), {
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

  <section class="action"><input type="hidden" value="Homework: Homework 4.5" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
