pragma Singleton

import QtQuick 2.15

Item {

    property var icon_fonts : this.font_tabler_icons.name

    property FontLoader font_tabler_icons: FontLoader {
        source: "../resources/fonts/tabler-icons.ttf"
    }
}
