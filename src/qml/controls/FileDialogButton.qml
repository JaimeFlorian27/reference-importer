import QtQuick 2.15
import QtQuick.Dialogs 1.0
import QtQuick.Window 2.0
import "."
import "../style"

Button {

    property alias file_dialog: file_dialog

    default_color: "transparent"
    hovered_color: "#50ffffff"
    pressed_color: "#20ffffff"

    font.family: Style.icon_fonts
    text: qsTr("\ufaf7") 
    font.pixelSize: 16

    onClicked: {
        file_dialog.visible = true
        }

    FileDialog {
        id: file_dialog
        selectMultiple: false
        title: "Please choose a file"
        folder: shortcuts.home

        function urlToPath(urlString) {
            var s
            if (urlString.startsWith("file:///")) {
                var k = urlString.charAt(9) === ':' ? 8 : 7
                s = urlString.substring(k)
            } else {
                s = urlString
            }
            return decodeURIComponent(s);
        }
    }
}
