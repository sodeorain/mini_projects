from shiny import ui, render, App, reactive
import pandas as pd

# User Interface
app_ui = ui.page_fluid(
    ui.input_slider(id = "n", label = "N", min = 0, max = 100, value = 40),
    ui.output_text_verbatim(id = "txt"),
    ui.hr(),
    ui.h3("Data Frame from CSV"),
    ui.output_table(id="data_table"),
    ui.h3("Another Data Frame from CSV"),
    ui.output_table(id="data_table_1")
)

# Server function
def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"
    
    @output
    @render.table
    def data_table():
        # Read the CSV file using pandas
        df = pd.read_csv("NSA54.20250415T200436.csv")
        df_selected = df[["Year", "VALUE"]]
        df_filtered = df_selected.groupby("Year", as_index=False).mean() # important to add "as_index=False" otherwise the year is lost !
        return df_filtered
    
    @output
    @render.table
    def data_table_1():
        # Read the CSV file using pandas
        df1 = pd.read_csv("NSA54.20250415T200436.csv")
        return df1

# This is a shiny.App object. It must be named `app`.
app = App(app_ui, server)