# Reference Importer
Tool to help artists import videos as image sequence in Maya without going through a 
video editing package. Supports multiple file formats, length trimming and specifying a
target frame rate.

## Features
- Video to image sequence conversion, for improved Reference Plane performance.
- Automatic frame rate conversion (Forget about using Premiere Pro to change the frame rate of your reference!).
- Automatic creation of a Reference Plane in Maya.
- Multiplatform support (Windows, Mac and Linux).
- [Ffmpeg](https://ffmpeg.org/) as the backend engine for video conversion.
- [Qt.py](https://github.com/mottosso/Qt.py) abstraction for multiple Maya versions support (2022+).

## Installation
1. Find the latest version under the [Releases](https://github.com/JaimeFlorian27/reference-importer/releases) section.
2. Download the right distribution for your platform. 
    - Distributions use the following naming pattern: `reference_importer_<version>_<platform>.zip`
3. Extract the zip file as a folder named `reference_importer` in your `$MAYA_APP_DIR/<MAYA_VERSION>/scripts` folder. 
    - ie: `/home/jaime/Maya/2024/scripts/reference_importer`
    - [What is my MAYA_APP_DIR?](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=GUID-228CCA33-4AFE-4380-8C3D-18D23F7EAC72) 

## Usage

To launch Reference Importer, run the following Python script:
```
import reference_importer
reference_importer.run()
```

### Workflow

1. Select a video file in the UI.
2. Set the desired start and end timecode.
   - End timecode will be populated by default to the end of the video.
   > Use HH:MM:SS.ms as the timecode format.
3. Set output image sequence name.
4. Set the output format.
4. Select the output directory for the sequence.
4. Set the desired target frame rate.
5. (Optional) Enable creation of an Image Plane in Maya for the sequence.
6. Import the video!

#### Demonstration Video:

[![Reference Importer demonstration video](https://img.youtube.com/vi/ObX9NU2BmZo/0.jpg)](https://www.youtube.com/watch?v=ObX9NU2BmZo "Script Walkthrough Video")
