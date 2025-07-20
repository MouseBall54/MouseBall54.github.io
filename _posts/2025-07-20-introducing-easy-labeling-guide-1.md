---
typora-root-url: ../
header:
  teaser: /images/2025-07-20-easy-labeling-guide-1/image-20250720232427171.png
layout: single
title: "Easy Labeling Guide (1) - Loading Images and Labels"
excerpt: "This is the first guide for the YOLO labeling tool, Easy Labeling. It provides basic instructions on how to load image folders and label files on a PC, and how to use class files."
date: 2025-07-20T22:00:00+09:00
categories:
  - Development
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

Hello! Starting with this post, I'll provide a detailed guide on how to use **Easy Labeling, a dedicated tool for YOLO data labeling**.

For this first installment, we'll explore **how to load image and label files** and **how to utilize class description files**.

---

## 1. Loading Images

First, **access the Easy Labeling website**. (A PC environment is recommended).

![Initial screen of Easy Labeling](/images/2025-07-20-easy-labeling-guide-1/image-20250720230233737.png)
*Initial screen of Easy Labeling*

Click the **"Load Image Folder"** button in the top-left corner to select the folder containing the images you want to label.

> **(Note)** Easy Labeling is a web program that runs directly in your browser without a server. Therefore, you can use it safely without worrying about your image or label data being transmitted or leaked externally.

![Image folder selection screen](/images/2025-07-20-easy-labeling-guide-1/image-20250720231802154.png)
*Select the folder containing the images you want to work on.*

If there is no `label` folder inside the selected image folder, a notification will appear asking if you want to create one. Click **"OK"** to automatically create a `label` folder under the image folder. All future labeling data will be saved here.

![Confirm label folder creation](/images/2025-07-20-easy-labeling-guide-1/image-20250720230951821.png)

![Image and label folder loaded successfully](/images/2025-07-20-easy-labeling-guide-1/image-20250720231126118.png)
*Images are loaded correctly, and the label folder has been created.*

Once the images are loaded successfully, the button will change to `label(created)` as shown above, allowing you to easily check the status.

---

## 2. Switching Images in Various Ways

Easy Labeling offers several ways to switch between images for faster workflow.

![Various image switching methods](/images/2025-07-20-easy-labeling-guide-1/image-20250720235716476.png)
*Choose the method that best suits your workflow.*

-   **Method 1:** Directly click on the desired image in the 'Image Files' list on the left.
-   **Method 2:** Click the arrow icons (◀, ▶) at the top of the site to switch to the previous/next image.
-   **Method 3:** Activate the 'Image Previews' window and click on the small thumbnails or arrow icons.
-   **Method 4:** Use the keyboard shortcuts **A** (previous) and **D** (next) to switch quickly.

Choose the most convenient method for you to increase your work efficiency.

---

## 3. Loading and Managing Label Data

### Loading a Label Folder

While the `label` folder was created automatically when starting a new labeling task, you may also need to load existing data or use a label folder from a different location.

There are three main ways to handle labels:

1.  **No `label` folder exists:** A new folder is created automatically. (`label(created)`)
2.  **A `label` folder already exists under the image folder:** It will be loaded automatically. (`label(auto)`)
3.  **Manually specifying a label folder:** You can click the "Load Label Folder" button to select any folder you want.

![Manually specifying a label folder](/images/2025-07-20-easy-labeling-guide-1/image-20250720232427171.png)

*You can also specify a label folder in a different path from the image folder.*

Once the label folder path is specified, the button's name will change to the name of that folder (in this case, 'Preview').

Now you can use the filter function in the file list on the left.

-   **Search files..:** Search for a specific file by entering part of its name.
-   **Labeled / Unlabeled:** Filter files based on whether a matching label data exists for the image.

Since no work has been done yet, if you click the **"Labeled"** filter, you will see that the list is empty.

![Labeled filter applied screen](/images/2025-07-20-easy-labeling-guide-1/image-20250720233244263.png)

*The list is empty because there are no labeled files.*

### Label Data Management Features

The bottom menu provides several features to assist with your labeling work.

![Label data management features](/images/2025-07-20-easy-labeling-guide-1/image-20250720234836438.png)

*Utilize auto-save, manual save, and class template features.*

-   **Auto Save:** This feature automatically saves your current work when you switch to another image. You can toggle it on or off as needed.
-   **Save Labels (Ctrl + S):** Manually saves the labeling data for the current image.
-   **Download Class Template:** Downloads a `custom-classes.yaml` template file that contains the list of classes (object names) to be used for labeling.

The downloaded `custom-classes.yaml` file is structured as follows:

![Example of custom-classes.yaml file](/images/2025-07-20-easy-labeling-guide-1/image-20250721000124127.png)

*You can directly edit the class numbers and names.*

By modifying this file, you can create your own list of classes. When labeling, the names you specify (e.g., person, car) will be displayed instead of class numbers, making the process much more intuitive. A feature to edit this file directly within Easy Labeling will be covered in detail in a future guide.

---

In this post, we have covered the most basic features of Easy Labeling: loading image and label files, and using class files.

In the next guide, we will provide a detailed explanation of the **actual labeling process**, so please look forward to it!

If you have any questions, feel free to leave a comment.

Thank you.
