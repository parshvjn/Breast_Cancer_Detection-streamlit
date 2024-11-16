import streamlit as st
import pandas as pd
import joblib
from warnings import filterwarnings
filterwarnings('ignore')
st.set_page_config(layout = 'wide')
model = joblib.load('logistic_model.pkl', 'r')

inputs = [f'data {x}' for x in range(1, 31)]

st.header('Breast Cancer Detection')
file_upload, manual = st.tabs(['File Upload', 'Manual Entry'])

placeHolders =['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']

def file_uploader():
    extensions = ['csv', 'xlsx']
    upload = st.file_uploader("Upload the file", type = extensions)
    if upload != None: 
        if upload.name.split('.')[-1] not in extensions:
            st.toast("Please choose only xlsx or csv file")
        else:
            if upload.name.split('.')[-1] == 'csv':
                df = pd.read_csv(upload)
                # if list(df.columns) in placeHolders:
                for i in df.values:
                    st.write(i)
                # else:
                    # st.toast('Please upload the file required')
                # st.write(df)
file_uploader()
# meanRadius, meanTexture, meanPerimeter, meanArea, meanSmoothness = st.columns(5)


values = []

with manual:
    # for x in range(30):
    #     values.append(st.text_input(label = inputs[x]))
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    for i, item in enumerate(placeHolders):
        with col1 if i <= 4 else col2 if i <= 9 else col3 if i <= 14 else col4 if i <= 19 else col5 if i <= 24 else col6:
            temp = st.text_input(label = item)
            values.append(temp)

    if st.button(label = 'submit'):
        valueCheck = [True if len(i) > 0 else False for i in values]
        if all(valueCheck):
            values = [float(i) for i in values]
            prediction = model.predict([values])
            st.write(prediction)
            st.text(f"Detected Type: {'Melanin' if prediction[0] == 0 else 'Benign'}")
        else:
            st.toast('Please fill up all inputs')

