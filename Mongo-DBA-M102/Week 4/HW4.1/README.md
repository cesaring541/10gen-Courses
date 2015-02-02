<div><h2 class="problem-header">
  Homework: Homework 4.1
</h2>

<section class="problem"><div><p>In this chapter’s homework we will create a replica set and add some data to it.</p><p>1. Unpack replication.js from the Download Handout zip file.</p><p>2. We will create a three member replica set.  Pick a root working directory to work in.  Go to that directory in a console window.  </p><p>Given we will have three members in the set, and three mongod processes, create three data directories: </p><pre>mkdir 1
mkdir 2
mkdir 3
</pre><p>3. We will now start a single mongod as a standalone server.  Given we will have three mongod processes on our single test server, we will explicitly specify the port numbers (this wouldn’t be necessary if we had three real machines or three virtual machines).  We’ll also use the --smallfiles parameter and --oplogSize so the files are small given we have a lot of server processes running on our test PC.</p><pre>$ # starting as a standalone server for problem 1:
$ mongod --dbpath 1 --port 27001 --smallfiles --oplogSize 50
</pre><p>Note: for all mongod startups in the homework this chapter, you can optionally use --logPath,  --logappend, and --fork.  Or, since this is just an exercise on a local PC, you could simply have a separate terminal window for all and forgo those settings.  Run “mongod --help” for more info on those.</p><p>4. In a separate terminal window (cmd.exe on Windows), run the mongo shell with the replication.js file:</p><pre>mongo --port 27001 --shell replication.js
</pre><p>Then run in the shell:</p><pre>&gt; homework.init()
</pre><p>This will load a small amount of test data into the database.</p><p>Now run:</p><pre> &gt; homework.a()
</pre><p>and enter the result.  This will simply confirm all the above happened ok.</p><span><section class="textbox" id="textbox_i4x-10gen-M102-problem-53823c198bb48b1135b71675_2_1"><div class="codeinput"><textarea id="input_i4x-10gen-M102-problem-53823c198bb48b1135b71675_2_1" name="input_i4x-10gen-M102-problem-53823c198bb48b1135b71675_2_1" cols="50" rows="4" style="display: none;">5001</textarea><div class="CodeMirror cm-s-default CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 6px; left: 55.6px;"><textarea style="position: absolute; padding: 0px; width: 1px; height: 1em; outline: medium none; font-size: 4px;" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-hscrollbar" style="left: 21px;"><div style="height: 1px;"></div></div><div class="CodeMirror-vscrollbar"><div style="width: 1px;"></div></div><div class="CodeMirror-scrollbar-filler"></div><div class="CodeMirror-gutter-filler"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="true"><div class="CodeMirror-sizer" style="margin-left: 21px; min-height: 26px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: medium none;"><div class="CodeMirror-measure"><pre><span>5</span><span>0</span><span>0</span><span>1</span></pre></div><div style="position: relative; z-index: 1; display: none;"></div><div class="CodeMirror-code" style=""><div style="position: relative;"><div style="position: absolute; left: -21px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 12px;">1</div></div><pre>5001</pre></div></div><div class="CodeMirror-cursor" style="left: 33.6px; top: 1px; height: 16px;">&nbsp;</div><div class="CodeMirror-cursor CodeMirror-secondarycursor" style="display: none;">&nbsp;</div></div></div></div></div><div style="position: absolute; height: 30px; width: 1px; top: 26px;"></div><div class="CodeMirror-gutters" style="height: 268px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 20px;"></div></div></div></div></div><div class="grader-status"><span id="status_i4x-10gen-M102-problem-53823c198bb48b1135b71675_2_1" class="correct">Correct</span><p class="debug"></p></div><span id="answer_i4x-10gen-M102-problem-53823c198bb48b1135b71675_2_1"></span><div class="external-grader-message">

  </div><script>
    // Note: We need to make the area follow the CodeMirror for this to work.
    $(function(){
      var cm = CodeMirror.fromTextArea(document.getElementById("input_i4x-10gen-M102-problem-53823c198bb48b1135b71675_2_1"), {
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

  <section class="action"><input type="hidden" value="Homework: Homework 4.1" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
