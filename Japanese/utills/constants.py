"""MIT License"""

"""Copyright (c) 2026 [TeamJapanese](https://github.com/TeamJapanese)"""

"""Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:"""

"""The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software."""

"""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


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

"Namaste","Shukriya","Dhanyavaad","Accha","Achha","Acha","Theek","TheekHai","Haan","Nahi",
"Bilkul","Jarur","Zaroor","Kyun","Kaise","Kab","Kahan","Kiska","Kisko","Kisliye",
"Mujhe","Tujhe","Tum","Aap","Hum","Sab","Apna","Apni","Apne","Mera",
"Meri","Mere","Tera","Teri","Tere","Hamara","Tumhara","Uska","Iska","Yeh",
"Woh","Idhar","Udhar","Aaj","Kal","Abhi","Baad","Pehle","Baadme","Hamesha",
"Kabhi","KabhiNahi","Jaldi","Dheere","Thoda","Zyada","Bahut","Kam","Sahi","Galat",
"Mast","Bindaas","Jhakaas","Zabardast","Shaandar","Solid","Bawal","Bakwas","Bekaar","Awesome",
"MindBlowing","Fadu","Kadak","Gazab","Ekdum","MastHai","Chill","Scene","Setting","System",
"Jugaad","Pakka","Kaccha","Desi","Swadeshi","Bandhan","Utsav","Adda","Dost","Dosti",
"Yaar","Bhai","Bhaiya","Behen","Didi","Uncle","Aunty","Chacha","Mama","Papa",
"Mummy","Nana","Nani","Dada","Dadi","Guru","Chela","Ustad","Sikandar","Badshah",
"Raja","Rani","Sher","Shikari","Yoddha","Veer","Bahadur","Tez","Hoshiyaar","Samajhdar",
"Mehnat","Jeet","Haar","Udaan","Safar","Manzil","Raasta","Khwab","Sapna","Hausla",
"Himmat","Junoon","Josh","Soch","Vishwas","Bharosa","Koshish","Tayyari","Mauka","Lakshya",
"Prerna","Sankalp","Shakti","Bal","Tejas","Agni","Jal","Vayu","Dharti","Aakash",
"Suraj","Chand","Taare","Bijli","Toofan","Barish","Hawa","Aandhi","Pahad","Nadi",
"Samundar","Jungle","Ped","Phool","Patta","Mitti","Beej","Kheti","Gaon","Shehar",
"Chai","Coffee","Paani","Doodh","Lassi","Sharbat","Roti","Dal","Sabzi","Chawal",
"Paratha","Kulcha","Naan","Biryani","Pulao","Khichdi","Idli","Dosa","Sambar","Vada",
"Poha","Upma","Thepla","Dhokla","Fafda","Jalebi","Kachori","Samosa","Pakoda","Chaat",
"PaniPuri","Golgappa","Bhel","Sev","Papad","Pickle","Achar","Halwa","Kheer","Rabdi",
"Barfi","Laddu","Peda","Rasgulla","GulabJamun","Rasmalai","Kulfi","Falooda","Mithai","Chocolate",
"Office","School","College","Class","Teacher","Student","Kitab","Copy","Homework","Exam",
"Result","Number","Question","Answer","Computer","Laptop","Mobile","Keyboard","Mouse","Screen",
"Internet","Network","Server","Coding","Program","Bug","Fix","Update","Download","Upload",
"Login","Logout","Password","Username","Message","Reply","Forward","Delete","Create","Search",
"Button","Click","Scroll","Window","Folder","File","Photo","Image","Video","Audio",
"Music","Game","Player","Winner","Loser","Champion","Legend","Pro","Noob","Clutch",
"Rank","Level","Mission","Target","Reward","Bonus","Daily","Weekly","Monthly","Event",
"Festival","Diwali","Holi","Eid","Navratri","Rakhi","Ganesh","Durga","Ram","Krishna",
"Shiva","Hanuman","Lakshmi","Saraswati","Vishnu","Mahadev","Mandir","Puja","Prasad","Bhajan",
"Dhyaan","Yoga","Mantra","Karma","Dharma","Seva","Prem","Pyaar","Mohabbat","Dil",
"Khushi","Muskaan","Hasi","Dua","Aashirwad","Umeed","Khayal","Ehsaas","Rishta","Parivaar"



"Bonjour","Bonsoir","Salut","Merci","Pardon","Excuse","Oui","Non","Peutetre","Bienvenue",
"Amour","Amitie","Bonheur","Joie","Paix","Espoir","Liberte","Egalite","Fraternite","Courage",
"Force","Puissance","Victoire","Succes","Respect","Confiance","Honneur","Gloire","Fierte","Sagesse",
"Intelligence","Patience","Discipline","Equilibre","Progres","Avenir","Objectif","Mission","Vision","Passion",
"Creation","Innovation","Leader","Champion","Legende","Elite","Maitre","Hero","Explorateur","Aventure",
"Voyage","Monde","Nature","Montagne","Riviere","Lac","Mer","Ocean","Foret","Arbre",
"Fleur","Feuille","Soleil","Lune","Etoile","Nuage","Pluie","Neige","Vent","Tempete",
"Feu","Eau","Terre","Air","Ciel","Univers","Galaxy","Cosmos","Planete","Espace",
"Maison","Appartement","Chambre","Cuisine","Fenetre","Porte","Jardin","Ville","Village","Route",
"Pont","Place","Marche","Ecole","College","Universite","Professeur","Etudiant","Livre","Stylo",
"Cahier","Classe","Examen","Question","Reponse","Lecon","Etude","Lecture","Ecriture","Langue",
"Francais","Anglais","Japonais","Chinois","Coreen","Latin","Europe","Paris","Lyon","Marseille",
"Train","Metro","Voiture","Bus","Avion","Velo","Moto","Bateau","Taxi","Voyager",
"Hotel","Restaurant","Cafe","Boulangerie","Fromage","Pain","Croissant","Baguette","Beurre","Confiture",
"Lait","CafeNoir","The","Chocolat","Gateau","Tarte","Soupe","Salade","Poulet","Poisson",
"Viande","Legume","Fruit","Pomme","Banane","Orange","Raisin","Fraise","Cerise","Citron",
"Travail","Entreprise","Bureau","Ordinateur","Clavier","Souris","Ecran","Internet","Reseau","Serveur",
"Logiciel","Programme","Code","Donnees","Memoire","Systeme","Application","Robot","Machine","Technologie",
"Science","Ingenieur","Architecture","Developpement","Communication","Collaboration","Strategie","Organisation","Gestion","Decision",
"Rapide","Lent","Grand","Petit","Fort","Faible","Jeune","Vieux","Beau","Belle",
"Heureux","Triste","Simple","Complexe","Facile","Difficile","Propre","Sale","Ouvert","Ferme",
"Rouge","Bleu","Vert","Jaune","Noir","Blanc","Gris","Violet","OrangeCouleur","Rose",
"Argent","Or","Bronze","Cristal","Diamant","Perle","Rubis","Saphir","Emeraude","Topaze",
"Matin","Midi","Soir","Nuit","Aujourdhui","Demain","Hier","Toujours","Jamais","Parfois",
"Encore","Maintenant","Bientot","Deja","Ici","LaBas","Avant","Apres","Debut","Fin"

    

"Arigato","Ohayo","Konnichiwa","Konbanwa","Sayonara","Oyasumi","Sumimasen","Gomen","Hai","Iie",
"Onegai","Douzo","Genki","Daijoubu","Ganbatte","Ganbare","Sugoi","Kawaii","Kakkoii","Oishii",
"Itadakimasu","Gochisousama","Sensei","Senpai","Kouhai","Tomodachi","Kazoku","Kodomo","Otousan","Okaasan",
"Oniisan","Oneesan","Ojisan","Obasan","Ojiisan","Obaasan","Inu","Neko","Tori","Sakana",
"Sakura","Fuji","Tokyo","Kyoto","Osaka","Hokkaido","Okinawa","Shinkansen","Torii","Kimono",
"Yukata","Tatami","Origami","Ikebana","Bonsai","Samurai","Ninja","Shogun","Ronin","Katana",
"Wakizashi","Shuriken","Dojo","Kendo","Karate","Judo","Aikido","Kyudo","Bushido","Zen",
"Reiki","Satori","Kaizen","Ikigai","Kizuna","Takumi","Hikari","Yume","Kokoro","Tamashii",
"Chikara","Yuuki","Kibou","Heiwa","Ai","Yasashii","Tanoshii","Ureshii","Kanashii","Sabishii",
"Hayai","Osoi","Atsui","Samui","Takai","Hikui","Ookii","Chiisai","Nagai","Mijikai",
"Akarui","Kurai","Shiro","Kuro","Aka","Ao","Midori","Kiiro","Murasaki","Pinku",
"Chairo","Gin","Kin","Mizu","Hi","Kaze","Tsuchi","Sora","Hoshi","Taiyou",
"Tsuki","Kumo","Ame","Yuki","Arashi","Kaminari","Umi","Yama","Kawa","Mori",
"Hana","Ki","Ha","Michi","Hashi","Mura","Machi","Kuni","Sekai","Uchuu",
"Gakusei","Gakkou","Kyoushitsu","Benkyou","Shiken","Shukudai","Hon","Eigo","Nihongo","Kotoba",
"Moji","Suuji","Jikan","Mainichi","Ashita","Kinou","Kyou","Asa","Hiru","Yoru",
"Hataraku","Asobu","Hashiru","Aruku","Taberu","Nomu","Miru","Kiku","Hanasu","Kaku",
"Yomu","Tsukuru","Arau","Noru","Kaeru","Matsu","Utau","Odoru","Warau","Naku",
"Kau","Uru","Ageru","Morau","Hajimeru","Owaru","Hajimari","Saigo","Shouri","Haiboku",
"Seikou","Shippai","Yuumei","Eiyuu","Ou","Joou","Hime","Ouji","Mahou","Dragon",
"Yokai","Kitsune","Tanuki","Tengu","Oni","Kami","Miko","Matsuri","Omamori","Daruma",
"ManekiNeko","Futon","Onsen","Ramen","Sushi","Tempura","Udon","Soba","Mochi","Dango",
"Matcha","Bento","Takoyaki","Okonomiyaki","Yakitori","Karaage","Onigiri","Miso","Tofu","Edamame",
"Anpan","Dorayaki","Taiyaki","Melonpan","Pocky","Ramune","Sake","Cha","Kocha","Gyuniku",
"Butaniku","Toriniku","Tamago","Yasai","Kudamono","Ringo","Mikan","Ichigo","Budou","Suika",
"Natsu","Aki","Fuyu","Haru","Getsuyoubi","Kayoubi","Suiyoubi","Mokuyoubi","Kinyoubi","Doyoubi","Nichiyoubi"


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
