{% extends "base.tpl" %}

{%block title %}
Login
{% endblock %}

{% block content %}
    <h1>Login to Blog</h1>
    {% if error %}
    <div class="alert alert-danger">
        {{error}}
    </div>
    {% endif%}
    <form id="login_form" class="form-inline" method="post" action="">
        {% csrf_token %}
        <div class="form-group">
        <label>Username:</label>
        <input class="form-control" type="text" name="username" value="" size="50" />
        <br />
        <label>Password::</label>
        <input class="form-control" type="password" name="password" value="" size="50" />
        <br />

        <input type="submit" class="btn btn-default" value="submit" />
        </div>
    </form>
{% endblock %}
