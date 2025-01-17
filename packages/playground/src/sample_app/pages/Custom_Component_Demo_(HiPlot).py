### Sample code copied from https://facebookresearch.github.io/hiplot/tuto_streamlit.html ###
import json
import streamlit as st
import hiplot as hip

x1, x2, x3 = st.slider('x1'), st.slider('x2'), st.slider('x3')

# Create your experiment as usual
data = [{'uid': 'a', 'dropout': 0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD', 'x': x1},
        {'uid': 'b', 'dropout': 0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam', 'x': x2},
        {'uid': 'c', 'dropout': 0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam', 'x': x3}]
xp = hip.Experiment.from_iterable(data)

# Instead of calling directly \`.display()\`
# just convert it to a streamlit component with \`.to_streamlit()\` before
ret_val = xp.to_streamlit(ret="selected_uids", key="hip").display()

st.markdown("hiplot returned " + json.dumps(ret_val))
