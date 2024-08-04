import streamlit as st 
from data import MedalsPerCountry

medals_per_country = MedalsPerCountry()

class Metrics:    
    def country_medals_top_5(self):
        
        st.markdown("## Top 5 countries with most medals")
        cols = st.columns(5)

        for col, country, data in zip(
            cols, medals_per_country.summer_noc.index, medals_per_country.summer_noc
        ):
            with col:
                st.metric(
                    label=country,
                    value=data,
                )

