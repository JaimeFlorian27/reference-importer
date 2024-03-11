import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: control

    property color default_color: "#339943"
    property color hovered_color: "#52E068"
    property color pressed_color: "#36633D"
    property color disabled_color: "#36633D"

    hoverEnabled: true
    text: qsTr("Button Text")
    state: ""
    height: 25
    highlighted: true
    states: [
        State {
            name: "pressed"
            when: control.pressed

            PropertyChanges {
                target: bg
                color: pressed_color
            }

        },
        State {
            name: "hovered"
            when: control.hovered || control.visualFocus

            PropertyChanges {
                target: bg
                color: hovered_color
            }

            PropertyChanges {
                target: control
                scale: 1.05
            }

        },
        State {
            name: "disabled"
            when: control.enabled == false

            PropertyChanges {
                target: bg
                color: disabled_color
            }

        }
    ]
    transitions: [
        Transition {
            from: "*"
            to: "*"
            reversible: true

            ColorAnimation {
                easing.bezierCurve: [0.455, 0.03, 0.515, 0.955, 1, 1]
                duration: 100
            }

            PropertyAnimation {
                property: "scale"
                easing.type: Easing.OutQuad
                duration: 100
            }

        }
    ]

    background: Rectangle {
        id: bg

        radius: 5
        color: default_color
    }

}
