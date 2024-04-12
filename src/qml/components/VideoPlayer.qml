import "../controls"
import QtGraphicalEffects 1.15
import QtMultimedia 5.15
import QtQuick 2.15
import QtQuick.Layouts 1.2

Item {
    id: item

    property string source

    width: 960
    height: 540

    Item {
        id: animation_state

        state: ""
        states: [
            State {
                name: "hovered"
                when: item_mouse_area.containsMouse

                PropertyChanges {
                    target: video_params
                    opacity: 1
                }

            }
        ]
        transitions: [
            Transition {
                from: ""
                to: "hovered"

                NumberAnimation {
                    properties: "opacity"
                    easing.type: Easing.OutQuad
                    duration: 100
                }

            },
            Transition {
                from: "hovered"
                to: ""

                SequentialAnimation {
                    NumberAnimation {
                        properties: "opacity"
                        easing.type: Easing.OutQuad
                        duration: 300
                    }

                }

            }
        ]
    }

    Rectangle {
        id: video_view_bg

        color: "#021017"
        border.width: 1
        border.color: "#082B3F"
        anchors.fill: parent
        radius: 8
        clip: true
    }

    MouseArea {
        id: item_mouse_area

        acceptedButtons: Qt.NoButton
        anchors.fill: parent
        hoverEnabled: true
        propagateComposedEvents: true

        Item {
            anchors.fill: parent
            layer.enabled: true

            Video {
                id: video

                x: parent.x
                y: parent.y
                anchors.fill: parent
                focus: true
                autoPlay: false
                muted: true
                // apply rounded corners mask
                source: item.source
                onSourceChanged: {
                    range_slider.min = 0;
                    range_slider.max = 1;
                }
                fillMode: VideoOutput.PreserveAspectFit
                flushMode: VideoOutput.FirstFrame
                notifyInterval: 50

                // muted: true
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        forceActiveFocus();
                        video.playbackState == MediaPlayer.PlayingState ? video.pause() : video.play();
                    }
                }

            }
            //time slider

            ColumnLayout {
                id: video_params

                anchors.fill: parent
                layer.enabled: true
                opacity: 0
                spacing: 8

                // filler to allow the other components to bunch at the bottom.
                Item {
                    id: filler

                    Layout.fillHeight: true
                }

                Item {
                    id: playback_controls

                    Layout.fillWidth: true
                    implicitHeight: 100

                    Rectangle {
                        anchors.fill: parent

                        gradient: Gradient {
                            GradientStop {
                                position: 0
                                color: "#00ffffff"
                            }

                            GradientStop {
                                position: 0.9
                                color: "#000000"
                            }

                        }

                    }

                    ColumnLayout {
                        anchors.fill: parent
                        anchors.bottomMargin: 20
                        spacing: 8

                        // range slider
                        VideoRangeSlider {
                            id: range_slider

                            Layout.leftMargin: 40
                            Layout.rightMargin: 40
                            Layout.fillWidth: true
                            video: video
                        }

                        // navigation
                        Item {
                            Layout.leftMargin: 40
                            Layout.rightMargin: 40
                            Layout.fillWidth: true
                            Layout.fillHeight: true
                            Layout.alignment: Qt.AlignBottom

                            TimecodeTextInput {
                                id: current_timestamp

                                position: video.position
                                anchors.horizontalCenter: parent.horizontalCenter
                                onAccepted: {
                                    video.seek(timecode_to_position(text));
                                }
                            }

                            Button {
                                anchors.right: parent.right
                                height: 36
                                text: "Export..."
                                default_color: "#2D3FE1"
                                hovered_color: "#5A69ED"
                                pressed_color: "#1A279B"
                            }

                        }

                    }

                    Rectangle {
                        anchors.fill: parent
                        color: "transparent"
                    }

                }

            }

            layer.effect: OpacityMask {

                maskSource: Rectangle {
                    width: video_view_bg.width
                    height: video_view_bg.height
                    radius: video_view_bg.radius
                }

            }

        }

    }

}
