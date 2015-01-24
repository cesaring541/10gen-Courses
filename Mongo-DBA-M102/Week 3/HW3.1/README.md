<div><p>Start a <code>mongod</code> server instance (if you still have a replica set, that would work too).
</p>
Next, download the handout and run:
<pre>mongo --shell localhost/performance performance.js
&gt; homework.init()
&gt;
</pre>
<p>Build an index on the "active" and "tstamp" fields. You can verify that you've done your job with </p><pre>db.sensor_readings.getIndexes()</pre>
<p>
When you are done, run:
</p><pre>homework.a()
</pre>
<p>
and enter the numeric result below (no spaces).
</p><p>
Note: if you would like to try different indexes, you can use <code>db.sensor_readings.dropIndexes()</code> to drop your old index before creating a new one. (For this problem you will only need one index beyond the _id index which is present by default.)
</p></div>
