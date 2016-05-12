{Strength}  = require "../../core/layout/solver"

LayoutDom = require "../layouts/layout_dom"


class WidgetView extends LayoutDom.View
  className: "bk-widget"

  initialize: (options) ->
    super(options)
    @bind_bokeh_events()
    @render()

  bind_bokeh_events: () ->
    @listenTo(@model, 'change', @render)
    @listenTo(@model.document.solver(), 'resize', @render)

  render: () ->
    @update_constraints()
    @$el.css({
      position: 'absolute'
      left: @mget('dom_left')
      top: @mget('dom_top')
      'width': @model._width._value - @model._whitespace_left._value - @model._whitespace_right._value
      'padding-left': @model._whitespace_left._value
      'padding-right': @model._whitespace_right._value
      'padding-top': @model._whitespace_top._value
      'padding-bottom': @model._whitespace_bottom._value
    })

  update_constraints: () ->
    s = @model.document.solver()
    if @el.scrollHeight == 0
      s.suggest_value(@model._height, 130)
    else
      s.suggest_value(@model._height, @el.scrollHeight)
    s.update_variables(false)


class Widget extends LayoutDom.Model
  type: "Widget"
  default_view: WidgetView

  get_edit_variables: () ->
    editables = []
    editables.push({edit_variable: @_height, strength: Strength.strong})
    return editables

module.exports =
  Model: Widget
  View: WidgetView
