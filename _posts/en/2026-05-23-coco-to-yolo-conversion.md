---
typora-root-url: ../
layout: single
title: >
  COCO to YOLO Conversion Mistakes: How to Avoid Broken Object Detection Labels
seo_title: >
  COCO to YOLO Conversion Mistakes
date: 2026-05-23T23:59:59+09:00
lang: en
translation_id: coco-to-yolo-conversion
header:
   teaser: /images/2026-05-23-coco-to-yolo-conversion/coco-to-yolo-conversion-hero.png
   overlay_image: /images/2026-05-23-coco-to-yolo-conversion/coco-to-yolo-conversion-hero.png
   overlay_filter: 0.35
excerpt: >
  Convert COCO annotations to YOLO format safely by handling category IDs, bbox coordinate conversion, image paths, empty images, and visual validation.
seo_description: >
  Convert COCO annotations to YOLO format safely by handling category IDs, bbox coordinate conversion, image paths, empty images, and visual validation.
categories:
  - en_easy_labeling
tags:
  - COCO
  - YOLO
  - ComputerVision
  - DataLabeling
  - ObjectDetection
---

## Quick Answer

COCO to YOLO conversion fails most often because category IDs are remapped incorrectly or bounding boxes are converted incorrectly.
COCO boxes are commonly stored as top-left `x`, top-left `y`, `width`, `height` in pixels.
YOLO detection labels use `class_id center_x center_y width height` normalized to the image size.

![COCO annotations converted to YOLO normalized bounding boxes with validation checks](/images/2026-05-23-coco-to-yolo-conversion/coco-to-yolo-conversion-hero.png)

The image shows the conversion flow.
The left side is source annotation data.
The right side is normalized YOLO labels.
The conversion step must preserve class meaning and box location.

## COCO and YOLO Store Different Things

A COCO annotation file is usually one JSON file with images, annotations, and categories.
YOLO detection datasets usually use one `.txt` label file per image.

YOLO line format:

```text
class_id center_x center_y width height
```

The key differences:

| Area | COCO | YOLO |
| --- | --- | --- |
| File shape | one JSON file | one text file per image |
| Box format | top-left x, top-left y, width, height | center x, center y, width, height |
| Coordinate unit | pixels | normalized ratios |
| Category IDs | may be sparse | usually zero-based continuous |

This is why a simple text rewrite is not enough.

## 1. Remap Category IDs

COCO category IDs are not always `0, 1, 2, 3`.
They may start at `1`.
They may skip numbers.

YOLO class IDs should normally be continuous and zero-based:

```text
0 person
1 car
2 bicycle
```

Build an explicit mapping:

```text
COCO category 1 -> YOLO class 0
COCO category 3 -> YOLO class 1
COCO category 17 -> YOLO class 2
```

Do not use COCO category IDs directly unless they already match your YOLO class list.

## 2. Convert Bounding Boxes Correctly

COCO bbox:

```text
x_min, y_min, box_width, box_height
```

YOLO needs:

```text
center_x, center_y, width, height
```

Conversion:

```text
center_x = (x_min + box_width / 2) / image_width
center_y = (y_min + box_height / 2) / image_height
width    = box_width / image_width
height   = box_height / image_height
```

After conversion, all four values should usually be between `0` and `1`.
If you see large pixel values in the YOLO label file, the conversion is wrong.

## 3. Match Image IDs to Filenames

COCO annotations reference an `image_id`.
You must join that ID to the correct image filename from the `images` list.

Mistakes here create labels for the wrong image.
That can be worse than missing labels because training appears to work while learning bad data.

Check:

```text
annotation.image_id -> images[id].file_name -> labels/file_name.txt
```

Also preserve train, validation, and test split boundaries.
Do not accidentally put validation labels into the training folder.

## 4. Handle Empty Images

Some images have no objects.
Decide how your training pipeline expects empty images:

- Empty `.txt` label file
- No label file
- Exclude the image

Be consistent.
If your tool expects empty files and they are missing, it may warn.
If your tool expects missing files and you create invalid empty rows, training may fail.

## 5. Validate Visually

After conversion, open a sample of images and draw the converted boxes.
Check:

```text
[ ] Boxes are on the correct objects.
[ ] Boxes are not shifted.
[ ] Boxes are not too large or too small.
[ ] Classes match the objects.
[ ] Empty images are handled correctly.
```

Visual validation catches errors that text validation cannot.

## Easy Labeling Workflow

If you use Easy Labeling, use it as a visual check after conversion.

```text
1. Convert COCO annotations to YOLO files.
2. Open the image folder.
3. Load the class list.
4. Load the YOLO labels.
5. Inspect a sample from every class.
```

Try the tool here: [Easy Labeling](https://mouseball54.github.io/easy_labeling/).

## Common Mistakes

The first mistake is using COCO category IDs directly.
That can shift every class.

The second mistake is forgetting to normalize by image width and height.

The third mistake is treating COCO bbox as `x_min y_min x_max y_max`.
COCO detection bbox commonly stores width and height, not bottom-right coordinates.

The fourth mistake is not checking images with unusual sizes.
A converter that assumes one fixed resolution can break mixed-size datasets.

## Easy Labeling Screen Example

The screen below shows the basic flow: open an image, draw a box, and assign a class.

![Easy Labeling sample screen for drawing object detection boxes](/images/easy_labeling_sample.png)

## Related Reading

- [YOLO Label Format](/en_easy_labeling/yolo-label-format/)
- [Easy Labeling Guide: Loading Images and Labels](/en_easy_labeling/easy-labeling-guide-1/)
- [COCO dataset format](https://cocodataset.org/#format-data)
- [Ultralytics YOLO dataset format](https://docs.ultralytics.com/datasets/detect/)

## Final Checklist

```text
[ ] Category IDs are remapped to YOLO class IDs.
[ ] COCO pixel boxes are converted to normalized YOLO center boxes.
[ ] Image IDs match the correct filenames.
[ ] Train and validation splits stay separate.
[ ] Empty images are handled consistently.
[ ] Converted labels are visually inspected before training.
```

COCO to YOLO conversion is simple only when the mapping is explicit.
Make the class map and box formula visible, then validate with real images.

## FAQ

### When should I use this guide?

Use it when you need a repeatable labeling workflow, cleaner dataset handoff, or clearer review rules for image annotation.

### What should beginners verify first?

Start with class definitions, positive and negative examples, review criteria, and export format. The tool works best when the labeling rule is explicit.

### Which keywords should I search next?

Search for "COCO to YOLO Conversion Mistakes: How to Avoid Broken Object Detection Labels" together with image labeling, dataset annotation, YOLO, COCO, review workflow, and labeling quality keywords.
