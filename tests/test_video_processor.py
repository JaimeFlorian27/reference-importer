import pytest
from core import VideoProcessor


def test_get_duration():
    """TODO: create extremely small and portable video file for testing"""
    # Check if the function returns the expected duration
    processor = VideoProcessor()
    assert processor.get_duration("path/to/video.mp4") == "00:01:30.250"


def test_get_duration_invalid_path():
    # Check if the function raises an Error for an invalid file path
    with pytest.raises(Exception):
        processor = VideoProcessor()
        processor.get_duration("invalid/path/to/video.mp4")
