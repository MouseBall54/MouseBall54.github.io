---
title: "Study"
layout: archive
permalink: /en_study/
lang: en
seo_description: >
  Study system articles about active recall, spaced repetition, mistake notes, coding study roadmaps, focus routines, and weekly review.
sidebar:
    nav: "sidebar-category"
---

The Study category focuses on learning systems that produce visible output. It covers recall, review intervals, mistake tracking, focus blocks, and study dashboards for exams, language learning, and programming practice.

Start with active recall and spaced repetition, then add mistake notes and weekly review to close the learning loop.

Each article includes a routine, template, or decision rule that can be tested in one study session. The goal is not to collect more study hacks, but to build a repeatable loop that shows what you can remember and use.

## Start Here

- [Active Recall Study Method](/en_study/active-recall-study-method/)
- [Spaced Repetition Schedule](/en_study/spaced-repetition-schedule/)
- [Exam Mistake Note System](/en_study/exam-mistake-note-system/)

## Latest Articles

{% assign posts = site.categories["en_Study"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
