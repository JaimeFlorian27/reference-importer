import "../controls"
import QtQuick 2.15
import QtQuick.Layouts 1.2
import QtQuick.Window 2.15


Item {
    id: control
    MouseArea{
        anchors.fill: parent
        onClicked: {
            control.visible = false
            }

    Item{
        anchors.centerIn: parent
        implicitWidth: 342
        implicitHeight: 254

        Rectangle {
            anchors.fill: parent
            color: "#041620"
            radius: 8
            border.width: 1
            border.color: "#10425F"
        }

        ColumnLayout{
            anchors.margins: 8
            anchors.fill: parent

            // PUT SECTIONS HERE
            ColumnLayout {
                Text {
                    text: "Output directory"
                    color: "white"
                }

                FileTextField {
                    select_folder: true
                    Layout.fillWidth: true
                }

            }

            RowLayout{
                ColumnLayout {
                    Text {
                        text: "File sequence name"
                        color: "white"
                    }

                    TextField {
                        Layout.fillWidth: true
                    }

                }

                ColumnLayout {
                    Text {
                        text: "File extension"
                        color: "white"
                    }

                    TextField {
                        Layout.fillWidth: true
                    }

                }

            }

            RowLayout{
                Text {
                    text: "Target frame rate"
                    }
                }




        }

    }

}
}
