import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.12
import QtMultimedia 5.15

Item {
    id: control
    property Video video
    property real from: 0.0
    property real to: 1.0

    property real min: 0.0
    property real max: 1.0

    property real value: video.position / video.duration
    property real position: 0.0

    signal at_limit()
    signal seek_moved()
    signal min_moved()
    signal max_moved()


    onValueChanged: {position = position_at(value)}
    onPositionChanged: {seek_handler.x = (position * width) - seek_handler.width / 2}

    onMin_moved: {valueChanged(); at_limit()}
    onMinChanged: {min_handler.x = min * width - min_handler.width / 2}

    onMax_moved: {valueChanged(); at_limit()}
    onMaxChanged: {max_handler.x = max * width - max_handler.width / 2}

    onSeek_moved: {video.seek(position * video.duration)}

    Connections{
      target: video
      function onPlaying() {
        if (position == max || position == min){
          video.pause()
          seek_moved()
        }
      }
    }

    onAt_limit: {}
    function position_at(x){
      let pos = (x - from) / (to - from);
      pos = Math.min(Math.max(pos, min), max);
      return pos;
      }

    height: 40
    width: 800

     // debugging rectangle
     // Rectangle {
     //   anchors.fill: parent
     //   color : "#00ffffff"
     //   border.color: "red"
     // }


    Rectangle{
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
      height: 24
      width: 4
      property real previous_position: 0.0
      anchors.verticalCenter: parent.verticalCenter

      Rectangle{
        anchors.fill: parent
        radius: 4
        }
      DragHandler{
        id: min_drag_handler
        target: null
        onActiveChanged: {
            if (active){
              min_handler.previous_position = min
            }
          }
        onTranslationChanged: (point) => {
          min = min_handler.previous_position + translation.x / control.width
          control.min_moved()
        }
        }
      }

    // min handler
    Item {
      id: max_handler
      height: 24
      width: 4
      property real previous_position: 0.0
      anchors.verticalCenter: parent.verticalCenter
      x: to * parent.width

      Rectangle{
        anchors.fill: parent
        radius: 4
        }
      DragHandler{
        id: max_drag_handler
        target: null
        onActiveChanged: {
            if (active){
              max_handler.previous_position = max
            }
          }
        onTranslationChanged: (point) => {
          max = max_handler.previous_position + translation.x / control.width
          control.max_moved()
        }
        }
      }

    // seek_handler
    Item {
      id: seek_handler
      property real previous_position: 0.0
      height: 16
      width: 16
      anchors.verticalCenter: parent.verticalCenter


      Rectangle{
        anchors.fill: parent
        radius: 4
        color: "red"
        }

      DragHandler{
        id: seek_drag_handler
        target: null
        onActiveChanged: {
            if (active){
              seek_handler.previous_position = position
            }
            else{
              value = Qt.binding(function() {return video.position / video.duration})
              }
          }
        onTranslationChanged: (point) => {
          value = seek_handler.previous_position + translation.x / control.width
          control.seek_moved()
        }
        }
      }
}
