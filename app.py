import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

# Page configuration
st.set_page_config(
    page_title="Mushroom Classifier",
    page_icon="🍄", 
    layout="wide",  # Layout of the app, options: "centered", "wide"
)

# Mapping dictionaries
cap_shape_map = {
    'bell': 'b', 'conical': 'c', 'convex': 'x', 'flat': 'f',
    'sunken': 's', 'spherical': 'p', 'others': 'o'
}

cap_color_map = {
    'brown': 'n', 'buff': 'b', 'gray': 'g', 'green': 'r', 'pink': 'p',
    'purple': 'u', 'red': 'e', 'white': 'w', 'yellow': 'y', 'blue': 'l',
    'orange': 'o', 'black': 'k'
}

does_bruise_bleed_map = {
    'yes': 't', 'no': 'f'
}

gill_color_map = {
    'brown': 'n', 'buff': 'b', 'gray': 'g', 'green': 'r', 'pink': 'p',
    'purple': 'u', 'red': 'e', 'white': 'w', 'yellow': 'y', 'blue': 'l',
    'orange': 'o', 'black': 'k', 'none': 'f'
}

stem_color_map = {
    'brown': 'n', 'buff': 'b', 'gray': 'g', 'green': 'r', 'pink': 'p',
    'purple': 'u', 'red': 'e', 'white': 'w', 'yellow': 'y', 'blue': 'l',
    'orange': 'o', 'black': 'k', 'none': 'f'
}

has_ring_map = {
    'ring': 't', 'none': 'f'
}

habitat_map = {
    'grasses': 'g', 'leaves': 'l', 'meadows': 'm', 'paths': 'p', 'heaths': 'h',
    'urban': 'u', 'waste': 'w', 'woods': 'd'
}

season_map = {
    'spring': 's', 'summer': 'u', 'autumn': 'a', 'winter': 'w'
}

class_labels = {0: 'poisonous', 1: 'edible'}

st.title('Mushroom Classifier')
st.markdown("""
    ## Welcome to the Mushroom Classifier
    This tool helps you determine whether a mushroom is poisonous or edible based on various features. 
    Please provide the details below and click **Predict** to see the classification.
""")

# Layout configuration
col1, col2, col3 = st.columns([1, 0.2, 2])

with col1:
    st.subheader('Mushroom Features')
    cap_diameter = st.slider('Cap Diameter (cm)', min_value=0.0, max_value=20.0, value=5.0, step=0.1, format="%.1f")
    cap_shape = st.selectbox('Cap Shape', list(cap_shape_map.keys()))
    cap_color = st.selectbox('Cap Color', list(cap_color_map.keys()))
    does_bruise_bleed = st.selectbox('Does it Bruise or Bleed?', list(does_bruise_bleed_map.keys()))
    gill_color = st.selectbox('Gill Color', list(gill_color_map.keys()))
    stem_height = st.slider('Stem Height (cm)', min_value=0.0, max_value=30.0, value=10.0, step=0.1, format="%.1f")
    stem_width = st.slider('Stem Width (mm)', min_value=0.0, max_value=50.0, value=10.0, step=0.1, format="%.1f")
    stem_color = st.selectbox('Stem Color', list(stem_color_map.keys()))
    has_ring = st.selectbox('Has Ring?', list(has_ring_map.keys()))
    habitat = st.selectbox('Habitat', list(habitat_map.keys()))
    season = st.selectbox('Season', list(season_map.keys()))

with col3:
    st.subheader('Prediction')
    
    # Convert inputs to model format
    input_features = {
        'cap-diameter': cap_diameter,
        'cap-shape': cap_shape_map[cap_shape],
        'cap-color': cap_color_map[cap_color],
        'does-bruise-or-bleed': does_bruise_bleed_map[does_bruise_bleed],
        'gill-color': gill_color_map[gill_color],
        'stem-height': stem_height,
        'stem-width': stem_width,
        'stem-color': stem_color_map[stem_color],
        'has-ring': has_ring_map[has_ring],
        'habitat': habitat_map[habitat],
        'season': season_map[season]
    }

    input_df = pd.DataFrame([input_features])

    if st.button("Predict", key="predict_button"):
        # Make prediction
        prediction = predict(input_df)
        predicted_label = class_labels[prediction[0]]
        
        # Display the result
        st.markdown(f"### The Mushroom is **{predicted_label}**")