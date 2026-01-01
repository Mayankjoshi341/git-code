import streamlit as st
from streamlit_js_eval import streamlit_js_eval
import streamlit.components.v1 as components 
import pandas as pd
import numpy as np
from joblib import load
from custom_transformers import SymptomEncoder
from GmailSender import Email_sender
from joblib import load
import re , requests
import time , folium
from streamlit_folium import st_folium
import googlemaps
model = load(r"C:\Users\mayan\OneDrive\git-projects\git-code\MyData-Warehouse\projects\MEDICSCAN\mediscan_model.pkl")
decoder = load(r"C:\Users\mayan\OneDrive\git-projects\git-code\MyData-Warehouse\projects\MEDICSCAN\Encoder.pkl")
data = pd.read_csv(r"C:\Users\mayan\OneDrive\git-projects\git-code\MyData-Warehouse\projects\MEDICSCAN\Data_final.csv")

all_symptoms = ['abdominal_pain','abnormal_menstruation','acidity','acute_liver_failure','altered_sensorium','anxiety','back_pain','belly_pain','blackheads','bladder_discomfort','blister',
 'blood_in_sputum','bloody_stool','blurred_and_distorted_vision', 'breathlessness', 'brittle_nails', 'bruising', 'burning_micturition', 'chest_pain', 'chills', 'cold_hands_and_feets',
 'coma', 'congestion', 'constipation', 'continuous_feel_of_urine', 'continuous_sneezing', 'cough', 'cramps', 'dark_urine', 'dehydration', 'depression', 'diarrhoea', 'dischromic_patches',
 'distention_of_abdomen','dizziness', 'drying_and_tingling_lips', 'enlarged_thyroid', 'excessive_hunger', 'extra_marital_contacts', 'family_history', 'fast_heart_rate', 'fatigue','fluid_overload', 'foul_smell_ofurine',
 'headache','high_fever', 'hip_joint_pain', 'history_of_alcohol_consumption', 'increased_appetite', 'indigestion', 'inflammatory_nails', 'internal_itching', 'irregular_sugar_level', 'irritability',
 'irritation_in_anus', 'itching', 'joint_pain', 'knee_pain', 'lack_of_concentration', 'lethargy', 'loss_of_appetite', 'loss_of_balance', 'loss_of_smell','malaise', 'mild_fever', 'mood_swings',
 'movement_stiffness', 'mucoid_sputum', 'muscle_pain','muscle_wasting' 'muscle_weakness', 'nausea', 'neck_pain', 'nodal_skin_eruptions', 'obesity','pain_behind_the_eyes', 'pain_during_bowel_movements',
 'pain_in_anal_region', 'painful_walking', 'palpitations','passage_of_gases', 'patches_in_throat', 'phlegm', 'polyuria','prognosis',
 'prominent_veins_on_calf','puffy_face_and_eyes', 'pus_filled_pimples', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'red_sore_around_nose', 'red_spots_over_body',
 'redness_of_eyes', 'restlessness', 'runny_nose', 'rusty_sputum','scurring' 'shivering', 'silver_like_dusting', 'sinus_pressure', 'skin_peeling', 'skin_rash','slurred_speech',
 'small_dents_in_nails', 'spinning_movements', 'spotting_urination', 'stiff_neck', 'stomach_bleeding', 'stomach_pain', 'sunken_eyes', 'sweating', 'swelled_lymph_nodes', 'swelling_joints','swelling_of_stomach',
 'swollen_blood_vessels', 'swollen_extremeties', 'swollen_legs', 'throat_irritation', 'toxic_look_(typhos)', 'ulcers_on_tongue''unsteadiness', 'visual_disturbances', 'vomiting','watering_from_eyes',
 'weakness_in_limbs','weakness_of_one_body_side', 'weight_gain', 'weight_loss', 'yellow_crust_ooze', 'yellow_urine' 'yellowing_of_eyes', 'yellowish_skin']
def make_input_vector(selected_symptoms):
    min_len = 17
    symptom_selected = selected_symptoms[:min_len]
    symptom_selected += ['None'] * (min_len - len(symptom_selected))
    symptom_selected = np.array(symptom_selected).reshape(1, -1) 
    return symptom_selected

