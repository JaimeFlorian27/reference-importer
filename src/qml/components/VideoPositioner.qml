import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.2

// Seek  indicator
Item {
    width: 4
    height: 40
    id: control

    property int min_pos: 0
    property int max_pos: 0
    property real position: 0
    property bool dragging: positioner_drag_handler.active

    Rectangle {
        anchors.fill: parent
    }

    DragHandler{
      id: positioner_drag_handler
      yAxis.enabled: false

      xAxis.minimum: control.min_pos
      xAxis.maximum: control.max_pos
      }

}

