---
title: "Study"
layout: archive
permalink: /en_study/
lang: en
seo_description: >
  Evidence-informed study system guides for active recall, spaced repetition, mistake notes, focus routines, coding practice, vocabulary, note taking, and exam strategy.
sidebar:
    nav: "sidebar-category"
---

The Study category focuses on learning systems that produce visible output. It covers retrieval, review intervals, mistake tracking, focus blocks, notes, reading, coding practice, language learning, exam strategy, and weekly review.

The articles refer to education and institution-grade sources such as IES, EEF, CDC, NIH MedlinePlus, Purdue OWL, Cornell Learning Strategies Center, Python.org, MDN, and Pro Git. The goal is not to collect more study hacks. The goal is to build one-session routines that leave recall evidence, feedback, and a next review task.

Start with active recall and spaced repetition, then add mistake notes, question banks, weekly review, sleep, and focus routines to close the learning loop.

## Start Here

- [Active Recall Study Method](/en_study/active-recall-study-method/)
- [Spaced Repetition Schedule](/en_study/spaced-repetition-schedule/)
- [Exam Mistake Note System](/en_study/exam-mistake-note-system/)
- [Question Bank System](/en_study/question-bank-system/)
- [Sleep and Study Performance](/en_study/sleep-study-performance/)

## Latest Articles

{% assign posts = site.categories["en_Study"] %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
