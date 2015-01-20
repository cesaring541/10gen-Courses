{% extends "base.tpl" %}

{% block content %}
    <h1>Login to Rango</h1>
    {% if error %}
    <div class="alert alert-danger">
        {{error}}
    </div>
    {% endif%}
    <form id="login_form" method="post" action="{% url 'login'%}">
        {% csrf_token %}

        Username: <input type="text" name="username" value="" size="50" />
        <br />
        Password: <input type="password" name="password" value="" size="50" />
        <br />

        <input type="submit" value="submit" />
    </form>
{% endblock %}
