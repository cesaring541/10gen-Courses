<li id="vert-0">
    <section data-type="MongoProc" class="xmodule_display xmodule_MongoProcModule">
    <h2 class="problem-header">Quiz: Using MongoProc</h2>
<section data-ajax-url="/courses/10gen/M202/2015_January/modx/i4x://10gen/M202/mongoproc/533ee6318bb48b0f7851b066" class="mongoproc">
  <h2>Overview</h2>
  <p>In this lesson we will be going over how to setup and use MongoProc, an assessment tool that will be used throughout the course to grade certain assignments.</p>
  <h2>Downloading</h2>
  <p>MongoProc is available for multiple operating systems and can be downloaded at <a href="https://university.mongodb.com/mongoproc">https://university.mongodb.com/mongoproc</a></p>
  <p>Please download the version appropriate for your Operating System. After downloading, extract MongoProc from the archive.</p>
  <h2>Running</h2>
  <h3>Windows</h3>
  <p>On Windows, MongoProc comes packaged with two shortcuts: one for GUI mode and one for Console mode. Opening either of these will start MongoProc.</p>
  <h3>Mac OS X</h3>
  <p>On Mac OS X, MongoProc comes in the form of an application bundle. All you need to do is double click on the green leaf.</p>
  <p>
If you wish to run MongoProc in console mode, you must take the following steps:
</p><ol><li>Open Terminal or any terminal like application</li><li>cd to the directory that mongoProc.app is in</li><li>Execute './mongoProc.app/Contents/MacOS/mongoProc --console'</li></ol><h3>Linux</h3>
  <p>
On Linux, MongoProc comes with a shell script called mongoProc.sh. Executing this will open MongoProc in GUI mode. To open it in Console mode, just execute './mongoProc --console'. <br><b>Note:</b> Make sure mongoProc.sh is executable (chmod +x mongoProc.sh).
</p>
  <h2>Logging In</h2>
  <p>Starting up MongoProc presents you with a login dialog.</p>
  <p>
    <img alt="MongoProc Login" src="https://s3.amazonaws.com/edu-static.mongodb.com/lessons/using_mongoproc/mongoProc_login.png"></p>
  <p>You must login with the same credentials you use to access MongoDB University</p>
  <p>
    <img alt="MongoProc Login with Credentials" src="https://s3.amazonaws.com/edu-static.mongodb.com/lessons/using_mongoproc/mongoProc_login_2.png"></p>
  <h2>Settings</h2>
  <h3>Servers</h3>
  <p>After logging in with MongoProc, you have the ability to configure server settings from within the application.</p>
  <p>Using the  + &amp; - buttons, you can add and remove as many servers as you would like. MongoProc comes with two servers by default: one destined for a web server at localhost:8082 and one destined for a mongod instance at localhost:27017</p>
  <p>
    <img alt="MongoProc Server Settings" src="https://s3.amazonaws.com/edu-static.mongodb.com/lessons/using_mongoproc/mongoProc_settings.png"></p>
  <p>Here you can configure the server's name, address (host), and port.</p>
  <h3>Network Proxy</h3>
  <p>If you require a proxy to access resources on the internet, then you may want to configure MongoProc to use a proxy. This is accomplished by editing the user_settings.json file. The location of this file varies by OS and is provided below.</p>
  <ul><li><b>Windows:</b> bin\user_settings.json</li>
    <li><b>Mac OS X:</b> mongoProc.app/Contents/MacOS/user_settings.json</li>
    <li><b>Linux:</b> ./bin/user_settings.json</li>
  </ul><p>
    <img alt="MongoProc Proxy Settings" src="https://s3.amazonaws.com/edu-static.mongodb.com/lessons/using_mongoproc/mongoProc_proxy.png"></p>
  <p>To configure a proxy you must edit the proxy field. Provided below are various configurations for different types of proxies.</p>
  <ul><li>
No Proxy (none) - Don't apply proxy to connection
<pre>"proxy": {
    "type": "none",
    "host": "localhost",
    "port": 80
}
</pre>
</li>
    <li>
