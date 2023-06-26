# Simple Python Application for Coordinate Extrapolation (SPACE)

import streamlit as st
import pandas as pd

from locationutils import Geocoder
from locationutils import PhysicalLocation
def main():
    # Load the image file
    with open('spacey.gif', 'rb') as f:
        image_data = f.read()
    st.image(image_data)

    st.write("Welcome to")
    st.title("S.P.A.C.E")
    st.write("Simple Python Application for Coordinate Extrapolation")
    text = """
    This application receives a .csv or .xls with columns containing (at minimum)
    LATITUDE and LONGITUDE columns. The names of these columns must be capitalized
    and spelled as shown here.
    
    The application will perform reverse geocoding operations on each lat/long
    pair, and return a .csv file with address information. 
    """
    st.write(text)
    # Receive spreadsheet from user
    uploaded_file = st.file_uploader("Upload spreadsheet file", type=["csv", "xlsx"])

    # Create dataframe and additional columns
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df['house_number'] = None
        df['road'] = None
        df['town'] = None
        df['state'] = None
        df['postcode'] = None
        df['country'] = None

        # Create a button to begin processing
        button = st.button('Continue')

        if button:
            # Provide a status bar - operations can take a long time
            bar = st.progress(0, text="Progress")
            # Iterate through dataframe
            for index, row in df.iterrows():
                latitude = str(row['LATITUDE'])
                longitude = str(row['LONGITUDE'])
                # decode lat/long using nominatim backend in loactionutils
                geocoder = Geocoder()
                location = geocoder.reverse(latitude, longitude)
                # standardize the responses
                physical = PhysicalLocation(location)
                df.loc[index, "house_number"] = physical.house_number
                df.loc[index, "road"] = physical.road
                df.loc[index, "town"] = physical.town
                df.loc[index, "state"] = physical.state
                df.loc[index, "postcode"] = physical.postcode
                df.loc[index, "country"] = physical.country
                # Update the status bar
                progress_text = f"{index + 1} of {len(df)}"
                bar.progress(int(index) / len(df), text=progress_text)
                progress_text = f"Complete: {len(df)}"
            bar.progress(100, text=progress_text)
            st.write("File Preview")
            st.write(df)
            st.write("File Download")
            df.to_csv('data.csv')
            # Provide download mechanism
            st.download_button('Download', file_name='data.csv', data=df.to_csv(index=False))

if __name__ == "__main__":
    main()
