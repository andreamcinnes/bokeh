from __future__ import print_function

import numpy as np
from bokeh.util.browser import view
from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.models.glyphs import Circle
from bokeh.models import (
    Plot, DataRange1d, LinearAxis, Grid, ColumnDataSource, PanTool, WheelZoomTool, Label
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

plot = Plot(x_range=xdr, y_range=ydr, min_border=20, plot_height=300, border_fill_color='aliceblue')

circle = Circle(
    x="petal_length", y="petal_width", size=10,
    fill_color="color", fill_alpha=0.2, line_color="color"
)
plot.add_glyph(source, circle)

xaxis = LinearAxis(bounds=(1,7), major_tick_in=0)
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis(bounds=(0,2.5), major_tick_in=0)
plot.add_layout(yaxis, 'left')

title = Label(x=0, y=0, text=["Iris plot"], x_units='screen', y_units='screen')
plot.add_layout(title, 'above')

left_title = Label(x=0, y=0, text=["Petal width"], x_units='screen', y_units='screen', angle=np.pi/3)
plot.add_layout(left_title, 'left')

below_title = Label(x=0, y=0, text=["Petal length"], x_units='screen', y_units='screen')
plot.add_layout(below_title, 'below')

right_title = Label(x=0, y=0, text=["Right label"], x_units='screen', y_units='screen')
plot.add_layout(right_title, 'right')

misc = Label(x=1, y=1, text=["Some stuff"], angle=np.pi/3)
plot.add_layout(misc)

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

plot.add_tools(PanTool(), WheelZoomTool())

doc = Document()
doc.add_root(plot)

if __name__ == "__main__":
    filename = "iris.html"
    with open(filename, "w") as f:
        f.write(file_html(doc, INLINE, "Iris Data Scatter Example"))
    print("Wrote %s" % filename)
    view(filename)
