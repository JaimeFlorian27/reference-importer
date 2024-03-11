import "../controls"
import QtQuick 2.15
import QtQuick.Layouts 1.2
import QtQuick.Window 2.15

Item {
    implicitWidth: 342
    implicitHeight: 254

    Rectangle {
        anchors.fill: parent
        color: "#041620"
        radius: 8
        border.width: 1
        border.color: "#10425F"
    }

    RowLayout {
        anchors.fill: parent

        ColumnLayout {
            Text {
                text: "Output directory"
                color: "white"
            }

            TextField {
                Layout.fillWidth: true
            }

        }

        ColumnLayout {
            Text {
                text: "Output name"
                color: "white"
            }

            TextField {
                Layout.fillWidth: true
            }

        }

    }

}
