"""Integration tests for reference importer."""

import subprocess
import tempfile
from pathlib import Path

from reference_importer import ProcessorOptions, Timecode, Video, VideoProcessor

TESTS_DIRECTORY = Path(__file__).parent
SAMPLE_VIDEO = TESTS_DIRECTORY / "data" / "sample_video.mp4"


def test_reference_importer_api() -> None:
    """Test the reference importer API.

    This test creates an image sequence from a video file and asserts that the number
    of files in the output directory is equal to the number of frames in the video. The
    test uses a temporary directory to store the output files.
    """
    temp_dir = tempfile.TemporaryDirectory()

    test_dir = Path(temp_dir.name)
    test_file_name = "image"

    video = Video(SAMPLE_VIDEO)
    options = ProcessorOptions(
        video_start=Timecode.from_milliseconds(0.0, video.metadata.frame_rate),
        video_end=video.metadata.duration,
        padding="%03d",
        frame_rate=24,
        output_dir=test_dir,
        output_file_name=test_file_name,
        output_extension=".jpg",
    )
    VideoProcessor.create_image_sequence(video, options)

    # List the files in the temp directory and assert that the number of
    # files is equal to the number of frames in the video.
    files = list(Path(temp_dir.name).iterdir())
    assert len(files) == video.metadata.duration.as_frames()

    temp_dir.cleanup()


def test_bin_reference_importer() -> None:
    """Test the reference importer command line interface.

    This test runs the reference importer binary with a sample video file and asserts
    that the number of files in the output directory is equal to the number of frames in
    the video. The test uses a temporary directory to store the output files.
    """
    # Initialize the video object for later access to it metadata.
    video = Video(SAMPLE_VIDEO)

    temp_dir = tempfile.TemporaryDirectory()
    test_dir = Path(temp_dir.name)
    test_file_name = "image"
    subprocess.run(
        [
            str(Path(__file__).parent.parent / "src" / "bin" / "reference_importer"),
            str(SAMPLE_VIDEO),
            "--output-dir",
            str(test_dir),
            "--output-file-name",
            test_file_name,
        ],
        check=True,
    )
    # List the files in the temp directory and assert that the number of
    # files is equal to the number of frames in the video.
    files = list(Path(temp_dir.name).iterdir())
    assert len(files) == video.metadata.duration.as_frames()
    temp_dir.cleanup()
