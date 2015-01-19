<!DOCTYPE html>

<html>
<head>
  <title>{% block title %} {% endblock %}</title>
  {% block stylesheet %}{% endblock %}
  {% block javascript %}{% endblock %}

</head>

<body>{%block nav %}{% endblock %}
  {% block content %}
  Welcome {{username}}

  {% if user.authenticate %}
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
        <a href="/signin">SignIn</a>
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
