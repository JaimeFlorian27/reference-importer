import "./components"
import "./controls"
import QtQuick 2.15
import QtQuick.Layouts 1.2
import QtQuick.Window 2.15

Window {
    minimumWidth: 1280
    minimumHeight: 720
    visible: true
    title: qsTr("Reference Importer")
    color: "#041620"

    ColumnLayout {
        anchors.fill: parent
        spacing: 10
        Layout.leftMargin: 24

        TextField {
            Layout.topMargin: 16
            Layout.leftMargin: 20
            Layout.rightMargin: 20
            Layout.fillWidth: true
            // bg color
            default_color: "transparent"
            hovered_color: "transparent"
            pressed_color: "transparent"
            disabled_color: "transparent"
            // border color
            border_default_color: "#0B2E41"
            border_hovered_color: "#2B424F"
            border_pressed_color: "#2B424F"
            border_disabled_color: "transparent"
            height: 30
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
                Layout.preferredWidth: 960
                Layout.preferredHeight: 540
                Layout.minimumHeight: 540
                Layout.minimumWidth: 960
                Layout.fillWidth: true
                onWidthChanged: {
                    Layout.preferredHeight = width / (16 / 9);
                }
            }

        }

    }

}
