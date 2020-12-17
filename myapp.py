"""
Name: Julia Towers
CS230: Section 005
Data: mcdonalds_clean1 (2).csv
URL: Link to your web application online 

Description: This program imports the McDonalds csv file to run queries.
My streamlit program starts off on a home page which shows an image of McDonalds
and the hyperlink to their webpage. Then on the left there is a select box where the user
can select what the want to see next. The map page shows a map and has all of the McDonalds
locations shown using a red dot. A zoom filter is shown on the left so the user can choose which
state the user would like to zoom in on.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import streamlit.components.v1 as components
#import pivottablejs
from pivottablejs import pivot_ui   #this is used to create the scrolling pivot table
#import numpy as np
#import statistics


# This is a select box that allows the user to chose which page they would like to view
# The options to chose from are the Home Page, Map, Bar Chart, and Pivot Table
functionOption = ["Home","Map","Stacked Bar Chart","Pivot Table"]
choseoption = st.sidebar.selectbox("Select a function to view ", functionOption)
print(choseoption)

# if home is selected this is the code that will be run
if choseoption == "Home":
    st.title('McDonalds Final Project')  #title

    st.markdown("McDonalds Official Website: ""https://www.mcdonalds.com/us/en-us.html", unsafe_allow_html=True,)
    #hyperlink to McDonalds webpage is shown in streamlit markdown

    from PIL import Image   #The McDonalds image is imported using the Python Imaging Library
    image = Image.open('mcdonalds.image.png')
    st.image(image, caption="McDonalds Logo", use_column_width=False, output_format='png')
    file = "mcdonalds_clean1 (2).csv" #name of the file
    #use pandas to read the csv file, show there is a header and the names
    df = pd.read_csv(file, header=0, names=["lon", "lat", "store num", "store type", "address", "city", "state", "zip", "phone", "play space", "drive thru", "arch card", "free wifi", "store URL"]) #reads the file
    df.columns = ["lon", "lat", "store num", "store type", "address", "city", "state", "zip", "phone", "play space", "drive thru", "arch card", "free wifi", "store URL"] #the dataframes column names

    st.subheader("McDonalds Data - Sorted Table ")
    st.write("The table shown is McDonalds data sorted in ascending order by store number")
    sortdata=df.sort_values(['store num'], ascending=[True], inplace=True) #shows the head of the data in ascending order by store number
    st.table(df.head())

#if map is selected this is the code that will be run to show McDonalds locations on a map
elif choseoption == "Map":
    file = "mcdonalds_clean1 (2).csv" #name of the file
    #use pandas to read the csv file, show there is a header and the names
    df = pd.read_csv(file, header=0, names=["lon", "lat", "store num", "store type", "address", "city", "state", "zip", "phone", "play space", "drive thru", "arch card", "free wifi", "store URL"]) #reads the file
    df.columns = ["lon", "lat", "store num", "store type", "address", "city", "state", "zip", "phone", "play space", "drive thru", "arch card", "free wifi", "store URL"] #the dataframes column names

    st.subheader('Map of McDonalds Locations: ')
    st.write(f"Below is a map used to show Mcdonalds locations using red dots. Using the select box function on the left select a state to zoom in on.")
    df2 = df[['lon', 'lat', 'state']]
    stateOption = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY"]

    stateZoom = st.sidebar.selectbox("Select a state to zoom in on: ", stateOption)  #zoom parameter that zooms in on selected state
    df2 = df2.loc[(df["state"] == stateZoom)] #this is what takes the selected state option from the select box and zooms in on the selected state
    st.map(df2)

    #tool tips
    #tool_tip = {"html": "Address:<br/> <b>{address}</b",
    #            "style":{"backgroundColor": "red", "color": "white"}}

#if Bar Chart is selected this is the code that will be run to show McDonalds data using the filters selected
elif choseoption == "Stacked Bar Chart":
    st.subheader("McDonalds Stacked Bar Chart: ")
    st.write(f"Below is stacked bar chart for McDonalds stores in each state")
    state = ["AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY"]
    files = "mcdonalds_clean1 (2).csv"
    dataframe = pd.read_csv(files, header=0, names=["lon", "lat", "store num", "store type", "address", "city", "state", "zip", "phone", "play space", "drive thru", "arch card", "free wifi", "store URL"])

    groupby_count = dataframe.groupby(['state']).count() #a group by state counting all the values for the states
    st.bar_chart(groupby_count)       #plotting each states total count for each of the other values


#if Pivot Table is selected this is the code that will be run to show all of McDonalds data and the count for each column's values
elif choseoption == "Pivot Table":
    files = "mcdonalds_clean1 (2).csv"
    df = pd.read_csv(files, header=0, names=["lon", "lat", "store num", "store type", "address", "city", "state", "zip", "phone", "play space", "drive thru", "arch card", "free wifi", "store URL"])
    df.columns = ["lon", "lat", "store num", "store type", "address", "city", "state", "zip", "phone", "play space", "drive thru", "arch card", "free wifi", "store URL"]

    st.subheader('Pivot Table of McDonalds Data')
    st.write("This shows all of the choices inside the McDonalds CSV file. Use the drop"
              "down arrows to see the value count of Mcdonalds for the selected choice.")

    t = pivot_ui(df)
    with open(t.src) as t:
        components.html(t.read(), width=700, height = 400, scrolling=True)  #pivot table with scrolling features
        plt.show()


# This pivot table uses the install pivottablejs package
# from pivottablejs import pivot_ui used for streamlit to read the data frame through
# the pivot table and opens it as in the src layout. With the data frame open thought the directory
# and with the src layout, the components are run.
# takes the components through the data frame and then shows the pivot table with a width of 700,
# height of 400 and enabled a scrolling feature.

