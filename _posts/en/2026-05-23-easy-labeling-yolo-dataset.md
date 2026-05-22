---
typora-root-url: ../
layout: single
title: >
  Build a YOLO Dataset with Easy Labeling: From Images to Training Folders
seo_title: >
  Build a YOLO Dataset with Easy Labeling
date: 2026-05-23T23:59:59+09:00
lang: en
translation_id: easy-labeling-yolo-dataset
header:
   teaser: /images/2026-05-23-easy-labeling-yolo-dataset/easy-labeling-yolo-dataset-hero.png
   overlay_image: /images/2026-05-23-easy-labeling-yolo-dataset/easy-labeling-yolo-dataset-hero.png
   overlay_filter: 0.35
excerpt: >
  Build a YOLO object detection dataset with Easy Labeling by preparing images, managing classes, saving labels, splitting train and validation folders, and verifying data.yaml.
seo_description: >
  Build a YOLO dataset with Easy Labeling by preparing images, managing classes, saving labels, splitting train and validation folders, and verifying data.yaml.
categories:
  - en_easy_labeling
tags:
  - EasyLabeling
  - YOLO
  - ImageLabeling
  - ComputerVision
  - Dataset
---

## Quick Answer

To build a YOLO dataset with Easy Labeling, prepare a stable class list, label images in small batches, save one YOLO `.txt` label file per image, review samples visually, then export aligned `images/train`, `images/val`, `labels/train`, and `labels/val` folders.
The most important rule is consistency.
Class IDs, image names, label names, and train-validation splits must stay aligned.

![Easy Labeling YOLO dataset workflow from image folder and class list to labels, review, data.yaml, and training folders](/images/2026-05-23-easy-labeling-yolo-dataset/easy-labeling-yolo-dataset-hero.png)

The image shows the full flow.
Easy Labeling helps with the annotation step, but dataset quality still depends on clear classes, repeated review, and a predictable export structure.

## Recommended Project Folder

Start with a simple folder layout:

```text
yolo-dataset-project/
  raw_images/
  working_images/
  labels/
  classes.txt
  export/
```

Keep `raw_images/` as the original source.
Do not edit or rename those files after backup.
Copy the files you want to label into `working_images/`.

This keeps the labeling work recoverable if you need to restart.

## 1. Prepare the Class List

Create `classes.txt` before labeling.

```text
helmet
vest
glove
person
forklift
```

YOLO class IDs are based on line order.
The first line is class `0`, the second line is class `1`, and so on.
After labeling starts, do not reorder this file.

If you need a new class later, add it at the end when possible.
Changing the order can silently corrupt existing labels.

## 2. Label Images in Easy Labeling

Open Easy Labeling and follow this workflow:

```text
1. Open the working image folder.
2. Load or create the class list.
3. Draw bounding boxes around target objects.
4. Assign the correct class.
5. Save labels in YOLO format.
6. Reopen a few saved images to confirm boxes and classes.
```

You can open the tool here: [Easy Labeling](https://mouseball54.github.io/easy_labeling/).

![Easy Labeling sample screen for drawing object detection boxes](/images/easy_labeling_sample.png)

Use the same labeling rule for every image.
For example, decide whether a partly hidden object should be labeled before the team starts.
Ambiguous rules create noisy training data.

## 3. Check the YOLO Label Files

A YOLO detection label file uses this shape:

```text
class_id x_center y_center width height
```

Example:

```text
0 0.512500 0.433333 0.180000 0.260000
3 0.720000 0.510000 0.120000 0.300000
```

Coordinates are normalized from `0` to `1`.
They are not pixel values.
Ultralytics documents the same normalized `class x_center y_center width height` pattern for YOLO detection datasets.

For a deeper explanation, see [How to Read YOLO Label Format](/en_easy_labeling/yolo-label-format/) and the [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/).

## 4. Review Before Splitting

Review a small batch before you label hundreds of images.

Check:

```text
[ ] Boxes are tight enough.
[ ] Class IDs match classes.txt.
[ ] Similar objects use the same class.
[ ] Empty images are handled intentionally.
[ ] Label filenames match image filenames.
[ ] Hard examples are documented.
```

Review is not optional.
Training can fail quietly when labels are inconsistent.

## 5. Export Train and Validation Folders

Use this final dataset shape:

```text
dataset/
  images/
    train/
    val/
  labels/
    train/
    val/
  data.yaml
```

If `images/train/photo_001.jpg` exists, the matching label should be:

```text
labels/train/photo_001.txt
```

If `images/val/photo_101.jpg` exists, the matching label should be:

```text
labels/val/photo_101.txt
```

Split images and labels together.
Never split images first and labels separately.

## 6. Write `data.yaml`

A minimal `data.yaml` can look like this:

```yaml
path: dataset
train: images/train
val: images/val
names:
  0: helmet
  1: vest
  2: glove
  3: person
  4: forklift
```

Keep the `names` order aligned with `classes.txt`.
If those orders disagree, the model can learn the wrong object names.

## 7. Run a Small Verification Pass

Before full training, verify the dataset.

```text
[ ] Open 10 random train images with labels.
[ ] Open 10 random validation images with labels.
[ ] Confirm every label file has valid numeric rows.
[ ] Confirm no image is missing its expected label unless it is intentionally empty.
[ ] Run a short training dry run if your environment is ready.
```

This catches most dataset mistakes before they become training failures.

## Related Reading

- [Local Image Labeling Workflow](/en_easy_labeling/local-image-labeling-workflow/)
- [How to Manage Classes for Image Labeling](/en_easy_labeling/image-labeling-classes/)
- [How to Read YOLO Label Format](/en_easy_labeling/yolo-label-format/)
- [Easy Labeling](https://mouseball54.github.io/easy_labeling/)
- [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/)

## Final Checklist

```text
[ ] Raw images are backed up.
[ ] classes.txt is stable.
[ ] Easy Labeling saves YOLO label files.
[ ] Image and label filenames match.
[ ] Train and validation splits are aligned.
[ ] data.yaml matches the class list.
[ ] A visual sample review is complete.
```

A good YOLO dataset is not just a folder full of images.
It is a repeatable labeling process where class definitions, label files, and export folders stay consistent from the first image to the training run.

## FAQ

### When should I use this guide?

Use it when you need a repeatable labeling workflow, cleaner dataset handoff, or clearer review rules for image annotation.

### What should beginners verify first?

Start with class definitions, positive and negative examples, review criteria, and export format. The tool works best when the labeling rule is explicit.

### Which keywords should I search next?

Search for "Build a YOLO Dataset with Easy Labeling: From Images to Training Folders" together with image labeling, dataset annotation, YOLO, COCO, review workflow, and labeling quality keywords.
