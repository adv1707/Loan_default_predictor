import streamlit as st

model_page = st.Page("model_page.py",title="Loan Fraud predictor",icon="💳",url_path="Model")
metrics = st.Page("metrics_page.py",title=":green[Metrics] :red[and] :blue[Data]",icon="📊",url_path="Metrics",default=False)

pg = st.navigation({
    ":green[Model]":[model_page],
    ":violet[Metrics]":[metrics]
})
pg.run()
