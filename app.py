import streamlit as st

import joblib

import string

import random

import math


# -----------------------------
# Load Model
# -----------------------------

model = joblib.load(
    "SecurePass_AI.pkl"
)



# -----------------------------
# Feature Engineering
# SAME AS TRAINING
# -----------------------------

def password_features(password):

    password = str(password)


    return [

        len(password),

        sum(c.isupper() for c in password),

        sum(c.islower() for c in password),

        sum(c.isdigit() for c in password),

        sum(c in string.punctuation for c in password),

        len(set(password)),

        password.count(" "),


        int(any(c.isupper() for c in password)),

        int(any(c.isdigit() for c in password)),

        int(any(c in string.punctuation for c in password))

    ]





# -----------------------------
# Password Generator
# -----------------------------

def generate_password(length=14):

    chars = (

        string.ascii_letters +

        string.digits +

        string.punctuation

    )


    return "".join(

        random.choice(chars)

        for i in range(length)

    )





# -----------------------------
# Entropy Calculator
# -----------------------------

def entropy(password):

    pool = 0


    if any(c.islower() for c in password):
        pool += 26


    if any(c.isupper() for c in password):
        pool += 26


    if any(c.isdigit() for c in password):
        pool += 10


    if any(c in string.punctuation for c in password):
        pool += 32


    if pool == 0:
        return 0


    return round(

        len(password) *

        math.log2(pool),

        2

    )





# -----------------------------
# Streamlit UI
# -----------------------------


st.set_page_config(

    page_title="SecurePass AI",

    page_icon="🔐"

)


st.title(
    "🔐 SecurePass AI"
)


st.write(
    "AI powered password strength checker and secure password generator"
)





password = st.text_input(

    "Enter your password",

    type="password"

)





if password:


    features = password_features(password)


    prediction = model.predict(

        [features]

    )[0]



    probability = model.predict_proba(

        [features]

    )[0]



    confidence = round(

        max(probability)*100,

        2

    )



    if prediction == 0:

        result = "Weak"

        st.error(
            "❌ Weak Password"
        )


    elif prediction == 1:

        result = "Medium"

        st.warning(
            "⚠️ Medium Password"
        )


    else:

        result = "Strong"

        st.success(
            "✅ Strong Password"
        )



    st.metric(

        "AI Confidence",

        f"{confidence}%"

    )


    st.metric(

        "Password Entropy",

        f"{entropy(password)} bits"

    )




    st.subheader(
        "Security Analysis"
    )


    if len(password)<8:

        st.write(
            "❌ Increase password length"
        )


    if not any(c.isupper() for c in password):

        st.write(
            "❌ Add uppercase letters"
        )


    if not any(c.isdigit() for c in password):

        st.write(
            "❌ Add numbers"
        )


    if not any(c in string.punctuation for c in password):

        st.write(
            "❌ Add special characters"
        )





    if prediction != 2:


        st.subheader(
            "Suggested Strong Password"
        )


        st.code(

            generate_password()

        )





# -----------------------------
# Generate button
# -----------------------------


st.divider()


st.subheader(
    "Generate Secure Password"
)


if st.button(
    "Generate Password"
):

    st.code(

        generate_password()

    )
