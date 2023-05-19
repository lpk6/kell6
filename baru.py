import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Concentration Machine', page_icon=':🤖:',layout='wide')

image=Image.open('coverr.JPEG')
st.image(image, width=None)
                
navbar=option_menu(menu_title=None, options=['Home','Konsentrasi',],
                  icons=['house','calculator'])
if navbar=='Home':
    st.title('📍 Aplikasi Perhitungan Konsentrasi Larutan')
    st.write('Sebuah aplikasi berbasis website yang dapat digunakan untuk menghitung konsentrasi larutan dengan mudah. Terdapat beberapa satuan konsentrasi yang dapat dihitung menggunakan aplikasi ini, diantaranya molaritas, molalitas, normalitas, fraksi mol, dan kadar (%).')
    left_column, right_column= st.columns(2)
    with left_column:
        st.write('Aplikasi ini dibuat dan dikembangkan oleh kelompok 6, kelas 1B :')
        st.write('🧑‍🔬 Achmed Zakky Zamani (2219024)')
        st.write('🧑🏽‍🔬 Aldo Floristo Parasian Pardede (2219029)')
        st.write('👩🏼‍🔬 Rani Khoerunnisa (2219152)')
        st.write('👩🏻‍🔬 Rayna Anggita Ramadhani (2219154)')
    with right_column:
        st.image("https://mbamo.com/wp-content/uploads/2020/09/MBAmo-your-MBA-Admissions-Calculator.gif", width=300)
    
