import streamlit as st 
import time as t
import pandas as pd
import main

col1,col2,col3 = st.columns([0.8,4,0.3],border=False,gap="xxsmall")
with col2:
    st.markdown(
        """
        <h1 style="
            text-align: center;
            color: #DC2626;
            font-size : 42px;
            font-weight: 700;
            margin-top: 5px;
        ">
            Loan Fraud Predictor
        </h1>
        """,
        unsafe_allow_html=True
    )
    
with col1:
    st.markdown(
        """
        <div style="
            width: 120%;
            height: 120px;
            overflow: hidden;
            border-radius: 20px;
        ">
            <video
                src="https://cdnl.iconscout.com/lottie/premium/preview-watermark/fraud-detection-animation-gif-download-5096960.mp4"
                autoplay
                loop
                muted
                playsinline
                style="
                    width: 140%;
                    height: 140%;
                    object-fit: cover;
                    margin-left: -15%;
                    margin-right: -15%;
                    margin-top: -20%;
                ">
            </video>
        </div>
        """,
        unsafe_allow_html=True
    )
    
main_container1 = st.container(border=False,gap="xsmall")
main_container2= st.container(border=False,gap="xsmall")
main_container3 = st.container(border=False,gap="xsmall")

with main_container1:
    main1_col1,main1_col2 = st.columns(2,gap="medium",border=False)

with main1_col1:
    name = st.text_input(":green[Enter the Name of person]")
    income = st.number_input(":green[Enter the income of person]",min_value=1)
    credit = st.number_input(":green[Enter the Credit score]")
    ncreditlines = st.number_input(":green[Enter the number of credit sources used]")
    loanterm = st.slider(":green[Enter the loan term in months]",0,70)
    
with main1_col2:
    age = st.number_input(":violet[Enter the age of person]",min_value=18,max_value=100)
    loan = st.number_input(":violet[Enter the loan amount taken]")
    months = st.number_input(":violet[Enter the months employed]")
    interest = st.number_input(":violet[Enter the interest rate]")
    dti = st.number_input(":violet[Enter debt-to-income ratio]",min_value=0.0,max_value=1.0,step=0.0001)
    
with main_container2:
    edu = st.selectbox(":orange[Select the education level of person]",["High School","Bachelor's","Master's","PhD"])
    employment = st.selectbox(":orange[Select the employment type of person]",["Unemployed","Self-employed","Part-time","Full-time"])
    married = st.selectbox(":orange[Select marriage status]",["Single","Married","Divorced"])
    loan_pupose = st.selectbox(":orange[Select loan purpose]",["Home","Auto","Business","Education","Other"])
    
with main_container3:
    main3_col1,main3_col2 = st.columns(2,gap="medium",border=False)
    
with main3_col1:
    mortgage = st.radio(":blue[Has Mortgage]",["Yes","No"])
    cosigner = st.radio(":blue[Has cosigner(Someone else to pay the loan)]",["Yes","No"])
    
with main3_col2:
    dependant = st.radio(":blue[Has dependants]",["Yes","No"])
    submit = st.button(":red[Submit response]")
    

result_window = st.container()

if(submit):
    list1 = []
    list1.append(age)
    list1.append(income)
    list1.append(loan)
    list1.append(credit)
    list1.append(months)
    list1.append(ncreditlines)
    list1.append(interest)
    list1.append(loanterm)
    list1.append(dti)
    list1.append(edu)
    list1.append(employment)
    list1.append(married)
    list1.append(mortgage)
    list1.append(dependant)
    list1.append(loan_pupose)
    list1.append(cosigner)
    df = pd.DataFrame([list1],columns=main.X.columns)
    prediction = main.mainpipe.predict(df)

    if(prediction==1):
        st.write(f":red[According to our prediction model, {name} is likely to be Fraud]")
        st.error(f"{name} is FRAUD according to our prediction")
    elif(prediction==0):
        st.write(f":green[According to our prediction model, {name} will not do any Fraud]")
        st.success(f"{name} is not FRAUD according to our prediction")
    t.sleep(17)
    st.rerun()
    

    
    
    
    
    
    
    
    