import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Omzet Data Entry Zone2000")

# Constants
CABANG = [
    "IFS",
    "RMS",
]

BUSINESS_TYPES = [
"Blok M Square",
"Tamini Square",
"Tanjung Priok",
"Klender (R-38) RMS",
"Cengkareng (R-40)",
"Pasar Minggu (R-22)",
"Kopro",
"Mega Mal Karawang (R-67) RMS",
"Serang (R-75) RMS",
"Cilegon",
"Bogor Trade Mall (R-71) RMS",
"Ciputat (R-20)",
"Depok (R-34) RMS",
"Ciledug (R-49) RMS",
"Tangerang (R-31) RMS",
"Cibitung (R-37) RMS",
"Garut (R-99) RMS",
"Cianjur (R-46) RMS",
"Sukabumi (RB-05) RMS",
"Cibinong 1 (R-43)",
"Cimahi (RB-12)",
"Bekasi (R-21)",
"Padalarang (R-97)",
"Sabar Subur",
"Kiddie Land Klender",
"Cipanas (R-137) RMS",
"Medan (R-58) RMS",
"Pematang Siantar (R-41) RMS",
"Tebing Tinggi",
"Tanjung Karang Lampung",
"Baturaja",
"Padang (R-66) RMS",
"Bukittinggi (R-77) RMS",
"Payakumbuh",
"Jambi (R-45) RMS",
"Palembang",
"Panbil Batam (RB-30)",
"Tanjung Pinang (RB-26)",
"Panam (R-96)",
"Kerinci (R-86)",
"Dumai (R-80)",
"Pangkal Pinang (R-52) RMS",
"Duri (R-85)",
"Batam (RB-21)",
"Kiddiezone Batam (ZD-43)",
"Banjarmasin",
"Tarakan (R-60)",
"Samarinda (R-94) RMS",
"Balikpapan (R-51)",
"Bontang (R-81)",
"Pontianak (R-57)",
"Mesra Samarinda (ZD-37)",
"Abepura (R-91)",
"Salatiga (RB-03) RMS",
"Kudus (RB-28)",
"Kebumen 2",
"Semarang",
"Banyuwangi",
"Malang (RB-M) RMS",
"Sidoarjo (RB-27) RMS",
"Gresik (RB-16) RMS",
"Kediri (R-98) RMS",
"Denpasar (RB-20) RMS",
"Sesetan",
"Kupang (R-61) RMS",
"Makasar 2 (R-70)",
"Makasar 3 (R-79)",
"Pasar Perumnas Klender",
"Pondok Gede",
"Klender (R-38) IFS",
"Pasar Minggu (R-11)",
"Jatinegara",
"Dewi Sartika Bogor",
"Parung",
"Depok (R-34) IFS",
"Ciledug (R-49) IFS",
"Tangerang (R-31) IFS",
"Tajur (R-121)",
"Cibadak (R-106)",
"Garut (R-99) IFS",
"Cikupa",
"Yasmin Bogor",
"Cibinong 2 (R-107)",
"Cirebon (R-100)",
"Sabar Subur Cikupa",
"Cipanas (R-137) IFS",
"Cimone (R-26) IFS",
"Medan (R-58) IFS",
"Pematang Siantar (R-41) IFS",
"Rajabasa Lampung",
"Bukittinggi (R-77) IFS",
"Rumbai - Damasraya",
"Plaza Sukaramai Pekanbaru (R-56)",
"Sorong (R-103)",
"Timika (R-138)",
"Pekalongan (R-110)",
"Wonosari",
"Banjarnegara",
"Dinoyo",
"Sidoarjo (RB-27) IFS",
"Gresik (RB-16) IFS",
"Krian (RB-23)",
"Bungurasih",
"Ponorogo (ZD-44)",
"Tulungagung (ZD-47)",
"Ubud Bali",

]

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Fetch existing Omzet data
existing_data = conn.read(worksheet="Omzet", usecols=list(range(25)), ttl=5)
existing_data = existing_data.dropna(how="all")



action = st.selectbox(
    "Choose an Action",
    [
        "Input Data Omzet",
        # "Update Data",
        "View All Omzet",
        # "Delete",
    ],
)

