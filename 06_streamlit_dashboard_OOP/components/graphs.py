from components.data import SwedishSummerMedals
import streamlit as st

class SwedishSummerGraphs:
    def __init__(self) -> None:
        self.swe_medals = SwedishSummerMedals()

    def bar_medals_sport(self):
        data = self.swe_medals.per_sport
        st.bar_chart(data, x_label="sport", y_label="medals per sport")

    def bar_medals_athlete_top10(self):
        data = self.swe_medals.per_athlete.iloc[:10]
        st.bar_chart(data, x_label="athlete", y_label="medals per athlete")