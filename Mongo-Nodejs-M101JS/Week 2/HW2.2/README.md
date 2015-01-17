<li id="vert-0">
    <section data-type="MongoProc" class="xmodule_display xmodule_MongoProcModule">
    <h2 class="problem-header">Homework: Homework 2.2 (MongoProc Beta Version)</h2>
<section data-ajax-url="/courses/10gen/M101JS/2015_January/modx/i4x://10gen/M101JS/mongoproc/52ddd8efe2d423744501cfce" class="mongoproc">
  <b><i>Preface to Homework 2.2 (MongoProc Beta Version)</i></b><br><br>

This version of homework 2.2 uses an experimental homework validation program.
Previously, we've used manual validation scripts to verify homework answers.
Every term, a number of students have had issues setting up the script.
This version of the MongoProc validation program is an attempt to work
around these issues.
<br><br>

If you have any difficulty using MongoProc, here are
<a target="_blank" href="http://www.youtube.com/playlist?list=PL4RCxklHWZ9vb8rR55iKEffkY-5GhCGvC"><b>2 video lectures</b></a>
showing how to set it up.
<br><br>

Furthermore, you still have the option of using the manual validation scripts
in the other version of homework 2.2. Please feel free to leave feedback
(positive or negative) about your experiences on the forum, or by emailing
education@mongodb.com.
<br><br><b><i>
        You only need to do <em>one</em> version of homework 2.2. If you
        complete it with MongoProc, don't do the manual validation version.
</i></b>
<br><br>

If you choose to do this version, you will need to download one of the
following versions of the MongoProc client, which will verify on your local
machine (port 8082) that the signup and login pages of the blog work properly.
<br><br><a href="https://education.mongodb.com/mongoproc">Download MongoProc</a>

<em>Linux users not using the Ubuntu 12.04 binaries need to have python 2.7 installed and the pymongo module installed.
They can also choose to to point mongoProc to any 2.7 compatible python implementation (like PyPy) in user_settings by changing the python field.</em>
<br>




Write a program that finds the document with the highest recorded temperature for each state, and adds a "month_high" field for that document, setting its value to true.  Use the weather dataset that you imported in HW 2.1. <br><br>

This is a sample document from the weather data collection:

<pre>&gt; use weather
switched to db weather
&gt; db.data.findOne()
{
    "_id" : ObjectId("520bea012ab230549e749cff"),
    "Day" : 1,
    "Time" : 54,
    "State" : "Vermont",
    "Airport" : "BTV",
    "Temperature" : 39,
    "Humidity" : 57,
    "Wind Speed" : 6,
    "Wind Direction" : 170,
    "Station Pressure" : 29.6,
    "Sea Level Pressure" : 150
}
</pre>

Assuming this document has the highest "Temperature" for the "State" of "Vermont" in our collection, the document should look like this after you run your program:
<pre>db.data.findOne({ "_id" : ObjectId("520bea012ab230549e749cff") })
{
    "_id" : ObjectId("520bea012ab230549e749cff"),
    "Day" : 1,
    "Time" : 54,
    "State" : "Vermont",
    "Airport" : "BTV",
    "Temperature" : 39,
    "Humidity" : 57,
    "Wind Speed" : 6,
    "Wind Direction" : 170,
    "Station Pressure" : 29.6,
    "Sea Level Pressure" : 150,
    "month_high" : true
}
</pre>

Note that this is only an example and not the actual document that you would be updating. Note also that our collection only has one month of data for each "State", which is why we are asking you to set "month_high".<br><br>

Hint: If you select all the weather documents, you can sort first by state, then by temperature. Then you can iterate through the documents and know that whenever the state changes you have reached the highest temperature for that state. <br><br>

From the top of this page, there was one additional program that should have
been downloaded: <i>mongoProc</i>.
<br><br>

With it, you can test your code and look at the Feedback section. When it says
"user creation successful" and "user login successful", you can
<em>Turn in</em> your assignment.
<br><br>

You will see a message below about your number of submissions, but you must
submit this assignment using MongoProc.

</section>

</section>

  </li>
