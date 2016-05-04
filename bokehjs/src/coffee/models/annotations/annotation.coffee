_ = require "underscore"

Renderer = require "../renderers/renderer"
SidePanel = require "../../core/layout/side_panel"
p = require "../../core/properties"
{logger} = require "../../core/logging"

class Annotation extends Renderer.Model
  type: 'Annotation'

  @define {
    plot:           [ p.Instance                  ]
  }

  @override {
    level: 'annotation'
  }

  @internal {
    layout_location: [ p.Any ]
  }

  initialize_layout: () ->
    side = @get('layout_location')
    if side == "above"
      @_size = @panel._height
    else if side == "below"
      @_size = @panel._height
    else if side == "left"
      @_size = @panel._width
    else if side == "right"
      @_size = @panel._width
    else
      logger.error("unrecognized side: '#{ side }'")

  add_panel: () ->
    # Only called if renderer is in a side
    @panel = new SidePanel.Model()
    @panel.attach_document(@document)

module.exports =
  Model: Annotation
