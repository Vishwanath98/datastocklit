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

import mplcursors  # Added for hovering support
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

economic_data = pd.read_csv('economic_indicatorsvc.csv', parse_dates=['date'])
economic_data.set_index('date', inplace=True)

st.set_page_config(page_title="Economic indicators", page_icon="📈")
# Streamlit app
st.title('Economic Indicators Line Chart')
#st.markdown("# Economic indicators")
#st.sidebar.header("Economic Indicators")
st.write(
    """This graph illustrates a combination of Economic Indicators plotted over time!"""
)



selected_columns = st.multiselect('Select Columns:', economic_data.columns)

# Plotting using matplotlib with unique colors
fig, ax = plt.subplots(figsize=(10, 6))

# Generating unique colors for each selected column
colors = plt.cm.get_cmap('tab10', len(selected_columns))

for column, color in zip(selected_columns, colors(np.arange(len(selected_columns)))):
    ax.plot(economic_data.index, economic_data[column], label=column, color=color)
    

# Plotting using matplotlib
ax.set_xlabel('Date')
#ax.set_ylabel(selected_column)
ax.set_title(f'Economic Indicators over Time')
ax.legend()

# Enable hovering support using mplcursors
mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f"{sel.artist.get_label()}: {sel.target[1]:.2f}"))

# Display the plot in Streamlit
st.pyplot(fig)


