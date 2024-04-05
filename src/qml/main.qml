import "./components"
import "./controls"
import QtQuick 2.15
import QtQuick.Layouts 1.2
import QtQuick.Window 2.15

Window {
    width: 1280
    height: 720
    visible: true
    title: qsTr("Reference Importer 2.0")
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

          height: 30
          text : "/Users/yunzhang/Downloads/BigBuckBunny_320x180.mp4"
          FileDialogButton{
              anchors.verticalCenter: parent.verticalCenter
              anchors.right: parent.right
              anchors.rightMargin: 2
              height: parent.height - 4
              
              file_dialog.onAccepted: {
                    video_file.text = file_dialog.fileUrl
                  }
              }

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
                  visible: false
                  anchors.centerIn: video_player

                  }
            }
        }


    }

}
