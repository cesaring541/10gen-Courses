<div><h2 class="problem-header">
  Homework: Homework 2.2 (Manual Validation Version)
</h2>

<section class="problem"><div><b><i>Preface to Homework 2.2 (Manual Validation Version)</i></b><br>

There are two versions of homework 2.2. You only need to do one. This is the
version that previous students have used. It involves running a manual
validation script on your local machine in order to verify that your blog is
working, and so this version will include instructions on running that script.
<br><br><b><i>You only need to do <em>one</em> version of homework 2.2. Do not do this
    version if you've already done the MongoProc version.
</i></b>
<br><br>

If you choose to do this version, you will need to download the homework packet
from the Download Handout link above, and unpack. This will include a
<em>validate.js</em> file in the hw2-2validate/ directory that we will use to
verify on your local machine (port 8082) that the signup and login pages of the
blog work properly. You will not yet be building functionality for displaying
posts. Don't worry, that will come later.
<br><br><p>Write a program that finds the document with the highest recorded temperature for each state, and adds a "month_high" field for that document, setting its value to true.  Use the weather dataset that you imported in HW 2.1. <br><br>

This is a sample document from the weather data collection: </p>

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

<p>Assuming this document has the highest "Temperature" for the "State" of "Vermont" in our collection, the document should look like this after you run your program:</p>
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

<p>Note that this is only an example and not the actual document that you would be updating. Note also that our collection only has one month of data for each "State", which is why we are asking you to set "month_high".<br><br>

Hint: If you select all the weather documents, you can sort first by state, then by temperature. Then you can iterate through the documents and know that whenever the state changes you have reached the highest temperature for that state. <br><br>

Once you've done this, download hw2-2.zip from the Download Handout link, uncompress and you can validate it using the validation script we've provided.  Just run the following commands:</p>

<pre>cd hw2-2validate
npm install
node validate.js
</pre>

<p>If you got it right, it will provide a validation code for you to enter into the box below. Enter just the code, no spaces.  If you fail validation or have messed up your collection beyond repair, run the following to drop the weather database so you can reimport the data and try again:</p>

<pre>mongo weather --eval "printjson(db.dropDatabase())"
</pre></div>

  <section class="action"><input type="hidden" value="Homework: Homework 2.2 (Manual Validation Version)" name="problem_id"><section class="submission_feedback">
      You have used 1 of 3 submissions
    </section></section></section></div>
