_ = require "underscore"

p = require "../../core/properties"

Widget = require "./widget"

template = require "./markup_template"

class MarkupView extends Widget.View
  template: template

  initialize: (options) ->
    super(options)
    @render()
    @listenTo(@model, 'change', @render)

  render: () ->
    @$el.empty()
    html = @template(@model.attributes)
    @$el.append(html)
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
