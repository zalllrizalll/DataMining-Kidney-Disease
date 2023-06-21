import streamlit as st
from web_functions import predict

def app(df, x, y):
    
    st.title("Halaman Prediksi")

    col1, col2, col3, col4= st.columns(4)

    with col1:
        bp = st.text_input('Tekanan darah')
    with col1:
        sg = st.text_input('Berat jenis')
    with col1:
        al = st.text_input('Albumin')
    with col1:
        su = st.text_input('Gula')
    with col1:
        rbc = st.text_input('Sel darah merah')
    with col1:
        pc = st.text_input('Sel darah putih')

    with col2:
        pcc = st.text_input('Gumpalan sel darah putih')
    with col2:
        ba = st.text_input('Bakteri')
    with col2:    
        bgr = st.text_input('Glukosa darah ack')
    with col2:    
        bu = st.text_input('Ureum darah')
    with col2:    
        sc = st.text_input('Kreatin serum')
    with col2:    
        sod = st.text_input('Natrium')

    with col3:    
        pot = st.text_input('Kalium')
    with col3:    
        hemo = st.text_input('Hemoglobin')
    with col3:    
        pcv = st.text_input('volume sel terkemas')
    with col3:    
        wc = st.text_input('Jumlah sel darah putihc')
    with col3:    
        rc = st.text_input('Jumlah sel darah merah')
    with col3:    
        htn = st.text_input('Hipertensi')


    with col4:    
        dm = st.text_input('Diabetes mellitus')
    with col4:    
        cad = st.text_input('Penyakit arteri koroner')
    with col4:    
        appet = st.text_input('Nafsu makan')
    with col4:    
        pe = st.text_input('Edema pedal')
    with col4:    
        ane = st.text_input('Anemia')

    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]

    #tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses...")

        if (prediction == 1):
            st.warning("Orang Tersebut Rentan Terkena Penyakit Ginjal")
        else:
            st.success("Orang Tersebut Relatif Aman Dari Penyakit Ginjal")

        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")