import streamlit as st

# Define the statements for each type of intelligence
statements = {
    1: "Rád robím veci vlastnými rukami.",
    2: "Trávim veľa času vonku, na čerstvom vzduchu.",
    3: "Najradšej sa učím spoločne s inými žiakmi.",
    4: "Mám rád prehľadnosť a poriadok vo veciach.",
    5: "Mám radšej muzikály ako dramatické hry.",
    6: "Rád čítam knihy.",
    7: "Zaujímajú ma cudzie jazyky.",
    8: "Som ochotný protestovať alebo podpísať petíciu v záujme správnej veci.",
    9: "Text si zapamätávam tak, že sa snažím skladať slová tak, aby sa rýmovali.",
    10: "Viem si myšlienky vo svojej hlave predstaviť.",
    11: "Viem dobre čítať mapy.",
    12: "Mám problém sedieť dlhšie nečinne.",
    13: "Rozčlenenie riešenia úloh na jednotlivé kroky mi veľmi uľahčuje riešenie.",
    14: "Rád sa učím botaniku a zoológiu.",
    15: "Prestavovanie nábytku v byte ma baví.",
    16: "Súhlasím s tvrdením, že „čím viac, tým lepšie“.",
    17: "Mám rád „talk show“ v televízii aj v rozhlase.",
    18: "Mám pevné morálne zásady.",
    19: "Zaujíma ma sociálna spravodlivosť.",
    20: "Rád kategorizujem veci podľa ich spoločných znakov.",
    21: "Nerobí mi problém vyjadriť rytmus pohybmi.",
    22: "Nie som spokojný, ak nepoznám zmysel (nechápem logiku) veci.",
    23: "Ľahko si pamätám lyrické piesne.",
    24: "Písanie poznámok mi uľahčuje chápanie a zapamätanie si učiva.",
    25: "Som „tímový“ hráč.",
    26: "Spravodlivosť je pre mňa veľmi dôležitá.",
    27: "Mám rád šport.",
    28: "Neverbálnu komunikáciu (gestá, posunky, mimiku) považujem za veľmi dôležitú.",
    29: "Zvieratá zohrávajú dôležitú úlohu v mojom živote.",
    30: "Ľahko rozoznávam vzory, modely (správania, šiat, látok a pod.).",
    31: "Ekologické problémy sú pre mňa veľmi dôležité.",
    32: "Píšem si denník.",
    33: "Neporiadni ľudia ma vedia ľahko rozčúliť.",
    34: "Dokážem rýchlo počítať aj v „hlave“.",
    35: "Rád tvorím rôzne umelecké veci ozdoby, sošky a pod.",
    36: "Rád sa učím činnosťou tak, že niečo robím, napr. ohmatávam, pohybujem s vecami.",
    37: "Najlepšie sa učím, ak k učivu mám aj citový vzťah.",
    38: "Zvyknem písať len tak, pre radosť.",
    39: "Dobre si pamätám učivo, ktoré obsahuje obrázky, schémy a pod.",
    40: "Mám rád diskusie.",
    41: "Chcel by som, aby náš dom mal recyklačný systém.",
    42: "Viem dobre riešiť problémové úlohy.",
    43: "Učenie sa v skupine je pre mňa veľmi efektívne.",
    44: "Mám rád videoklipy.",
    45: "Dobre rozlišujem rôzne zvuky.",
    46: "Politickú angažovanosť považujem za dôležitú.",
    47: "Rád stanujem.",
    48: "Bavia ma rôzne hádanky, pri lúštení ktorých treba rozmýšľať.",
    49: "Žijem veľmi aktívny život.",
    50: "Páči sa mi vyjadrenie pocitov tancom.",
    51: "Dokážem si veci vo svojej pamäti veľmi živo predstaviť.",
    52: "Baví ma práca v záhrade.",
    53: "Vždy ma zaujímala hra na nejaký hudobný nástroj.",
    54: "Nezačnem riešiť nejakú úlohu, pokiaľ nie sú zodpovedané všetky moje otázky vzťahujúce sa na riešenie.",
    55: "Nerád pracujem (učím sa) sám.",
    56: "Prv ako s niečím súhlasím, chcem vedieť prečo sa to robí.",
    57: "Motivácia veľmi ovplyvňuje ako sa učím.",
    58: "Zriaďovanie a udržiavanie prírodných rezervácií považujem za veľmi dôležité.",
    59: "Pri prednese poézie ma zaujíma intonácia prednesu.",
    60: "Individuálna práca môže byť rovnako efektívna ako práca v skupine.",
    61: "Rád mám učivo, ktoré obsahuje rôzne diagramy, schémy, tabuľky.",
    62: "Slovné hračky sú veľmi zábavné.",
    63: "Viem ľahko vysvetliť svoje myšlienky iným ľuďom.",
    64: "Veciam rozumiem lepšie, ak ich usporiadam podľa dôležitosti.",
    65: "Keď som presvedčený o správnosti veci, dokážem sa jej venovať na 100%.",
    66: "Balet a tanečné umenie je pre mňa veľkým pôžitkom.",
    67: "Ťažko sa viem sústrediť, pokiaľ počúvam rádio alebo pozerám televíziu.",
    68: "Zdravé telo je pre zdravú myseľ veľmi dôležité.",
    69: "Umenie a remeslá sú zábavným spôsobom trávenia voľného času.",
    70: "Rád sa hrám so slovíčkami, napr. v podobe dvojzmyselných výrazov.",
    71: "Rád sa zapájam do aktivít, ktoré môžu pomôcť iným.",
    72: "Rád sa zapájam do verejných diskusií.",
    73: "Rád pracujem s rôznymi nástrojmi.",
    74: "Mám rád rôzne druhy hudby.",
    75: "Rád vykonávam rôzne mimoškolské aktivity, napr. navštevujem rôzne krúžky.",
    76: "Lepšie chápem učivo rozdelené do menších častí.",
    77: "Zaujímam sa o sociálne záležitosti.",
    78: "Dobrovoľne, z vlastného záujmu si dopisujem s priateľmi (aj elektronicky).",
    79: "Rád pracujem s počítačovými programami.",
    80: "Rád sa hrám s trojrozmernými hlavolamami, ako napr. s Rubikovou kockou."
}

