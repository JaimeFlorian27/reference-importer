import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.2
import QtMultimedia 5.15

TextField{
    id: item

    property real position

    horizontalAlignment: TextInput.AlignHCenter
    function position_to_timecode(position){
      
      var totalSeconds = position / 1000;
      var hours = Math.floor(totalSeconds / 3600);
      var minutes = Math.floor((totalSeconds % 3600) / 60);
      var seconds = Math.floor(totalSeconds % 60);

      return (
        (hours < 10 ? "0" : "") + hours + ":" +
        (minutes < 10 ? "0" : "") + minutes + ":" +
        (seconds < 10 ? "0" : "") + seconds
      );
    }

    function timecode_to_position(timecode){
      
      var timeParts = timecode.split(':');
      var hours = parseInt(timeParts[0], 10);
      var minutes = parseInt(timeParts[1], 10);
      var seconds = parseInt(timeParts[2], 10);
      
      var totalSeconds = hours * 3600 + minutes * 60 + seconds
      var totalMilliseconds = totalSeconds * 1000;
      
      return totalMilliseconds;
    }

    onPositionChanged: {
        text = position_to_timecode(position);
    }
    Component.onCompleted: {
        text = position_to_timecode(position);
      }


    color: "#FFFFFF"
    background: Rectangle {
        anchors.fill: parent
        color: "#061F2D"
        radius: 8
        border.width: 2
        border.color: "#082B3F"
    }
  }
