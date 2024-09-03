import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
from constants import Color


def read_data():
    data_path = Path(__file__).parents[1] / "data"
    df = pd.read_csv(data_path / "cleaned_yh_region.csv", index_col=0, parse_dates=[0])
    df.index = df.index.year
    return df


def layout():

    df = read_data()
    # to fix streamlits comma for thousands
    df_reset = df.reset_index(names=["year"]).style.format({"year": lambda x: f"{x}"})
    st.title("YH dashboard")

    st.write("This is a simple dashboard about yrkeshögskola")

    st.header("Raw data")
    st.write("This data shows number of started educations per region and per year")
    st.dataframe(df_reset)

    st.header("Trends per region")
    region = st.selectbox("Choose region", df.columns)

    region_stats = df[region].describe()
    cols = st.columns(4)
    stats = ["min", "50%", "max"]
    labels = ["min", "median", "max"]
    for col, stat, label in zip(cols, stats, labels):
        with col:
            st.metric(label=label, value=f"{region_stats[stat]:.0f}")

    fig = px.line(
        data_frame=df,
        x=df.index,
        y=df[region],
        title=f"started educations in {region} 2007-2023",
        labels={"index": "year", region: "started educations"},
    )

    fig.update_traces(
        line=dict(
            width=4,
            color=Color.PRIMARY,
        )
    )
    fig.update_layout(
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        paper_bgcolor=Color.BACKGROUND,
        plot_bgcolor=Color.BACKGROUND,
    )
    st.plotly_chart(fig)

    read_css()


def read_css():
    css_path = Path(__file__).parent / "style.css"

    with open(css_path) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    # print(read_data())
    layout()
