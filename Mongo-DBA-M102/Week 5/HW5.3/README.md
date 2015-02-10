<div><p>At the beginning of the section, "W Timeout and Capacity Planning", Dwight mentioned something that hasn't yet been touched upon in this class: Batch Inserts.</p><p>He mentions that you can find information on them in the docs, but he hasn't used them in the shell during this course.</p><p>Your job is to look this functionality up in the documentation, and use it for the following problem:</p><p>Please insert into the <em>m102</em> collection, the following 3 documents, using only one shell query (please use double quotes around each key in each document in your answer):</p><ul><li>{ "a" : 1 }</li><li>{ "b" : 2 }</li><li>{ "c" : 3 }</li></ul><p><em>Hints: This is not the same as the Bulk() operations, which were discussed earlier in this course. Also, this does not involve semicolons, so don't put any into the text box. You probably want to test this on your machine, and then copy and paste the insert query in the box below. Do not include the &gt; sign from the beginning of the shell.</em></p><span><section class="textbox" id="textbox_i4x-10gen-M102-problem-538d51ad8bb48b3debc2db25_2_1"><div class="codeinput"><textarea id="input_i4x-10gen-M102-problem-538d51ad8bb48b3debc2db25_2_1" name="input_i4x-10gen-M102-problem-538d51ad8bb48b3debc2db25_2_1" cols="50" rows="4" style="display: none;"></textarea><div class="CodeMirror cm-s-default CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 6px; left: 22px;"><textarea style="position: absolute; padding: 0px; width: 1px; height: 1em; outline: medium none; font-size: 4px;" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 21px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="true"><div class="CodeMirror-sizer" style="margin-left: 21px; min-height: 26px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: medium none;"><div class="CodeMirror-measure"><pre><span>&#8203;</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div style="position: relative;"><div style="position: absolute; left: -21px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 12px;">1</div></div><pre>&nbsp;</pre></div></div><div class="CodeMirror-cursor" style="left: 0px; top: 1px; height: 16px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 26px;"></div><div class="CodeMirror-gutters" style="height: 268px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 20px;"></div></div></div></div></div><div class="grader-status"><span id="status_i4x-10gen-M102-problem-538d51ad8bb48b3debc2db25_2_1" style="display:inline-block;" class="unanswered">Unanswered</span><p class="debug"></p></div><span id="answer_i4x-10gen-M102-problem-538d51ad8bb48b3debc2db25_2_1"></span><div class="external-grader-message">

  </div><script>
    // Note: We need to make the area follow the CodeMirror for this to work.
    $(function(){
      var cm = CodeMirror.fromTextArea(document.getElementById("input_i4x-10gen-M102-problem-538d51ad8bb48b3debc2db25_2_1"), {
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
