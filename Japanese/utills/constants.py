import os
import random


# ================= BASE DIR =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ================= IMAGE =================
# Background / heart image (1536x1024 recommended)

import random

last_image = None

def get_random_image():
    global last_image

    images = [
        "japanese.png",
        "japanese1.png",
        "japanese2.png",
        "japanese3.png",
        "japanese4.png",
        "japanese5.png",
        "japanese6.png",
        "japanese7.png",
        "japanese8.png",
        "japanese9.png",
        "japanese10.png",
        "japanese11.png",
        "japanese12.png",
        "japanese13.png",
        "japanese14.png",
        "japanese15.png",
        "japanese16.png",
        "japanese17.png",
        "japanese18.png",
        "japanese19.png",
        "japanese20.png",
        "japanese21.png",
    ]

    image = random.choice(images)

    while image == last_image:
        image = random.choice(images)

    last_image = image
    return image


BASE_IMAGE = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "img",
    get_random_image()
)








# ================= FONT =================
# Bold & highly readable font
FONT_PATH = os.path.join(
    BASE_DIR, "..", "..", "font", "Roboto-Regular.ttf"
)

# ================= FONT SETTINGS =================
FONT_SIZE = 80         # Main font size (Telegram safe)
MIN_FONT_SIZE = 140      # Never go below this
STROKE_WIDTH = 5         # Outline thickness

# ================= CHALLENGE =================
CHALLENGE_INTERVAL = 120 # 5 minutes
# CHALLENGE_INTERVAL = 60 # 1 minutes

