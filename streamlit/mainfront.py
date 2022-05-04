import streamlit as st



with st.sidebar:
    st.title('-----------Menu-----------')
    st.text("")
    st.text("")
    add_selectbox = st.radio(
        "Choose one:",
        ("Home", "Neural Network", "Classificator")
    )

if add_selectbox == 'Home':
    st.write('Home')
elif add_selectbox == 'Neural Network':
    st.write('Neural Network')
elif add_selectbox == 'Classificator':
    st.title('Classificator')
    st.write("Drag into the box or click in 'browse files' to pick a file and classify in dog or cat.")
    INPUT_IMAGE = st.file_uploader('',accept_multiple_files=True)


else:
    pass