# Reference Importer
## Description
Script that automates the importing of video reference into Maya, automatically creating an image sequence from a video file and creating an image plane with the sequence.
# Installation
## 1. Download the correct version from the Releases tab
>If Using Maya 2021 or under, download ***ReferenceImporter.zip***.

>If Using Maya 2022 or higher, download ***ReferenceImporter_Python3.zip***.
## 2. Copy the contents of the zip to you Maya scripts folder
>found under 'Documents/maya/***InsertMayaVerion***/scripts'
## 2. Run the following command in Maya
    from  ReferenceImporterMain import ReferenceImporterDialog
    ReferenceImporterDialog.run()
make sure to run it using Python

# Usage

## for a demonstration of usage please watch the video :

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ObX9NU2BmZo/0.jpg)](https://www.youtube.com/watch?v=ObX9NU2BmZo "Script Walkthrough Video")
### 1. Choose a video file
### 2. Set the desired trimming
> Use format HH:MM:SS.ms for the timecode
### 3. Set output sequence name and format
### 4. Set output directory for the sequence
### 5. (Optional) auto creation of image plane in Maya for the sequence
### 6. Import the video!!