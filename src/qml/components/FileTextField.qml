import "../controls"
import QtQuick 2.15

TextField {
    id: text_field

    property alias file_dialog: file_dialog_button.file_dialog
    property bool select_folder: false

    implicitHeight: 30
    text: "/Users/yunzhang/Downloads/BigBuckBunny_320x180.mp4"
    file_dialog.selectFolder: select_folder

    FileDialogButton {
        id: file_dialog_button

        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right
        anchors.rightMargin: 2
        implicitHeight: parent.height - 3
        file_dialog.onAccepted: {
            text_field.text = file_dialog.urlToPath(file_dialog.fileUrl.toString());
        }
    }

}
