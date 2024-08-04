import streamlit as st
import pandas as pd
from graphs import SwedishSummerGraphs
from components import Metrics

swedish_graphs = SwedishSummerGraphs()
metrics = Metrics()


def layout():
    st.markdown("# Summer olympics dashboard")
    st.markdown(
        """
        This dashboard shows 124 years of olympic data. In this demo, only summer olympics will be shown.
        The source of the dataset comes from here https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020
        
        """
    )

    

    metrics.country_medals_top_5()



    st.markdown("## Medals per sport in Sweden")

    swedish_graphs.bar_medals_sport()

    st.markdown("## Medals per athlete in Sweden (top 10)")
    swedish_graphs.bar_medals_athlete_top10()

    st.markdown("## Filter selections")
    


if __name__ == "__main__":
    layout()
