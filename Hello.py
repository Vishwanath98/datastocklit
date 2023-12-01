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

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import requests

def topgl():
    
    top_gl_url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=OEW6DWI5S3P1B2N1'


    r = requests.get(top_gl_url)
    data = r.json()
    
    top_gainers_df = pd.DataFrame(data['top_gainers'])
    top_losers_df = pd.DataFrame(data['top_losers'])
    most_actively_traded_df = pd.DataFrame(data['most_actively_traded'])
    
    top_gainers_df['category'] = 'Top Gainers'
    top_losers_df['category'] = 'Top Losers'
    most_actively_traded_df['category'] = 'Most Actively Traded'

    # Concatenate the DataFrames vertically
    merged_df = pd.concat([top_gainers_df, top_losers_df, most_actively_traded_df], ignore_index=True)
    merged_df['change_percentage'] = merged_df['change_percentage'].replace('%', '', regex=True)

    # Convert columns to numeric if needed
    numeric_columns = ['price', 'change_amount', 'change_percentage', 'volume']
    merged_df[numeric_columns] = merged_df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
    return merged_df

#topgl().to_csv('day_topstocks.csv', index=True)
day_top=topgl()
# Load your data
day_top = pd.read_csv('day_topstocks.csv')
econ_ind = pd.read_csv('economic_indicatorsvc.csv')
option_data = pd.read_csv('outputt.csv')

# Assuming day_top DataFrame has columns: 'Stock', 'Change'
# 'Change' column can be positive for gainers and negative for losers


# Separate top gainers and top losers
top_gainers = day_top[day_top['category']=='Top Gainers']  # Adjust the number based on your preference
top_losers = day_top[day_top['category']=='Top Losers']  # Adjust the number based on your preference
most_actively_traded = day_top[day_top['category'] == 'Most Actively Traded'] # Adjust the number based on your preference

# Create a Streamlit app
st.title('Day Top Gainers and Losers')


fig,(ax1, ax3) = plt.subplots(ncols=2, figsize=(50,40))
ax1.barh(top_losers['ticker'], top_losers['change_percentage'], color='red')
ax1.set_xlabel('Change Percentage (%)',fontsize=25)
ax1.set_ylabel('Ticker',fontsize=25)
ax1.set_title('Top Gainers and Losers',fontsize=25)
ax1.tick_params(axis='both', labelsize=25)

# Create a second y-axis for top gainers on the right side
ax2 = ax1.twinx()
ax2.barh(top_gainers['ticker'], top_gainers['change_percentage'], color='green')
ax2.set_ylabel('Ticker',fontsize=25)
ax2.tick_params(axis='both', labelsize=25)


ax3.bar(most_actively_traded['ticker'], most_actively_traded['volume'], color='orange')
ax3.set_xlabel('Volume (in 100M)', fontsize=25)
ax3.set_ylabel('Ticker', fontsize=25)
ax3.set_title('Most Actively Traded', fontsize=25)
ax3.tick_params(axis='both', labelsize=25)

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
st.pyplot(fig)
