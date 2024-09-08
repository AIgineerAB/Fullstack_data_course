import streamlit as st  
from components.data import MedalsPerCountry

medals_per_country = MedalsPerCountry()

class Metrics:
    def country_medals_top_5(self):
        st.markdown("## Top 5 countries with most medals")
        cols = st.columns(5)

        for col, country, data in zip(cols, medals_per_country.summer_noc.index, medals_per_country.summer_noc):
            with col:
                st.metric(label=country, value=data)

class MedalsCountry:
    def __init__(self, country) -> None:
        self.country = country
        self._medals_per_country = MedalsPerCountry()
        self._summer_medals_type = self._medals_per_country.summer_medals_type

    def _total(self):
        medals_series = self._medals_per_country.summer_noc

        st.metric(label="Total medals", value=medals_series[self.country])

    def display_medals(self):
        cols = st.columns(4)
        medals = (self._total, self._gold, self._silver, self._bronze)
        for col, medal in zip(cols, medals):
            with col:
                medal()

    def _gold(self):
        st.metric(
            label="Gold medals", value=self._summer_medals_type["Gold"][self.country]
        )

    def _silver(self):
        st.metric(
            label="Silver medals",
            value=self._summer_medals_type["Silver"][self.country],
        )

    def _bronze(self):
        st.metric(
            label="Bronze medals",
            value=self._summer_medals_type["Bronze"][self.country],
        )