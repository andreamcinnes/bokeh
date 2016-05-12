_ = require "underscore"

p = require "../../core/properties"

Widget = require "./widget"


class MarkupView extends Widget.View

  render: () ->
    super()
    # Override browser stylesheet value for paragraph
    @$el.css({
      margin: 0
    })
    # TODO: This isn't smart and doesn't play nicely with layout
    if @mget('height')
      @$el.height(@mget('height'))
    if @mget('width')
      @$el.width(@mget('width'))


class Markup extends Widget.Model
  type: "Markup"

  initialize: (options) ->
    super(options)

  @define {
    text: [ p.String, '' ]
  }

module.exports =
  Model: Markup
  View: MarkupView