if navbar=='Konsentrasi':
    tab1,tab2=st.tabs(['🧪 Materi Konsentrasi','🔎 Perhitungan Konsentrasi'])
    
    with tab1:
        st.header('🧪 Konsentrasi')
        st.write('Konsentrasi larutan adalah jumlah zat yang terlarut dalam setiap satuan larutan atau pelarut. Konsentrasi larutan dapat dinyatakan dalam beberapa satuan, yaitu molaritas (M), molalitas (m), normalitas (N), fraksi mol (X), dan kadar (%).')
        
        st.subheader(':blue[A. Molaritas]')
        st.write('Molaritas dalam konsentrasi larutan dikenal dengan istilah konsentrasi molar. Molaritas adalah satuan yang menyatakan jumlah mol suatu zat dalam satu liter larutan. Satuan molaritas disimbolkan dengan huruf M atau disebut juga Molar.')
        st.write('Rumus :')
        st.latex('M= \dfrac{n}{V}')
        st.write('Keterangan :')
        st.write('M = Molaritas zat (molar)')
        st.write('n = Mol suatu zat (mol)')
        st.write('V = Volume larutan (liter)')
        
        st.subheader(':blue[B. Molalitas]')
        st.write('Molalitas adalah satuan konsentrasi larutan yang menyatakan jumlsh mol suatu zat dalam satu kilogram larutan. Satuan molalitas disimbolkan dengan huruf m.')
        st.write('Rumus :')
        st.latex('M= \dfrac{n}{p}')
        st.write('Keterangan :')
        st.write('m = Molalitas zat (molal)')
        st.write('n = Mol suatu zat (mol)')
        st.write('p = Massa pelarut (gram)')
        
        st.subheader(':blue[C. Normalitas]')
        st.write('Normalitas adalah ukuran yang menunjukkan besaran konsentrasi pada berat ekivalen setara dalam gram per larutan. Normalitas juga dapat didefinisikan sebagai jumlah mol ekivalen dari suatu zat per liter larutan. Satuan normalitas disimbolkan dengan huruf N. Perhitungan menggunakan normalitas larutan biasanya digunakan dalam tiga peristiwa reaksi, yaitu reaksi asam dan basa, reaksi redoks, dan reaksi deposisi (pengendapan). Nilai valensi untuk reaksi asam dan basa adalah jumlah ion H+ atau OH-, valensi untuk reaksi redoks adalah banyaknya elektron, dan valensi untuk reaksi pengendapan adalah jumlah muatan kation atau anion')
        st.write('Rumus :')
        st.latex('N= {M}x{a}')
        st.write('Keterangan :')
        st.write('M = Molaritas zat (M)')
        st.write('a = Valensi (banyaknya ion)')
        
        st.subheader(':blue[D. Fraksi Mol]')
        st.write('Fraksi mol adalah perbandingan jumlah mol suatu zat terlarut atau zat pelarut dengan jumlah mol total yang ada dalam sebuah larutan. Simbol dari fraksi mol ini adalah huruf X.')
        st.write('Rumus :')
        st.latex('Xt= \dfrac{nt}{nt+np}')
        st.latex('Xp= \dfrac{np}{nt+np}')
        st.write('Keterangan :')
        st.write('Xt = Fraksi mol zat terlarut (X)')
        st.write('Xp = Fraksi mol zat pelarut (X)')
        st.write('nt = Mol zat terlarut (mol)')
        st.write('np = Mol zat pelarut(mol)')
        
        st.subheader(':blue[E. Kadar]')
        st.write('Konsentrasi dalam persen dapat dinyatakan menjadi dua bentuk, yaitu persen berat (%b/b) dan persen berat volume (%b/v).')
        st.write('Rumus :')
        st.latex('Kadar (\%b/b) = \dfrac{massa zat}{massa campuran} x 100\%')
        st.latex('Kadar (\%b/v) = \dfrac{massa zat}{volume campuran} x 100\%')
        
    with tab2:
        st.header('🔎 Penentuan Konsentrasi Larutan')
        option=st.selectbox(
        'Silahkan pilih satuan konsentrasi yang ingin dicari ',
        ('Molaritas (M)','Molalitas (m)','Normalitas (N)','Fraksi mol terlarut (Xt)','Fraksi mol pelarut (Xp)','Kadar (%b/b)','Kadar (%b/v)'))
        if option=='Molaritas (M)':
            mol=st.number_input('Masukkan mol zat (mol)')
            volume=st.number_input('Masukkan volume larutan (L)')
            if st.button('Hitung'):
                Molaritas=mol/volume
                st.success(f'Molaritas larutan sebesar {Molaritas} M')
                st.write('Rumus:')
                st.latex('M= \dfrac{n}{V}')
                st.write('Keterangan :')
                st.write('M = Molaritas zat (molar)')
                st.write('n = Mol suatu zat (mol)')
                st.write('V = Volume larutan (liter)')
        elif option=='Molalitas (m)':
            mol=st.number_input('Masukkan mol zat (mol)')
            p=st.number_input('Masukkan massa pelarut (kg)')
            if st.button('Hitung'):
                Molalitas=mol/p
                st.success(f'Molalitas larutan sebesar {Molalitas} molal')
                st.write('Rumus :')
                st.latex('M= \dfrac{n}{p}')
                st.write('Keterangan :')
                st.write('m = Molalitas zat (molal)')
                st.write('n = Mol suatu zat (mol)')
                st.write('p = Massa pelarut (gram)')
        elif option=='Normalitas (N)':
            jumlah_digit=4
            M=st.number_input(f'Masukkan molaritas zat (M)', format='%.'+str(jumlah_digit)+'f')
            jumlah_digit=0
            a=st.number_input(f'Masukkan valensi (banyaknya ion)', format='%.'+str(jumlah_digit)+'f')
            if st.button('Hitung'):
                Normalitas=M*a
                st.success(f'Normalitas larutan sebesar {Normalitas} N')
                st.write('Rumus :')
                st.latex('N= {M}x{a}')
                st.write('Keterangan :')
                st.write('M = Molaritas zat (M)')
                st.write('a = Valensi (banyaknya ion)')
        elif option=='Fraksi mol terlarut (Xt)':
            t=st.number_input('Masukkan mol terlarut (mol)')
            p=st.number_input('Masukkan mol pelarut (mol)')
            if st.button('Hitung'):
                FraksiMol=t/(p+t)
                st.success(f'Fraksi mol terlarut sebesar {FraksiMol} ')
                st.write('Rumus :')
                st.latex('Xt= \dfrac{nt}{nt+np}')
                st.write('Keterangan :')
                st.write('Xt = Fraksi mol zat terlarut (X)')
                st.write('nt = Mol zat terlarut (mol)')
                st.write('np = Mol zat pelarut(mol)')
        elif option=='Fraksi mol pelarut (Xp)':
            p=st.number_input('Masukkan mol terlarut (mol)')
            t=st.number_input('Masukkan mol pelarut (mol)')
            if st.button('Hitung'):
                FraksiMol=p/(p+t)
                st.success(f'Fraksi mol pelarut sebesar {FraksiMol} ')
                st.write('Rumus :')
                st.latex('Xp= \dfrac{np}{nt+np}')
                st.write('Keterangan :')
                st.write('Xp = Fraksi mol zat pelarut (X)')
                st.write('nt = Mol zat terlarut (mol)')
                st.write('np = Mol zat pelarut(mol)')
        elif option=='Kadar (%b/b)':
            m=st.number_input('Masukkan massa zat terlarut (gram)')
            mt=st.number_input('Masukkan massa zat total (gram)')
            if st.button('Hitung'):
                Kadar=m/mt
                st.success(f'Kadar (%b/b) sebesar {Kadar} %(b/b) ')
                st.write('Rumus :')
                st.latex('Kadar (\%b/b) = \dfrac{massa zat}{massa campuran} x 100\%')
        elif option=='Kadar (%b/v)':
            m=st.number_input('Masukkan massa zat terlarut (gram)')
            vt=st.number_input('Masukkan volume zat total (mL)')
            if st.button('Hitung'):
                Kadar=m/vt
                st.success(f'Kadar (%b/v) sebesar {Kadar} %(b/v) ') 
                st.write('Rumus :')
                st.latex('Kadar (\%b/v) = \dfrac{massa zat}{volume campuran} x 100\%')
