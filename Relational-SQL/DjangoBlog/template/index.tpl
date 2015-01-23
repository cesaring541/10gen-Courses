{% extends "base.tpl" %}

{% block title %}
My Blog
{% endblock %}

{%block content %}



{% if request.user %}
Welcome {{request.user}}        <a href="/logout">Logout</a> | <a href="/newpost">New Post</a><p>
{%endif %}

<h1>My Blog</h1>

{%for post in myposts %}
<h2><a href="/post/{{ post['permalink'] }}">{{ post['title'] }}</a></h2>
Posted {{post['post_date']}} <i>By {{post['author']}}</i><br>
Comments:


{%endblock%}
