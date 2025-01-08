---
layout: page
title: projects
permalink: /projects/
nav: true
nav_order: 3
display_categories: [work, fun]
horizontal: false
---

<!-- pages/projects.md -->

{% assign sorted_projects = site.projects | sort: "time" | reverse %}

<div class="container mt-5">
    {% for project in sorted_projects %}
    {% include project_card.liquid %}
    {% endfor %}
</div>