Automatic (automatic, auto) - Use system proxy settings to determine if proxy should be used
<pre>"proxy": {
    "type": "automatic"
}
</pre>
</li>
    <li>
HTTP/S (http, https) - Use an HTTP/S proxy
<pre>"proxy": {
    "type": "http",
    "host": "123.45.67.89",
    "port": 5600
}
</pre>
<pre>"proxy": {
   "type": "https",
   "host": "123.45.67.89",
   "port": 5600,
   "username": "John",
   "password": "Doe"
}
</pre>
</li>
    <li>
SOCKS5 (socks, socks5) - Use a SOCKS5 proxy
<pre>"proxy": {
    "type": "socks",
    "host": "123.45.67.89",
    "port": 5600
}
</pre>
<pre>"proxy": {
    "type": "socks5",
    "host": "123.45.67.89",
    "port": 5600,
    "username": "John",
    "password": "Doe"
}
</pre>
</li>
  </ul><p>MongoProc will tell you if a proxy connection has failed.</p>
  <h2>Testing/Submitting an Assignment</h2>
  <p>After completing an assignment that uses MongoProc, you will want to test and submit your assignment using MongoProc. In order to do so, navigate to the assignment using the left-side pane.</p>
  <p>
    <img alt="MongoProc Assignment" src="https://s3.amazonaws.com/edu-static.mongodb.com/lessons/using_mongoproc/mongoProc_assignment.png"></p>
  <p>The test button will perform the same validation as the grade button except you will not actually be submitting an attempt. This is useful to check if you have done the assignment correct. It also allows for iterative development on your assignments. Both test and grade will provide you with feedback relating to the assignment at hand. This feedback ranges from error messages to messages letting you know everything looks good.</p>
  <p>
    <img alt="MongoProc Feedback" src="https://s3.amazonaws.com/edu-static.mongodb.com/lessons/using_mongoproc/mongoProc_feedback.png"></p>
  <p>When you are ready to submit your assignment for a grade, just click grade and you're good to go!</p>
  <h2>Common Issues</h2>
  <ul><li>
"Failed to check for updates."
<p>The most common cause seen for this issues is that you require a proxy to connect to the internet. Please see Proxy Settings above to configure a proxy for MongoProc.</p>
</li>
    <li>
"The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program"
<p>This is most likely caused from running MongoProc from the wrong location. The Running section specifies how to run MongoProc on each supported Operating System.</p>
</li>
    <li>
MongoProc is telling you that your assignment is not correct.
<p>MongoProc carefully validates your solutions and tries to provide helpful feedback. If it is saying something is wrong, chances are you may have overlooked a small detail in the assignment. If you are sure you are correct, feel free to head over to the discussion board and ask for help.</p>
</li>
    <li>
MongoProc is telling you that it cannot connect to a server when testing/grading.
<p>Verify that your settings reflect the server(s) you are running for the assignment. Be sure not to change the default server names provided.</p>
</li>
    <li>
On Linux: "Failed to load platform plugin "xcb". Available platforms are:"
<p>This happens when MongoProc cannot find the xcb plugin that is required for the application to draw windows. To resolve this dependency you will need libx11-xcb1. For Ubuntu (or Debian based) users, you can run the following:</p>
<pre>sudo apt-get install libx11-xcb1
</pre>
</li>
    <li>
On Linux: "error while loading shared libraries: libGL.so.1: cannot open shared object file: No such file or directory"
<p>This typically happens on a server that doesn't have any graphics libraries (which is normal) but MongoProc requires them to operate as a dual-mode application. For Ubuntu (or Debian based) users, you can run the following:</p>
<pre>sudo apt-get install libgl1-mesa-dev
</pre>
</li>
  </ul><h2>Sample MongoProc Assignment</h2>
  <p>A non-graded MongoProc assignment is now available in MongoProc which you can use to mess around with settings and make sure everything is running O.K.</p>

  <div class="mongoproc-status"><div class="status ">

  <span class="indicator correct"></span> Correct

</div>

<div class="action">
</div>
</div>
</section>

</section>

  </li>
