import QtGraphicalEffects 1.15
import QtMultimedia 5.15
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.2

Item {
    id: item
    width: 960
    height: 540


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
            anchors.fill: parent
            focus: true
            autoPlay: true
            muted: true

            // avoids a segmentation fault while seeking with no loaded frame...
            onStatusChanged: {
                if (status == MediaPlayer.Buffered)
                {
                    pause()
                    muted = false
                }
            }
            // apply rounded corners mask
            layer.enabled: true
            source: "/home/jflorian/Downloads/big_buck_bunny_720p_h264.mov"
            fillMode: VideoOutput.PreserveAspectFit
            flushMode: VideoOutput.FirstFrame
            notifyInterval: 50
            // muted: true

            MouseArea {
                anchors.fill: parent
                onClicked: video.playbackState == MediaPlayer.PlayingState ? video.pause() : video.play()
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
            id: range_slider
            Layout.leftMargin: 40
            Layout.rightMargin: 40
            Layout.bottomMargin: 20
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignBottom
            video: video
        }
        // navigation
        Item {
          height: 40
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignBottom
        }

    }

}
