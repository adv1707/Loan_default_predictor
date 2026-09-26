import streamlit as st 
import main 


#metrics
precision = main.precision
recall = main.recall
f1 = main.f1 
accuracy = main.accuracy
confusion = main.confusion

heading = st.container(border=True,gap="small")
with heading:
    st.write(""":rainbow[This website works using a classification model known a Logistic Regression and also
             uses a L1 penalty to basically indirectly do feature selection.]""")
    st.write(''':orange[Link of the Dataset : https://www.kaggle.com/datasets/nikhil1e9/loan-default]''')
    
body = st.container(border=True)
with body:
    st.write(f":yellow[Accuracy of this model with test data is] :red[{accuracy:0.4f}]")
    st.write(f''':violet[Precision of this model with test data is] :red[{precision:0.4f}]''')
    st.write(f''':green[Recall of this model with test data is] :red[{recall:0.4f}]''')
    st.write(f''':orange[F1 of this model with test data is] :red[{f1:0.4f}]''')
    