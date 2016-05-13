from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.models import Row, Column
from bokeh.resources import INLINE
from bokeh.util.browser import view

layout = Column(
    Row(Column(), Column()),
    Row(Column(), Column()),
    Row(),
    Row(Column(), Column()),
)

doc = Document()
doc.add_root(layout)

if __name__ == "__main__":
    filename = "row_column_empty.html"
    with open(filename, "w") as f:
        f.write(file_html(doc, INLINE, "Empty rows and columns."))
    print("Wrote %s" % filename)
    view(filename)
