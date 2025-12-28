---
layout: page
title: Notes
subtitle: Knowledge Base
show_sidebar: false
---

<div class="notes-list">
  <p class="subtitle">A collection of notes from my Obsidian vault.</p>
  
  <div class="notes-grid">
    {% for note in site.notes %}
    <article class="note-card">
      <a href="{{ note.url | relative_url }}">
        <h3 class="note-title">{{ note.title }}</h3>
        {% if note.subtitle %}
        <p class="note-subtitle">{{ note.subtitle }}</p>
        {% endif %}
        {% if note.tags %}
        <div class="note-tags">
          {% for tag in note.tags limit:3 %}
          <span class="tag is-small is-info is-light">{{ tag }}</span>
          {% endfor %}
        </div>
        {% endif %}
      </a>
    </article>
    {% endfor %}
  </div>
</div>

<style>
.notes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.note-card {
  background: #fff;
  border: 1px solid #e1e4e8;
  border-radius: 8px;
  padding: 1.5rem;
  transition: all 0.2s ease;
}

.note-card:hover {
  border-color: #3273dc;
  box-shadow: 0 4px 12px rgba(50, 115, 220, 0.15);
  transform: translateY(-2px);
}

.note-card a {
  text-decoration: none;
  color: inherit;
}

.note-title {
  margin: 0 0 0.5rem;
  color: #363636;
  font-size: 1.1rem;
}

.note-subtitle {
  margin: 0;
  color: #7a7a7a;
  font-size: 0.9rem;
}

.note-tags {
  margin-top: 0.75rem;
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .note-card {
    background: #1a1a1a;
    border-color: #333;
  }
  
  .note-card:hover {
    border-color: #3273dc;
    box-shadow: 0 4px 12px rgba(50, 115, 220, 0.3);
  }
  
  .note-title {
    color: #f5f5f5;
  }
  
  .note-subtitle {
    color: #999;
  }
}
</style>
