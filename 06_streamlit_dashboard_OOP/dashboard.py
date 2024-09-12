import streamlit as st
from components.data import MedalsSummer, Countries
from components.metrics import Metrics, MedalsCountry
from components.graphs import SwedishSummerGraphs

# this script is slim, its purpose is to collect classes from different components
# and create objects from them so that we can use them in the layout

medals_df = MedalsSummer()
metrics = Metrics()
countries = Countries()
swedish_graphs = SwedishSummerGraphs()


def layout():
    st.markdown("# Summer olympics dashboard")
    st.markdown(
        """
        This dashboard shows 124 years of olympic data. In this demo, only summer olympics will be shown.
        The source of the dataset comes from here https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020
        
        """
    )

    metrics.country_medals_top_5()
    

    st.markdown("## Medals filter country")
    selected_country = st.selectbox("Select a country", options = countries.noc)
    MedalsCountry(selected_country).display_medals()


    st.markdown("## Medals per sport in Sweden")
    swedish_graphs.bar_medals_sport()

    st.markdown("## Medals per athlete in Sweden (top 10)")
    swedish_graphs.bar_medals_athlete_top10()




if __name__ == "__main__":
    layout()