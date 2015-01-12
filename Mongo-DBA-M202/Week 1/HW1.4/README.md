<li id="vert-0">
    <section data-type="MongoProc" class="xmodule_display xmodule_MongoProcModule">
    <h2 class="problem-header">Homework: Homework 1.4: Reclaiming disk space</h2>
<section data-ajax-url="/courses/10gen/M202/2015_January/modx/i4x://10gen/M202/mongoproc/536902e88bb48b28524500e7" class="mongoproc">
  <p>
    <i>Note: MongoProc validation for this exercise requires that you are running MongoDB 2.6</i>
  </p>
  <p>Over time a MongoDB database can become fragmented and cause reduced storage efficiency.</p>
  <p>In this problem we have provided you with an already fragmented database. You will want to extract the handout and set your mongod's dbpath to the extracted 'fragDB' directory. You'll be working with the <i>fragDB</i> database, and the <i>fragColl</i> collection.</p>
  <p>Your goal in this homework is to increase storage efficiency and reclaim disk space. You may use any method learned thus far to accomplish this goal. However, please do not tamper (remove/update/insert) with the documents in the database given, apart from querying the database to find out more information about the fragmented components.</p>
  <p>You are encouraged to use MongoProc to continuously test your progress until you are ready to grade the homework.</p>
  <h2>Useful Formulas</h2>
  <ul><li>Collection Storage Efficiency: <pre>db.fragColl.stats().size/db.fragColl.stats().storageSize</pre></li>
    <li>Database Storage Efficiency: <pre>(db.stats().dataSize + db.stats().indexSize) / db.stats().fileSize</pre></li>
  </ul>

</section>

</section>

  </li>
