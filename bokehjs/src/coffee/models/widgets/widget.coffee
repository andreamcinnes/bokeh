WidgetBox = require "../layouts/widget_box"


class WidgetView extends WidgetBox.View
  className: "bk-widget"


class Widget extends WidgetBox.Model
  type: "Widget"
  default_view: WidgetView


module.exports =
  Model: Widget
  View: WidgetView
