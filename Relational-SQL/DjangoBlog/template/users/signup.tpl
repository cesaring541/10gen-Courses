{% extends "base.tpl" %}

{% block content %}

  <form id="register_form" action="" method="POST">
    {% csrf_token %}

    {% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}
    <input type="submit" name="submit" value="OK" />
  </form>

{% endblock %}
