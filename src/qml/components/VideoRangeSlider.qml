import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12

Item {
    // debugging rectangle
    // Rectangle {
    //   anchors.fill: parent
    //   color : "#00ffffff"
    //   border.color: "red"
    // }

    id: item

    property int indicator_position: 0

    function position_indicator(position, duration) {
        let x = Math.max(width * (position / duration) + control.first.handle.width, control.first.handle.x);
        return x;
    }

    height: 40
    width: 800

    RangeSlider {
        id: control

        anchors.fill: parent
        from: 1
        to: 100
        first.value: 0
        second.value: 100

        // Seek positioner
        Item {
            id: seek_indicator

            Rectangle {
                width: 4
                height: 40
                x: indicator_position
                y: control.topPadding + control.availableHeight / 2 - height / 2
            }

        }

        background: Rectangle {
            x: control.leftPadding
            y: control.topPadding + control.availableHeight / 2 - height / 2
            implicitWidth: 200
            implicitHeight: 4
            width: control.availableWidth
            height: implicitHeight
            radius: 2
            color: "#bdbebf"

            Rectangle {
                x: control.first.visualPosition * parent.width
                width: control.second.visualPosition * parent.width - x
                height: parent.height
                color: "#21be2b"
                radius: 2
            }

        }

        first.handle: Rectangle {
            x: control.leftPadding + control.first.visualPosition * (control.availableWidth - width)
            y: control.topPadding + control.availableHeight / 2 - height / 2
            implicitWidth: 10
            implicitHeight: 26
            radius: 4
            color: control.first.pressed ? "#f0f0f0" : "#f6f6f6"
            border.color: "#bdbebf"
        }

        second.handle: Rectangle {
            x: control.leftPadding + control.second.visualPosition * (control.availableWidth - width)
            y: control.topPadding + control.availableHeight / 2 - height / 2
            implicitWidth: 10
            implicitHeight: 26
            radius: 4
            color: control.second.pressed ? "#f0f0f0" : "#f6f6f6"
            border.color: "#bdbebf"
        }

    }

}
