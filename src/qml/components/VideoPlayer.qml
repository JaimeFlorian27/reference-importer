import QtGraphicalEffects 1.15
import QtMultimedia 5.15
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.2

Item {
    id: item
    height: 600
    width: 800

    Rectangle {
        id: video_view_bg

        color: "#021017"
        border.width: 1
        border.color: "#082B3F"
        anchors.fill: parent
        radius: 8
        clip: true

        Video {
            id: video

            x: parent.x
            y: parent.y
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            focus: true
            Keys.onSpacePressed: video.playbackState == MediaPlayer.PlayingState ? video.pause() : video.play()
            // apply rounded corners mask
            layer.enabled: true
            source: "https://download.blender.org/peach/bigbuckbunny_movies/BigBuckBunny_320x180.mp4"
            fillMode: VideoOutput.PreserveAspectFit
            notifyInterval: 16
            muted: true

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    video.play();
                }
            }

            layer.effect: OpacityMask {

                maskSource: Rectangle {
                    x: video_view_bg.x
                    y: video_view_bg.y
                    width: video_view_bg.width - 1
                    height: video_view_bg.height - 1
                    radius: video_view_bg.radius
                }

            }

        }

    }
    //time slider

    ColumnLayout {
        id: video_params

        anchors.fill: parent
        spacing: 8

        // filler to allow the other components to bunch at the bottom.
        Item {
            id: filler

            Layout.fillHeight: true
        }

        // range slider
        VideoRangeSlider {
            Layout.leftMargin: 20
            Layout.rightMargin: 20
            Layout.bottomMargin: 20
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignBottom

            indicator_position: position_indicator(video.position, video.duration)
        }

        // navigation
        Item {
            height: 40
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignBottom
        }

    }

}
