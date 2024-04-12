import "../controls"
import QtQuick 2.15

TextField {
    id: text_field

    property alias file_dialog: file_dialog_button.file_dialog

    implicitHeight: 30
    text: "/Users/yunzhang/Downloads/BigBuckBunny_320x180.mp4"

    FileDialogButton {
        id: file_dialog_button

        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right
        anchors.rightMargin: 2
        implicitHeight: parent.height - 3
    }

}
