<div><p>In this problem, you will be using an old weather dataset.  Download weather_data.csv from the Download Handout link.  This is a comma separated value file that you can import into MongoDB as follows:<br></p><pre>mongoimport --type csv --headerline weather_data.csv -d weather -c data
</pre><p><br>You can verify that you've imported the data correctly by running the following commands in the mongo shell:</p><pre>&gt; use weather
&gt; db.data.find().count()
&gt; 2963
</pre><p><br>Reading clockwise from true north, the wind direction is measured by degrees around the compass up to 360 degrees. <br><br>

90 is East<br><br>

180 is South<br><br>

270 is West<br><br>

360 is North<br><br>

Your assignment is to figure out the "State" that recorded the lowest "Temperature" when the wind was coming from the west ("Wind Direction" between 180 and 360). Please enter the name of the state that meets this requirement. Do not include the surrounding quotes in providing your answer.</p></div>
