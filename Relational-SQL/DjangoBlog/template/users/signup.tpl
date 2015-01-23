{% extends "base.tpl" %}

{% block content %}

  <form id="register_form" class="form-inline" action="" method="POST">

    {% csrf_token %}
    {% load widget_tweaks %}
    <div class="form-group">
    {% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {% render_field field.label_tag %}
        {% render_field field class+="form-control" %}
    </div>
    {% endfor %}
    <input type="submit" class="btn" name="submit" value="OK" size="40" />
    </div>
  </form>

{% endblock %}