if action == "Input Data Omzet":
    st.markdown("Input Omzet Sesuai dengan toko ( RMS / IFS )")
    with st.form(key="vendor_form", clear_on_submit=True):
        company_name = st.selectbox(
            "Toko*", options=CABANG, index=None
        )
        business_type = st.selectbox(
            "Nama Toko*", options=BUSINESS_TYPES, index=None
        )
        # products = st.multiselect("Products Offered", options=PRODUCTS)
        # years_in_business = st.slider("Years in Business", 0, 50, 5)
        onboarding_date = st.date_input(label="Tanggal")
        # additional_info = st.text_area(label="Additional Notes")
        # branch = st.text_input(label="Branch")

        "---"
        st.markdown('Input omzet Zone | zonevip | Playcafe dst')
        zone = st.number_input(label="Zone", min_value=0, format="%i", step=10)
        zonevip = st.number_input(label="ZoneVIP", min_value=0, format="%i", step=10)
        kiddieland = st.number_input(label="KiddieLand", min_value=0, format="%i", step=10)
        playcafe = st.number_input(label="PlayCafe", min_value=0, format="%i", step=10)
        fnb = st.number_input(label="FnB", min_value=0, format="%i", step=10)
        "---"
        ('Input Hulala | indoor/outdoor | kiddiecut (khusus R67)')
        hulala = st.number_input(label="Hulala", min_value=0, format="%i", step=10)
        inout = st.number_input(label="Indoor/Outdoor", min_value=0, format="%i", step=10)
        kiddiecut = st.number_input(label="KiddieCut", min_value=0, format="%i", step=10)
        "---"
        total = st.number_input(label="Total", min_value=0, format="%i", step=10)
        "---"
        ('Input Fintec')
        gopay = st.number_input(label="Gopay", min_value=0, format="%i", step=10)
        ovo = st.number_input(label="OVO", min_value=0, format="%i", step=10)
        dana = st.number_input(label="DANA", min_value=0, format="%i", step=10)
        traveloka = st.number_input(label="Traveloka", min_value=0, format="%i", step=10)
        tiket = st.number_input(label="TiketCom", min_value=0, format="%i", step=10)
        "---"
        ('Input BCA')
        bcadeb = st.number_input(label="K.Debit BCA", min_value=0, format="%i", step=10)
        bcakre = st.number_input(label="K.Kredit BCA", min_value=0, format="%i", step=10)
        bcaqris = st.number_input(label="QRIS BCA", min_value=0, format="%i", step=10)
        "---"
        ('Input BRI')
        brideb = st.number_input(label="K.Debit BRI", min_value=0, format="%i", step=10)
        brikre = st.number_input(label="K.Kredit BRI", min_value=0, format="%i", step=10)
        briqris = st.number_input(label="QRIS BRI", min_value=0, format="%i", step=10)

        # with st.expander("Income"):
        #     for income in incomes:
        #         st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
        # with st.expander("Expenses"):
        #     for expense in expenses:
        #         st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
        # with st.expander("Comment"):
        #     comment = st.text_area("", placeholder="Enter a comment here ...")

       

        st.markdown("**required*")
        submit_button = st.form_submit_button(label="Simpan Data")

        if submit_button:
            if not company_name or not business_type:
                st.warning("Toko* dan Nama Toko Harus dipilih.")
            # elif existing_data["CompanyName"].str.contains(company_name).any():
            #     st.warning("A vendor with this company name already exists.")
            else:
                vendor_data = pd.DataFrame(
                    [
                        {
                            "Toko": company_name,
                            "NamaToko": business_type,
                            # "Products": ", ".join(products),
                            # "YearsInBusiness": years_in_business,
                            "Tanggal": onboarding_date.strftime("%Y-%m-%d"),
                            # "AdditionalInfo": additional_info,
                            # "Branch": branch,
                            "Zone" : zone,
                            "ZoneVIP" : zonevip,
                            "KiddieLand" : kiddieland,
                            "PlayCafe" : playcafe,
                            "FnB": fnb,
                            "Hulala" : hulala,
                            "Indoor/Outdoor" : inout,
                            "KiddieCut" : kiddiecut,
                            "Total" : total,
                            "Gopay" : gopay,
                            "OVO" : ovo,
                            "DANA" : dana,
                            "Traveloka" : traveloka,
                            "TiketCom" : tiket,
                            "K.Debit BCA" : bcadeb,
                            "K.Kredit BCA" : bcakre,
                            "QRIS BCA" : bcaqris,
                            "K.Debit BRI" : brideb,
                            "K.Kredit BRI" : brikre,
                            "QRIS BRI" : briqris,


                        }
                    ]
                )
                updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

                conn.update(worksheet="Omzet", data=updated_df)
                st.success("Simpan Data Berhasil!")

