import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    // Rectangle {
    //   anchors.fill: parent
    //   color : "#00ffffff"
    //   border.color: "red"
    //
    // }

    height: 40
    width: 800

    RangeSlider {
        anchors.fill: parent
        from: 1
        to: 100
        first.value: 25
        second.value: 75
    }

}
