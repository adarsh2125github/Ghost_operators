# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:01:43 2023

@author: Lenovo
"""

import numpy as np
import pickle as pk
import streamlit as st
 

t=pk.load(open("C:/Users/Lenovo/Desktop/Untitled Folder/ILPD/ILPD_Logistic.sav","rb"))
t=pk.load(open("C:/Users/Lenovo/Desktop/Untitled Folder/Stroke_prediction/LogisticR_model.sav","rb"))
a=pk.load(open("C:/Users/Lenovo/Desktop/Untitled Folder/Diabetic paitents/trained_model.sav",'rb'))


def diabetic_predictive_system(t):
    y=np.asarray(t)
    u=y.reshape(1,-1)
    i=a.predict(u)
    print(i)
    if(i==1):
      return """You are Prone to be having diabetes ,Some of the common ways to treat diabetes include:

1.Taking medications, such as insulin injections or oral drugs, to lower blood sugar levels and prevent complications.\n
2.Monitoring blood sugar levels regularly and adjusting medications accordingly.\n
3.Following a healthy diet that is low in sugar, fat, and salt, and high in fiber, protein, and complex carbohydrates.\n
4.Exercising regularly to improve blood circulation, reduce stress, and maintain a healthy weight.\n
5.Quitting smoking and limiting alcohol intake, as these can worsen diabetes and increase the risk of complications.\n
6.Managing other health conditions, such as high blood pressure, high cholesterol, and kidney disease, that can affect diabetes.\n
7.Seeking regular check-ups and screenings from health care providers to monitor diabetes and prevent or treat any complications.\n


Some of the best hospitals and clinics for diabetes treatment in India are:

1.All India Institute of Medical Sciences (AIIMS), New Delhi\n
2.Christian Medical College (CMC), Vellore\n
3.Apollo Hospitals, Chennai\n
4.Medanta - The Medicity, Gurugram\n
5.Fortis Hospital, Mumbai\n"""
    else:
      return """I can help you sort this paragraph into points and summarize it in 100 words. Here is the result:

1.Get tested for diabetes regularly, especially if you have risk factors.\n
2.Follow a healthy diet that is low in sugar, fat, and salt, and high in fiber, protein, and complex carbohydrates. Consult a dietitian if needed.\n
3.Exercise regularly to lower your blood sugar, boost your insulin sensitivity, and maintain a healthy weight. Do both aerobic and resistance exercises.\n
4.Avoid smoking and limit alcohol to prevent worsening your diabetes and increasing your risk of complications.\n
5.Monitor your blood sugar and take your medications as instructed by your health care provider. Know the side effects and warning signs of your medications and blood sugar levels.\n
6.Seek regular check-ups and screenings from your health care provider and other specialists to monitor your diabetes and prevent or treat any complications.\n"""

def  stroke_predictive_system(t):
    k=np.asarray(t)
    j=k.reshape(1,-1)
    h=t.predict(j)
    print(h)
    if(h==0):
      return""" tips for a person who is prone to stroke:

1.Lower your blood pressure by eating healthy, exercising, and taking medications.\n
2.Lose weight if you are overweight or obese by reducing calories and increasing activity.\n
3.Exercise more by doing at least 150 minutes of moderate-intensity aerobic exercise per week.\n
4.Drink alcohol in moderation, no more than one or two drinks per day.\n
5.Treat atrial fibrillation and diabetes by taking blood thinners, antiarrhythmic drugs, or controlling blood sugar levels.\n
6.Quit smoking to reduce your risk of stroke by half within two years.\n"""
    else:
      return"""You are completely fit but some points to prevent you from strokes are:
1.Keep your blood pressure, cholesterol, and blood sugar in normal ranges\n
2.Quit smoking if you are a smoker\n
3.Maintain a healthy weight\n
4.Be physically active\n
5.Limit your alcohol intake\n
6.Consult your doctor before changing your lifestyle\n
6.Seek emergency help if you have heart stroke symptoms\n"""
def Predictive_System(l):

    k=np.asarray(l)
    j=k.reshape(1,-1)
    h=t.predict(j)
    if(h==0):
        return ("""you are suffering from lever issue,
The treatment for liver problems depends on the cause and severity of the condition.
Some general tips are:

