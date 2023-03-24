# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:03:52 2023

@author: Kandi Computers
"""



import numpy as np
import pandas as pd
import pickle
import streamlit as st
#loading the saved model

loaded_model = pickle.load(open('data.pkl', 'rb'))

#Creating a function for prediction
def main():
    
    
    # giving a title
    st.title('Consignment Price Prediction')
    
    
    # getting the input data from the user
    country_names = {0:'Congo, DRC',1:'Ethiopia',2:'Guyana',3:'Haiti',4:'Ivory Coast',5:'Mozambique',6:'Nigeria',
    7:'Rwanda',8:'South Africa',9:'South Sudan',10:'Tanzania',11:'Uganda',12:'Vietnam',13:'Zambia',
    14:'Zimbabwe',15:'others'}
    
    Country_Destination = st.selectbox('country',country_names.keys(),format_func=lambda x: country_names[x])
    
    vendor_inco_names = {0:'CIP',1:'DDP',2:'EXW',3:'FCA',4:'N/A - From RDC',5:'others'}
    Vendor_Inco_Term = st.selectbox('vendor_inco_term',vendor_inco_names.keys(),format_func=lambda x:vendor_inco_names[x])
    
    shipment_names = {0:'Air',3:'Truck',1:'Air Charter',2:'Ocean'}
    Shipment_Mode = st.selectbox('shipment_mode',shipment_names.keys(),format_func = lambda x:shipment_names[x])
    
    unit_of_measure_per_pack = st.number_input('unit_of_measure_per_pack')
    
    Line_Item_quantity = st.number_input('line_item_quantity')

    source_names = {0:'Canada',1:'China',2:'France',3:'Germany',4:'India',5:'Ireland',6:'Italy',7:'Japan',
                   8: 'Korea',9:'Nether Lands',10:'South Africa',11:'USA',12:'United Kingdom',13:'others'}
    
    Source = st.selectbox('manufacturing_site',source_names.keys(),format_func=lambda x:source_names[x])
    
    Weight_kilograms = st.number_input('weight_kilograms')
    
    managed_names = {0:'PMO - US',1:'others'}
    Managed_By = st.selectbox('managed_by_others',managed_names.keys(),format_func=lambda x:managed_names[x])
    
    fullfill_names = {0:'Direct Drop',1:'From RDC'}
    Fullfill_Via = st.selectbox('fulfill_via_From_RDC',fullfill_names.keys(),format_func=lambda x:fullfill_names[x])
    
    first_names = {0:'No',1:'Yes'}
    First_line_designation = st.selectbox('first_line_designation_Yes',first_names.keys(),format_func=lambda x:first_names[x])
    
    
    
    input_dict = {'country': Country_Destination,
                  'vendor_inco_term': Vendor_Inco_Term,
                  'shipment_mode': Shipment_Mode,
                  'unit_of_measure_per_pack': unit_of_measure_per_pack,
                  'line_item_quantity': Line_Item_quantity,
                  'pack_price': Pack_price,
                  'unit_price': Unit_price,
                  'manufacturing_site': Source,
                  'weight_kilograms': Weight_kilograms,
                  'managed_by_others': Managed_By,
                  'fulfill_via_From_RDC': Fullfill_Via,
                  'first_line_designation_Yes': First_line_designation}
    
    # code for Prediction
    Consignment_Price = ''
    
    # creating a button for Prediction
    
    if st.button('Predict Consignment Price'):
        
        
        
        # converting the input dictionary into a numpy array
        input_df = pd.DataFrame([input_dict])
     
        # making the prediction using the loaded model
        Consignment_Price = loaded_model.predict(input_df)[0]
        # displaying the predicted consignment price
        st.success(f'The predicted consignment price is ${Consignment_Price:.2f}')
    
    
    
    
    
if __name__ == '__main__':
    main()