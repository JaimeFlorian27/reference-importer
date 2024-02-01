import "./components"
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.2
import QtQuick.Window 2.15

Window {
    width: 1133
    height: 607
    visible: true
    title: qsTr("Reference Importer")
    color: "#041620"

    ColumnLayout {
        anchors.fill: parent
        spacing: 10
        Layout.leftMargin: 24

        // menu bar
        // TODO: Separate into its own component and style
        Item {
            id: menu_bar

            Layout.alignment: Qt.AlignTop
            Layout.preferredHeight: 24
            Layout.fillWidth: true

            Rectangle {
                id: menu_bar_bg

                y: -8
                color: "#061F2D"
                height: parent.height + 8
                anchors.left: parent.left
                anchors.right: parent.right
                radius: 8
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
                Layout.preferredWidth: 800
                Layout.preferredHeight: 600
                Layout.fillWidth: true
                Layout.fillHeight: true
            }

            // Parameters column
            Item {
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
