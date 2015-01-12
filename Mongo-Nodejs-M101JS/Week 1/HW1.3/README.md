<div><h2 class="problem-header">
  Homework: Homework 1.3
</h2>

<section class="problem"><div><p>Your assignment for this part of the homework is to install the mongodb driver for Node.js, Express, and other required dependencies and run the test application.  This homework is meant to give you practice using the "package.json" file, which will include some of the code that we provide.</p><p>To do this, first download the hw1-3.zip from Download Handout link, uncompress and change into the hw1-3 directory:</p><pre>cd hw1-3
</pre><p>Use mongorestore to restore the dump into your running mongod. Do this by opening a terminal window (mac) or cmd window (windows) and navigating to the directory so that the dump directory is directly beneath you. Now type:
</p><pre>mongorestore dump
</pre><p>Note you will need to have your path setup correctly to find mongorestore.</p>

Then install all the dependencies listed in the 'package.json' file.  Calling 'npm install' with no specific package tells npm to look for 'package.json':

<pre>npm install
</pre>

This should create a "node_modules" directory with all the dependencies.  Now run the application to get the answer to hw1-3:

<pre>node app.js
</pre>

<p>If you have all the dependencies installed correctly, this will print the message 'Express server started on port 8080'.  Navigate to 'localhost:8080' in a browser and write the text that is displayed on that page in the text box below.</p></div>

  <section class="action"><input type="hidden" value="Homework: Homework 1.3" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