WORDS_POOL = [


"Ab","Abtak","AbhiTak","Aage","Peeche","Upar","Neeche","Andar","Bahar","Paas",
"Door","Samne","Piche","Aaspaas","Yahin","Wahin","Kahin","HarJagah","Roz","Rojana",
"Subah","Dopahar","Shaam","Raat","RaatBhar","DinBhar","Parso","Naukar","Filhaal","Fauran",
"Turant","Der","DerSe","Waqt","Samay","Ghadi","Pal","Lamha","Mahina","Saal",
"Saawan","Garmi","Sardi","Thand","Dhoop","Chhaon","Mausam","Aasmaan","Badal","Kohra",
"Os","Ola","Garaj","Chamk","Dhund","Lehar","Kinara","Ret","Pathar","Chattan",
"Registan","Jheel","Talab","Kuan","Jharna","Jharokha","Gufa","Ghati","Maidan","Khet",
"Fasal","Anaaj","Gehu","Chana","Makka","Bajra","Jowar","Sarson","Dhan","Ganna",
"Neem","Peepal","Bargad","Tulsi","Gulab","Chameli","Mogra","Surajmukhi","Kamala","Kamal",
"Bel","Lata","Daali","Jad","Tana","Chhaal","Kali","Khushboo","Mehak","Sugandh",
"Janwar","Pashu","Pakshi","Chidiya","Kabootar","Tota","Maina","Kauwa","Mor","Hans",
"Baaz","Ullu","Gauraiya","Koyal","Bulbul","Cheenti","Titli","Madhumakhi","Machhar","Makkhi",
"Makdi","Keeda","Saanp","Bichhu","Chipkali","Girgit","Kachhua","Magarmachh","Mendhak","Machhli",
"Haathi","Ghoda","Gadha","Oont","Sherni","Baagh","Cheetah","Bhalu","Lomdi","Bhediya",
"Bandar","Langoor","Hiran","Khargosh","Bakri","Bhed","Gai","Bhains","Kutta","Billi",
"Chuha","Gilahari","Suar","Murgi","Murga","Batakh","Kabootari","Bachda","Pilla","Bachcha",
"Insaan","Aadmi","Aurat","Ladka","Ladki","Baccha","Bacchi","Jawan","Buzurg","Budha",
"Budhi","Padosi","Mehmaan","Mezbaan","Rishtedaar","Damad","Bahu","Beta","Beti","Bhaiya",
"Jija","Saala","Sali","Bhatija","Bhatiji","Bhanja","Bhanji","Fufa","Fufi","Mausi",
"Chachi","Chacha","Taya","Tayi","Sasur","Saas","Nanad","Devar","Jeth","Jethani",
"Patni","Pati","Dulha","Dulhan","Premi","Premika","Humraaz","Humsafar","Saathi","Sangathi",
"Chehra","Aankh","Naak","Kaan","Muh","Honth","Daant","Zubaan","Gala","Gardan",
"Kandha","Seena","Pet","Peeth","Kamar","Haath","Ungli","Nakhun","Pair","Edhi",
"Ghutna","Kohni","Kalai","Baazu","Jangh","Pindli","Maatha","Gaal","Thodi","Palak",
"Baalo","Baal","Daadhi","Moonch","Dilasa","Dard","Takleef","Aaram","Sukoon","Thakaan",
"Neend","Bhukh","Pyaas","Bukhar","Khansi","Chheenk","Zakhm","Chot","Marham","Dawai",
"Doctor","Dawa","Aspataal","Dukaan","Bazaar","Market","Gali","Sadak","Chauraha","Mohalla",
"Colony","Ilaaka","Rajdhani","Desh","Videsh","Pradesh","Zila","Kasba","Panchayat","Sarkar",
"Mantri","Netaji","Adhikari","Police","Sipahi","Fauji","Jawan","Adalat","Vakil","Judge",
"Kanoon","Niyam","Faisla","Saza","Inaam","Haq","Farz","Zimmedari","Azaadi","Gulaami",
"Samvidhan","Loktantra","Chunav","Matdaan","Janta","Nagrik","Samaj","Sangathan","Sanstha","Yojana",
"Paise","Rupaye","Sikka","Note","Kharcha","Bachat","Kamai","Aamdani","Munafa","Nuksaan",
"Karz","Udhar","Byaaj","Kisht","Bill","Raseed","LenDen","Tijori","Khazana","Daulat",
"Ameer","Gareeb","Mehanga","Sasta","Muft","Keemat","Daam","Tol","Wazan","Maal",
"Saamaan","Samaan","Thaila","Jhola","Batua","Purse","Almari","Darwaza","Khidki","Deewar",
"Chhat","Farsh","Kamra","Rasoi","Bistar","Takia","Chadar","Kambal","Gadda","Kursi",
"Mez","Sofa","Pankha","Bulb","Tube","Switch","Plug","Tar","Taala","Chaabi",
"Sheesha","Aaina","Bartaan","Thali","Katori","Chamach","Kaanta","Chaku","Kadhai","Tawa",
"Patila","Bhagona","Balti","Mug","Lota","Jug","Glass","Bottle","Dabba","Tiffin",
"Masala","Haldi","Mirch","Dhaniya","Jeera","Ajwain","Methi","Elaichi","Laung","Dalchini",
"Namak","Cheeni","Gud","Shahad","Ghee","Makhan","Malai","Dahi","Paneer","Cream",
"Atta","Maida","Besan","Sooji","Suji","Murmura","Chivda","Namkeen","Biscuit","Rusk",
"Toast","Bread","Sandwich","Burger","Pizza","Pasta","Noodles","Momos","Chowmein","Manchurian",
"Fries","Chips","Popcorn","Cake","Pastry","Donut","IceCream","Juice","NimbuPani","Thandai",
"Aam","Seb","Kela","Santra","Mosambi","Angoor","Amrood","Papita","Anar","Tarbooz",
"Kharbooja","Nariyal","Nimbu","Aloo","Pyaaz","Tamatar","Bhindi","Baingan","Gobhi","Gajar",
"Matar","Mooli","Lauki","Tori","Karela","Palak","Methi","Adrak","Lehsun","Mirchi",
"Kaddu","Shalgam","ShimlaMirch","Kheera","Kakdi","Arbi","Shakarkandi","Mushroom","Rajma","Lobia",
"Chhole","Moong","Masoor","Urad","Toor","Soyabean","Duniya","Zindagi","Maut","Paidaish",
"Janam","Bachpan","Jawani","Budhapa","Yaadein","Yaad","Bhool","Galti","Sach","Jhooth",
"Raaz","Baat","Charcha","Guftagu","Sawaal","Jawaab","Mashwara","Salah","Shikayat","Tareef",
"Taana","Mazaak","Hansi","Rona","Aansu","Gussa","Nafrat","Jalan","Irsha","Fikr",
"Chinta","Pareshani","Uljhan","Hairani","Dar","Khauf","Honsla","Lalach","Izzat","Beizzati",
"Sharam","Guroor","Ahankaar","Vinmarta","Sabr","Sahanshilta","Imandari","Wafadari","Dhokha","Fareb",
"Chalaki","Shararat","Nadan","Pagal","Deewana","Aalsi","Furtila","Shaant","Gambhir","Khush",
"Udaas","Naraz","Pareshan","Hairan","Thaka","Taza","Naram","Sakht","Garam","Thanda",
"Meetha","Khatta","Kadwa","Teekha","Feeka","Namkeen","KurKura","Geela","Sukha","Ganda",
"Saaf","Maila","Chamkila","Andhera","Ujala","Rang","Laal","Neela","Peela","Hara",
"Safed","Kaala","Gulabi","Baingani","Narangi","Bhura","Sunehra","Chandi","Sona","Tamba",
"Loha","Lakdi","Kapda","Resham","Sooti","Joota","Chappal","Mojdi","Sandal","Kapde",
"Kameez","Kurta","Pajama","Jeans","Shirt","Pant","Jacket","Sweater","Topi","Pagdi",
"Gamcha","Dupatta","Saari","Lehenga","Blouse","Ghaghra","Salwar","Suit","Uniform","Jeb",
"Button","Silai","Bunai","Kadhai","Darzi","Naai","Dhobi","Mochi","Sunar","Lohar",
"Kumhar","Badhai","Mistri","Mazdoor","Kisaan","Vyapari","Dukaandaar","Grahak","Khareed","Bikri",
"Vyapar","Naukri","Rozgaar","Kaam","Dhanda","Kaarobar","Karkhana","Company","Daftar","Manager",
"Malik","Maalik","Karmchari","Sahyogi","Sahayak","Boss","Team","Meeting","Training","Interview",
"Resume","NaukriPesha","Tankhwa","Vetan","Chhutti","Hajiri","Anubhav","Kaushal","Pratibha","Yogyata",
"Degree","Certificate","Diploma","Vishay","Ganit","Vigyan","Itihaas","Bhugol","Hindi","Angrezi",
"Urdu","Sanskrit","Bhasha","Vyakaran","Shabd","Vakya","Akshar","Matra","Kavita","Kahani",
"Upanyas","Lekhak","Kavi","Patrakar","Sampadak","Akhbaar","Patrika","Samachar","Khabar","Headline",
"Radio","Television","Camera","Tasveer","Tasveerein","Selfie","Reel","Status","Story","Caption",
"Comment","Like","Share","Subscribe","Channel","Website","App","Software","Hardware","Database",
"Code","Script","Function","Variable","Class","Object","Element","Design","Developer","Engineer",
"Technology","Digital","Online","Offline","WebsiteLink","Browser","Chrome","Google","Email","Inbox",
"Attachment","Document","PDF","Excel","Word","PowerPoint","Data","Backup","Restore","Security",
"Privacy","Permission","Access","Account","Profile","Setting","Notification","Alert","Error","Warning",
"Success","Failure","Support","Customer","Service","Complaint","Ticket","Solution","Problem","Request",
"Process","Feature","Option","Menu","Tool","Shortcut","Command","Control","Automation","Integration",
"Payment","Refund","Transaction","Transfer","Bank","Accountant","Hisab","Kitab","Khata","Ledger",
"Invoice","Voucher","Billing","Tax","GST","PAN","Aadhaar","Form","Signature","Stamp",
"Agreement","Contract","Policy","Rule","Report","Statement","Balance","Profit","Loss","Audit",
"Stock","Inventory","Purchase","Sales","Order","Delivery","Courier","Parcel","Transport","Safar",
"Gaadi","Car","Bus","Train","Metro","Cycle","Scooter","Bike","Truck","Auto",
"Rickshaw","HawaiJahaz","Helicopter","Jahaz","Station","Airport","Platform","Ticket","SafarNama","Musafir",
"Driver","Conductor","Pilot","Raahi","ManzilTak","Mod","Rukawat","Raftaar","Speed","Brake",
"Clutch","Gear","Engine","Petrol","Diesel","BijliGhar","Battery","Charging","Tyre","Puncture",
"Helmet","Seatbelt","Signal","Traffic","Jam","Flyover","Pul","Surang","Footpath","Parking",
"Mandir","Masjid","Gurudwara","Church","Dargah","Aastha","Shraddha","Bhakti","Aarti","Ghanti",
"Diya","Agarbatti","Dhoopbatti","Havan","Yagya","Teerth","Darshan","Vrath","Vrat","Upvaas",
"Roza","Ibadat","Namaz","Salaam","Rab","Khuda","Bhagwan","Ishwar","Parmatma","Srishti",
"Vishwa","Brahmand","Atma","Rooh","Jeevan","Moksha","Shanti","Ahimsa","Satya","Nyay",
"Karuna","Daya","Daan","Punya","Paap","Sanskar","Parampara","Riwaaz","Tehzeeb","Tyohaar",
"Shaadi","Byah","Mangni","Baraat","Mehndi","HaldiRasme","Vidaai","Janamdin","Salgirah","Jashn",
"Juloos","Mela","Mubarak","Badhai","Tohfa","Upahaar","Yaadgaar","Khushiyan","Raunak","Rangoli",
"Patakhe","Phuljhari","AnarBomb","Dhol","Nagada","Dholak","Tabla","Sitar","Bansuri","Shehnai",
"Geet","Gaana","Sur","Taal","Raag","Awaaz","Lafz","Alfaaz","Nazm","Ghazal",
"Shayari","SherOShayari","Kahawat","Muhavra","Paheli","Kissa","Dastaan","Qissa","Andaaz","Lehja",
"Style","Fashion","Trend","Look","Personality","Swag","Attitude","Confidence","Talent","Skill",
"Creativity","Innovation","Idea","Planning","Strategy","Decision","Choice","Option","Preference","Priority",
"Focus","Concentration","Attention","Practice","Revision","Learning","Knowledge","Education","Taleem","Ilm",
"Samajh","Akal","Buddhi","Dimag","Dimaag","Dimaagi","Tark","Logic","Reason","Saboot",
"Pramaan","Nateeja","Anjaam","Shuruaat","Ant","Khatam","Poora","Adhoora","Mukammal","Adhura",
"Behtar","Behtareen","Aasaan","Mushkil","Saral","Kathin","Seedha","Tedha","Lamba","Chhota",
"Uncha","Neecha","Mota","Patla","Bhari","Halka","Teek","Perfect","Average","Normal",
"Khaas","Aam","Anokha","Alag","Naya","Purana","Prachin","Aadhunik","Asli","Nakli",
"Zaroori","Anivarya","Laazmi","Mumkin","Namumkin","SaafSaaf","Khulkar","Chupke","Akele","Saath",
"Milkar","Alvida","PhirMilenge","Swagat","MaafKaro","KoiBaatNahi","KyaBaatHai","Shubhkamnayein","ShubhRatri","ShubhPrabhat"

    



    



"Adieu","Allo","Coucou","Enchanté","Felicitation","Bravo","MerciBeaucoup","Svp","Silence","Daccord",
"Certainement","PeutEtre","JamaisPlus","Volontiers","Pourquoi","Comment","Quand","Combien","Lequel","Laquelle",
"Qui","Quoi","Ou","Dont","ParceQue","Puisque","Cependant","Pourtant","Donc","Alors",
"Ainsi","Sinon","Malgre","Pendant","Depuis","Jusqua","Vers","Chez","Entre","Contre",
"Sur","Sous","Devant","Derriere","Autour","Parmi","Selon","Avec","Sans","Pour",
"Continent","Pays","Region","Province","Departement","Capitale","Frontiere","Territoire","Quartier","Centre",
"Banlieue","Campagne","Metropole","Port","Plage","Ile","Desert","Vallee","Colline","Sommet",
"Volcan","Cascade","Source","Ruisseau","Ruisselet","Marais","Etang","Grotte","Caverne","Falaise",
"Roche","Sable","Gravier","Boue","Argile","Mineral","Pierre","Marbre","Granite","Charbon",
"Petrole","Gaz","Energie","Electricite","Lumiere","Ombre","Chaleur","Froid","Humidite","Temperature",
"Climat","Saison","Printemps","Ete","Automne","Hiver","Orage","Eclair","Tonnerre","Brouillard",
"Brume","Givre","Gelee","Flocon","ArcEnCiel","Rayon","Aube","Crepuscule","Clarte","Obscurite",
"ForetVierge","Prairie","Savane","Jungle","Brousse","Bambou","Palmier","Chene","Sapin","Pin",
"Erable","Olivier","Pommier","Cerisier","Citronnier","Oranger","Vigne","Herbe","Mousse","Fougere",
"Roseau","Racine","Tronc","Branche","Ecorce","Graine","Fruitier","Pollen","Petale","Bouquet",
"Jardinier","Jardinage","Potager","Serre","Semence","Recolte","Moisson","Agriculture","Elevage","Ferme",
"Fermier","Berger","Vacher","Cheval","Jument","Poulain","Ane","Mouton","Agneau","Chevre",
"Chevreau","Vache","Taureau","Veau","Cochon","Porc","Sanglier","Lapin","Liebre","Ecureuil",
"Renard","Loup","Ours","Panda","Koala","Lion","Tigre","Leopard","Jaguar","Panthere",
"Elephant","Rhinoceros","Hippopotame","Girafe","Zebre","Kangourou","Chameau","Dromadaire","Gazelle","Antilope",
"Chien","Chat","Chaton","Chiot","Animal","Creature","Mammifere","Reptile","Amphibien","Insecte",
"Oiseau","PoissonRouge","Dauphin","Baleine","Requin","Pieuvre","Calamar","Crabe","Crevette","Homard",
"Langouste","Moule","Huitre","Escargot","Limace","Meduse","Corail","EtoileDeMer","Tortue","Serpent",
"Crocodile","Lezard","Iguane","Grenouille","Crapaud","Salamandre","Aigle","Faucon","Hibou","Chouette",
"Perroquet","Canari","Pigeon","Corbeau","Cigogne","Heron","Flamant","Pingouin","Autruche","Paon",
"PouletFermier","Coq","Poule","Poussin","Dinde","Dindon","Oie","Canard","Cygne","Hirondelle",
"Papillon","Chenille","Coccinelle","Libellule","Fourmi","Abeille","Guepe","Frelon","Moustique","Sauterelle",
"Grillon","Criquet","Scorpion","Araignee","Ver","Larve","Parasite","Microbe","Bacterie","Virus",
"Corps","Tete","Visage","Front","Tempe","Joue","Menton","Oreille","Oeil","Nez",
"Bouche","Langue","Dent","Gencive","Cou","Epaule","Bras","Coude","Poignet","Main",
"Doigt","Pouce","Index","Majeur","Annulaire","Auriculaire","Ongle","Poitrine","Ventre","Dos",
"Taille","Hanche","Jambe","Cuisse","Genou","Mollet","Cheville","Pied","Orteil","Talon",
"Peau","Os","Muscle","Nerf","Veine","Artere","Sang","Coeur","Poumon","Foie",
"Rein","Estomac","Intestin","Cerveau","Crane","Squelette","Articulation","Respiration","Digestion","Circulation",
"Sante","Maladie","Medecin","Medecine","Infirmier","Infirmiere","Patient","Clinique","Pharmacie","Ordonnance",
"Traitement","Operation","Chirurgie","Consultation","Diagnostic","Symptome","Douleur","Blessure","Fracture","Infection",
"Allergie","Fatigue","Sommeil","Repos","Reveil","Hygiene","Prevention","Vaccin","Therapie","Guerison",
"Medicament","Comprime","Sirop","Pommade","Creme","Pansement","Bandage","Thermometre","Stethoscope","Seringue",
"PetitDejeuner","Dejeuner","Diner","Gouter","Repas","Menu","Entree","Plat","Dessert","Boisson",
"EauMinerale","EauGazeuse","Limonade","Soda","TheVert","TheNoir","Infusion","Tisane","Espresso","Cappuccino",
"Latte","CafeAuLait","JusDePomme","JusDOrange","Smoothie","Milkshake","Yaourt","FromageBlanc","Emmental","Camembert",
"Brie","Roquefort","Mozzarella","Parmesan","Gruyere","Cheddar","PainComplet","PainGrille","PainAuChocolat","Brioche",
"Crepe","Gaufre","Pancake","Muffin","BiscuitSec","Madeleine","Macaron","Eclair","Profiterole","MousseAuChocolat",
"CremeBrulee","Flan","Pudding","Glace","Sorbet","Compote","Marmelade","Caramel","Vanille","Cannelle",
"Poivre","Paprika","Safran","Gingembre","Persil","Basilic","Menthe","Thym","Romarin","Origan",
"Vinaigre","Huile","HuileDolive","Mayonnaise","Moutarde","Ketchup","Sauce","Farine","Levure","Pate",
"Riz","PommeDeTerre","PatateDouce","Haricot","Lentille","PoisChiche","PetitPois","Mais","Avoine","Orge",
"Seigle","Quinoa","Boulgour","Couscous","Semoule","Spaghetti","Macaroni","Ravioli","Lasagne","PizzaMargherita",
"Frite","Puree","Omelette","Oeuf","Bacon","Jambon","Saucisse","Steak","Boeuf","Veau",
"Agneau","CanardConfit","DindeRotie","Saumon","Thon","Sardine","Truite","Cabillaud","Moules","FruitsDeMer",
"Tomate","Concombre","Courgette","Aubergine","Poivron","Brocoli","Chou","ChouFleur","Epinard","Laitue",
"SaladeVerte","Endive","Asperge","Artichaut","Poireau","Celeri","Navet","Betterave","Radis","Ail",
"Oignon","Echalote","Poire","Peche","Abricot","Prune","Mangue","Ananas","Kiwi","Melon",
"Framboise","Myrtille","Mure","Groseille","Pamplemousse","Figue","Datte","Pruneau","Noix","Amande",
"Noisette","Pistache","Cacahuete","Chataigne","RaisinSec","FruitSec","NoixDeCoco","Grenade","Litchi","Papaye",
"Date","CuisineFrancaise","Recette","Ingredient","Cuisson","Four","Poele","Casserole","Refrigerateur","Congelateur",
"MicroOndes","Mixeur","Blender","GrillePain","Bouilloire","MachineACafe","LaveVaisselle","Evier","Robinet","Eponge",
"Serviette","Nappe","Torchon","Assiette","Bol","Tasse","Verre","Carafe","Fourchette","Couteau",
"Cuillere","Louche","Spatule","Fouet","Planche","Passoire","Marmite","Couvercle","Plateau","Tablier",
"Salon","Sejour","SalleDeBain","Toilette","Couloir","Escalier","Balcon","Terrasse","Garage","Grenier",
"Cave","SousSol","Entree","Toit","Mur","Plafond","Plancher","Carrelage","Parquet","Tapis",
"Rideau","Voilage","Store","Canape","Fauteuil","Pouf","BureauMeuble","Bibliotheque","Etagere","Commode",
"Placard","Penderie","Lit","Matelas","Oreiller","Couverture","Drap","Couette","Lampe","Lustre",
"Applique","Bougie","Photographie","Cadre","Horloge","ReveilMatin","Miroir","Vase","Pot","Panier",
"Poubelle","Balai","Aspirateur","Serpillere","Lessive","Detergent","Savon","Shampooing","Dentifrice","Brosse",
"Peigne","Rasoir","Parfum","Deodorant","Maquillage","RougeALevres","Mascara","FondDeTeint","Vernis","Bijou",
"Collier","Bracelet","Bague","BoucleDOreille","Montre","Lunettes","LunettesDeSoleil","Sac","Valise","Portefeuille",
"Ceinture","Cravate","NoeudPapillon","Chapeau","Casquette","Echarpe","Bonnet","Gants","Manteau","Impermeable",
"Robe","Jupe","Pantalon","Short","Tshirt","Pull","Cardigan","Chemise","Veste","Blouson",
"Costume","Smoking","Pyjama","Peignoir","Maillot","MaillotDeBain","SousVetement","Chaussette","Collant","Chaussure",
"Botte","Bottine","Basket","Sandale","Pantoufle","Semelle","Lacet","TalonHaut","Cuir","Laine",
"Coton","Lin","Soie","Polyester","Velours","Denim","Tissu","Textile","Aiguille","Fil",
"MachineACoudre","Boutonniere","FermetureEclair","Poche","Manche","Col","Ourlet","Modele","TailleVestimentaire","Collection",
"Metier","Profession","Carriere","Emploi","Poste","Salaire","Paie","Contrat","Recrutement","Candidature",
"Entretien","Patron","Employeur","Employe","Collegue","Directeur","Directrice","Secretaire","Assistant","Assistante",
"Comptable","Caissier","Vendeur","Vendeuse","Commercial","Technicien","Technicienne","Informaticien","Programmeur","Developpeur",
"Designer","Graphiste","Architecte","Artiste","Peintre","Musicien","Chanteur","Chanteuse","Danseur","Acteur",
"Actrice","Ecrivain","Journaliste","Photographe","Cuisinier","Cuisiniere","Serveur","Serveuse","Boulanger","Boulangere",
"Patissier","Patissiere","Agriculteur","Agricultrice","Ingenieur","Ingenieure","Avocat","Avocate","Juge","Policier",
"Policiere","Pompier","Soldat","ProfesseurDeMusique","Chercheur","Scientifique","Astronaute","Pilote","Marin","Conducteur",
"Chauffeur","Mecanicien","Electricien","Plombier","Menuisier","Maçon","PeintreEnBatiment","JardinierPaysagiste","Facteur","Livreur",
"Agent","Responsable","Chef","Equipe","Reunion","OrdreDuJour","CompteRendu","Projet","Tache","Delai",
"Priorite","Calendrier","Planning","Horaire","Pause","Retard","Absence","Presence","Conges","Formation",
"Competence","Experience","Qualification","Diplome","Stage","Apprentissage","Promotion","Demission","Licenciement","Retraite",
"EntrepriseIndividuelle","Societe","Commerce","Industrie","Production","Fabrication","Distribution","Marketing","Publicite","Vente",
"Achat","Client","Fournisseur","Partenaire","Concurrent","Marque","Produit","Article","ServiceClient","Abonnement",
"Facture","Devis","Paiement","Remboursement","Reduction","Remise","PromotionCommerciale","Garantie","Livraison","Commande",
"Stockage","Entrepot","Magasin","Supermarche","Hyperm arche","Epicerie","Boucherie","Poissonnerie","Fromagerie","Librairie",
"Papeterie","PharmacieDeGarde","Banque","Assurance","Agence","Immobilier","AppartementMeuble","Loyer","Proprietaire","Locataire",
"Immobilier","Hypotheque","Pret","Epargne","Budget","Depense","Revenu","Benefice","Perte","Dette",
"Credit","Debit","Monnaie","Billet","Piece","CarteBancaire","Cheque","Virement","Retrait","Depot",
"Distributeur","Guichet","Compte","Solde","Transaction","Investissement","Action","Obligation","Bourse","Finance",
"Economie","Fiscalite","Impot","Taxe","TVA","Declaration","Bilan","Comptabilite","AuditInterne","RapportFinancier",
"OrdinateurPortable","Telephone","Smartphone","Tablette","MontreConnectee","Ecouteur","Casque","Microphone","HautParleur","Imprimante",
"Scanner","Photocopieuse","DisqueDur","CleUSB","CarteMemoire","Processeur","CarteGraphique","CarteMere","EcranTactile","Batterie",
"Chargeur","Cable","Adaptateur","Routeur","Modem","Connexion","Telechargement","Televersement","Navigateur","MoteurDeRecherche",
"PageWeb","Lien","Adresse","Domaine","Hebergement","Cloud","ServeurWeb","BaseDeDonnees","Algorithme","Programmation",
"Variable","Constante","Boucle","Condition","Tableau","Chaine","Entier","Booleen","Fonction","Methode",
"Classement","ObjetConnecte","Interface","Utilisateur","Identifiant","MotDePasse","Authentification","Chiffrement","Cryptage","PareFeu",
"Malware","Antivirus","Cybersecurite","Hameconnage","Pirate","Piratage","Robotique","IntelligenceArtificielle","ApprentissageAutomatique","ReseauSocial",
"Publication","Abonne","Abonnement","Influenceur","Hashtag","FilDActualite","NotificationPush","Discussion","Messagerie","AppelVideo",
"AppelAudio","Courriel","PieceJointe","Brouillon","Spam","Corbeille","Archive","Synchronisation","MiseAJour","Version",
"Installation","Configuration","Parametre","Preference","TableauDeBord","Statistique","Graphique","Analyse","Donnee","Fichier",
"Dossier","Document","Texte","Tableur","Presentation","Diapositive","Formulaire","ModeleDeDocument","SignatureNumerique","Impression",
"Education","Apprentissage","Enseignement","Pedagogie","Connaissance","Savoir","SavoirFaire","Recherche","Laboratoire","ExperienceScientifique",
"Observation","Hypothese","Theorie","Formule","Equation","Calcul","Addition","Soustraction","Multiplication","Division",
"Fraction","Pourcentage","Decimale","Nombre","Chiffre","Unite","Mesure","Longueur","Largeur","Hauteur",
"Profondeur","Distance","Vitesse","Acceleration","Masse","Volume","Surface","Perimetre","Angle","Geometrie",
"Algebre","Arithmetique","Statistique","Probabilite","Physique","Chimie","Biologie","Geologie","Astronomie","Ecologie",
"Mathematiques","Histoire","Geographie","Philosophie","Litterature","Grammaire","Orthographe","Conjugaison","Vocabulaire","Prononciation",
"Accent","Expression","Conversation","Dialogue","Traduction","Interpretation","Dictionnaire","Encyclopedie","Roman","Poeme",
"Poésie","Conte","Fable","Theatre","Piece","Scene","Personnage","Intrigue","Chapitre","Paragraphe",
"Phrase","Mot","Lettre","Alphabet","Voyelle","Consonne","Syllabe","Verbe","Nom","Adjectif",
"Adverbe","Pronom","Preposition","Conjonction","ArticleDefini","ArticleIndefini","Singulier","Pluriel","Masculin","Feminin",
"Passe","Present","Futur","Imparfait","Conditionnel","Subjonctif","Imperatif","Participe","Infinitif","Indicatif",
"Sport","Football","Basketball","Volleyball","Handball","Tennis","Badminton","Rugby","Cricket","Baseball",
"Golf","Natation","Cyclisme","Athletisme","Gymnastique","Boxe","Judo","Karate","Taekwondo","Escrime",
"Equitation","Ski","Snowboard","Patinage","Escalade","Course","Marathon","Yoga","Meditation","Fitness",
"Musculation","Entrainement","Exercice","Echauffement","Etirement","Endurance","Souplesse","Agilite","Coordination","Performance",
"Competition","Championnat","Tournoi","Match","Partie","Joueur","Joueuse","Arbitre","Entraineur","Capitaine",
"Gardien","Defenseur","Attaquant","Milieu","Remplacant","EquipeAdverse","Stade","Terrain","Piste","Piscine",
"Gymnase","Vestiaire","VestiaireSportif","Ballon","Raquette","Filet","But","PanierDeBasket","Medaille","Trophee",
"Podium","Record","Score","Point","Set","MancheSportive","Penalty","Faute","VictoireSportive","DefaiteSportive",
"Enfant","Adolescent","Adulte","Famille","Parent","Mere","Pere","Frere","Soeur","GrandPere",
"GrandMere","Oncle","Tante","Cousin","Cousine","Neveu","Niece","Epoux","Epouse","Fiance",
"Fiancee","Mariage","Divorce","Naissance","Anniversaire","Celebration","Fete","Ceremonie","Invitation","Invite",
"Amoureux","Couple","AmitieSincere","Compagnon","Compagne","Voisin","Voisine","Ami","Amie","Camarade",
"Enfance","Adolescence","Vieillesse","Generation","Ancetre","Descendant","Heritage","Souvenir","Tradition","Culture",
"Religion","Croyance","Spiritualite","Foi","Priere","Temple","Eglise","Mosquee","Synagogue","Monastere",
"Rituel","CeremonieReligieuse","MeditationSpirituelle","Pelerinage","FeteNationale","NouvelAn","Noel","Paques","AnniversaireDeMariage","Carnaval",
"CostumeTraditionnel","DanseTraditionnelle","MusiqueClassique","MusiquePop","Rock","Jazz","Blues","Rap","HipHop","Reggae",
"MusiqueElectronique","Opera","Ballet","Concert","FestivalMusical","Orchestre","Chorale","Melodie","Harmonie","Rythme",
"Guitare","Piano","Violon","Violoncelle","Contrebasse","Flute","Clarinette","Saxophone","Trompette","Trombone",
"Accordeon","Harpe","BatterieMusicale","Tambour","Cymbale","Maracas","Ukulele","Mandoline","Synthétiseur","Partition",
"Cinema","Film","Serie","Episode","Documentaire","Animation","DessinAnime","ActeurPrincipal","Realisateur","Producteur",
"Scenario","DialogueDeFilm","SousTitre","Doublage","BandeAnnonce","Affiche","BilletCinema","SalleDeCinema","Projection","Spectateur",
"Telefilm","CourtMetrage","LongMetrage","Comedie","Drame","Action","AventureFilm","ScienceFiction","Fantastique","Horreur",
"Thriller","Romance","PolicierFilm","Western","Musical","Mystere","Suspense","AnimationNumerique","EffetsSpeciaux","Montage",
"Photographie","ObjectifPhoto","Lentille","Flash","Trépied","Portrait","Paysage","Panorama","SelfieStick","Resolution",
"Pixel","CouleurPhoto","Contraste","Luminosite","Exposition","Filtre","Retouche","Edition","Illustration","Dessin",
"Peinture","Sculpture","Ceramique","Artisanat","Poterie","Calligraphie","Broderie","Tricot","Crochet","Origami",
"Papier","Carton","Crayon","Gomme","Regle","Compas","Ciseaux","Colle","Pinceau","Palette",
"Toile","Encre","Aquarelle","Gouache","Acrylique","Pastel","Fusain","Craie","Carnet","Croquis",
"PeintureMurale","Mosaïque","Galerie","Musee","Exposition","Oeuvre","ChefDoeuvre","ArtistePeintre","Collectionneur","Antiquite",
"Voyageur","Touriste","Guide","GuideTouristique","Passeport","Visa","Reservation","Reception","Receptionniste","Bagage",
"Bagagerie","Auberge","Camping","Tente","Caravane","Chalet","Villa","Bungalow","Suite","ChambreDouble",
"ChambreSimple","CleDeChambre","Ascenseur","Escalator","Hall","Lobby","PiscineHotel","Spa","Sauna","Jacuzzi",
"Plongee","Surf","Voile","Kayak","Canoe","Randonnee","Trekking","CampingSauvage","Excursion","Visite",
"Monument","Chateau","Palais","Cathedrale","Basilique","Tour","Statue","Fontaine","PlacePublique","Parc",
"ParcNational","Zoo","Aquarium","JardinBotanique","ReserveNaturelle","SiteHistorique","Patrimoine","Ruine","Vestige","Archeologie",
"TransportPublic","TransportPrive","Autoroute","RouteNationale","Boulevard","Avenue","Rue","Impasse","Carrefour","RondPoint",
"Trottoir","PassagePieton","FeuRouge","FeuVert","Panneau","PanneauRoutier","Permis","Conduite","StationService","Essence",
"Diesel","Recharge","Vehicule","Automobile","Camion","Camionnette","Tracteur","Tramway","Trolleybus","Funiculaire",
"Telepherique","Ferry","Paquebot","Voilier","SousMarin","Aeroport","Gare","GareRoutiere","PortMaritime","Terminal",
"Embarquement","Decollage","Atterrissage","Correspondance","RetardDeTrain","Annulation","Trajet","Itineraire","Carte","Boussole",
"GPS","Navigation","Direction","Nord","Sud","Est","Ouest","NordEst","NordOuest","SudEst",
"SudOuest","Gauche","Droite","ToutDroit","Prochain","Precedent","Premier","Dernier","PremierEtage","RezDeChaussee",
"PremierSecours","Urgence","Ambulance","PompierVolontaire","Sauvetage","Secours","Danger","Risque","Accident","Incendie",
"Explosion","Inondation","Seisme","TremblementDeTerre","GlissementDeTerrain","Cyclone","Ouragan","Tsunami","Canicule","Secheresse",
"Pollution","Dechet","Recyclage","Compost","Environnement","Biodiversite","Ecosysteme","Conservation","Protection","Durabilite",
"Renouvelable","Solaire","Eolien","Hydraulique","Geothermie","PanneauSolaire","Eolienne","Centrale","Nucleaire","Carbone",
"EmpreinteCarbone","Emission","GazAEffetDeSerre","Ozone","Atmosphere","Oxygene","Hydrogene","Azote","Carburant","Combustible",
"Metallurgie","Materiau","Acier","Aluminium","Cuivre","Plomb","Zinc","Etain","ArgentMassif","Alliage",
"Plastique","Caoutchouc","VerreTrempe","Porcelaine","Beton","Ciment","Brique","Tuile","Cimenterie","Construction",
"Batiment","Chantier","Fondation","Charpente","Toiture","Isolation","Peinture","Renovation","Decoration","Amenagement",
"Meuble","Mobilier","Interieur","Exterieur","ArchitectureModerne","Urbanisme","Ingenierie","Mecanique","Electronique","Robot",
"Automatisation","Impression3D","Nanotechnologie","Biotechnologie","Informatique","Telecommunication","Satellite","FibreOptique","Bluetooth","WiFi",
"ApplicationMobile","SystemeExploitation","Windows","Linux","Android","iOS","MacOS","Python","Java","JavaScript",
"HTML","CSS","React","NodeJS","Git","GitHub","API","JSON","XML","SQL",
"PHP","CSharp","Cpp","Ruby","Swift","Kotlin","TypeScript","Django","Flask","Laravel",
"Framework","Bibliotheque","Editeur","Terminal","Console","Debogage","Compilation","Execution","Test","Deploiement",
"ServeurLocal","HebergementWeb","NomDeDomaine","CertificatSSL","Referencement","SEO","InterfaceUtilisateur","ExperienceUtilisateur","UX","UI",
"Maquette","Prototype","Wireframe","Responsive","Accessibilite","DesignSystem","Typographie","MiseEnPage","PaletteDeCouleurs","AnimationWeb",
"Transition","Composant","Widget","Plugin","Extension","Theme","Template","Depot","BrancheGit","Commit",
"Fusion","PullRequest","Issue","Documentation","Licence","OpenSource","Versionnage","Sauvegarde","SynchronisationCloud","StockageCloud",
"Intelligence","Creativite","Imagination","Curiosite","Motivation","Determination","Ambition","Inspiration","Optimisme","Pessimisme",
"Emotion","Sentiment","Tendresse","Affection","Gentillesse","Generosite","Compassion","Empathie","Sympathie","Amabilite",
"Politesse","Courtoisie","Honnetete","Loyaute","Fidelite","Serenite","Tranquillite","Calme","JoieDeVivre","Enthousiasme",
"Excitation","Surprise","Etonnement","Colere","Tristesse","Melancolie","Nostalgie","Anxiete","Stress","Inquietude",
"Jalousie","Envie","Culpabilite","Regret","Remords","Honte","Folie","Rire","Sourire","Pleurer",
"Pleurnicher","Crier",



    



"ArigatouGozaimasu","Doumo","DomoArigato","OhayouGozaimasu","Oyasuminasai","MataNe","JaNe","JaMata","MataAshita","Ittekimasu",
"Itterasshai","Tadaima","Okaeri","Okaerinasai","Hajimemashite","Yoroshiku","YoroshikuOnegaishimasu","Shitsurei","Shitsureishimasu","Ojamashimasu",
"OsakiNi","OsakiniShitsurei","Kashikomarimashita","Wakarimashita","Wakarimasen","Shirimasen","SouDesu","SouDesuNe","SouKa","Hontou",
"HontouNi","Mochiron","Tabun","Zenzen","Chotto","Sukoshi","Takusan","Totemo","Meccha","Sugoku",
"Yappari","Naruhodo","Eeto","Ano","Soredewa","Dakara","Demo","Kedo","Mada","Mou",
"Yatto","Sugu","Itsumo","Tokidoki","TamaNi","Yoku","Amari","Hotondo","Kitto","Zettai",
"TabunNe","Naze","Doushite","Dore","Dono","Dare","Doko","Ikutsu","Ikura","Nanji",
"Nannen","Nangatsu","NanYoubi","NanNichi","Nani","Nandemo","Dareka","Nanimono","Dokoka","Itsuka",
"Watashi","Watakushi","Boku","Ore","Atashi","Uchi","Kimi","Anata","Omae","Kare",
"Kanojo","Karera","Watashitachi","Bokura","Minna","Minasan","Jibun","Jishin","Kochira","Sochira",
"Achira","Docchi","Kore","Sore","Are","Kono","Sono","Ano","Koko","Soko",
"Asoko","DokoKa","Kocchi","Socchi","Acchi","Mukai","Tonari","Hidari","Migi","Mae",
"Ushiro","Naka","Soto","Shita","Ue","Yoko","Mannaka","Chikaku","Tooi","Mottomo",
"Hitotsu","Futatsu","Mittsu","Yottsu","Itsutsu","Muttsu","Nanatsu","Yattsu","Kokonotsu","Too",
"Ichi","Ni","San","Yon","Go","Roku","Nana","Hachi","Kyuu","Juu",
"Hyaku","Sen","Man","Oku","Ban","Dai","Kai","Mai","Hon","Hiki",
"Nin","Ko","Satsu","TsukiKazu","Nen","Gatsu","Nichiyou","Getsuyou","Kayou","Suiyou",
"Mokuyou","Kinyou","Doyou","Shuumatsu","Heijitsu","Shukujitsu","Kyuujitsu","Renkyuu","Tanjoubi","TanjoubiOmedetou",
"Seinen","Seijin","Otona","Akachan","Baby","Shounen","Shoujo","Joshi","Danshi","Otoko",
"Onna","Hito","Ningen","Minzoku","Shujin","Okusan","Danna","Tsuma","Otto","Musuko",
"Musume","Chichi","Haha","Chichiue","Hahaue","Sofu","Sobo","Mago","Otomodachi","Shinyuu",
"Yujin","Yuujin","Nakayoshi","Senzo","Shison","Shinseki","Oya","Ryoushin","Kyoudai","Shimai",
"Futago","Ani","Ane","Imouto","Otouto","Itoko","Oji","Oba","Giri","Shiawase",
"Kanashimi","Sabishisa","Tanoshimi","Yorokobi","Ikari","Osore","Fuan","Shinpai","Anshin","Kandou",
"Kyoumi","Suki","Daisuki","Kirai","Daikirai","Aisuru","Koi","KoiBito","Renai","Kokuhaku",
"Yakusoku","Kizutsuku","Namida","Egao","Hohoemi","Nakigao","Manzoku","Fuman","Koukai","Kansha",
"Shinrai","Shinsetsu","Shinsetsuna","Yuujou","Aijou","Kanjou","Seishin","Ishi","Kakugo","Shinnen",
"Shoujiki","Uso","Himitsu","Nazo","Fushigi","YumeMitai","Kiseki","Unmei","Inochi","Seimei",
"Seikatsu","Nichijou","Shumi","Tokugi","Nouryoku","Chishiki","Keiken","Rikai","Riyuu","Mokuteki",
"Keikaku","Junbi","Yotei","Yakuwari","Kettei","Kadai","Mondai","Kotae","Kaiketsu","Houhou",
"Jouhou","Joukyou","Kankei","Katsudou","Taiken","Taido","Shuukan","Shuushoku","Shigoto","Kaisha",
"Shain","Buchou","Shachou","Kaichou","Shunin","Joushi","Buka","Douryou","Senmonka","Shokugyou",
"Kyaria","Mensetsu","Rirekisho","Gakureki","Shikaku","Naiyou","Gyoumu","Eigyou","Keiri","Soumu",
"Jinji","Kaihatsu","Seisan","Eigyoubu","Kaigishitsu","Jimushitsu","Shokuba","Shucchou","Zangyou","Teate",
"Kyuyo","Bonus","Koukyu","Taishoku","Tenshoku","Saishuu","Shokubaiki","Kenshuu","Shidou","Hyouka",
"Seika","Mokuhyou","Seiseki","Tassei","Kouritsu","Kouka","Koujou","Kaizen","Hatten","Shinka",
"Shinpo","Kakushin","Hatsumei","Hakken","Kaihatsu","Sekkei","Kousou","Kikaku","Teian","Shiryou",
"Shorui","Bunsho","Meishi","Inkan","Hanko","Denwa","Keitai","Sumaho","Bangou","DenwaBangou",
"Juusho","Yubin","YuubinBangou","Tegami","Fuutou","Kitte","Hagaki","DenwaChou","Renraku","Henshin",
"Henji","Soushin","Jushin","Tsushin","Kakunin","Touroku","Shinsei","Moushikomi","Shounin","Kyoka",
"Shitsumon","Henji","Setsumei","Houkoku","Soudan","Shirase","Tsutaeru","Kotaeru","Oshieru","Manabu",
"Narau","Renshuu","Fukushuu","Yoshuu","Fukuzatsu","Kantan","Muzukashii","Yasashii","Kibishii","Ureshii",
"Kanashii","Tanoshii","Sabishii","Samishii","Hazukashii","Kowai","Osoroshii","Urusai","Shizuka","Nigiyaka",
"Genki","Byouki","Kenko","Daiji","Taisetsu","Hitsuyou","Fuben","Benri","Anzen","Kiken",
"Abunai","Muzukashisa","KantanNa","Raku","Shindoi","Tsuyoi","Yowai","Kashikoi","Baka","Orokamono",
"AtamaIi","Majime","Yakamashii","Shincho","Yuukan","Kirei","Kitanai","Utsukushii","Kakkoyoku","Subarashii",
"Kirakira","Pikapika","FuwaFuwa","Mochimochi","NikoNiko","WakuWaku","DokiDoki","Zawazawa","Gangan","Bikkuri",
"Hayaku","Osoi","Ookiku","Chiisaku","Takaku","Hikuku","Nagai","Mijikai","Futoi","Hosoi",
"Marui","Shikakui","Hiroi","Semai","Atsuku","Samuku","Atatakai","Suzushii","Nurui","Nukumori",
"Yawarakai","Kataku","Karui","Omoi","Amai","Suppai","Nigai","Karai","Shoppai","Mazui",
"Umai","Kou","Aoi","Akai","Kiiroi","Shiroi","Kuroi","MidoriNo","MurasakiNo","ChairoNo",
"Pinkui","Haiiro","KinIro","GinIro","Nijiiro","Kon","MomoIro","HadaIro","Kogecha","Aizome",
"Kokuban","Enpitsu","Pen","Ballpen","Manshon","Ie","Uchi","Jutaku","Yashiki","Tatemono",
"Birudingu","Heya","DaidoKoro","Daidokoro","Shokudou","Washitsu","Youshitsu","Genkan","Roubu","Roushitsu",
"Toire","Ofuro","Furoba","Sentou","HeyaBoshi","Niwa","Mon","Kabe","Yuka","Yane",
"Tenjou","Mado","Tobira","Kagi","Kakushi","Kaidan","Erebeetaa","Esukareetaa","Denki","Akari",
"Tsukue","Isu","Beddo","Sofa","Tana","Hondana","Tansu","Hako","Fukuro","Kaban",
"Rucksack","Kasa","Nagagutsu","Kutsu","KutsuShita","Fuku","Shatsu","Zubon","Sukaato","Wanピース",
"Seetaa","Kooto","Boushi","Megane","Tokei","Keshou","Kagami","Kushi","Towel","Sekken",
"Shampoo","HaBurashi","HaMigaKi","Kami","Kamikazari","Ribon","Nuno","Ito","Hari","Hasami",
"Hotchikisu","Nori","Keshigomu","Jougi","Nouto","Techou","Jisho","Zasshi","Shinbun","Shashin",
"Eiga","Dorama","Anime","Manga","Geemu","Ongaku","E","Shodou","Bijutsu","Bunka",
"Rekishi","Chiri","Shakai","Seiji","Keizai","Tetsugaku","Shinrigaku","Suugaku","Rika","Butsuri",
"Kagaku","Seibutsu","Chigaku","Tenmon","Kenkyuu","Jikken","Kansatsu","Kadai","Jugyou","Kougi",
"Kyoushi","Kyoushitsu","Seito","Juku","Gakunen","Gakubu","Daigaku","SenmonGakkou","Shougakkou","Chuugakkou",
"Koukou","Nyuugaku","Sotsugyou","ShikenBenkyou","Goukaku","Fugoukaku","Tensuu","SeisekiHyou","Kokugo","EigoBenkyou",
"SuugakuBenkyou","Shukudai","KokubanKeshigomu","Kyoukasho","Sansuu","RikaShitsu","Toshokan","Zemi","Kouza","Kentei",
"ShikakuShiken","GakuseiSeikatsu","GakuseiShou","Koushitsu","Gakuryoku","NouryokuShiken","Moshi","Kakomon","MondaiShuu","Anki",
"Seikatsu","Asagohan","Hirugohan","Bangohan","Yushoku","Shokuji","Ryouri","Chouri","Shokuzai","Niku",
"GyuuNiku","ButaNiku","ToriNiku","Horumon","Sashimi","SushiMeshi","Nigiri","Maki","Temaki","Gunkan",
"Wasabi","Shouyu","Shoga","Nori","Kombu","Wakame","Katsuobushi","Dashi","MisoShiru","Shirumono",
"Yakisoba","Yakimeshi","Karee","KareeRaisu","Gyudon","Katsudon","Tendon","Oyakodon","Donburi","Omuraisu",
"HayashiRaisu","Chahan","Gyoza","Shumai","Nikuman","Manju","Kushiage","Tonkatsu","ShabuShabu","Sukiyaki",
"Nabemono","Oden","Mizutaki","Yakiniku","HiyashiChuka","Somen","Hiyamugi","Chawanmushi","TamagoYaki","Natto",
"Tsukemono","Umeboshi","Furikake","Shichimi","Kombucha","Hojicha","Genmaicha","Sencha","Gyokuro","Kukicha",
"Yuzu","Ume","Kaki","Nashi","Momo","Satsumaimo","Kabocha","Daikon","Gobo","Renkon",
"Shiitake","Maitake","Enoki","Shimeji","Takenoko","Konnyaku","Mame","KuroMame","Azuki","Koshian",
"Shiratama","Kuzumochi","WarabiMochi","Yokan","Monaka","Anmitsu","MitarashiDango","Zenzai","Oshiruko","Kakigori",
"Senbei","Arare","Okaki","Kasutera","Baumkuchen","Cheesecake","Purin","CreamPan","MelonSoda","Calpis",
"Juusu","Mugicha","Amazake","Umeshu","Shochu","Nihonshu","Beeru","Wain","Whisky","Kokutou",
"Honey","Mitsu","Satou","Shio","Koshou","Goma","GomaAbura","Rayu","Ponzu","Mirin",
"RyouriNin","Itamae","Shokunin","Okami","Ryokan","Minshuku","Hotel","Hoteru","Kissaten","Izakaya",
"Yatai","ShokudouTen","RamenYa","SushiYa","Depaato","Konbini","Suupaa","Mise","Ya","Tenpo",
"KaishaIn","Tenin","Tencho","Shihainin","Kachou","Shunin","Shachou","Koumuin","Isha","Kangoshi",
"Keisatsu","Keisatsukan","Shouboushi","Bengoshi","Saibankan","Kisha","Housousha","Unten","Untenshu","Shufu",
"Ryourishi","Bengoshi","Kashu","Haiyuu","Sakka","Mangaka","Gaka","Shashinka","Kashu","Sakkyokuka",
"ShujinKou","Koumu","Koujou","KoujouIn","Kensetsu","Doboku","Kenchiku","DenkiKouji","Kikai","KikaiKou",
"Nouka","Ryouriten","Shokunin","Biyoushi","Riyoushi","Hoken","Nenkin","Zeikin","Shiharai","Ryoushuusho",
"Kaikei","Keisan","Yosan","Shuushi","Shisan","Shakkin","Chokin","Ginkou","KouzaBangou","Furikomi",
"Genkin","Kurejitto","KurejittoKaado","KouzaZandaka","Tegata","Kawase","Kabu","Toushi","Shoken","Shikin",
"Keiyaku","Yakusoku","Kisoku","Hourei","Kenri","Gimu","Sekinin","ShakaiHoken","Koyou","Roudou",
"Shakai","Seido","Seifu","Kokka","Kokumin","Minshu","Senkyou","Touhyou","Giin","Shuchou",
"Shimin","Chihou","Toshi","Inaka","Shima","Hanto","ShimaGuni","Kyoukai","Kokkyou","Chizu",
"ChizuChou","Higashi","Nishi","Minami","Kita","Higashiguchi","Nishiguchi","Minamiguchi","Kitaguchi","Chuo",
"Shiyakusho","Kuyakusho","Kouban","Byouin","Yakkyoku","Gakko","Eki","Kuukou","Minato","BasuTei",
"Jitensha","Kuruma","Takushii","Densha","ShinkansenNori","Chikatetsu","RomenDensha","Fune","Hikouki","Herikoputaa",
"Jidousha","Baiku","Torakku","Sharyou","Untenshu","Untenseki","SharyouKensa","Menkyou","Koutsuu","Shingou",
"Shingouki","Hodou","Kousaten","Hashi","Tonneru","KousokuDouro","Shuuchakueki","Norikae","Kippu","Teikiken",
"Ryokou","Kankou","Kankoukyaku","Ryokan","Shukuhaku","Yoyaku","PasuPoto","Biza","Nimotsu","Ryokoukaisha",
"Annai","Chizu","MichiAnai","Mokutekichi","Shuppatsu","Touchaku","Kaisatsu","Noriba","Bansen","Hassha",
"Teisha","Unkou","JikokuHyou","Okure","Unkyuu","Kyuukou","Tokkyuu","Futsuu","Kakueki","Shuuden",
"Norimono","Jidouhanbaiki","KippuUriage","Koutsuuhi","Gasorin","GasoRinSutando","Chuusha","Chuurin","Parking","Hoken",
"Shizen","Shinrin","Kouen","YamaMich","Yamabiko","Tani","TaniGawa","KawaGishi","Nagare","Nami",
"Shio","Nagisa","SunaHama","Iwa","Ishikawa","Kouyou","Momiji","Take","Matsu","UmeNoKi",
"Tsuru","Kusa","Shibafu","HanaNoKi","Kiku","Yuri","Himawari","Ajisai","Tsubaki","UmeBana",
"Tanpopo","Sumire","Asagao","FujiBana","Kikyou","Suisen","Ran","Koke","Kinoko","Matsutake",
"YamaNoKami","KawaNoMizu","ShinrinYoku","KouenRyokuchi","Kougen","Kazan","Jishin","Taifuu","YukiGuni","Fubuki",
"TaiyouKou","HoshiZora","Amanogawa","Ginga","Wakusei","Chikyuu","Kasei","Mokusei","Dosei","Kisei",
"Suisei","Gesshoku","Nisshoku","UchuuHikoushi","UchuuSen","Eisei","TenmonGaku","Inseki","Ryuusei","Hoshikuzu",
"Seiun","UchuuRyokou","Kisetsu","HaruKaze","NatsuYasumi","AkiKaze","FuyuYasumi","HaruYasumi","NatsuMatsuri","YukiMatsuri",
"Hanami","Tsukimi","Momijigari","Oshougatsu","Setsubun","Hinamatsuri","KodomoNoHi","Tanabata","Obon","ShichiGoSan",
"SeijinNoHi","BunkaNoHi","KenpouKinenbi","KinrouKanshaNoHi","Kurisumasu","KurisumasuIbu","Oomisoka","Hatsumoude","Hatsuyume","Nengajou",
"Otoshidama","Fukubukuro","Koinobori","Hagoita","Kadomatsu","Shimenawa","KagamiMochi","Ema","Omikuji","Ofuda",
"Jinja","Otera","Butsuzou","Daibutsu","Jizou","Inari","Amaterasu","Susanoo","Tsukuyomi","Raijin",
"Fujin","Ryuu","Tatsu","Kappa","YukiOnna","Nekomata","Bakeneko","Karakasa","Nurarihyon","Kodama",
"ZashikiWarashi","Kitsunebi","Hitodama","Yurei","Obake","Bakemono","Mononoke","Ayakashi","Shinigami","Tennou",
"Koutei","Koushitsu","Kizoku","SamuraiDama","Bushi","Daimyou","Shogunate","Bakufu","NinjaDo","Ninjutsu",
"Kenjutsu","Iaido","Kyujutsu","Sumo","Sumotori","Yokozuna","Dohyo","Shiai","Budou","Bujutsu",
"KatanaKaji","Tsuba","Saya","Tsuka","Koshirae","Nihonto","Tachi","Tanto","Naginata","Yari",
"Yumi","Ya","Kabuto","Menpo","Yoroi","Hakama","Haori","Hachimaki","Geta","Zori",
"Tabi","Jinbei","Happi","Furoshiki","Tenugui","Sensu","Uchiwa","Chouchin","Washi","Shuji",
"Shodo","Sumi","SumiE","Kintsugi","Kintsukuroi","Chado","Sadou","Kado","Karesansui","Chashitsu",
"Chawan","Chasen","Chashaku","Natsume","Kama","Furo","Tokonoma","Shoji","Fusuma","Engawa",
"Zabuton","Hibachi","Kotatsu","Shikibuton","Kakejiku","Byobu","Tansu","Getabako","GenkanMat","Noren",
"FutonBedding","TatamiRoom","RyokanRoom","WashitsuStyle","JapaneseGarden","Shakkei","Tsukubai","Ishidoro","Toro","ShishiOdori",
"Odori","BonOdori","AwaOdori","NihonBuyou","Kabuki","Noh","Kyogen","Bunraku","Rakugo","Manzai",
"Karaoke","Taiko","Shamisen","Koto","Biwa","Shakuhachi","Kokyu","Fue","Shinobue","Sanshin",
"JPop","JRock","Enka","Vocaloid","AnimeSong","Opening","Ending","Soundtrack","Character","Heroine",
"ShounenAnime","ShoujoAnime","SeinenAnime","JoseiAnime","Isekai","Mecha","SliceOfLife","RomCom","ShoujoManga","ShounenManga",
"LightNovel","VisualNovel","Doujinshi","Cosplay","Cosplayer","Otaku","MangaKa","AnimeKa","Seiyuu","VoiceActor",
"Studio","Sakuga","SakugaArtist","Genga","Doga","Storyboard","Sakuhin","Sakuhinsha","Kousaku","Eizou",
"SenpaiKouhai","KawaiiCulture","Moe","Tsundere","Yandere","Kuudere","Dandere","Chuunibyou","BakaYarou","Aho",
"Temee","Kisama","Yarou","Kuso","Chikusho","Yabai","Maji","Majide","UsoDesho","Sokka",
"SouNanda","Shouganai","Muri","Mendokusai","UrusaiYo","Yamete","Yamero","Ikuzo","Ikimashou","GanbatteNe",
"DaijoubuDesu","MondaiNai","Kiotsukete","Omedetou","OmedetouGozaimasu","Tasukete","Help","AbunaiYo","Matte","ChottoMatte",
"HayakuShite","Yukkuri","MouIchiDo","MouSukoshi","KocchiKite","AcchiIke","KokoNi","SokoNi","AsokoNi","DokoNi",
"Ikou","Kaerou","Tabeyou","Nomou","Miyou","Kikou","Hanashou","Yomou","Kakou","Asobou",
"Shiyou","Yarou","MouIikai","IiDesu","Dame","Iyada","IiNe","IiYo","SukiDa","Aishiteru",
"DaikiraiDa","KimiGaSuki","IsshoNi","Zutto","Eien","MataAimashou","MataKondo","OdaijiNi","ItadakimasuNe","GochisousamaDeshita"





"Hola","Adiós","Gracias","Por favor","Perdón","Sí","No","Bueno","Malo","Amigo",
"Amiga","Familia","Casa","Hogar","Escuela","Trabajo","Libro","Mesa","Silla","Puerta",
"Ventana","Coche","Auto","Calle","Ciudad","País","Mundo","Agua","Fuego","Tierra",
"Aire","Sol","Luna","Estrella","Cielo","Mar","Río","Montaña","Árbol","Flor",
"Perro","Gato","Pájaro","Pez","Caballo","Vaca","León","Tigre","Oso","Conejo",
"Mano","Cabeza","Ojo","Nariz","Boca","Oreja","Pelo","Cara","Brazo","Pierna",
"Pie","Corazón","Amor","Vida","Tiempo","Día","Noche","Mañana","Tarde","Año",
"Hoy","Ayer","Mañana","Ahora","Después","Antes","Siempre","Nunca","Pronto","Tarde",
"Grande","Pequeño","Alto","Bajo","Bonito","Hermoso","Nuevo","Viejo","Joven","Feliz",
"Triste","Rápido","Lento","Fuerte","Débil","Caliente","Frío","Fácil","Difícil","Importante"
    

"Hallo","Tschüss","Danke","Bitte","Entschuldigung","Ja","Nein","Gut","Schlecht","Freund",
"Freundin","Familie","Haus","Zuhause","Schule","Arbeit","Buch","Tisch","Stuhl","Tür",
"Fenster","Auto","Straße","Stadt","Land","Welt","Wasser","Feuer","Erde","Luft",
"Sonne","Mond","Stern","Himmel","Meer","Fluss","Berg","Baum","Blume","Hund",
"Katze","Vogel","Fisch","Pferd","Kuh","Löwe","Tiger","Bär","Kaninchen","Hand",
"Kopf","Auge","Nase","Mund","Ohr","Haar","Gesicht","Arm","Bein","Fuß",
"Herz","Liebe","Leben","Zeit","Tag","Nacht","Morgen","Abend","Jahr","Heute",
"Gestern","Morgen","Jetzt","Später","Früher","Immer","Niemals","Bald","Groß","Klein",
"Hoch","Niedrig","Schön","Hübsch","Neu","Alt","Jung","Glücklich","Traurig","Schnell",
"Langsam","Stark","Schwach","Heiß","Kalt","Einfach","Schwierig","Wichtig","Richtig","Falsch"



"Ciao","Arrivederci","Grazie","Prego","Scusa","Sì","No","Buono","Cattivo","Amico",
"Amica","Famiglia","Casa","Scuola","Lavoro","Libro","Tavolo","Sedia","Porta","Finestra",
"Macchina","Strada","Città","Paese","Mondo","Acqua","Fuoco","Terra","Aria","Sole",
"Luna","Stella","Cielo","Mare","Fiume","Montagna","Albero","Fiore","Cane","Gatto",
"Uccello","Pesce","Cavallo","Mucca","Leone","Tigre","Orso","Coniglio","Mano","Testa",
"Occhio","Naso","Bocca","Orecchio","Capelli","Viso","Braccio","Gamba","Piede","Cuore",
"Amore","Vita","Tempo","Giorno","Notte","Mattina","Pomeriggio","Sera","Anno","Oggi",
"Ieri","Domani","Adesso","Dopo","Prima","Sempre","Mai","Presto","Grande","Piccolo",
"Alto","Basso","Bello","Brutto","Nuovo","Vecchio","Giovane","Felice","Triste","Veloce",
"Lento","Forte","Debole","Caldo","Freddo","Facile","Difficile","Importante","Vero","Falso"








"Привет","Здравствуйте","Пока","До свидания","Спасибо","Пожалуйста","Извините","Да","Нет","Хорошо",
"Плохо","Друг","Подруга","Семья","Дом","Школа","Работа","Книга","Стол","Стул",
"Дверь","Окно","Машина","Улица","Город","Страна","Мир","Вода","Огонь","Земля",
"Воздух","Солнце","Луна","Звезда","Небо","Море","Река","Гора","Дерево","Цветок",
"Собака","Кошка","Птица","Рыба","Лошадь","Корова","Лев","Тигр","Медведь","Кролик",
"Рука","Голова","Глаз","Нос","Рот","Ухо","Волосы","Лицо","Рука","Нога",
"Ступня","Сердце","Любовь","Жизнь","Время","День","Ночь","Утро","Вечер","Год",
"Сегодня","Вчера","Завтра","Сейчас","Потом","Раньше","Всегда","Никогда","Скоро","Большой",
"Маленький","Высокий","Низкий","Красивый","Новый","Старый","Молодой","Счастливый","Грустный","Быстрый",
"Медленный","Сильный","Слабый","Горячий","Холодный","Лёгкий","Трудный","Важный","Правильный","Неправильный"


"Olá","Tchau","Obrigado","Obrigada","Por favor","Desculpa","Sim","Não","Bom","Mau",
"Amigo","Amiga","Família","Casa","Lar","Escola","Trabalho","Livro","Mesa","Cadeira",
"Porta","Janela","Carro","Rua","Cidade","País","Mundo","Água","Fogo","Terra",
"Ar","Sol","Lua","Estrela","Céu","Mar","Rio","Montanha","Árvore","Flor",
"Cachorro","Gato","Pássaro","Peixe","Cavalo","Vaca","Leão","Tigre","Urso","Coelho",
"Mão","Cabeça","Olho","Nariz","Boca","Orelha","Cabelo","Rosto","Braço","Perna",
"Pé","Coração","Amor","Vida","Tempo","Dia","Noite","Manhã","Tarde","Ano",
"Hoje","Ontem","Amanhã","Agora","Depois","Antes","Sempre","Nunca","Logo","Grande",
"Pequeno","Alto","Baixo","Bonito","Feio","Novo","Velho","Jovem","Feliz","Triste",
"Rápido","Lento","Forte","Fraco","Quente","Frio","Fácil","Difícil","Importante","Verdadeiro"
    







    



    






"Geureohda","Ireohda","Itta","Eoptta","Hada","Meokda","Masida","Boda","Deutda","Malhada",
"Gada","Oda","Jada","Il-eonada","Anjda","Seoda","Geotda","Dallida","Ttwida","Nolda",
"Utda","Ulda","Useuda","Sseuda","Ilkda","Sseuda","Baeuda","Gareuchida","Mandeulda","Sada",
"Palda","Juda","Badda","Bonaeda","Gajida","Deurida","Chatda","Chajda","Chajaboda","Gieokhada",
"Ihaehada","Saenggakhada","Gominhada","Gyeoljeonghada","Seontaekhada","Sijakhada","Kkeutnada","Kkeutnaeda","Junbihada","Yaksokhada",
"Yoyonghada","Pilyohada","Wonhada","Barahada","Gidae하다","Saranghada","Jon경hada","Mideuda","Mitda","Bandae하다",
"Chanhada","Buhada","Geochada","Gongbu하다","Yeonseuphada","Gyeongheomhada","Yeongu하다","Gyesanhada","Jeongri하다","Seolmyeong하다",
"Munje","Haegyeol","Dapbyeon","Yoyak","Juje","Jaryo","Jeongbo","Jisik","Gyehoek","Gyeongheom",
"Yeojeong","Gyeolgwа","Wonin","Iy유","Mokjeok","Bangbeop","Sujeong","Gae선","Baljeon","Seongjang",
"Byeonhwa","Gisul","Neung력","Ja능","Sillyeok","Sil력","Jaryo실","Gyeong력","Jeon문가","Jeon문성",
"Geun무","Jigeob","Hoe사","Sang사","Sang담","Hyeop력","Hyeop상","Hoeui","Bogo","Gyeol재",
"Geum액","Sugeum","Jigeup","Yeon봉","Bogeum","Hyuga","Chul근","Toegeun","Chuljang","Hoe식",
"Samusil","Hoesa원","Dong료","Sang사","Bujang","Gw장","Sajang","Daepyo","Tim장","Sils장",
"Jigeum","Geuttae","Dae신","Geureonde","Hajiman","Geuraeseo","Ttaemune","Ttara서","Geureom","Mande",
"Am튼","Gakkeum","Jaju","Hang상","Jeon혀","Daero","Gakkeumssik","Maeil","Bam마다","Eonjenga",
"Amu때","Eotteonji","Eodiseo","Eodiro","Eoddeon","Eotteon geot","Ireoke","Geureoke","Jeogi","Yeogi",
"Geogi","Ijjok","Geujjok","Eoneu jjok","Ape","Dwie","O른쪽","Oen쪽","Wiye","Arae",
"An","Bakkat","Gakkai","Meolli","Saie","Gaunde","Kkeut","Sijak","Gajang","Jeil",
"Deo","Deol","Manhi","Jeogeun","Jeokdanghi","Chungbunhi","Neomu","Maeu","Ajik","Beolsseo",
"Jogeum","Jom","Dasi","Tto","Gyesok","Gakkeum","Jaju","Hang상","Jeon혀","Daero",
"Saenghwal","Il상","Seupgwan","Gwan습","Gyuje칙","Yak속","Yaksok","Yeo가","Chwie미","Hyeon실",
"Jayeon","Munhwa","Yeoksa","Cheolhak","Gw학","Mihak","Eumak","Misul","Muj용","Yeon극",
"Yeong화","Deurama","Yeb능","Nyuseu","Sin문","Jabji","Chaekbang","So설","Si","Sijo",
"Mun학","Sang징","Pyo현","Chang작","Ye술가","Jak가","Hw가","Sajin","Yeongsang","Nol이터",
"Chuk구","Yagu","Nong구","Jok구","Taegwondo","Suy영","Dallyeogi","Yog가","Deung산","Jajeongeo",
"Geolleum","Cheheom","Gyeonggi","Hun련","Seung리","Pa배","Muj승부","Gyeol승","Jum수","Gyeong기장",
"Seon수","Gamdok","Sim판","Eung원","Gwan중","Gyeong기력","Sok도","Gisul력","Jeollyeok","Jip중",
"Geongang","Undong","Sikdan","Yeongyang","Sumswi","Sims박","Pim곤","Piro","Hyu식","Jam",
"Jamsi","Jamsi man","Gip-eun jam","Kkae다","Pigonhada","Geonganghada","Apeuda","Nappeuda","Naseuda","Joahjida",
"Byeong","Gamgi","Yeol","Gichim","Kong","Meor리아","Baega apeuda","Moksori","Mok apeuda","Sok apeuda",
"Nun apeuda","I apeuda","Heo리 apeuda","Piryohan","Yag","Yabyeong","Byeongwon","Uisa","Gan호사","Jin료",
"Geon강검진","Cheob방","Yakguk","Yagmul","Bokyong","Juseosa","Juseong","Hyeol액","Sumsu","Che온",
"Achim siksa","Jeomsim siksa","Jeonyeok siksa","Gansik","Banchan","Gochu","Maneul","Yangpa","Gamja","Goguma",
"Oi","Danggeun","Baechu","Sangchu","Sigeumchi","Beoseot","Hobak","Gaji","Daepa","Mug",
"Tomato","Gwa일","Sagewa","Bae","Gam","Gyul","Ddalgi","Podo","Chamse외","Bok숭아",
"Jadu","Yuja","Lemon","Pineapple","Mango","Cherry","Blueberry","Raspberry","Coconut","Avocado",
"Mil","Ssal","Guksu","Myeon","Mandu피","Gogi-guk","Miyeok-guk","Doenjang-guk","Gimchi-jjigae","Sundubu-jjigae",
"Samgyetang","Galbitang","Seolleongtang","Gamjatang","Budae-jjigae","Bokkeumbap","Jumeokbap","Gimbap","Bibim-guksu","Kalguksu",
"Jajangmyeon","Jjamppong","Tangsu-yuk","Pajeon","Kimchi-jeon","Gamja-jeon","Tteokguk","Songpyeon","Yakgwa","Hangwa",
"Mat","Masitda","Maepda","Dalkda","Sseuda","Jjapjjalhada","Gopsohada","Sangkeumhada","Gudeulhada","Budeureopda",
"Jjeolgitjjeolgit","Bakkak하다","Chagaun","Ttatteuthada","Tteugeopda","Sikda","Jageun","Keuda","Gireuda","Jjalbda",
"Nopda","Najda","Dugeopda","Eodupda","Balkda","Heurida","Kkaekkeuthada","Deoreopda","Kkeulkkulhada","Gwiyeopda",
"Yeppeuda","Motsaenggida","Meotjida","Gongsonhada","Chin절하다","Bulsanghada","Mujag하다","Jung요하다","Pyeonhada","Bulpyeonhada",
"Jae미있다","Jae미없다","Jis루하다","Sing기하다","Teukbyeolhada","Pyeongbeom하다","Yong감하다","Museopda","Duryeopda","Buseureopda",
"Jinsil하다","Geojit말","Jeong직하다","Seong실하다","Chak하다","Yaks속을 지키다","Yaks속을 어기다","Mian하다","Gom맙다","Gippeuda",
"Seul프다","Hw나다","Jjeung나다","Dap답하다","Se운하다","Oe롭다","Pye안하다","Gippeum","Seul픔","Hw남",
"Chinggu","I웃","Dong네","Gajok","Chin척","Bumo","Hyeong제","Jamae","Nam매","Jach녀",
"Sonja","Suk모","Suk부","Sajon","Sajangnim","Seonsaengnim","Gyo수","Hak생","Dong생","Seon배",
"Hubae","Chinguya","Yeobo","Jagiya","Abeoji","Eomeoni","Harabeoji","Halmeoni","Samchon","Gomo",
"I모","Sacheon","Suk모님","Suk부님","Jipsa","Gwan장","Sajangnim","Gyeong찰","Sop방관","Gong무원",
"Uisa seonsaengnim","Byeonhosa","Gisulja","Yeong업","Hoegye사","Gwan리자","Gae발자","디자이너","Gyeong비원","Gid사",
"Jip","A파트","B파트","Geosil","Chim실","Jubang","Yoksil","Hyeon관","Balkoni","Chang고",
"Byeok","Cheon장","Badak","Mun","Changmun","Hyeon관문","Yeol쇠","Jomyeong","Deung","Seonpunggi",
"Naeng장고","Ses탁기","Cheong소기","Gas레인지","Jeongi","Jeonseon","Chungjeon기","Jeong수기","Jeong리함","Sse레기통",
"Geon물","A파트","O피스텔","A파트먼트","Bildeing","Jutaek","Gye단","El리베이터","Gy통","Juje차장",
"Geori","Gil","Sageori","Gyocha로","Gogae","Dari","Gang","Hosu","San","Sup",
"Deul","Beolpan","Bada","Haebyeon","Seom","Gye곡","Pogpo","Dong굴","Bulkkot","Haneul",
"Gureum","Byeolbit","Haetsal","Dal빛","Mulgyeol","Paranmul","Garam","Sumeul","Namu","Ip",
"Kkot","Ppul","Ssi","Yeol매","Gaji","Bam나무","Sora","Gaeul","Gyeoul","Bom",
"Yeoreum","Gyejeol","Nalssi","Geurimja","Bit","Sori","Baram","Biga","Nun","Seori",
"Angae","Cheondung","Beongae","Mujigae","Taeyang","Taeyangbit","Dal빛","Byeol자리","Uju","Haengseong",
"Geumseong","Hwasong","Mokseong","Toseong","Cheonwangseong","Haewangseong","Sujeong","Geumseong","Eunha","Seongun",
"Yeongha","Gonggi","Saneop","Nong업","Gong업","Gyeong제","Jeong치","Sahoe","Guk가","Jibang",
"Dos시","Gun","Eup","Myeon","Dong","Ri","Gil","Beonji","Juso","U편번호",
"Jang소","Gong공서","Sijang","Mart","Pyeonuijeom","Baek화점","Sang가","Sik당","Kape","Bbangjip",
"Seom유점","Yak국","Byeong원","Eun행","U체국","Doseogwan","Bak물관","Mis술관","Gong원","Undong장",
"Yeong화관","Geuk장","Noraebang","PC방","Mujang","Gyeong찰서","Soseol","Gwan공서","Guk민센터","Jumin센터",
"Jadongcha","Taeksi","Beoseu","Jihacheol","Gicha","Hang공기","Bae","Jajeongeo","Oto바이","Jeon동차",
"Jeong류장","Jeongcha장","Gong항","Gichayeok","Jihacheolyeok","Beoseujeong류장","Pyo","Seung차권","Gyo통카드","Gyo통비",
"Un전","Un전하다","Chul발","Do착","Hwan승","Gireul chajda","Gireul ileuda","Gireul mutda","Gyeong로","Jido",
"Yeong어","Junggukeo","Hangugeo","Ilboneo","Seupeineo","Dokileeo","Peulangseueo","Ita리어","Be트남어","Tae국어",
"Mun법","Dan어","Eo휘","Bal음","Malsseum","Daehwa","Munjang","Daneo장","Sajeon","Beonyeok",
"Haeseok","Gyojeong","Gong부","Sugo","Sigan표","Suj업","Gwa제","Siseom","Jeom수","Seongjeok",
"Chul석","Jigyeyang","Hakgi","Bok학","Ip학","Jol업","Hak위","Jang학금","Gyo재","Gang의",
"Gyosil","Gang의실","Doseogwan","Gong부방","Sil험실","Yeong어실","Cheyuk관","Hakgyo종","Hakgyo버스","Hakgyo생활",
"Il","I","Sam","Sa","O","Yuk","Chil","Pal","Gu","Sip",
"Yeolhana","Yeol-dul","Yeol-set","Yeol-net","Yeol-daseot","Yeol-yeoseot","Yeol-ilgop","Yeol-yeodeol","Yeol-ahop","Seumul",
"Seumulhana","Seumul-dul","Seumul-set","Seumul-net","Seumul-daseot","Seumul-yeoseot","Seumul-ilgop","Seumul-yeodeol","Seumul-ahop","Seoreun",
"Seun","Maheun","Swin","Yesun","Ilheun","Yeo deun","Aheun","Baek","Cheon","Man",
"Yeok","Eok","Jo","Gye","Gyeong","Naeil","Geujeokke","Geujeokke bam","Oneul achim","Oneul bam",
"Jigeum dangjang","Itta","Jom itta","Geumse","Gakkeumssik","Maeju","Maedal","Mae nyeon","Pyeongsaeng","Eon젠가",
"Chul근 sigan","Toegeun sigan","Jeomsim sigan","Siksa sigan","Sigan eopseo","Sigan isseo","Neujeotda","Ireotda","Ppalli","Cheoncheonhi",
"Jigeum","Ije","Ajik","Beolsseo","Dasi hanbeon","Hanbeon deo","Geuman","Meomchwo","Gyesokhae","Sijakhae",
"Junbi dwaesseo","Junbi dwaesseoyo","Gajaboda","Haeboda","Jalhae","Jalhaesseo","Jal mot hae","Geureoji ma","Gwaenchanha","Mollayo",
"Algesseoyo","Arasseoyo","Jinjja","Geurae","Geureom","Ani","Eung","Eo","Ne","Joesonghaeyo",
"Jal moreugesseoyo","Dasi malhaejuseyo","Cheoncheonhi malhaejuseyo","Ihaehaesseoyo","Jal deureoyo","Jal an deullyeoyo","Mwo라고요","Eotteoke haeyo","Eodi isseoyo","Eolma예요",
"Yeogi isseoyo","Jeogi isseoyo","Ige mwoyeyo","Geuge mwoyeyo","Nugu예요","Eonje예요","Wae요","Eotteoke요","Mwo haeyo","Jigeum mwonhaeyo",
"Jigeum gayo","Jigeum wasseoyo","Jibe gayo","Jibe wasseoyo","Hakgyo gayo","Hoesa gayo","Jom swieoyo","Jamkkan gidaryeoyo","Gachi gayo","Ddaeume bwayo",
"Naega halge","Uri hamkke haja","Gachi meogeoyo","Gachi masyeoyo","Gachi gongbuhaeyo","Gachi yeonseuphaeyo","Gachi noraeyo","Gachi georeoyo","Gachi undonghaeyo","Gachi yeohaeng gayo"




"Nihao ma","Nin","Women","Nimen","Tamen","Ziji","Bieren","Dajia","Meiyou","Youshi",
"Shenme","Shei","Nali","Nage","Zhege","Zhexie","Naxie","Duoshao","Jige","Zenme",
"Weishenme","Zenmeyang","Keshi","Yinwei","Suoyi","Ruguo","Ranhou","Danshi","Erqie","Huozhe",
"Yijing","Haishi","Yiding","Keneng","Yinggai","Bixu","Xuyao","Xiwang","Jueding","Tongyi",
"Fandui","Jieshou","Jujue","Xuanze","Fasheng","Faxian","Jide","Wangji","Zhidao","Mingbai",
"Renshi","Jieshao","Wenhou","Dianhua","Shouji","Hao ma","Dianhua hao","Xinxi","Duanxin","Youjian",
"Diannao","Pingban","Shubiao","Jianpan","Pingmu","Wenjian","Wenjianjia","Wangzhan","Liulanqi","Mima",
"Zhanghao","Yonghu","Ruanjian","Yingjian","Biancheng","Kaifa","Ceshi","Shengji","Xiazai","Shangchuan",
"Anzhuang","Shanchu","Baocun","Fuzhi","Zhantie","Qiehuan","Dianji","Anniu","Chuangkou","Biaoge",
"Shujuku","Zhuji","Jiekou","Duanlu","Dianzi","Xinli","Yingxiang","Yunxing","Jiance","Xiufu",
"Zhongxin","Bumen","Gongsi","Danwei","Bangongshi","Laoban","Jingli","Zhuguan","Yuangong","Zhiyuan",
"Mianguan","Mianshi","Jianli","Xinzi","Gongzi","Jiangjin","Tongshi","Kehu","Huiyi","Baogao",
"Hetong","Xiangmu","Renwu","Zeren","Jinbu","Jingyan","Jineng","Zhiye","Hangye","Shichang",
"Jingzheng","Jingying","Xiaoshou","Goumai","Chushou","Jiage","Jinqian","Yinhang","Xinyongka","Xianjin",
"Qianbao","Shouru","Zhichu","Zhangdan","Fapiao","Shangdian","Chaoshi","Shichang","Shangpin","Huowu",
"Kuai di","Baoguo","Yunfei","Dingdan","Fukuan","Tuikuan","Youhui","Zhekou","Tejia","Pinpai",
"Chima","Yanliao","Kuzi","Shangyi","Waitao","Maozi","Xiezi","Wazi","Yifu","Qunzi",
"Chenshan","Niuzai ku","Duanku","Changku","Yundong xie","Pijiu","Shoubiao","Yan jing","Beibao","Xianglian",
"Shafa","Zhuozi","Yizi","Chuang","Guizi","Shujia","Dengzi","Dianfengshan","Kongtiao","Bingxiang",
"Weibolu","Xiyiji","Diannao tai","Dianshi","Yinxiang","Kongzhiqi","Chazuo","Dianchi","Dianxian","Menling",
"Jianzi","Suojia","Maojin","Zhen","Beizi","Panzi","Wan","Kuaizi","Daozi","Cha chi",
"Shuiping","Piaobei","Guozi","Shaguo","Zao","Xiangzao","Yagao","Yashua","Shangye","Weijin",
"Shenti","Tou","Lian","Yanqing","Erduo","Bizi","Zui","Yachi","She tou","Bozi",
"Jianbang","Shoubi","Shouzhang","Shouzhi","Shoubei","Dadu","Yao","Tunbu","Xigai","Xiaotui",
"Jiaojian","Jiaozhi","Pifu","Xueye","Xinzang","Fei","Wei","Gan","Shen","Guli",
"Jingli","Shengti","Jiankang","Yiyuan","Yisheng","Hushi","Bingren","Yaofang","Zhenduan","Shoushu",
"Yimiao","Tizhong","Shengao","Xueya","Tengtong","Fashao","Touyun","Pang","Shou","Lei",
"Jingcha","Xiaofangyuan","Junyiren","Laoshi men","Nongmin","Gongren","Jingliang","Chushi","Fuwuyuan","Siji",
"Feiji","Chuan","Huoche","Didi","Chuzuche","Motoche","Huochezhan","Feijichang","Gangkou","Lukou",
"Shizi lu kou","Renxingdao","Honglvdeng","Dengche","Xiaoche","Dache","Zixingche","Diandongche","Motuoche","Youyongchi",
"Fandian","Luguan","Kezhan","Lvguan","Can ting","Jiudian","Fuwu tai","Dingfang","Tuifang","Lvxing",
"Luxingzhe","Daoyou","Jingdian","Menpiao","Hulianwang","Ditu","Fangxiang","Dongnan","Xinan","Dongbei",
"Xibei","Zhongguo","Beijing","Shanghai","Guangzhou","Shenzhen","Chengdu","Chongqing","Hangzhou","Nanjing",
"Tianjin","Wuhan","Xian","Suzhou","Qingdao","Xiamen","Kunming","Changsha","Harbin","Lasa",
"Shengfen","Shiqu","Xiancheng","Zhenzi","Nongcun","Dushi","Jianzhu","Dasha","Loufang","Gonglu",
"Gaoqiao","Tielu","Huanghe","Changjiang","Shamo","Caoyuan","Huangshan","Taihu","Donghai","Nanhai",
"Beihai","Haidian","Haidong","Didao","Shanmai","Pingyuan","Pendi","Shuiku","Hedi","Hupo",
"Ziran","Huanjing","Kongwu","Wuran","Lajixiang","Laji","Huishou","Nengyuan","Dianli","Shiyou",
"Meitan","Tianranqi","Fadian","Fengneng","Taiyangneng","Shuidian","Dianwang","Shengtai","Senlinbao hu","Shuye",
"Shuizhu","Huaicao","Zhongzi","Shumiao","Guanli","Shifei","Shoucheng","Jingji","Shehui","Zhengfu",
"Falv","Fayuan","Faguan","Jingcha ju","Jundui","Guofang","Guoqi","Guoge","Guohui","Huiyuan",
"Xuanju","Minzhu","Gongmin","Quanli","Yifu","Shuiping","Jiaoyu","Wenhua","Jiaoyu ju","Daxuesheng",
"Zhongxuesheng","Xiaoxuesheng","Youeryuan","Boshi","Shuoshi","Xuewei","Xueqi","Xuefei","Zuoye","Lianxi",
"Yufa","Cihui","Fayin","Kouyu","Yuedu","Tingli","Xiezuo","Fanyi","Kecheng","Jiaoxue",
"Jiangtai","Heiban","Fenbi","Xiuding","Zuowen","Shuxue","Wuli","Huaxue","Shengwu","Dili",
"Lishi","Zhengzhi","Yishu","Tiyu","Waiyu","Zhexue","Xinwen","Baokan","Zazhi","Guangbo",
"Dianshitai","Dianying","Yanyuan","Daoyan","Juqing","Yinyuehui","Yanchang","Wudao","Huazhan","Biaoyan",
"Shouji youxi","Diannao youxi","Zhuoyou","Qipai","Weiqi","Xiangqi","Ma jiang","Pai","Qiu","Pangqiu",
"Zuqiuchang","Lanqiuchang","Wangqiu","Yumaoqiu","Pangkeqiu","Pingtai","Yundongyuan","Jiaolian","Bisai","Xunlian",
"Jianshen","Paobu","Sanbu","Tiaosheng","Tiaoyuan","Tiaogao","Dengshan","Huaxue","Bingqiu","Huachuan",
"Shuishang","Huwai","Ziranjie","Luying","Zhangpeng","Dengju","Huoshan","Dizhen","Hongshui","Taifeng",
"Baoyu","Qingkong","Qingtian","Yintian","Duoyun","Wendu","Shidu","Jidu","Jieri","Jiaqi",
"Chunjie","Zhongqiujie","Duānwu jie","Qingming jie","Yuandan","Guoqing jie","Shengdan jie","Shengri","Zhuri","Xingqi",
"Xingqiyi","Xingqier","Xingqisan","Xingqisi","Xingqiwu","Xingqiliu","Xingqitian","Yuefen","Riqi","Shijian biao",
"Zhongdian","Fenzhong","Xiaoshi","Xingqi","Jidu","Bannian","Niandu","Shiji","Shidai","Congqian",
"Xianzhi","Jianglai","Guguo","Zhengzai","Ganggang","Liji","Yuanlai","Yibian","Yizhi","Zongshi",
"Yiban","Tebie","Qingchu","Zhengque","Cuowu","Zhunque","Anquan","Weixian","Fangbian","Mafan",
"Shufu","Jingcai","Youqu","Wuyiliao","Xiangxin","Danxin","Fangan","Zhuyi","Jinggao","Zhuyao",
"Zhongyao","Tinghua","Bangmang","Guanxin","Zhaogu","Zhaodai","Jiedai","Tao lun","Jiaoliu","Fenxiang",
"Jieshi","Tixing","Jianyi","Jueding","Chengren","Chengdan","Baohu","Zunzhong","Guli","Biaoyang",
"Jinqing","Nuli","Jianchi","Xuehui","Tigao","Gaijin","Shixian","Chuangzao","Fuwu","Gongzuo",
"Xiuxi","Fangjia","Jiawu","Shenghuo","Rizi","Xiguan","Yundong","Xingqu","Aihao","Shengyin",
"Yanjing","Xiangwei","Qiqiu","Qingjing","Ganqing","Xinqing","Yiyi","Xiaolian","Xiaosheng","Daxiao",
"Shengyin","Weidao","Kouwei","Wenrou","Yinglang","Congming","Keai","Youhao","Renzhen","Yonggan"






    















    


    
    






    



    




"Annyeong","Annyeonghaseyo","Gamsahamnida","Gomawo","Mianhae","Joesonghamnida","Ne","Aniyo","Jalga","Jaljayo",
"Sarang","Saranghae","Chingu","Gajok","Appa","Eomma","Oppa","Unni","Hyung","Noona",
"Halabeoji","Halmeoni","Agi","Haksaeng","Seonsaeng","Hakgyo","Daehak","Gongbu","Chaek","Yeonseup",
"Siheom","Jilmun","Dab","Hangugeo","Yeongeo","Ilboneo","Junggukeo","Bulgieo","Latingeo","Hanguk",
"Seoul","Busan","Incheon","Daegu","Daejeon","Gwangju","Jeju","Namsan","HanRiver","Gyeongbokgung",
"Taekwondo","Hanbok","Kimchi","Bibimbap","Bulgogi","Japchae","Tteokbokki","Kimbap","Ramyeon","Mandu",
"Doenjang","Gochujang","Makgeolli","Soju","Bingsu","Hotteok","Samgyeopsal","Galbi","Naengmyeon","Jajangmyeon",
"Haneul","Hae","Dal","Byeol","Bada","San","Gang","Sup","Kkot","Namu",
"Baram","Bi","Nun","Eoreum","Bul","Mul","Heuk","Gureum","Cheonguk","Uju",
"Segye","Jigu","Galaxy","Universe","Him","Yonggi","Huimang","Pyeonghwa","Jayu","Jeonseung",
"Seonggong","Silpae","Mokpyo","Ggum","Yeoljeong","Noryeok","Innae","Jasin","Jihye","Jisik",
"Chingudeul","Yeohaeng","Moheom","Yeongung","Jeonseol","Champion","Master","Elite","Power","Energy",
"Bballi","Cheoncheonhi","Keuda","Jageun","Nopda","Najda","Gin","Jjalbda","Saeroun","Oraedoen",
"Yeppeuda","Meotjida","Ganghada","Yakhada","Ppareuda","Neurida","Kkaekkeutha","Eoryeopda","Swipda","Bokjapda",
"Geomjeong","Hayang","Ppalgang","Parang","Noran","Chorok","Bora","Bunhong","Eun","Geum",
"Diamondeu","Jinjoo","Ruby","Sapphire","Emerald","Apple","Banana","Orange","Grape","Strawberry",
"Subak","Melon","Peach","Pear","Rice","Bap","Guk","Kim","Yachae","Gogi",
"Dakgogi","Dwaejigogi","Sogogi","Gyeran","Dubu","Coffee","Cha","Mul","Juice","Milk",
"Eumak","Norae","Game","Player","Winner","Loser","Legend","Hero","Level","Mission",
"Reward","Bonus","Daily","Weekly","Monthly","Event","Festival","Chuseok","Seollal","Lotus",
"Code","Program","Computer","Internet","Server","Network","Data","Memory","Cache","Logic",
"Engine","System","Module","Cloud","Thread","Packet","Signal","Process","Automation","Technology",
"Development","Engineer","Architecture","Programming","Optimization","Leadership","Management","Strategy","Planning","Execution",
"One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
"Hana","Dul","Set","Net","Daseot","Yeoseot","Ilgop","Yeodeol","Ahop","Yeol"


"Buna","Salut","LaRevedere","Multumesc","Scuze","TeRog","Da","Nu","Poate","Bine",
"FoarteBine","Perfect","Excelent","Minunat","Frumos","Puternic","Curajos","Rapid","Incet","Mare",
"Mic","Lung","Scurt","Nou","Vechi","Cald","Rece","Curat","Simplu","Greu",
"Usor","Lumina","Umbra","Soare","Luna","Stea","Cer","Nor","Ploaie","Zapada",
"Vant","Foc","Apa","Pamant","Aer","MareApa","Ocean","Lac","Raul","Munte",
"Vale","Padure","Copac","Floare","Frunza","Gradina","Drum","Pod","Oras","Sat",
"Casa","Camera","Usa","Fereastra","Scoala","Universitate","Profesor","Student","Carte","Caiet",
"Pix","Creion","Examen","Intrebare","Raspuns","Invatare","Limba","Romana","Engleza","Japoneza",
"Chineza","Coreeana","Franceza","Latina","Familie","Mama","Tata","Frate","Sora","Bunic",
"Bunica","Copil","Prieten","Erou","Campion","Legenda","Maestru","Rege","Regina","Print",
"Printesa","Razboinic","Soldat","Pilot","Medic","ProfesorX","Inginer","Artist","Scriitor","Cititor",
"Munca","Birou","Companie","Calculator","Laptop","Tastatura","Mouse","Ecran","Internet","Retea",
"Server","Date","Cod","Program","Aplicatie","Sistem","Motor","Modul","Memorie","Cache",
"Fir","Pachet","Semnal","Proces","Automatizare","Tehnologie","Stiinta","Arhitectura","Dezvoltare","Optimizare",
"Succes","Victorie","Respect","Onoare","Mandrie","Incredere","Credinta","Pace","Libertate","Speranta",
"Vis","Scop","Plan","Strategie","Conducere","Management","Echipa","Comunicare","Colaborare","Creatie",
"Inovatie","Explorare","Aventura","Calatorie","Viitor","Progres","Energie","Putere","Spirit","Minte",
"Inima","Suflet","Fericire","Bucurie","Zambet","Iubire","Prietenie","FamilieX","Responsabilitate","Disciplina",
"Rabdare","Perseverenta","Determinare","Motivatie","Performanta","Excelenta","Creativitate","Inteligenta","Cunoastere","Experienta",
"Rosu","Albastru","Verde","Galben","Alb","Negru","Mov","Portocaliu","Roz","Argint",
"Aur","Bronz","Diamant","Perla","Rubin","Smarald","Safir","Mar","Banana","Portocala",
"Capsuna","Strugure","Pepene","Paine","Lapte","Cafea","Ceai","Supa","Orez","Carne",
"Pui","Peste","Leguma","Fruct","Muzica","Joc","Jucator","Nivel","Misiune","Premiu",
"Bonus","Zilnic","Saptamanal","Lunar","Festival","Traditie","Primavara","Vara","Toamna","Iarna"


"Salve","Vale","Gratias","Quaeso","Ita","Non","Fortis","Virtus","Honor","Gloria",
"Pax","Amor","Spes","Fides","Veritas","Lux","Nox","Dies","Tempus","Vita",
"Mors","Anima","Mens","Cor","Ignis","Aqua","Terra","Caelum","Ventus","Mare",
"Sol","Luna","Stella","Natura","Silva","Flumen","Mons","Campus","Via","Domus",
"Urbs","Villa","Regnum","Imperium","Civitas","Populus","Familia","Pater","Mater","Frater",
"Soror","Filius","Filia","Amicus","Magister","Discipulus","Rex","Regina","Princeps","Miles",
"Bellum","Victoria","PaxX","Gladius","Scutum","Sagitta","Arcus","Equus","Leo","Lupus",
"Canis","Felis","Aquila","Draco","Serpens","Avis","Piscis","Bos","Ovis","Capra",
"Panis","Vinum","AquaVitae","Lac","Mel","Fructus","Malum","Pirum","Uva","Cibus",
"Forum","Templum","Ecclesia","Bibliotheca","Schola","Academia","Scientia","Sapientia","Doctrina","Lingua",
"Littera","Liber","Scriptum","Numerus","Calculus","Ratio","Cogitatio","Memoria","Ingenium","Consilium",
"Labor","Opus","Ars","Machina","Ferrum","Aurum","Argentum","Cuprum","Plumbum","Stannum",
"Successus","Progressus","Motus","Potentia","Vis","Robur","Constantia","Patientia","Disciplina","Perseverantia",
"Excellentia","Magnitudo","Altitudo","Longitudo","Latitudo","Celeritas","Gravitas","Claritas","Puritas","Unitas",
"Libertas","Aequitas","Iustitia","Prudentia","Temperantia","Fortitudo","SapientiaX","Humanitas","Dignitas","Nobilitas",
"Universum","Cosmos","Orbis","Planeta","Galaxia","Astrum","Cometa","Nebula","Caeli","Aether",
"Initium","Finis","Primus","Secundus","Tertius","Quartus","Quintus","Sextus","Septimus","Octavus",
"Nonus","Decimus","Unus","Duo","Tres","Quattuor","Quinque","Sex","Septem","Octo",
"Novem","Decem","Centum","Mille","Infinitus","Aeternus","Novus","Antiquus","Parvus","Magnus",
"Bonus","Malus","Pulcher","Tristis","Laetus","Felix","Miser","Calidus","Frigidus","Albus",
"Niger","Ruber","Viridis","Caeruleus","Flavus","Purpureus","Roseus","Argenteus","Aureus","Brunneus",
"Navigare","Currere","Ambulare","Legere","Scribere","Audire","Videre","Dicere","Facere","Creare",
"Laborare","Discere","Docere","Vivere","Ridere","Flere","Cantare","Saltare","Vincere","Servare",
"Custodire","Mutare","Aperire","Claudere","Invenire","Cogere","Ferre","Dare","Accipere","Tenere",
"Praemium","Donum","Munus","Officium","Negotium","Mercator","Artifex","Agricola","Poeta","Orator",
"Philosophus","Medicus","Architectus","Imperator","Senator","Consul","Praetor","Centurio","Legatus","Explorator"



"Nihao","Zaoshanghao","Wanans","Xiexie","Bukeqi","Duibuqi","Qing","Zaijian","Shi","Bu",
"Haode","Keyi","Dangran","Meiguanxi","Henhao","Feichanghao","Kaixin","Gaoxing","Xingfu","Heping",
"Ai","Pengyou","Jiaren","Laoshi","Xuesheng","Tongxue","Haizi","Baba","Mama","Gege",
"Jiejie","Didi","Meimei","Yeye","Nainai","Shushu","Ayi","Shifu","Yingxiong","Guowang",
"Gongzhu","Wangzi","Long","Laohu","Mao","Gou","Niao","Yu","Xiongmao","Huli",
"Shizi","Daxiang","Houzi","Tuzi","Yang","Niu","Ma","Ji","Ya","E",
"Shan","He","Hai","Hu","Senlin","Shulin","Hua","Shu","Yezi","Taiyang",
"Yueliang","Xingxing","Tiankong","Yun","Yu","Xue","Feng","Lei","Shandian","Huo",
"Shui","Tu","Kongqi","Shijie","Yuzhou","Yinhe","Diqiu","Tian","Guojia","Chengshi",
"Xiangcun","Jia","Fangjian","Chufang","Men","Chuanghu","Yuanzi","Qiao","Lu","Jiedao",
"Xuexiao","Daxue","Jiaoshi","Keben","Biji","Gangbi","Kaoshi","Wenti","Huida","Xuexi",
"Yuwen","Yingyu","Riyu","Hanyu","Hanguoyu","Fayu","Ladingyu","Shijian","Jintian","Mingtian",
"Zuotian","Zaoshang","Zhongwu","Wanshang","Meitian","Xianzai","Yihou","Yiqian","Kaishi","Jieshu",
"Chi","He","Kan","Ting","Shuo","Xie","Du","Pao","Zou","Gongzuo",
"Wan","Changge","Tiaowu","Mai","MaiChu","Song","Shou","Dakai","Guanbi","Deng",
"Chenggong","Shibai","Shengli","Jiangli","Mubiao","Mengxiang","Xiwang","Yongqi","Liliang","Zhihui",
"Jihua","Lingdao","Chuangxin","Jishu","Kexue","Gongcheng","Jisuanji","Wangluo","Fuwuqi","Shuju",
"Daima","Chengxu","Neicun","Huancun","Xitong","Yingyong","Jiqiren","Zidonghua","Tongxin","Hezuo",
"Kuai","Man","Da","Xiao","Gao","Di","Chang","Duan","Xin","Jiu",
"Qiang","Ruo","Piaoliang","Ganjing","Fuza","Jiandan","Rongyi","Kunnan","Hong","Lan",
"Lv","Huang","Hei","Bai","Hui","Zi","Fen","Jin","Yin","Tong",
"Zuanshi","Baoshi","Zhenzhu","Shuijing","Pingguo","Xiangjiao","Chengzi","Caomei","Xigua","Putao",
"Fan","Mian","Jiaozi","Baozi","Chaofan","Tang","Doufu","Mifan","Miantiao","Jidan",
"Jirou","Zhurou","Niurou","Yumi","Qingcai","Shucai","Shuiguo","Naitang","Kafei","Cha",
"Yinyue","Youxi","Wanjia","Guanjun","Chuanqi","Gaoshou","Dashi","Jingying","Shengji","Weilai",
"Chaoji","Wudi","Zuijia","Diyi","DiEr","DiSan","ShengliZhe","Tiaozhan","Tanxian","Qiji"  





"Adapt","Adaptable","Adaptation","Adopt","Adjust","Adjusted","Adjustment","Admire","Adore","Agile",
"Agility","Agree","Agreement","Aid","Assist","Assistance","Ally","Alliance","Ambition","Ambitious",
"Ample","Anchor","Animate","Announce","Answer","Appeal","Apply","Appreciate","Approach","Aspire",
"Assure","Astonish","Attain","Attempt","Attend","Attract","Authentic","Authority","Awareness","Beacon",
"Beaming","Beauty","Begin","Beginning","Belong","Benefit","Benevolent","Beyond","Bold","Boldness",
"Bound","Boundless","Breakthrough","Breathe","Breeze","Brilliant","Brilliance","Broaden","Brotherly","Capability",
"Capable","Capacity","Care","Careful","Carefree","Caring","Catalyst","Caution","Celebrate","Celebration",
"Center","Certain","Certainty","Change","Character","Charity","Charm","Cheer","Cheerful","Cherish",
"Choice","Choose","Climb","Closer","Coherent","Coincide","Comfort","Comforting","Command","Compassion",
"Compete","Competition","Competence","Competent","Complete","Completion","Compose","Composure","Concentrate","Concept",
"Connect","Connection","Conquer","Conquest","Conscious","Consider","Construct","Constructive","Consume","Contribute",
"Contribution","Conviction","Convince","Cooperate","Courage","Courteous","Craft","Craftsmanship","Credible","Credibility",
"Cultivate","Curious","Curiosity","Daring","Dash","Dawn","Decent","Decide","Decisive","Deep",
"Deepen","Defend","Defense","Define","Definite","Delight","Deliverance","Demand","Depend","Dependable",
"Depth","Deserve","Desire","Destiny","Detail","Detect","Determine","Devote","Devoted","Devotion",
"Dignity","Discover","Discovery","Distinct","Distinction","Diverse","Diversity","Doable","Donate","Double",
"Durable","Duty","Dynamic","Eager","Ease","Easygoing","Educate","Education","Effective","Effectiveness",
"Efficient","Efficiency","Effort","Empower","Empowerment","Enable","Encourage","Endurance","Endure","Engage",
"Engagement","Enlighten","Enrich","Ensure","Enterprising","Enthusiasm","Enthusiastic","Entire","Equality","Equip",
"Equitable","Establish","Esteem","Ethical","Evaluate","Evolve","Evolution","Exact","Exceed","Excite",
"Excitement","Expand","Expansion","Expect","Express","Expression","Extend","Extension","Fair","Fairness",
"Fame","Familiar","Famous","Fancy","Fantastic","Fascinate","Fearless","Feature","Finish","Firm",
"Fit","Fitness","Flexible","Flexibility","Flourish","Flow","Fluent","Fly","Follow","Forceful",
"Forgive","Forgiveness","Fortunate","Fortune","Forward","Foster","Foundation","Frank","Frankness","Friendly",
"Friendship","Fulfill","Fulfillment","Fun","Fundamental","Funny","Generous","Generosity","Genuine","Gift",
"Gifted","Giveback","Glad","Gladness","Goal","Goal-oriented","Goodness","Grateful","Gratitude","Grounded",
"Guarantee","Guidance","Guide","Guideline","Habit","Harmony","Harmonious","Heal","Healing","Healthy",
"Helpful","Helpfulness","Heroic","Highlight","Honest","Honesty","Hopeful","Horizon","Humble","Humility",
"Humor","Ideal","Idealism","Identify","Identity","Ignite","Illustrious","Imagine","Imagination","Immense",
"Immortal","Impartial","Implement","Important","Impress","Impressive","Improvement","Include","Inclusion","Independent",
"Independence","Individual","Influence","Influential","Inform","Inspire","Inspiration","Integrity","Intense","Intensity",
"Intent","Intentional","Interact","Interaction","Interest","Interesting","Interpret","Invent","Inventive","Invention",
"Invest","Investment","Invite","Involve","Involvement","Joy","Joyful","Joyfulness","Judge","Judgment",
"Just","Justice","Keen","Kind","Kindness","Knowledgeable","Labor","Launch","Lawful","Legacy",
"Liberty","Lifelong","Limitless","Lively","Livelihood","Logical","Longevity","Loyal","Loyalty","Luck",
"Lucky","Magic","Magical","Magnify","Magnitude","Maintain","Maintenance","Makeover","Manifest","Manifestation",
"Marvel","Marvelous","Meaning","Meaningful","Meditate","Meditation","Mentor","Mentorship","Merit","Method",
"Methodical","Mighty","Mindful","Mindfulness","Miracle","Miraculous","Mission","Modest","Moderation","Momentum",
"Motivate","Motivation","Motivational","Motive","Multitask","Natural","Nature","Navigate","Navigation","Nearness",
"Neat","Necessity","Nerve","Nurture","Objective","Objective-minded","Observe","Obtain","Occupy","Offer",
"Open-minded","Opportunity","Optimism","Optimistic","Option","Order","Organized","Original","Originality","Outcome",
"Outperform","Outstanding","Overcome","Ownership","Pace","Passion","Passionate","Peaceful","Peak","Perceive",
"Perfect","Perfection","Perfectly","Perfectionist","Perspective","Persuade","Phenomenal","Pioneer","Pioneering","Plan",
"Pleasant","Pleasure","Pledge","Plentiful","Poise","Polished","Possibility","Possible","Potential","Practical",
"Practice","Precise","Precision","Predictable","Prepare","Preparedness","Presence","Present","Preserve","Principle",
"Prioritize","Priority","Privilege","Proactive","Problem-solve","Prodigy","Profound","Promise","Promote","Promotion",
"Prosper","Prosperity","Protect","Protection","Proud","Prove","Prudence","Punctual","Punctuality","Pure",
"Purity","Pursue","Pursuit","Quality","Quest","Question","Quickness","Quiet","Radiant","Radiance",
"Raise","Rally","Rational","Reach","Reassure","Rebirth","Rebuild","Reclaim","Recognize","Recommend",
"Reconcile","Record","Recover","Recovery","Refine","Refinement","Reflect","Reflection","Refresh","Refreshing",
"Regard","Regenerate","Regeneration","Rejoice","Reliable","Reliability","Remarkable","Remedy","Renew","Renewal",
"Renovate","Repair","Replace","Represent","Reputation","Resilience","Resilient","Resolve","Resolution","Resourceful",
"Respond","Response","Restore","Restoration","Retain","Reveal","Reverence","Rewarding","Rhythm","Rich",
"Richness","Rise-up","Robust","Robustness","Rooted","Routine","Safehouse","Satisfy","Satisfaction","Satisfactory",
"Savvy","Succeed","Sacrifice","Sacred","Sage","Salient","Salute","Satisfying","Savor","Savory",
"Scholar","Scholarship","Scientific","Scope","Score","Seize","Select","Selection","Self-aware","Self-belief",
"Self-control","Self-esteem","Self-improvement","Self-respect","Sensible","Sensitivity","Serene","Serenity","Serve","Service",
"Settle","Sharpness","Shelter","Showcase","Significant","Significance","Simple","Simplicity","Sincere","Sincerity",
"Singular","Sizable","Social","Solidarity","Solution","Solve","Solver","Soothing","Soul","Spark",
"Sparkle","Special","Specialize","Specific","Speedy","Spellbinding","Splendid","Spontaneous","Stability","Stabilize",
"Stable","Standard","Standout","Startling","Steadfast","Steadfastness","Steady","Stellar","Stimulate","Stimulating",
"Stimulus","Straightforward","Strategic","Strength","Strengthen","Strive","Striving","Structure","Structured","Stunning",
"Sublime","Substance","Substantial","Subtlety","Sufficient","Suitability","Suitable","Sumptuous","Super","Superbly",
"Superior","Superiority","Surpass","Surprise","Surprising","Sustain","Sustainable","Sustainability","Swiftly","Sympathy",
"Synergy","Tact","Tactful","Tangible","Target","Team","Teamwork","Temperate","Tenacious","Tenacity",
"Tender","Thankful","Thankfulness","Thorough","Thoroughness","Thrive","Thriving","Timeless","Tolerant","Tolerance",
"Top-notch","Tough","Toughness","Tranquil","Tranquility","Transcend","Transparent","Transparency","Tremendous","Triumph",
"Trustworthy","Truth","Truthful","Ultimate","Unbiased","Unconditional","Understandable","Undertake","Unified","Unify",
"Unique","Uniqueness","Unite","Unity","Universal","Unlimited","Unmatched","Unparalleled","Unstoppable","Useful",
"Usefulness","Uplift","Uplifting","Upright","Urgent","Usable","Utility","Valid","Validate","Validation",
"Valuable","Variety","Vast","Versatile","Versatility","Vibrant","Vibrancy","Vigor","Vigorous","Virtue",
"Virtuous","Visible","Vital","Vitality","Vivid","Volunteer","Warm","Warmth","Welcome","Welcoming",
"Wellbeing","Whole","Wholesome","Willing","Willpower","Win-win","Wisdom","Worth","Worthwhile","Worthy",
"Youth","Youthful","Zeal","Zealous","Zenith"
]



    














    
    
