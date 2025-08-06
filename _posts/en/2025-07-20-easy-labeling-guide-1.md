---
typora-root-url: ../
header:
  teaser: /images/2025-07-20-easy-labeling-guide-1/image-20250720232427171.png
title: "Easy Labeling Guide (1) - Loading Images and Labels"
excerpt: "This is the first guide for the YOLO labeling tool, Easy Labeling. It provides basic instructions on how to load image folders and label files from your PC and how to use class files."

lang: en
translation_id: easy-labeling-guide-1
categories:
  - en_easy_labeling
tags:
  - Easy Labeling
  - Guide
  - YOLO labeling
  - YOLO
  - Data Labeling
  - AI
  - Computer Vision
  - Annotation
  - YOLO Annotation
---

<p><strong>Easy Labeling Project Page: <a href="https://mouseball54.github.io/easy_labeling/">https://mouseball54.github.io/easy_labeling/</a></strong></p>

Hello! Starting with this post, I will explain in detail how to use **Easy Labeling, a dedicated tool for YOLO data labeling**.

For this first session, we will learn **how to load image and label files** and **how to use class description files**.

---

## 1. Loading Images

### 1.1 Recommended Environment

We recommend using the following environment:  
> **Operating System**: Windows 10 or higher, macOS 10.14 or higher  
> **Browser**: Chrome 93+, Firefox 91+, Edge 93+  
> **Screen Resolution**: 1280×720 or higher  

### 1.2 Accessing the Website
Access the Easy Labeling project page ([https://mouseball54.github.io/easy_labeling/](https://mouseball54.github.io/easy_labeling/)) in your web browser.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720230233737.png" alt="Easy Labeling initial screen">
  <figcaption>Figure 1. Easy Labeling initial screen. Click the <code>Load Image Folder</code> button in the top left corner.</figcaption>
</figure>



### 1.3 Selecting the Image Folder

- Click the <code>Load Image Folder</code> button to select the folder where your images for labeling are stored.

> **(Note)** Easy Labeling is a web program that runs directly in your browser without a server. Therefore, you can use it safely without worrying about your images or label data being transmitted or leaked externally.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720232309611.png" alt="Image folder selection screen">
  <figcaption>Figure 2. Image folder selection screen.</figcaption>
</figure>



### 1.4 Creating the Label Folder

- If there is no <code>label</code> folder in the selected image folder, a notification window will appear asking if you want to create one.  
- Click "OK" to automatically create the <code>label</code> folder, where your label data will be stored in the future.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720230951821.png" alt="Confirm label folder creation">
  <figcaption>Figure 3. <code>label</code> folder creation confirmation window.</figcaption>
</figure>

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720231126118.png" alt="Image and label folders loaded successfully">
  <figcaption>Figure 4. Image and label folders loaded successfully. The button changes to <code>label (created)</code>.</figcaption>
</figure>



---

## 2. How to Switch Images

Easy Labeling provides various methods for quick navigation. Choose the method that is most convenient for you to increase your efficiency.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720235716476.png" alt="Various ways to switch images">
  <figcaption>Figure 5. Various ways to switch images.</figcaption>
</figure>


- **Method 1**: Click on the desired image directly from the <code>Image Files</code> list on the left.  
- **Method 2**: Click the arrow icons (<code>◀</code>, <code>▶</code>) at the top.  
- **Method 3**: Click the thumbnails or arrows in the <code>Image Previews</code> window.  
- **Method 4**: Use the keyboard shortcuts <code>A</code> (previous) and <code>D</code> (next).  

---

## 3. Loading and Managing Label Data

### 3.1 Loading the Label Folder
Refer to the following methods to load existing label data or use a folder from a different location.

1. If no <code>label</code> folder exists, it is created automatically (<code>label (created)</code>).  
2. If the folder is a subfolder of the image folder, it is loaded automatically (<code>label (auto)</code>).  
3. Manual selection: Click the <code>Load Label Folder</code> button.

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720232427171.png" alt="Manually specifying the label folder">
  <figcaption>Figure 6. Screen for manually specifying the label folder.</figcaption>
</figure>


- <code>Search files...</code>: Search by a part of the file name.  
- <code>Labeled</code> / <code>Unlabeled</code> filter: Classify files based on whether they have labels.  

<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250720233244263.png" alt="Labeled filter applied screen">
  <figcaption>Figure 7. Screen with the <code>Labeled</code> filter applied.</figcaption>
</figure>


### 3.2 Label Data Management Features
<figure>
  <img src="/images/2025-07-20-easy-labeling-guide-1/image-20250721010743987.png" alt="Label data management features">
  <figcaption>Figure 8. Label data management menu (<code>Auto Save</code>, <code>Save Labels</code>, <code>Download Class Template</code>).</figcaption>
</figure>


- <code>Auto Save</code>: Automatically saves when switching images.  
- <code>Save Labels</code> (<code>Ctrl + S</code>): Manual save.  
- <code>Download Class Template</code>: Downloads the <code>custom-classes.yaml</code> template.  

---

## 4. Using Class Description Files

The downloaded <code>custom-classes.yaml</code> file is provided in the following format. Modify the class IDs and names as desired.

```yaml
# This is a YAML file for class definitions.
# Each line should be in the format: id: name
# The ID must be an integer.

0: person
1: car
2: bicycle
3: dog
10: traffic light
```

By modifying this file to create your own class list, you can work more intuitively as the specified names (person, car, etc.) will be displayed instead of class numbers during labeling. The feature to edit this file directly within Easy Labeling will be covered in detail in a future guide.

In this post, we have covered the most basic features of Easy Labeling: loading image and label files, and using class files.

In the next guide, we will provide a detailed explanation of **how to perform the actual labeling work**, so please look forward to it!

If you have any questions, feel free to ask in the comments.

Thank you.

------

## 5. FAQ and Tips

### FAQ

**Q1. The image folder does not load.**
 A. Check if you are using a supported extension (.jpg, .png, .bmp, tiff, etc.) and verify that you have allowed folder access permissions in your browser.

**Q2. The label folder creation window does not appear.**
 A. Disable the browser's pop-up blocker and then run <code>Load Image Folder</code> again.

### Tips

- It is recommended to save manually with <code>Ctrl + S</code> before labeling.
- Manage your class templates with a version control system like Git to maintain consistency when collaborating.

------

▶️ [Next: Guide to Labeling Work (Coming Soon)](easy-labeling-guide-2.md)
