import pandas as pd
import parser_1
import plotly
import plotly.express as px


def map2D(filename):
    data = parser_1.readTextFile(filename)
    df = pd.DataFrame.from_records(data)

    # plotting map using plotly
    # add altitude and time
    fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', zoom=13)

    # setting title for the map
    # Different style: "open-street-map"
    fig.update_layout(mapbox_style="stamen-terrain")

    # displaying the map
    # fig.show()

    plotly.offline.plot(fig, filename=f'/Users/dasa3/PycharmProjects/fight_dashboard_v2/static/{filename}_2D.html')
