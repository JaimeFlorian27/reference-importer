name = "reference_importer"

version = "2.0.0"

description = (
    "Script that automates the importing of video reference into"
    "Maya, automatically creating an image sequence from a video file and "
    "creating an image plane with the sequence."
)

def build_commands():
    pass

def commands():
    env.PYTHONPATH.append("{root}/python")
