<!DOCTYPE html>

<html>
<head>

  {% load staticfiles %}
  <title>{% block title %} {% endblock %}</title>
  {% block stylesheet %}
    <link href="{% static 'bower_components/bootstrap/dist/css/bootstrap.css' %}" rel="stylesheet">

  {% endblock %}
  {% block javascript %}
      <script src="{% static 'bower_components/polymer/polymer.js' %}"></script>
      <script src="{% static 'bower_components/webcomponentsjs/webcomponents.js' %}"></script>

  {% endblock %}

</head>

<body>
  {%block nav %}
  {% endblock %}
  {% block content %}

  Welcome {{ request.path }}

  {% if request.user.is_authenticated %}
  <p>
    <ul>
      <li><a href="/">Goto Blog Home</a></li>
      <li>
        <a href="/logout">Logout</a>
      </li>
      <li>
        <a href="/newpost">Create a New Post</a>
      </li>
    </ul>
  </p>
  {% else %}
  <p>
    <ul>
      <li>
        <a href="/signup">SignUp</a>
      </li>
      <li>
        <a href="/login">Login</a>
      </li>
    </ul>
  </p>
  {% endif %}
  {%endblock %}

  {% block footer %}{% endblock %}
</body>



</html>
