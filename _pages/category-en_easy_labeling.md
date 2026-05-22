---
title: "Easy Labeling"
layout: archive
permalink: /en_easy_labeling/
lang: en
seo_description: >
  Easy Labeling articles about image annotation, YOLO datasets, COCO conversion, class management, and local labeling workflows.
sidebar:
    nav: "sidebar-category"
---

The Easy Labeling category explains how to make image labeling faster and more consistent. It covers class rules, YOLO datasets, COCO conversion, local review workflows, and the dataset quality decisions that matter before model training.

Start with the local labeling workflow, then read YOLO format and class management to make the dataset rules explicit.

Each article connects tool usage with dataset quality. Use the guides to define labels, avoid format mistakes, review edge cases, and make exports easier to hand off to a training pipeline.

## Start Here

- [Local Image Labeling Workflow](/en_easy_labeling/local-image-labeling-workflow/)
- [Create a YOLO Dataset with Easy Labeling](/en_easy_labeling/easy-labeling-yolo-dataset/)
- [YOLO Label Format](/en_easy_labeling/yolo-label-format/)

## Latest Articles

{% assign posts = site.categories.en_easy_labeling %}
{% for post in posts %}
  {% include archive-single.html type=page.entries_layout %}
{% endfor %}
