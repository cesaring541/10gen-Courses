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
  {%endblock %}

  {% block footer %}{% endblock %}
</body>



</html>