1.Follow a healthy diet that is low in salt, fat, and sugar, and high in fruits, vegetables, whole grains, and lean protein.\n
2.Avoid alcohol, tobacco, and other substances that can harm the liver.\n
3.Take prescribed medications as directed and avoid over-the-counter drugs that can damage the liver, such as acetaminophen.\n
4.Exercise regularly and maintain a healthy weight.\n
5.Get vaccinated for hepatitis A and B, and avoid exposure to hepatitis C and other viral infections that can affect the liver.\n
6.Seek medical attention if you have symptoms of liver problems, such as jaundice, abdominal pain, swelling, nausea, vomiting, or fatigue.\n
7.If the liver damage is severe or irreversible, a liver transplant may be needed.\n""")
    else:
        return ("""You are not suffering from any sort of liver issue.
Some tips to prevent any liver issue for a longer term are:

1.Eat a healthy diet that is low in salt, fat, and sugar, and high in fruits, vegetables, whole grains, and lean protein.\n
2.Avoid alcohol, tobacco, and other substances that can harm the liver.\n
3.Take prescribed medications as directed and avoid over-the-counter drugs that can damage the liver, such as acetaminophen.\n
4.Exercise regularly and maintain a healthy weight.\n
5.Get vaccinated for hepatitis A and B, and avoid exposure to hepatitis C and other viral infections that can affect the liver.\n
6.Be careful with traditional medicine and remedies.\n
7.Be careful of weight loss pills or fad diets.\n""")
def main():
    st.title("PERSONALISED HEALTHCARE RECOMMENDATION SYSTEM")
    name=st.text_input("Give the prediction model you would like to choose: ")
    if name.lower()=="liver":
        st.title("LIVER INFECTION CHEAKUP SYSTEM")
        age=st.number_input("AGE")
        gender=st.number_input("gender:")
        tot_bilirubin=st.number_input("tot_bilirubin Value")
        direct_bilirubin=st.number_input("direct_bilirubin Value")
        tot_proteins=st.number_input("tot_proteins Value")
        albumin=st.number_input("albumin Value")
        ag_ratio=st.number_input("ag_ratio Value")
        sgpt=st.number_input("sgpt Value")
        sgot=st.number_input("sgot Value")
        alkphos=st.number_input("alkphos Value ")
        pred=""
          
        if st.button(" LIVER INFECTION CHEAKUP SYSTEM Result"):
            pred=Predictive_System([age,gender,tot_bilirubin,direct_bilirubin,tot_proteins,albumin,ag_ratio,sgpt,sgot,alkphos])
         
        st.success(pred)
    elif name.lower()=="stroke":
        st.title("STROKE PREDICTION MODEL")
        
        age =st.number_input("age of person")
        
        hypertension=st.text_input("hypertension level")
        heart_disease=st.text_input("heart_disease")
        avg_glucose_level=st.text_input("avg_glucose_level")
        bmi=st.text_input("BMI")
        Sex=st.text_input("SEX")
        Address=st.text_input("Address")
        Designation=st.text_input("Designation")
        Smoker=st.text_input("Smoker")
        Marriage=st.text_input("Marriage")
        
        diagonsis =''
        
        if st.button("Stroke Test Result"):
            diagonsis=stroke_predictive_system([age,hypertension,heart_disease,avg_glucose_level,bmi,Sex,Address,Designation,Smoker,Marriage ])
        
        st.success(diagonsis)
    elif name.lower()=="diabetes":
        st.title("DIABETES PREDICTION MODEL")
        
        
        Pregnancies=st.text_input("Number of Pregnancy")
        Glucose=st.text_input("Glucose Level")
        BloodPressure=st.text_input("Blood Pressure")
        SkinThickness=st.text_input("Skin Thickness")
        Insulin=st.text_input("Insulin Level")
        BMI=st.text_input("BMI value")
        DiabetesPedigreeFunction=st.text_input("Diabetes Pe digree Function")
        Age=st.text_input("Age of Person")
        
        diagnosis =''
        
        if st.button("Diabetes Test Result"):
            diagnosis=diabetic_predictive_system([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
            
        
        
        st.success(diagnosis)


if __name__=="__main__":
    main()