{% extends "base.tpl" %}

{% block title %}
My Blog
{% endblock %}

{%block content %}


{% if request.user.is_authenticated %}
Welcome {{request.user}} <a href="{% url 'logout' %}">Logout</a> | <a href="{% url 'newpost' %}">New Post</a><p>
{% else %}
<a href="{% url 'login' %}">Login</a> | <a href="{% url 'signup' %}">SignUp</a><p>
{%endif %}

<h1>My Blog</h1>

{%for post in posts %}
<h2><a href="{% url 'add_comment' post.permalink %}">{{ post.title }}</a></h2>
Posted {{post.publication_date }} <i>By {{ post.author_id.username }}</i><br>
Comments: <a href="{% url 'add_comment' post.permalink %}">{{ post.comment_id.count }}</a>
<hr>
{{ post.body }}

Filed Under:
{% for tag in post.tag_id.all %}
{{ tag.name }}
{% endfor %}
{% endfor %}

{%endblock%}
