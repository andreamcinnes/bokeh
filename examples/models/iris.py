from __future__ import print_function

from bokeh.util.browser import view
from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.models.glyphs import Circle
from bokeh.models import (
    Plot, DataRange1d, LinearAxis, Grid, ColumnDataSource, PanTool,
    WheelZoomTool, Label, Button, VBox, CustomJS
)
from bokeh.resources import INLINE
from bokeh.sampledata.iris import flowers

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}

flowers['color'] = flowers['species'].map(lambda x: colormap[x])

source = ColumnDataSource(
    data=dict(
        petal_length=flowers['petal_length'],
        petal_width=flowers['petal_width'],
        sepal_length=flowers['sepal_length'],
        sepal_width=flowers['sepal_width'],
        color=flowers['color']
    )
)

xdr = DataRange1d()
ydr = DataRange1d()

plot = Plot(x_range=xdr, y_range=ydr, min_border=20, plot_height=300)

xaxis = LinearAxis(axis_label="petal length", bounds=(1,7), major_tick_in=0)
plot.add_layout(xaxis, 'above')

xaxis_2 = LinearAxis(axis_label="petal length", bounds=(1,7), major_tick_in=0)
plot.add_layout(xaxis_2, 'below')

# Manually add title
title = Label(x=1, y=1, text=["Iris plot plot"])
plot.add_layout(title)

title_2 = Label(x=0, y=0, text=["Iris plot paneled"], text_color='blue', text_font_size='12pt', x_units='screen', y_units='screen')
plot.add_layout(title_2, 'above')

big_callback = CustomJS(args=dict(title=title_2, xaxis=xaxis), code="""
    title.text_font_size='20pt'
    xaxis.major_label_text_font_size='20pt'
""")
big_button = Button(label='big', callback=big_callback)
small_callback = CustomJS(args=dict(title=title_2, xaxis=xaxis), code="""
    title.text_font_size='10pt'
    xaxis.major_label_text_font_size='10pt'
""")
small_button = Button(label='small', callback=small_callback)

circle = Circle(
    x="petal_length", y="petal_width", size=10,
    fill_color="color", fill_alpha=0.2, line_color="color"
)
plot.add_glyph(source, circle)


yaxis = LinearAxis(axis_label="petal width", bounds=(0,2.5), major_tick_in=0)
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

plot.add_tools(PanTool(), WheelZoomTool())

doc = Document()
doc.add_root(VBox(children=[big_button, small_button, plot]))

if __name__ == "__main__":
    filename = "iris.html"
    with open(filename, "w") as f:
        f.write(file_html(doc, INLINE, "Iris Data Scatter Example"))
    print("Wrote %s" % filename)
    view(filename)
