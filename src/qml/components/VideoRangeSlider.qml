import QtMultimedia 5.15
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

    /*

    This Item defines a custom video range slider with three main components:

    positioner: visually displays the current seek position of the video and can be
    dragged to change the seek position.
    min_handler: Visually defines the minimum seek value that the position can be at.
    max_handler: Visually defines the maximum seek value that the position can be at.

    The slider operates between a range determined by the properties from and to,
    with a default range of 0.0 to 1.0, operating within the width of the slider.

    for keeping track of positioning, the following properties are used:
      value: holds the current, limitless value of the slider, useful while dragging,
      as value will keep growing past the mix and max limit, as well as the from and to
      values.

      position: it's the value bound by the limits, it's used to calculate the visual
      location of the handle.

    The value is binded to the position of the video divided by the width of the slider.

    The x property of the handlers is never modified directly, instead it is the result
    of video playback or handler manipulation.

    Whenever the seek positioner is moved by direct user manipulation (dragging it
    directly, or position changes due to dragging the limit handlers) the signal
    seek_moved is emitted, it is used to call the seek() method of the video to give it
    a new position.

    If video is played:
    value -> position -> new X value for positioner

    If handler is dragged:
    onTranslationChanged -> value -> new X for positioner -> emit seek_moved()

    If limit handler is dragged:
    onTranslationChanged -> value -> new X for limit handle -> If the position is at
    the limit emit seek_moved() (as it was moved at the result of a drag)

    The range slider provides a custom playback behaviour, where if

    To handle width changes, every time it changes it emits a positionChanged,
    minChanged and maxChanged.
    */
    id: control

    property Video video
    property real from: 0
    property real to: 1
    property real min: 0
    property real max: 1
    property real value: video.position / video.duration
    property bool auto_paused: false
    property real position: 0

    signal at_max_limit()
    signal seek_moved()
    signal min_moved()
    signal max_moved()

    function position_at(x) {
        let pos = ((x) - from) / (to - from);
        pos = Math.min(Math.max(pos, min), max);
        return pos;
    }

    function positioner_at_max_limit() {
        return (Math.round(position * 1000) >= Math.round(max * 1000));
    }

    function positioner_at_min_limit() {
        return (Math.round(position * 1000) <= Math.round(min * 1000));
    }

    onValueChanged: {
        position = position_at(value);
    }
    onPositionChanged: {
        seek_handler.x = (position * width) - seek_handler.width / 2;
    }
    // min signals
    onMin_moved: {
        if (positioner_at_min_limit()) {
            valueChanged();
            seek_moved();
        }
    }
    onMinChanged: {
        min_handler.x = min * width;
    }
    // max signals
    onMax_moved: {
        if (positioner_at_max_limit()) {
            at_max_limit();
            valueChanged();
            seek_moved();
        }
    }
    onMaxChanged: {
        max_handler.x = max * width;
    }
    // seek moved
    onSeek_moved: {
        if (video.availability == MediaPlayer.Available && 
            video.error == MediaPlayer.NoError){

            video.seek(position * video.duration);

          }

    }
    height: 40
    width: 800

    Connections {
        function onPositionChanged() {
            if (video.playbackState == MediaPlayer.PlayingState) {
                if (positioner_at_max_limit())
                    video.pause();

            }
            position = position_at(value);
            seek_handler.x = (position * width) - seek_handler.width / 2;
        }

        function onPlaying() {
            if (positioner_at_max_limit())
                video.seek(min * video.duration);

        }
        target: video
    }

    Timer {
        id: durTrig

        running: false
        repeat: false
        onTriggered: {
            video.pause();
        }
    }

    Rectangle {
        id: bg

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.verticalCenter: parent.verticalCenter
        height: 4
        radius: 4
    }

    // min handler
    Item {
        id: min_handler

        property real previous_position: 0

        height: 24
        width: 24
        anchors.verticalCenter: parent.verticalCenter

        Rectangle {
            width: parent.width
            height: parent.height
            x: -width
            anchors.verticalCenter: parent.veticalCenter
            radius: 4

        DragHandler {
            id: min_drag_handler

            target: null
            onActiveChanged: {
                if (active)
                    min_handler.previous_position = min;

            }
            onTranslationChanged: (point) => {
                min = min_handler.previous_position + translation.x / control.width;
                control.min_moved();
            }
        }

        }
    }

    // max handler
    Item {
        id: max_handler

        property real previous_position: 0
        height: 24
        width: 24

        anchors.verticalCenter: parent.verticalCenter
        x: to * parent.width

        Rectangle {
            radius: 4
            width: parent.width
            height: parent.height
            x: 0
            anchors.verticalCenter: parent.verticalCenter

            DragHandler {
                id: max_drag_handler

                target: null
                onActiveChanged: {
                    if (active)
                        max_handler.previous_position = max;

                }
                onTranslationChanged: {
                    max = max_handler.previous_position + translation.x / control.width;
                    control.max_moved();
                }
            }

        }
    }

    // seek_handler
    Item {
        id: seek_handler

        property real previous_position: 0

        height: 32
        width: 4
        anchors.verticalCenter: parent.verticalCenter

        Rectangle {
            anchors.fill: parent
            radius: 4
            color: "red"
            DragHandler {
                id: seek_drag_handler

                target: null
                onActiveChanged: {
                    if (active)
                        seek_handler.previous_position = position;
                    else
                        value = Qt.binding(function() {
                            return video.position / video.duration;
                        });
                }
                onTranslationChanged: {
                    value = seek_handler.previous_position + translation.x / control.width;
                    control.seek_moved();
                }
            }
        }
    }

}
