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

import time

import numpy as np

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

economic_data = pd.read_csv('economic_indicatorsvc.csv', parse_dates=['date'])
economic_data.set_index('date', inplace=True)

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# Streamlit app
st.title('Economic Indicators Line Chart')

# Dropdown to select column
selected_column = st.selectbox('Select Column:', economic_data.columns)


st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

# Plotting using matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(economic_data.index, economic_data[selected_column])
ax.set_xlabel('Date')
#ax.set_ylabel(selected_column)
ax.set_title(f'{selected_column} over Time')


# Display the plot in Streamlit
st.pyplot(fig)



"""def plotting_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()"""

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    #st.button("Re-run")



#plotting_demo()

#show_code(plotting_demo)
