import pandas as pd
import parser_1
import plotly
import plotly.express as px


def map3D(file_name):
    data = parser_1.readTextFile(file_name)
    df = pd.DataFrame.from_records(data)

    fig = px.scatter_3d(df, x='longitude', y='latitude', z='altitude')
    # fig.show()

    # html file
    plotly.offline.plot(fig, filename=f'/Users/dasa3/PycharmProjects/fight_dashboard_v2/static/{file_name}_3D.html')
