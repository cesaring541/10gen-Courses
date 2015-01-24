{% extends "base.tpl" %}

{% block title %}
Add Comments
{% endblock %}

{% block content %}
<a href="{% url 'index' %}">Blog Home</a>

<h2>{{ post.permalink }}</h2>
<div>Posted {{ post.publication_date }} By {{ post.author_id.username }} </div>
<hr>
<p>
{{ post.body }}
</p>
<p>
Filed Under:
{% for tag in post.tag_id.all %}
{{ tag.name }}
{% endfor %}
</p>
<p>Comments: </p>
{% for comment in post.comment_id.all %}

<span>Author: {{comment.name}}</span>
<span>{{ comment.comment_text }}</span>
<hr>
{% endfor %}
<form class="form-inline" action="" method="POST">
	{% csrf_token %}
	{% load widget_tweaks %}
	<div class="row">
	<div class="col-xs-1 col-sm-1 col-md-1 col-lg-1">

	</div>
	<div class="col-xs-11 col-sm-11 col-md-11 col-lg-11">

	<div class="form-group">
	    <h3><strong>Add a comment</strong></h3>
		<div class="fieldWrapper">
		{{ form.name.errors }}
		<h4 for="{{ form.name.id_for_label }}">Name</h4>
		{% render_field form.name class+="form-control" size="60" %}
		</div>
		<div class="fieldWrapper">
		{{ form.email.errors }}

		<h4 for="{{ form.email.id_for_label }}">Email</h4>
		{% render_field form.email class+="form-control" size="60" %}
				</div>
		<div class="fieldWrapper">

		{{ form.comment_text.errors }}
		<h4 for="{{ form.comment_text.id_for_label }}">Comment</h4>
		{% render_field form.comment_text class+="form-control" size="60" cols="80" %}
		</div>


		<br>
		<input type="submit" class='btn btn-default' value="Submit">

	</div>
	</form>

	</div>
	</div>

{% endblock %}