# Define the intelligence categories and their corresponding statements
intelligence_categories = {
    "Lingvistická inteligencia": [6, 7, 24, 32, 38, 62, 63, 70, 72, 78],
    "Logicko-matematická inteligencia": [4, 13, 22, 33, 34, 42, 48, 54, 76, 79],
    "Priestorová inteligencia": [10, 11, 15, 35, 39, 44, 51, 61, 66, 80],
    "Telesno-kinestetická inteligencia": [1, 12, 27, 28, 36, 49, 50, 68, 69, 73],
    "Muzikálna inteligencia": [5, 9, 21, 23, 30, 45, 53, 59, 67, 74],
    "Interpersonálna inteligencia": [3, 16, 17, 25, 40, 43, 46, 55, 75, 77],
    "Intrapersonálna inteligencia": [8, 18, 19, 26, 37, 56, 57, 60, 65, 71],
    "Prírodná inteligencia": [2, 14, 20, 29, 31, 41, 47, 52, 58, 64]
}

# App Title
st.title("Dotazník na zistenie učebných štýlov podľa prevažujúcich druhov inteligencií")

st.write("Zakrúžkujete tie z uvedených výrokov, ktoré vystihujú (sú typické) Vašu činnosť, spôsob učenia, Vaše záujmy a záľuby. Na jednotlivé položky dotazníka neexistujú správne, dobré, ani nesprávne či zlé odpovede. Preto ho vyplňujte úprimne, čestne a zodpovedne.")

# Checkbox for each statement
selected_statements = []
for statement_id, statement_text in statements.items():
    if st.checkbox(statement_text, key=statement_id):
        selected_statements.append(statement_id)

# Button to evaluate intelligences
if st.button("Vyhodnotiť inteligencie"):
    # Count responses for each intelligence category
    intelligence_scores = {category: 0 for category in intelligence_categories}

    for category, ids in intelligence_categories.items():
        intelligence_scores[category] = sum(1 for id in selected_statements if id in ids)

    # Display results
    st.subheader("Vaše výsledky:")
    st.write("Riadky, v ktorých ste dosiahli najvyšší počet bodov, označujú tie druhy inteligencie (a súčasne aj učebné štýly), ktoré Vám pri učení sa najviac vyhovujú. Pozor! Najvyšší počet bodov  ste mohli dosiahnuť aj vo viacerých riadkoch.")
    for category, score in intelligence_scores.items():
        st.write(f"{category}: {score} bodov")

    # Optional: Provide feedback based on scores
    max_score_category = max(intelligence_scores, key=intelligence_scores.get)
    st.write(f"Najsilnejšia inteligencia: {max_score_category}")
