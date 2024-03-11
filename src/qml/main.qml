import "./components"
import "./controls"
import QtQuick 2.15
import QtQuick.Layouts 1.2
import QtQuick.Window 2.15

Window {
    width: 1280
    height: 720
    visible: true
    title: qsTr("Reference Importer")
    color: "#041620"

    ColumnLayout {
        anchors.fill: parent
        spacing: 10
        Layout.leftMargin: 24

        TextField{
          id: video_file
          Layout.topMargin: 16
          Layout.leftMargin: 20
          Layout.rightMargin: 20
          Layout.fillWidth: true

          // bg color
          default_color : "transparent"
          hovered_color : "transparent"
          pressed_color : "transparent"
          disabled_color : "transparent"

          // border color
          border_default_color : "#0B2E41"
          border_hovered_color : "#2B424F"
          border_pressed_color : "#2B424F"
          border_disabled_color : "transparent"

          height: 30
          text : "/home/jflorian/Downloads/big_buck_bunny_720p_h264.mov"

          }

        RowLayout {
            spacing: 10
            // Layout
            Layout.leftMargin: 20
            Layout.rightMargin: 20
            Layout.bottomMargin: 20
            Layout.fillWidth: true
            Layout.fillHeight: true

            // Video
            VideoPlayer {
                id: video_player
                Layout.preferredWidth: 960
                Layout.preferredHeight: 540
                Layout.fillWidth: true
                Layout.fillHeight: true
                source: video_file.text
                clip: true

                ExportPanel{
                  anchors.centerIn: video_player

                  }
            }
        }


    }

}
