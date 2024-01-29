import QtQuick 2.15
import QtMultimedia 5.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15
import QtQuick.Layouts 1.2
import QtQuick.Window 2.15

Window {
    width: 1133
    height: 607
    visible: true
    title: qsTr("Reference Importer")
    color: "#041620"

    ColumnLayout{
      anchors.fill: parent
      spacing: 10
      Layout.leftMargin: 24

      // menu bar
      Item{
        id: menu_bar
        Layout.alignment: Qt.AlignTop
        Layout.preferredHeight: 24
        Layout.fillWidth: true

        Rectangle {
          y: -8
          id: menu_bar_bg
          color: "#061F2D"
          height: parent.height + 8
          anchors.left: parent.left
          anchors.right: parent.right
          radius: 8
          }
        }


    RowLayout{
      Layout.leftMargin: 20
      Layout.rightMargin: 20
      Layout.bottomMargin: 20
      spacing: 12

      ColumnLayout{
        spacing: 10
        // video
        Item {
          id: video_view
          Layout.preferredWidth : 800
          Layout.preferredHeight : 600
          Layout.fillWidth: true
          Layout.fillHeight: true

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
              layer.effect: OpacityMask {
              maskSource: Rectangle {
                x: video_view_bg.x; y: video_view_bg.y
                width: video_view_bg.width
                height: video_view_bg.height
                radius: video_view_bg.radius
              }
          }

              source: "/home/jflorian/Downloads/BigBuckBunny_320x180.mp4"
              fillMode: VideoOutput.PreserveAspectFit
              muted: true
              MouseArea {
                  anchors.fill: parent
                  onClicked: {
                      video.play()
                  }

              }
            }
          }
        }

        //time slider
        Item {
          id: video_params
          Layout.preferredHeight: 60
          Layout.fillWidth: true

          Rectangle {
            id: video_params_bg
            color: "#061F2D"
            border.width: 1
            border.color: "#082B3F"
            anchors.fill: parent
            radius: 8
            }

          RangeSlider{
                anchors.fill: parent
                from: 1
                to: 100
                first.value: 25
                second.value: 75
            }
          }
        }

      Item{
        Layout.fillHeight: true
        Layout.preferredWidth: 266

          Rectangle {
            id: importer_params
            color: "#061F2D"
            border.width: 1
            border.color: "#082B3F"
            anchors.fill: parent
            radius: 8
            }

        }
      }
    }

}
