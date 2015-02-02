<div><h2 class="problem-header">
  Homework: Homework 4.4
</h2>

<section class="problem"><div><p>We will now remove the first member (@ port 27001) from the set.</p><p>As a first step to doing this we will shut it down.  (Given the rest of the set can maintain a majority, we can still do a majority reconfiguration if it is down.)</p><p>We could simply terminate its mongod process, but if we use the replSetStepDown command, the failover may be faster.  That is a good practice, though not essential.  Connect to member 1 (port 27001) in the shell and run:</p><pre>&gt; rs.stepDown()
</pre><p>Then cleanly terminate the mongod process for member 1.</p><p>Next, go to the new primary of the set. You will probably need to connect with the mongo shell, which you'll want to run with '--shell replication.js' since we'll be getting the homework solution from there.  Once you are connected, run rs.status() to check that things are as you expect.  Then reconfigure to remove member 1.  </p><p><i>Tip: You can either use rs.reconfig() with your new configuration that does not contain the first member, or rs.remove(), specifying the host:port of the server you wish to remove as a string for the input.</i></p><p>When done, run</p><pre>&gt; homework.d()
</pre><p>and enter the result.</p><p><i>Tip: If you ran the shell without replication.js on the command line, restart the shell with it.</i></p><span><section class="textbox" id="textbox_i4x-10gen-M102-problem-53825a298bb48b1135b7167c_2_1"><div class="codeinput"><textarea id="input_i4x-10gen-M102-problem-53825a298bb48b1135b7167c_2_1" name="input_i4x-10gen-M102-problem-53825a298bb48b1135b7167c_2_1" cols="50" rows="4" style="display: none;">6</textarea><div class="CodeMirror cm-s-default CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 6px; left: 22px;"><textarea style="position: absolute; padding: 0px; width: 1px; height: 1em; outline: medium none; font-size: 4px;" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 21px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="true"><div class="CodeMirror-sizer" style="margin-left: 21px; min-height: 26px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: medium none;"><div class="CodeMirror-measure"><pre><span>6</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div style="position: relative;"><div style="position: absolute; left: -21px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 12px;">1</div></div><pre>6</pre></div></div><div class="CodeMirror-cursor" style="left: 0px; top: 1px; height: 16px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 26px;"></div><div class="CodeMirror-gutters" style="height: 268px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 20px;"></div></div></div></div></div><div class="grader-status"><span id="status_i4x-10gen-M102-problem-53825a298bb48b1135b7167c_2_1" class="correct">Correct</span><p class="debug"></p></div><span id="answer_i4x-10gen-M102-problem-53825a298bb48b1135b7167c_2_1"></span><div class="external-grader-message">

  </div><script>
    // Note: We need to make the area follow the CodeMirror for this to work.
    $(function(){
      var cm = CodeMirror.fromTextArea(document.getElementById("input_i4x-10gen-M102-problem-53825a298bb48b1135b7167c_2_1"), {
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

  <section class="action"><input type="hidden" value="Homework: Homework 4.4" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