"Win","Run","Go","Try","Do","Up","Now","Move","Play","Fast","Real","True","Safe","Next","Rise","Aim","Act","Lead","Hope","Step",
"Jump","Grow","Shine","Glow","Lift","Push","Pull","Gain","Earn","Give","Take","Hold","Keep","Make","Turn","Open","Close","Start","Stop","Think",
"Power","Smile","Peace","Trust","Light","Heart","Focus","Brave","Calm","Level","Build","Learn","Boost","Energy","Create","Vision","Winner","Spirit","Leader","Impact",
"Charge","Dream","Drive","Skill","Strong","Bright","Talent","Honor","Value","Faith","Grace","Glory","Pride","Sharp","Quick","Smart","Wise","Alert","Clear","Clean",
"Fresh","Ready","Solid","Basic","Prime","Elite","Royal","Urban","Rural","Local","Global","Total","Final","Major","Minor","Rapid","Speed","Flash","Storm","Force",
"Guard","Watch","Check","Proof","Secure","Shield","Action","Motion","Growth","Clarity","Success","Respect","Future","Progress","Victory","Achieve","Believe","Balance","Journey","Freedom",
"Mindset","Purpose","Results","Winning","Upgrade","Advance","Stronger","Creator","Builder","Explorer","Thinker","Planner","Manager","Supporter","Teacher","Student","Warrior","Fighter","Runner","Climber",
"Driver","Pilot","Artist","Writer","Reader","Speaker","Develop","Improve","Enhance","Perform","Execute","Control","Manage","Operate","Deliver","Produce","Design","Testing","Debugging","Scaling",
"Loading","Rendering","Parsing","Encoding","Decoding","Discipline","Patience","Determined","Consistent","Performance","Transform","Dedication","Achievement","Commitment","Confidence","Persistence","Productivity","Excellence","Hardworking","Visionary",
"Strategist","Organizer","Innovator","Decision","Responsibility","Professional","Experience","Knowledge","Understanding","Development","Engineering","Architecture","Technology","Programming","Automation","Optimization","Communication","Collaboration","Leadership","Management",
"Execution","Implementation","Perseverance","Magnificent","Extraordinary","Unbreakable","Relentless","Determination","Unbelievable","Revolutionary","Unpredictable","Spectacular","Masterpiece","Transformation","Intelligence","Acceleration","Configuration","Critical","Analytical","Creative",
"Resource","Challenge","Adventure","Mystery","Treasure","Champion","Legend","Supreme","Invincible","Greatness","Trailblazer","Gamechanger","Trendsetter","Pathfinder","Explorer","Future","Alpha","Beta","Gamma","Omega",
"Ultra","Mega","Hyper","Prime","Core","Zone","Edge","Point","Line","Grid","Node","Link","Chain","Block","Stack","Layer","Frame","System","Module","Engine",
"Server","Client","Host","Cloud","Data","Code","Script","Logic","Input","Output","Signal","Process","Thread","Memory","Cache","Buffer","Stream","Packet","Network","Router",
"Switch","Bridge","Gateway","Protocol","Latency","Bandwidth","Shadow","Thunder","Lightning","Rain","Wind","Snow","Ice","Frost","Heat","Fire","Water","Earth","Air","Sky",
"Space","Galaxy","Cosmos","Universe","Infinite","Infinity","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","First","Second","Third","Fourth"
]

# ================= REWARDS =================
REWARD_MIN = 10
REWARD_MAX = 50

# ================= SERVER =================
PING_INTERVAL = 600
