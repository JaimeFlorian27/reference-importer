import QtGraphicalEffects 1.15
import QtMultimedia 5.15
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.2

Item {
    id: item
    width: 960
    height: 540
    property string source: "/home/jflorian/Downloads/big_buck_bunny_720p_h264.mov";

    Rectangle {
        id: video_view_bg

        color: "#021017"
        border.width: 1
        border.color: "#082B3F"
        anchors.fill: parent
        radius: 8
        clip: true

    }

    Item{
      anchors.fill: parent
        Video {
            id: video
            x: parent.x
            y: parent.y
            anchors.fill: parent
            focus: true
            autoPlay: true
            muted: true

            onStatusChanged: {
                if (status == MediaPlayer.Buffered)
                {
                    pause()
                    muted = false
                }
            }
            // apply rounded corners mask
            source: item.source
            fillMode: VideoOutput.PreserveAspectFit
            flushMode: VideoOutput.FirstFrame
            notifyInterval: 50
            // muted: true
            MouseArea {
                anchors.fill: parent
                onClicked: {
                  forceActiveFocus()
                  video.playbackState == MediaPlayer.PlayingState ? video.pause() : video.play()
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
        Item{
          height: 120
          id: playback_controls
          Layout.fillWidth: true
          Rectangle {
            anchors.fill: parent
            gradient: Gradient {
                GradientStop { position: 0.0; color: "#00ffffff" }
                GradientStop { position: 0.9; color: "#000000" }
            }
        }
        ColumnLayout{
          anchors.fill: parent
        // range slider
        VideoRangeSlider {
          Layout.leftMargin: 40
          Layout.rightMargin: 40
          Layout.bottomMargin: 20
          Layout.fillWidth: true
            id: range_slider
            video: video
        }
        // navigation
        RowLayout {
            Layout.leftMargin: 40
            Layout.rightMargin: 40
            Layout.bottomMargin: 20
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignBottom

            TimecodeTextInput{
              id: min_timestamp
              position: range_slider.min * video.duration


              onAccepted: {
                  video.seek(timecode_to_position(text))
                }
            }
            Item{Layout.fillWidth: true}
            TimecodeTextInput{
              id: current_timestamp
              position: video.position

              onAccepted: {
                  video.seek(timecode_to_position(text))
                }

            }
            Item{Layout.fillWidth: true}
            TimecodeTextInput{id: max_timestamp; 
              position: range_slider.max * video.duration
            }
        }
      }
    }
}

    layer.enabled: true
    layer.effect: OpacityMask {
        maskSource: Rectangle {
            width: video_view_bg.width - 10
            height: video_view_bg.height - 10
            radius: video_view_bg.radius
        }

    }

  }
}
