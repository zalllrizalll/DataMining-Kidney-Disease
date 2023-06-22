import streamlit as st
from web_functions import predict

def app(df, x, y):
    
    st.title("Halaman Prediksi")

    col1, col2, col3, col4= st.columns(4)
    opsiNormal = {"Normal": 1, "Abnormal": 0}
    opsiPresent = {"Present": 1, "Not Present": 0}
    opsiYN = {"Yes": 1, "No": 0}
    opsiPoor = {"Good": 1, "Poor": 0}

    with col1:
        bp = st.text_input('Tekanan darah (mm/Hg)')
    with col1:
       # sg = st.text_input('Berat jenis (1.005,1.010,1.015,1.020,1.025)')
       sg = st.selectbox('Berat jenis',(1.005,1.010,1.015,1.020,1.025))
    with col1:
        # al = st.text_input('Albumin (0,1,2,3,4,5)')
        al = st.selectbox('Albumin',(0,1,2,3,4,5))
    with col1:
        # su = st.text_input('Gula (0,1,2,3,4,5)')
        su = st.selectbox('Gula',(0,1,2,3,4,5))
    with col1:
        # rbc = st.text_input('Sel darah merah(normal,abnormal)')
        rbc = st.selectbox('Sel darah merah',list(opsiNormal.keys()))
        rbc = opsiNormal[rbc]
    with col1:
        # pc = st.text_input('Sel darah putih  (normal,abnormal)')
        pc = st.selectbox('Sel darah putih',list(opsiNormal.keys()))
        pc = opsiNormal[pc]
    with col2:
        # pcc = st.text_input('Gumpalan sel darah putih  (present,notpresent)')
        pcc = st.selectbox('Gumpalan sel darah putih',list(opsiPresent.keys()))
        pcc = opsiPresent[pcc]
    with col2:
        # ba = st.text_input('Bakteri (present,notpresent)')
        ba = st.selectbox('Bakteri',list(opsiPresent.keys()))
        ba = opsiPresent[ba]
    with col2:    
        bgr = st.text_input('Glukosa darah ack(mgs/dl)')
    with col2:    
        bu = st.text_input('Ureum darah(mgs/dl)')
    with col2:    
        sc = st.text_input('Kreatin serum(mgs/dl)')
    with col2:    
        sod = st.text_input('Natrium(mEq/L)')

    with col3:    
        pot = st.text_input('Kalium(mEq/L)')
    with col3:    
        hemo = st.text_input('Hemoglobin gms)')
    with col3:    
        pcv = st.text_input('volume sel terkemas')
    with col3:    
        wc = st.text_input('Jumlah sel darah putih(cells/cumm)')
    with col3:    
        rc = st.text_input('Jumlah sel darah merah(millions/cmm)')
    with col3:    
        # htn = st.text_input('Hipertensi')
        htn = st.selectbox('Hipertensi', list(opsiYN.keys()))
        htn = opsiYN[htn]


    with col4:    
        # dm = st.text_input('Diabetes mellitus')
        dm=  st.selectbox('Diabetes mellitus', list(opsiYN.keys()))
        dm = opsiYN[dm]
    with col4:    
        # cad = st.text_input('Penyakit arteri koroner')
        cad=  st.selectbox('Penyakit arteri koroner', list(opsiYN.keys()))
        cad = opsiYN[cad]
    with col4:    
        # appet = st.text_input('Nafsu makan')
        appet=  st.selectbox('Nafsu makan', list(opsiPoor.keys()))
        appet = opsiPoor[appet]
    with col4:    
        # pe = st.text_input('Edema pedal')
        pe=  st.selectbox('Edema pedal', list(opsiYN.keys()))
        pe = opsiYN[pe]
    with col4:    
        # ane = st.text_input('Anemia')
        ane=  st.selectbox('Anemia', list(opsiYN.keys()))
        ane = opsiYN[ane]


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