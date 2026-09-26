# Loan_default_predictor
Loan default predictor using Logistic regression only

## 📋 Table of Contents
- [About](#about)
- [Dataset](#dataset)
- [Demo](#Demo)
- [Usage](#usage)
- [Model / Approach](#model--approach)
- [Results](#results)

# ABOUT 🔥
This is a simple project of a Loan default predictor using only the concepts of Logistic regression

# Demo 
<img width="1917" height="1034" alt="Screenshot 2026-09-26 220950" src="https://github.com/user-attachments/assets/5db9f6a8-b42d-4dfb-b5bd-a242d52348ef" />
<img width="1917" height="1018" alt="Screenshot 2026-09-26 221519" src="https://github.com/user-attachments/assets/08a9ccd9-0fef-4e8d-a00f-8d0b95f0bcf4" />
<img width="1917" height="1026" alt="Screenshot 2026-09-26 222200" src="https://github.com/user-attachments/assets/30c340d1-d45d-425a-863a-d386b3115024" />

# Dataset 📈
The dataset used for training this model was taken from Kaggle 
link :- https://www.kaggle.com/datasets/nikhil1e9/loan-default

# Usage ⚙️
- To use this model/code , just download all the files attached onto a same folder
- In terminal run the following command :- streamlit run main_page.py
- If using vs code then open main_page.py file then in the terminal of the vs code enter :- streamlit run main_page.py 

# Approach 🧠
Following were the steps taken :-
- Acquiring a good and usable dataset
- Doing some feature engineering like removing low contributing column.
- Using Logistic Regression model with L1 penalty system so that it indirectly does the job of feature selection
- Instead of building a CLI interface used Streamlit for making a web app so that its more visually appealing
- Designing web app in Streamlit and also attaching model to the web app
- Making predictions !!

# Results 📄
- The following results are obtained after doing many tweaks into the model such as trying different scaling methods , varying the intensity of penalty etc.
- Accuracy :- 0.5658
- Precision :- 0.1814
- Recall :- 0.7809
- F1 :- 0.2943

# Note 📝
- We could have used any other algorithms which would have given much more better results than this model , but honestly this is the proof of work after learning Logistic Regression and only using it to make a model by fully understanding it.
- Also according to me having low precision and F1 is obvious as this model is made only using logistic regression not any other boosting technique etc . But having a good Recall in this type of problem is good as its always better to flag a non-defaulter as defaulter rather than leaving a defaulter and flagging him/her as non-defaulter .
