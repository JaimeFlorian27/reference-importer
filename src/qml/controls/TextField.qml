import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.2
import QtQuick.Window 2.15

TextField {
    id: item

    property real radius: 8



    // bg color
    property color default_color : "transparent"
    property color hovered_color : "transparent"
    property color pressed_color : "transparent"
    property color disabled_color : "transparent"

    // border color
    property color border_default_color : "#0B2E41"
    property color border_hovered_color : "#2B424F"
    property color border_pressed_color : "#2B424F"
    property color border_disabled_color : "transparent"

    hoverEnabled: true
    selectByMouse: true
    color: "white"

    Item {
        id: animation_states

        states: [
            State {
                name: "focused"
                when: item.focus

                PropertyChanges {
                    target: bg
                    color: hovered_color
                }

                PropertyChanges {
                    target: bg
                    border.color: border_hovered_color
                }

            },
            State {
                name: "hovered"
                when: item.hovered

                PropertyChanges {
                    target: bg
                    color: hovered_color
                }

                PropertyChanges {
                    target: bg
                    border.color: border_hovered_color
                }

            },
            State {
                name: "disabled"
                when: item.enabled == false

                PropertyChanges {
                    target: bg
                    color: hovered_color
                }

                PropertyChanges {
                    target: bg
                    border.color: border.hovered_color
                }

            }
        ]
        transitions: [
            Transition {
                from: "*"
                to: "*"
                reversible: true

                ColorAnimation {
                    easing.bezierCurve: [0.215, 0.61, 0.355, 1, 1, 1]
                    duration: 300
                }

                NumberAnimation {
                    target: bg
                    property: "border.width"
                    easing.bezierCurve: [0.455, 0.03, 0.515, 0.955, 1, 1]
                    duration: 300
                }

            }
        ]
    }

    background: Rectangle {
        id: bg

        anchors.fill: parent
        color: item.default_color
        radius: item.radius
        border.color: item.border_default_color
    }

}
