# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st
#loading the saved model

loaded_model = pickle.load(open('train_model.sav', 'rb'))

#Creating a function for prediction


def con_price_prediction(input_data):
    
# changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    return prediction
  
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
    
    unit_of_measure_per_pack = st.slider('unit_of_measure_per_pack',0,1000)
    
    Line_item_quantity = st.slider('line_item_quantity', 1,619999)
    
    Pack_price = st.slider('pack_price', 0.0 ,1345.64)
    
    Unit_price = st.slider('unit_price', 0.0 ,238.65)
    
    source_names = {0:'Canada',1:'China',2:'France',3:'Germany',4:'India',5:'Ireland',6:'Italy',7:'Japan',
                   8: 'Korea',9:'Nether Lands',10:'South Africa',11:'USA',12:'United Kingdom',13:'others'}
    
    Source = st.selectbox('manufacturing_site',source_names.keys(),format_func=lambda x:source_names[x])
    
    Weight_kilograms = st.slider('weight_kilograms', 0.0 ,857354.0)
    
    managed_names = {0:'PMO - US',1:'others'}
    Managed_By = st.selectbox('managed_by_others',managed_names.keys(),format_func=lambda x:managed_names[x])
    
    fullfill_names = {0:'Direct Drop',1:'From RDC'}
    Fullfill_Via = st.selectbox('fulfill_via_From RDC',fullfill_names.keys(),format_func=lambda x:fullfill_names[x])
    
    first_names = {0:'No',1:'Yes'}
    First_line_designation = st.selectbox('first_line_designation_Yes',first_names.keys(),format_func=lambda x:first_names[x])
    
    # code for Prediction
    Consignment_Price = ''
    
    # creating a button for Prediction
    
    if st.button('Consignment Price Prediction'):
        Consignment_Price = con_price_prediction([Country_Destination,
                                                  Vendor_Inco_Term,
                                                  Shipment_Mode,
                                                  unit_of_measure_per_pack,
                                                  Line_item_quantity,
                                                  Pack_price,
                                                  Unit_price,
                                                  Source,
                                                  Weight_kilograms,
                                                  Managed_By,
                                                  Fullfill_Via,
                                                  First_line_designation])
        
        
    st.success(Consignment_Price)
    
    
    
    
    
if __name__ == '__main__':
    main()
    