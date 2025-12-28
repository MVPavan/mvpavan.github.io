---
title: MVPavan
subtitle: Collection of technical notes
layout: page
show_sidebar: true
---

# Welcome to MVPavan's Notes

A personal knowledge base covering AI, Machine Learning, and more.

---

## 📚 Recent Notes

<div class="columns is-multiline">
{% for note in site.notes limit:6 %}
<div class="column is-4">
  <div class="box">
    <h4><a href="{{ note.url | relative_url }}">{{ note.title }}</a></h4>
    {% if note.subtitle %}
    <p class="is-size-7 has-text-grey">{{ note.subtitle }}</p>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>

<p class="has-text-centered">
  <a href="/notes/" class="button is-primary is-outlined">View All Notes →</a>
</p>
