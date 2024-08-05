import streamlit as st
from graphs import SwedishSummerGraphs
from components.metrics import Metrics, MedalsCountry
from data import Countries

swedish_graphs = SwedishSummerGraphs()
metrics = Metrics()
countries = Countries()

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

    st.markdown("## Medals filter country")
    selected_country = st.selectbox("Select a country", options=countries.noc)
    print(selected_country)
    MedalsCountry(selected_country).display_medals()




if __name__ == "__main__":
    layout()
