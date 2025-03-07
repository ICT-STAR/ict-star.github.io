---
layout: page
title: seminars
permalink: /seminars/
nav: true
nav_order: 4
horizontal: false
---

<!-- pages/seminars.md -->

{% assign sorted_seminars = site.seminars | sort: "date" | reverse %}

<div class="container mt-5">
    {% for seminar in sorted_seminars %}
    {% include seminar_card.liquid %}
    {% endfor %}
</div> 