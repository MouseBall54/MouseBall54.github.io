---
typora-root-url: ../
layout: single
title: >
  YOLO Label Format: How to Read Class, Center X, Center Y, Width, and Height
seo_title: >
  YOLO Label Format Explained
date: 2026-05-23T23:59:59+09:00
last_modified_at: 2026-05-23T23:59:59+09:00
lang: en
translation_id: yolo-label-format
header:
   teaser: /images/2026-05-23-yolo-label-format/yolo-label-format-hero.png
   overlay_image: /images/2026-05-23-yolo-label-format/yolo-label-format-hero.png
   overlay_filter: 0.35
excerpt: >
  Learn the YOLO object detection label format: one text file per image, one object per line, class id plus normalized center x, center y, width, and height.
seo_description: >
  Learn the YOLO object detection label format: one text file per image, one object per line, class id plus normalized center x, center y, width, and height.
categories:
  - en_easy_labeling
tags:
  - YOLO
  - ComputerVision
  - DataLabeling
  - ObjectDetection
  - EasyLabeling
---

## Quick Answer

YOLO object detection labels usually store one `.txt` file for each image.
Each line describes one object.
The common format is:

```text
class_id center_x center_y width height
```

The four box values are normalized.
That means they are not pixel values.
They are ratios from `0` to `1` relative to the image width and height.

![YOLO label format diagram with bounding box, center point, width and height arrows, and abstract label rows](/images/2026-05-23-yolo-label-format/yolo-label-format-hero.png)

The image shows the idea.
The object is surrounded by a bounding box.
The label stores the class and the box position using the center point, width, and height.

## Basic Example

Suppose an image contains one bottle.
The label file might contain:

```text
0 0.500000 0.520000 0.250000 0.640000
```

Read it like this:

| Value | Meaning |
| --- | --- |
| `0` | class id |
| `0.500000` | center x position |
| `0.520000` | center y position |
| `0.250000` | bounding box width |
| `0.640000` | bounding box height |

The class id is an index.
If your class list is:

```text
0 bottle
1 cup
2 box
```

Then class id `0` means `bottle`.

## One Image, One Label File

In a YOLO dataset, image and label files usually share the same base name.

```text
images/train/photo_001.jpg
labels/train/photo_001.txt
```

If `photo_001.jpg` contains three objects, `photo_001.txt` has three lines.
If the image has no objects, the label file may be empty or absent depending on the training pipeline.
Always check the expected behavior of the tool you use.

## Why Values Are Normalized

YOLO uses normalized coordinates so labels remain valid when images are resized during training.
For example, `center_x = 0.5` means the center of the image horizontally.
It does not matter whether the image is `640x480`, `1280x720`, or another size.

The conversion is:

```text
center_x = box_center_x_in_pixels / image_width
center_y = box_center_y_in_pixels / image_height
width    = box_width_in_pixels / image_width
height   = box_height_in_pixels / image_height
```

To convert back to pixels:

```text
box_width_pixels  = width * image_width
box_height_pixels = height * image_height
```

This is the most common place where labeling mistakes happen.
People sometimes write pixel values into the YOLO text file.
That usually breaks training because the values should be between `0` and `1`.

## Center Format, Not Corner Format

YOLO labels use center format.
Many annotation tools and image libraries use corner format:

```text
x_min y_min x_max y_max
```

To convert corner coordinates to YOLO format:

```text
box_width  = x_max - x_min
box_height = y_max - y_min
center_x   = x_min + box_width / 2
center_y   = y_min + box_height / 2
```

Then normalize those values by image width and height.

If you convert from COCO, Pascal VOC, or custom CSV annotations, check this carefully.
Wrong coordinate conversion can make boxes appear shifted, too large, or too small.

## Class IDs Must Match the Class List

The label file stores only the numeric class id.
The class name usually lives in a dataset configuration file or class list.

For example:

```text
0 car
1 bus
2 truck
```

If you later reorder the class list, old labels can become wrong.
A label that used to mean `car` may suddenly mean `bus`.

Use this rule:

```text
Once labeling starts, do not reorder class IDs.
Add new classes at the end when possible.
```

This is especially important when multiple people label data together.

## Common YOLO Label Mistakes

The first mistake is using pixel coordinates instead of normalized coordinates.
If you see values like `340 220 120 80`, that is probably not valid YOLO format.

The second mistake is using top-left corner coordinates instead of center coordinates.
YOLO expects the center of the box, not the top-left corner.

The third mistake is mixing image and label filenames.
`photo_001.jpg` should match `photo_001.txt`.

The fourth mistake is class id drift.
This happens when the class list changes after labels were created.

The fifth mistake is drawing loose boxes.
Object detection labels should be tight enough to describe the visible object, but not so tight that important edges are cut off.

## Verification Checklist

Before training, sample several images and check:

```text
[ ] Every image has the expected label file.
[ ] Every object line has five values.
[ ] Class IDs exist in the class list.
[ ] Coordinate values are between 0 and 1.
[ ] Boxes appear over the correct objects.
[ ] Boxes are not shifted after resizing.
[ ] Empty images are handled consistently.
```

Visual inspection is important.
A dataset can look valid as text and still have boxes in the wrong place.

## Easy Labeling Workflow

If you use Easy Labeling, the key workflow is:

```text
1. Load an image folder.
2. Load or define the class list.
3. Draw boxes around objects.
4. Save labels in YOLO format.
5. Reopen a sample image and verify the boxes.
```

The verification step is worth doing before you label hundreds of images.
It catches class-order mistakes and coordinate export problems early.

You can try the tool here: [Easy Labeling](https://mouseball54.github.io/easy_labeling/).

## Easy Labeling Screen Example

The screen below shows the basic flow: open an image, draw a box, and assign a class.

![Easy Labeling sample screen for drawing object detection boxes](/images/easy_labeling_sample.png)

## Related Reading

- [Easy Labeling Guide: Loading Images and Labels](/en_easy_labeling/easy-labeling-guide-1/)
- [Easy Labeling In-Depth Features](/en_easy_labeling/easy-labeling-in-depth-features/)
- [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/)

## Final Advice

YOLO label format is simple, but it is strict.
One line means one object.
The order is class id, center x, center y, width, height.
The box values are normalized, not pixels.

If you remember those rules and verify visually before training, you avoid many object detection dataset problems.

## FAQ

### When should I use this guide?

Use it when you need a repeatable labeling workflow, cleaner dataset handoff, or clearer review rules for image annotation.

### What should beginners verify first?

Start with class definitions, positive and negative examples, review criteria, and export format. The tool works best when the labeling rule is explicit.

### Which keywords should I search next?

Search for "YOLO Label Format: How to Read Class, Center X, Center Y, Width, and Height" together with image labeling, dataset annotation, YOLO, COCO, review workflow, and labeling quality keywords.
