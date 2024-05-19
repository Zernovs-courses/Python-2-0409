from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv("/home/gleb/Documents/Python/Python-2-0409/lessons/dash/world2015.csv")

app = Dash("My first dash")

app.layout = html.Div(
    [
        html.Div(children="Hello world! Nice to meet you!"),
        dcc.Checklist(
            df["Continent"].unique(), df["Continent"].unique(), inline=True, id="check"
        ),
        dcc.Graph(
            id="graph",
            figure=px.scatter(
                df,
                y="Life_expectancy",
                x="GDP_per_capita",
                color="Continent",
                size="Population",
                hover_name="Country",
                log_x=True,
                size_max=50,
            ),
        ),
        dash_table.DataTable(
            df.to_dict("records"),
            page_size=10,
            style_header={"backgroundColor": "rgb(30, 30, 30)", "color": "white"},
            style_data={"backgroundColor": "rgb(50, 50, 50)", "color": "white"},
        ),
    ]
)


@callback(Output("graph", "figure"), Input("check", "value"))
def check_continents(value):
    return px.scatter(
        df[df["Continent"].isin(value)],
        y="Life_expectancy",
        x="GDP_per_capita",
        color="Continent",
        size="Population",
        hover_name="Country",
        log_x=True,
        size_max=50,
    )


if __name__ == "__main__":
    app.run(debug=True)
