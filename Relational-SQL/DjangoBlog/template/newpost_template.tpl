{% extends 'base.tpl' %}
{% block title %}
<title>Create a new post</title>
{% endblock %}

{% block content %}
{% if request.user %}
Welcome {{request.user}}
<a href="/logout">Logout</a> | <a href="/">Blog Home</a><p>
<form class="form-inline" action="/newpost" method="POST">
	{% csrf_token %}
	{% load widget_tweaks %}
	<div class="form-group">

		<div class="fieldWrapper">
		{{ form.title.errors }}
		<h2 for="{{ form.title.id_for_label }}">Title</h2>
		{% render_field form.title class+="form-control" size="60" %}
		</div>
		<div class="fieldWrapper">

		{{ form.body.errors }}
		<h2 for="{{ form.body.id_for_label }}">Body</h2>
		{% render_field form.body class+="form-control" size="60" cols="80" %}
		</div>
		<div class="fieldWrapper">
		{{ form.tag_id.errors }}

		<h2 for="{{ form.tag_id.id_for_label }}">Tags</h2>
		<p> Comma separated, please</p>
		{% render_field form.tag_id class+="form-control" size="60" %}
				</div>

		<br>
		<input type="submit" class='btn btn-default' value="Submit">

	</div>
	{% endif %}
	{% endblock %}