elif action == "Update Data":
    st.markdown("Select a vendor and update their details.")

    vendor_to_update = st.selectbox(
        "Select a Vendor to Update", options=existing_data["Toko"].tolist()
    )
    vendor_data = existing_data[existing_data["Toko"] == vendor_to_update].iloc[
        0
    ]

    with st.form(key="update_form"):
        company_name = st.text_input(
            label="Company Name*", value=vendor_data["Toko"]
        )
        business_type = st.selectbox(
            "Nama Toko*",
            options=BUSINESS_TYPES,
            index=BUSINESS_TYPES.index(vendor_data["NamaToko"]),
        )
        # products = st.multiselect(
        #     "Products Offered",
        #     options=PRODUCTS,
        #     default=vendor_data["Products"].split(", "),
        # )
        # years_in_business = st.slider(
        #     "Years in Business", 0, 50, int(vendor_data["YearsInBusiness"])
        # )
        onboarding_date = st.date_input(
            label="Tanggal", value=pd.to_datetime(vendor_data["Tanggal"])
        )
        # additional_info = st.text_area(
        #     label="Additional Notes", value=vendor_data["AdditionalInfo"]
        # )
        #  branch = st.text_input(
        #     label="Branch", value=vendor_data["Branch"]
        # )

       

        st.markdown("**required*")
        update_button = st.form_submit_button(label="Update Vendor Details")

        if update_button:
            if not company_name or not business_type:
                st.warning("Ensure all mandatory fields are filled.")
            else:
                # Removing old entry
                existing_data.update(
                    existing_data[
                        existing_data["CompanyName"] == vendor_to_update
                    ].index,
                    
                )
                # Creating updated data entry
                updated_vendor_data = pd.DataFrame(
                    [
                        {
                            "CompanyName": company_name,
                            "BusinessType": business_type,
                            "Products": ", ".join(products),
                            "YearsInBusiness": years_in_business,
                            "OnboardingDate": onboarding_date.strftime("%Y-%m-%d"),
                            "AdditionalInfo": additional_info,
                            "Branch": branch,
                        }
                    ]
                )
                # Adding updated data to the dataframe
                updated_df = pd.concat(
                    [existing_data, updated_vendor_data], ignore_index=True
                )
                conn.update(worksheet="Omzet", data=updated_df)
                st.success("Vendor details successfully updated!")

# View All Omzet
elif action == "View All Omzet":

    col1, col2 = st.columns((2))
    

    existing_data["Tanggal"] = pd.to_datetime(existing_data["Tanggal"])

    # Getting the min and max date 
    startDate = pd.to_datetime(existing_data["Tanggal"]).max()
    endDate = pd.to_datetime(existing_data["Tanggal"]).max()

    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))

    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))

    existing_data = existing_data[(existing_data["Tanggal"] >= date1) & (existing_data["Tanggal"] <= date2)].copy()

    toko=st.selectbox("Filter By Toko:",
                            # options=existing_data["NamaToko"] , index=None 
                            options=existing_data["NamaToko"].unique()                          
                            )
    selection_query=existing_data.query(
    "NamaToko== @toko"
    )


   # _, view1, dwn1, view2, dwn2 = st.columns([0.15,0.20,0.20,0.20,0.20])

   #  with view1:
   #      expander = st.expander( "omzet totakl")
   #      dataom = existing_data[["Zone, KiddieLand, PlayCafe, FnB"]].groupby(by="Tanggal")["Total"].sum()
   #      expander.write(dataom)

    # sumlist = conn.read(worksheet="Omzet", usecols=list(range(12)), ttl=5)

    # sumlist = [col4, col5, col6]

    st.dataframe(selection_query)

    view1, dwn1 = st.columns((2))
    with view1:
        expander = st.expander("Sales by Branch")
        vendor_data = existing_data[["NamaToko","Zone", "ZoneVIP", "Total"]].groupby(by="NamaToko")["Total"].sum()
        expander.write(vendor_data)
    with dwn1:
        st.download_button("Get Data", data = vendor_data.to_csv().encode("utf-8"),
                           file_name="RetailerSales.csv", mime="text/csv")
    # st.dataframe(existing_data)

# Delete
# elif action == "Delete":
#     exp = st.expander("See Pic")
#     exp.write(

#         zone = st.number_input(label="Zone", min_value=0, format="%i", step=10),
#         zonevip = st.number_input(label="ZoneVIP", min_value=0, format="%i", step=10),
#         kiddieland = st.number_input(label="KiddieLand", min_value=0, format="%i", step=10),

#         )

#     onboarding_date = st.date_input(label="Tanggal")

#     # vendor_to_delete = st.selectbox(
#     #     "Select a Vendor to Delete", options=existing_data["NamaToko"].tolist()
#     # )

#     toko=st.selectbox("Filter By Toko:",
#                             # options=existing_data["NamaToko"] , index=None 
#                             options=existing_data["NamaToko"].unique()                          
#                             )
#     selection_query=existing_data.query(
#     "NamaToko== @toko"
#     )


#     if st.button("Delete"):
#         existing_data.drop(
#             existing_data[existing_data["NamaToko"] == selection_query  ].index,
#             inplace=True,
#         )

#         conn.update(worksheet="Omzet", data=existing_data)
#         st.success("Vendor successfully deleted!")
