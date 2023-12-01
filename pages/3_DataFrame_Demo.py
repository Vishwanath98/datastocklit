# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
from streamlit.hello.utils import show_code


def data_frame_demo():
    @st.cache_data
    econ_ind = pd.read_csv('economic_indicatorsvc.csv')    

    try:
        econ_ind = pd.read_csv('economic_indicatorsvc.csv') 
        indicators = st.multiselect(
            "Choose indicators", list(econ_ind.index), ["Consumer Price Inflation", "FED Interest Rate"]
        )
        if not indicators:
            st.error("Please select at least one indicator.")
        else:
            data = econ_ind.loc[indicators]
            st.write("### Economic Data of USA", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Indicator:Q", stack=None),
                    color="Indicator:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )


st.set_page_config(page_title="DataFrame Demo", page_icon="📊")
st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This Data shows the relation between different economic indicators"""
)

data_frame_demo()

#show_code(data_frame_demo)