st.set_page_config(page_title="MediScan AI", page_icon="🩺", layout="wide")
st.title("🩺 MediScan - Disease Prediction App")
st.write("Select your symptoms and get an AI-powered disease prediction.")

#getting user location 
coords = streamlit_js_eval(
    js_expressions="""
    new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            pos => resolve({latitude: pos.coords.latitude, longitude: pos.coords.longitude}),
            err => resolve(null)  // return null if denied/error
        );
    })
    """,
    key="get_location"
)
lat = coords['latitude']
log = coords['longitude']
# Multiselect from trained symptom list
selected_symptoms = st.multiselect("Choose your symptoms:", all_symptoms)
if st.button("Predict"):
    if not selected_symptoms:
        st.warning("⚠️ Please select at least one symptom.")
    else:
        input_df = pd.DataFrame([selected_symptoms])
        prediction = model.predict(input_df)[0]
        probs = model.predict_proba(input_df)[0]
        decoded_pred = decoder.inverse_transform([prediction])[0]

        st.subheader(f"🔍 Predicted Disease: **{decoded_pred}**")
        try:
            data_row = data[data["Disease"] == decoded_pred]
            st.subheader("Description")
            Description = data_row["Description"].values[0]
            st.write(Description)
            st.subheader("Precautions to keep in mind")
            Precaution_1 , Precaution_2 , Precaution_3 ,Precaution_4 = data_row["Precaution_1"].values[0], data_row["Precaution_2"].values[0] , data_row["Precaution_3"].values[0] , data_row["Precaution_4"].values[0]
            st.write(f"1) {Precaution_1}")
            st.write(f"2) {Precaution_2}")
            st.write(f"3) {Precaution_3}")
            st.write(f"4) {Precaution_4}")
            st.subheader("Recommended home remedies ")
            Home_remedy = data_row["Home remedy"].values[0]
            st.write(Home_remedy)
        except:
            st.write("Nothing to show here")
        with st.expander("Disclaimer"):
             st.error("The information provided here is for educational purposes only and not a substitute for professional medical advice.")
        print(max(probs)*100)

        top3_idx = np.argsort(probs)[::-1][:3]
        st.write("### Top 3 Possible Diseases")
        for idx in top3_idx:
            st.write(f"- {decoder.inverse_transform([idx])[0]} ({probs[idx]*100:.2f}%)")
        sym_1 = selected_symptoms[0] if len(selected_symptoms) > 0 else "-"
        sym_2 = selected_symptoms[1] if len(selected_symptoms) > 1 else "-"
        sym_3 = selected_symptoms[2] if len(selected_symptoms) > 2 else "-"        

        def is_valid_gmail(email):
            pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
            return re.match(pattern, email) is not None 
        time.sleep(10)
        with st.sidebar:
            st.subheader("MediScan login")
            st.write("Enter your details below :")
            receiver_gmail = st.text_input("Enter your gmail :" , placeholder= "@gamil.com")
            password_user = st.text_input("Make an password :" , type="password")
            if password_user:
                conform_password = st.text_input("conform password :" , type="password")
                if st.button("Login"):
                    if is_valid_gmail(receiver_gmail):
                        if password_user == conform_password:
                            st.success("Login successful")
                            if st.button("Send report to email"):
                                Email_sender(
                            receiver_gmail,
                            sym_1,
                            sym_2,
                            sym_3,
                            decoded_pred,
                            Description,
                            Precaution_1,
                            Precaution_2,
                            Precaution_3,
                            Precaution_4,
                            Home_remedy)
                                st.success("📧 Report sent successfully!")
                        else:
                            st.error("Passwords is not matching.")
                    else:
                        st.error("Gmail is invalid please enter correct gmail")
                else:
                    st.error("gmail or password is invalid")
                    st.write("your gamil is ", receiver_gmail , "and password is " , password_user)
            
        #seting us the api
        my_key = "AIzaSyBSUrSudF7neYoTA52DTM2mVZnF_x9K5aM"
        gmaps =  googlemaps.Client(key = my_key)

        #dict to find the hospital according to the dieseas
        disease_to_keywords = {"Drug Reaction": "emergency hospital","Malaria": "infectious disease hospital","Allergy": "allergy specialist hospital","Hypothyroidism": "endocrinology hospital","Psoriasis": "dermatology hospital","GERD": "gastroenterology hospital",
                               "Chronic cholestasis": "liver hospital", "hepatitis A": "liver hospital", "Osteoarthristis": "orthopedic hospital", "(vertigo) Paroymsal Positional Vertigo": "neurology hospital", "Hypoglycemia": "endocrinology hospital",
                               "Acne": "skin hospital","Diabetes": "diabetes specialist hospital","Impetigo": "skin infection hospital","Hypertension": "cardiology hospital","Peptic ulcer diseae": "gastroenterology hospital","Dimorphic hemorrhoids(piles)": "gastroenterology hospital",
                               "Common Cold": "general hospital", "Chicken pox": "infectious disease hospital", "Cervical spondylosis": "orthopedic hospital", "Hyperthyroidism": "endocrinology hospital", "Urinary tract infection": "urology hospital",
                               "Varicose veins": "vascular surgery hospital","AIDS": "infectious disease hospital","Paralysis (brain hemorrhage)": "neurology hospital","Typhoid": "infectious disease hospital","Hepatitis B": "liver hospital",
                               "Fungal infection": "dermatology hospital", "Hepatitis C": "liver hospital", "Migraine": "neurology hospital", "Bronchial Asthma": "pulmonology hospital", "Alcoholic hepatitis": "liver hospital",
                               "Jaundice": "liver hospital",  "Hepatitis E": "liver hospital",  "Dengue": "infectious disease hospital","Hepatitis D": "liver hospital",  "Heart attack": "cardiology hospital",  "Pneumonia": "pulmonology hospital",
                               "Arthritis": "rheumatology hospital",  "Gastroenteritis": "gastroenterology hospital", "Tuberculosis": "chest hospital"  }
        Keyword = disease_to_keywords[decoded_pred]

        #geting the palces
        hospital_results = gmaps.places_nearby(
                       location=(lat, log),
                       keyword = Keyword,
                       radius=3000,   # set range for better resultes 
                       type="hospital")
        print("api called")

        #displaying the reults
        hospitals = []
        for hospital in hospital_results["results"]:

            name = hospital.get("name")
            rating = hospital.get("rating" , "N\A")
            address = hospital.get("vicinity")
            latitude = hospital["geometry"]["location"]["lat"]
            longitude=  hospital["geometry"]["location"]["lng"]
            total_rating = hospital.get("user_ratings_total", 0)

            if rating < 3.5:
                continue
            if total_rating < 30:
                continue
            if "clinic" in name.lower() or "diagnostic" in name.lower() or "pathology" in name.lower():
                continue

            hospitals.append({
                "name": name,
                "rating": rating,
                "total rating" : total_rating,
                "address": address,
                "latitude": latitude,
                "longitude": longitude
            })


        col1 ,col2 = st.columns(spec=[0.4 , 0.6] , gap= "small" ,  vertical_alignment= "center" , border= True)
        with col1:
                st.subheader("List Of Nearest Hospitals")
                for h in hospitals:
                            st.write(f"**{h['name']}**")
                            st.write(f"⭐ {h['rating']} | 📍 {h['address']}")
                            #st.markdown(f"[Open in Maps](https://www.google.com/maps/search/?api=1&query={h['lat']},{h['lng']})", unsafe_allow_html=True)
                            st.markdown("---")
        with col2:
            st.subheader("Map View")
            m = folium.Map(location=[lat,log], zoom_start=13)

            # Add user marker
            folium.Marker(
                [lat, log],
                tooltip="You are here",
                icon=folium.Icon(color="blue", icon="user")
            ).add_to(m)
            
            # Add hospital markers
            for h in hospitals:
                folium.Marker(
                    [h["latitude"], h["longitude"]],
                    tooltip=h["name"],
                    popup=h["name"]  
                ).add_to(m)
            
            # Render map in Streamlit
            map_data = st_folium(m, width=700, height=500)



        
