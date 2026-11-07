# Ivan開源：多人認定的鳥類真實照片庫

<img src="previews/header.jpg" alt="人選鳥圖網站：每種鳥一張真實照片，每張都經至少3人認定" width="100%">

[English](README.md) · [简体中文](README.zh-Hans.md) · **繁體中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

<a href="https://flychicken067.github.io/bird-human-picks/zh-hant/"><img src="docs/assets/og.png" alt="人選鳥圖網站：每種鳥一張真實照片，每張都經至少3人認定" width="100%"></a>

**這些照片的完整用法，請到[網站](https://flychicken067.github.io/bird-human-picks/zh-hant/)看。** 人選鳥圖網站有15種語言，1209種鳥每種一個頁面：照片、幾個人認定、體型、保育等級、分布、各語言鳥名、引用方式和回報入口，也能和花叔的AI貼紙並排對比。

[Ivan](https://github.com/flychicken067)開源的鳥類真實照片庫，起因是想看看：不讓AI畫、只用人的判斷，能把花叔的「huashu-bird-sticker」做到什麼程度。每種鳥一張iNaturalist上的野外照片，至少3個人在至少3個不同月份認定為同一物種，沒有人給出別的物種。依全球統一鳥類名錄[AviList v2026](https://www.avilist.org/)整理，目前1209種、39目145科，和[huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)使用同一套編號，可以直接對接。照片全部可以免費商用，每張都記錄了作者、授權和認定依據。

> **iNaturalist全量查詢已經跑完。** 11011種裡有10993種拿到了鑑定資料，另外18種學名對不上。新查到的鳥種還要做構圖檢查和逐張看圖，做完後入選數會增加。花叔版有10973種貼紙，我們目前是其中的1209種。

**授權一句話：** 照片可以免費用於任何用途，包括商用，只要依每張照片自己的授權署名（CC0不用署名，CC BY和CC BY-SA要署名，CC BY-SA改過的要以相同授權分享）。我們整理的資料採CC BY 4.0，程式碼採MIT，第三方部分見[NOTICE](NOTICE.md)。

## 畫廊

10個照片最多、最有代表性的類群，每組12張，同一屬盡量只放一張，優先選認定人數多的；最後是每個目各一隻。每張圖下方列出攝影師。

### 蜂鳥 · *Trochilidae* — 122種

![蜂鳥](previews/families/trochilidae.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Archilochus colubris* — [Blake Ross](https://www.inaturalist.org/photos/239401590), CC BY
2. *Sephanoides fernandensis* — [iNaturalist](https://www.inaturalist.org/photos/64734837), CC0
3. *Eulampis jugularis* — [Annika Lindqvist](https://www.inaturalist.org/photos/2906217), CC BY
4. *Selasphorus platycercus* — [Texas Bird Family](https://www.inaturalist.org/photos/444286145), CC BY
5. *Loddigesia mirabilis* — [Thibaud Aronson](https://www.inaturalist.org/photos/114707728), CC BY-SA
6. *Anthracothorax nigricollis* — [graciela arballo](https://www.inaturalist.org/photos/468129910), CC BY
7. *Coeligena torquata* — [Kristiina Hurme](https://www.inaturalist.org/photos/1618568), CC BY
8. *Eupetomena macroura* — [iNaturalist](https://www.inaturalist.org/photos/543676913), CC0
9. *Heliactin bilophus* — [agujaceratops](https://www.inaturalist.org/photos/348331475), CC BY
10. *Mellisuga helenae* — [iNaturalist](https://www.inaturalist.org/photos/258810323), CC0
11. *Colibri cyanotus* — [Annika Lindqvist](https://www.inaturalist.org/photos/2383409), CC BY
12. *Chrysolampis mosquitus* — [Inacio Oliveira](https://www.inaturalist.org/photos/474805261), CC BY

</details>

### 翠鳥、蜂虎、鸚鵡和其他彩色鳥 · *Alcedinidae* · *Meropidae* · *Coraciidae* · *Ramphastidae* · *Megalaimidae* · *Psittacidae* · *Psittaculidae* · *Thraupidae* · *Nectariniidae* · *Paradisaeidae* · *Pipridae* — 40種

![翠鳥、蜂虎、鸚鵡和其他彩色鳥](previews/families/colourful.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Anodorhynchus hyacinthinus* — [Millie Basden](https://www.inaturalist.org/photos/48862196), CC BY
2. *Coracias caudatus* — [Tony Eales](https://www.inaturalist.org/photos/298432395), CC BY-SA
3. *Todiramphus sanctus* — [Jacqui Geux](https://www.inaturalist.org/photos/29504195), CC BY
4. *Corythornis cristatus* — [iNaturalist](https://www.inaturalist.org/photos/9765521), CC0
5. *Pteroglossus bailloni* — [Júlio Castellain](https://www.inaturalist.org/photos/112488961), CC BY
6. *Psittacula alexandri* — [iNaturalist](https://www.inaturalist.org/photos/53579798), CC0
7. *Merops persicus* — [Вячеслав Юсупов](https://www.inaturalist.org/photos/48887225), CC BY
8. *Amazona vinacea* — [iNaturalist](https://www.inaturalist.org/photos/119298615), CC0
9. *Cinnyris mariquensis* — [Brian du Preez](https://www.inaturalist.org/photos/15210726), CC BY-SA
10. *Megaceryle lugubris* — [Jagdish Singh Negi](https://www.inaturalist.org/photos/242964394), CC BY
11. *Tangara icterocephala* — [Annika Lindqvist](https://www.inaturalist.org/photos/2208350), CC BY
12. *Paradisornis rudolphi* — [iNaturalist](https://www.inaturalist.org/photos/474206316), CC0

</details>

### 鳩鴿 · *Columbidae* — 89種

![鳩鴿](previews/families/columbidae.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Hemiphaga novaeseelandiae* — [Jon Sullivan](https://www.inaturalist.org/photos/1196415), CC BY
2. *Caloenas nicobarica* — [iNaturalist](https://www.inaturalist.org/photos/67573689), CC0
3. *Columba trocaz* — [Thibaud Aronson](https://www.inaturalist.org/photos/175416523), CC BY-SA
4. *Zenaida asiatica* — [Fyn Kynd](https://www.inaturalist.org/photos/2781440), CC BY-SA
5. *Alectroenas pulcherrimus* — [iNaturalist](https://www.inaturalist.org/photos/11497396), CC0
6. *Streptopelia decaocto* — [Kostas Zontanos](https://www.inaturalist.org/photos/13943172), CC BY
7. *Geophaps plumifera* — [patrickc](https://www.inaturalist.org/photos/253427575), CC BY
8. *Treron affinis* — [sunnyjosef](https://www.inaturalist.org/photos/316300731), CC BY
9. *Ptilinopus perousii* — [Ben Hayden](https://www.inaturalist.org/photos/32892871), CC BY
10. *Geotrygon leucometopia* — [Zac Peterson](https://www.inaturalist.org/photos/261733714), CC BY
11. *Oena capensis* — [Dmitry Ivanov](https://www.inaturalist.org/photos/196747956), CC BY
12. *Spilopelia senegalensis* — [Sam Kieschnick](https://www.inaturalist.org/photos/357541010), CC BY

</details>

### 鴨、雁與天鵝 · *Anatidae* — 78種

![鴨、雁與天鵝](previews/families/anatidae.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Somateria fischeri* — [Nigel Voaden](https://www.inaturalist.org/photos/2946643), CC BY
2. *Alopochen aegyptiaca* — [iNaturalist](https://www.inaturalist.org/photos/499763170), CC0
3. *Tadorna ferruginea* — [egorbirder](https://www.inaturalist.org/photos/118676181), CC BY
4. *Aix galericulata* — [Blake Ross](https://www.inaturalist.org/photos/170995013), CC BY
5. *Anas platyrhynchos* — [Codrin Bucur](https://www.inaturalist.org/photos/180394066), CC BY
6. *Branta ruficollis* — [Константин Селивёрстов](https://www.inaturalist.org/photos/324712726), CC BY
7. *Spatula clypeata* — [Michael D Fox](https://www.inaturalist.org/photos/5654279), CC BY
8. *Polysticta stelleri* — [Nigel Voaden](https://www.inaturalist.org/photos/2963206), CC BY
9. *Hymenolaimus malacorhynchos* — [William Harland](https://www.inaturalist.org/photos/348799185), CC BY
10. *Biziura lobata* — [Ellen Rykers](https://www.inaturalist.org/photos/52756144), CC BY
11. *Radjah radjah* — [Andrew Allen](https://www.inaturalist.org/photos/48510025), CC BY
12. *Aythya ferina* — [Andrew Bazdyrev](https://www.inaturalist.org/photos/330781096), CC BY

</details>

### 雉雞、鶉與塚雉 · *Phasianidae* · *Odontophoridae* · *Numididae* · *Megapodiidae* · *Cracidae* — 110種

![雉雞、鶉與塚雉](previews/families/phasianidae.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Phasianus colchicus* — [John Krampl](https://www.inaturalist.org/photos/127255695), CC BY
2. *Tetrao urogallus* — [Christoph Moning](https://www.inaturalist.org/photos/92440673), CC BY
3. *Lophophorus impejanus* — [egorbirder](https://www.inaturalist.org/photos/483766041), CC BY
4. *Pavo muticus* — [scaup](https://www.inaturalist.org/photos/71308373), CC BY
5. *Lagopus muta* — [Karsten Rohweder](https://www.inaturalist.org/photos/60398822), CC BY
6. *Colinus virginianus* — [iNaturalist](https://www.inaturalist.org/photos/12497659), CC0
7. *Gallus lafayettii* — [Christoph Moning](https://www.inaturalist.org/photos/92434873), CC BY
8. *Meleagris ocellata* — [Ricard Busquets Reverte](https://www.inaturalist.org/photos/331661906), CC BY
9. *Acryllium vulturinum* — [Annika Lindqvist](https://www.inaturalist.org/photos/49916377), CC BY
10. *Tetrastes bonasia* — [Dmitry Kulakov](https://www.inaturalist.org/photos/53607821), CC BY
11. *Syrmaticus humiae* — [Christoph Moning](https://www.inaturalist.org/photos/104702114), CC BY
12. *Lophura diardi* — [Christoph Moning](https://www.inaturalist.org/photos/105704194), CC BY

</details>

### 鴞 · *Strigidae* · *Tytonidae* — 44種

![鴞](previews/families/owls.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Surnia ulula* — [Laurel Meredyk](https://www.inaturalist.org/photos/251510806), CC BY
2. *Bubo scandiacus* — [Matt Felperin](https://www.inaturalist.org/photos/175457284), CC BY
3. *Asio otus* — [Dean Hester](https://www.inaturalist.org/photos/56530053), CC BY
4. *Aegolius acadicus* — [Louis Imbeau](https://www.inaturalist.org/photos/248803541), CC BY
5. *Athene cunicularia* — [Devon Bradley](https://www.inaturalist.org/photos/6483198), CC BY
6. *Glaucidium passerinum* — [Mikhail Nevsky](https://www.inaturalist.org/photos/111639130), CC BY
7. *Tyto alba* — [Jan Ebr &amp; Ivana Ebrová](https://www.inaturalist.org/photos/168696231), CC BY
8. *Micrathene whitneyi* — [Nigel Voaden](https://www.inaturalist.org/photos/2523379), CC BY
9. *Ninox novaeseelandiae* — [Saryu Mae 前 朝琉](https://www.inaturalist.org/photos/465647720), CC BY
10. *Otus scops* — [Alexander A. Fomichev](https://www.inaturalist.org/photos/5794998), CC BY
11. *Strix uralensis* — [iNaturalist](https://www.inaturalist.org/photos/183131406), CC0
12. *Ketupa philippensis* — [Forest Botial-Jarvis](https://www.inaturalist.org/photos/261946784), CC BY

</details>

### 猛禽 · *Accipitridae* · *Falconidae* · *Cathartidae* — 34種

![猛禽](previews/families/raptors.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Buteo lineatus* — [Don Loarie](https://www.inaturalist.org/photos/14603656), CC BY
2. *Icthyophaga vocifer* — [Wynand Uys](https://www.inaturalist.org/photos/20939777), CC BY
3. *Astur cooperii* — [Becky Matsubara](https://www.inaturalist.org/photos/43282408), CC BY
4. *Daptrius albogularis* — [Jeff Young](https://www.inaturalist.org/photos/12549808), CC BY
5. *Spizaetus ornatus* — [iNaturalist](https://www.inaturalist.org/photos/440105675), CC0
6. *Vultur gryphus* — [Ezequiel Racker](https://www.inaturalist.org/photos/202029519), CC BY
7. *Circus maurus* — [Jacobus Retief](https://www.inaturalist.org/photos/320798192), CC BY
8. *Tachyspiza badia* — [Rejoice Gassah](https://www.inaturalist.org/photos/544347124), CC BY
9. *Busarellus nigricollis* — [Laura Gaudette](https://www.inaturalist.org/photos/61160829), CC BY
10. *Microhierax fringillarius* — [anukma](https://www.inaturalist.org/photos/12291410), CC BY
11. *Coragyps atratus* — [Ricard Busquets Reverte](https://www.inaturalist.org/photos/158143837), CC BY
12. *Falco cenchroides* — [Graham Winterflood](https://www.inaturalist.org/photos/55944121), CC BY-SA

</details>

### 鷺、䴉與鸛 · *Ardeidae* · *Threskiornithidae* · *Ciconiidae* — 64種

![鷺、䴉與鸛](previews/families/herons.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Ardea herodias* — [mostbittern](https://www.inaturalist.org/photos/134213334), CC BY
2. *Ephippiorhynchus senegalensis* — [Wynand Uys](https://www.inaturalist.org/photos/13753257), CC BY
3. *Egretta tricolor* — [Julien Renoult](https://www.inaturalist.org/photos/13014839), CC BY
4. *Platalea ajaja* — [Nigel Voaden](https://www.inaturalist.org/photos/2069153), CC BY
5. *Mycteria ibis* — [Wynand Uys](https://www.inaturalist.org/photos/20939802), CC BY
6. *Zonerodius heliosylus* — [Norma Malinowski](https://www.inaturalist.org/photos/49724965), CC BY
7. *Geronticus eremita* — [Paolo Zucca](https://www.inaturalist.org/photos/42804068), CC BY
8. *Lophotibis cristata* — [Nigel Voaden](https://www.inaturalist.org/photos/3550286), CC BY
9. *Ciconia nigra* — [iNaturalist](https://www.inaturalist.org/photos/76887117), CC0
10. *Threskiornis aethiopicus* — [iNaturalist](https://www.inaturalist.org/photos/64691895), CC0
11. *Botaurus lentiginosus* — [Fyn Kynd](https://www.inaturalist.org/photos/2831441), CC BY-SA
12. *Plegadis falcinellus* — [Paolo Zucca](https://www.inaturalist.org/photos/23542356), CC BY

</details>

### 鷸、鴴與鷗 · *Scolopacidae* · *Charadriidae* · *Laridae* · *Recurvirostridae* · *Haematopodidae* — 115種

![鷸、鴴與鷗](previews/families/shorebirds.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Larus michahellis* — [Chris Sulots](https://www.inaturalist.org/photos/248836478), CC BY
2. *Recurvirostra avosetta* — [iNaturalist](https://www.inaturalist.org/photos/60898454), CC0
3. *Pagophila eburnea* — [Nigel Voaden](https://www.inaturalist.org/photos/1596263), CC BY
4. *Scolopax saturata* — [Forest Botial-Jarvis](https://www.inaturalist.org/photos/413011677), CC BY
5. *Himantopus himantopus* — [Paolo Zucca](https://www.inaturalist.org/photos/20455456), CC BY
6. *Rissa brevirostris* — [iNaturalist](https://www.inaturalist.org/photos/231087091), CC0
7. *Anous stolidus* — [Annika Lindqvist](https://www.inaturalist.org/photos/1448593), CC BY
8. *Vanellus armatus* — [linkie](https://www.inaturalist.org/photos/126909977), CC BY
9. *Charadrius vociferus* — [Sam Kieschnick](https://www.inaturalist.org/photos/67100327), CC BY
10. *Ichthyaetus ichthyaetus* — [Константин Селивёрстов](https://www.inaturalist.org/photos/56961778), CC BY
11. *Calidris pygmaea* — [Sevin Dee](https://www.inaturalist.org/photos/181630913), CC BY
12. *Leucophaeus fuliginosus* — [Doug Macaulay](https://www.inaturalist.org/photos/5701950), CC BY

</details>

### 鳴禽：鶲、鶇、鶯、霸鶲與鴉 · *Muscicapidae* · *Turdidae* · *Parulidae* · *Tyrannidae* · *Icteridae* · *Corvidae* · *Paridae* · *Fringillidae* · *Estrildidae* — 63種

![鳴禽：鶲、鶇、鶯、霸鶲與鴉](previews/families/songbirds.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Pica pica* — [bitsnbirds](https://www.inaturalist.org/photos/199815492), CC BY
2. *Protonotaria citrea* — [Owen Strickland](https://www.inaturalist.org/photos/164622322), CC BY
3. *Geothlypis philadelphia* — [Jason Hill](https://www.inaturalist.org/photos/20357505), CC BY
4. *Parus major* — [Codrin Bucur](https://www.inaturalist.org/photos/120815678), CC BY
5. *Oenanthe leucopyga* — [iNaturalist](https://www.inaturalist.org/photos/9709483), CC0
6. *Eumyias thalassinus* — [Cheongweei Gan](https://www.inaturalist.org/photos/175806086), CC BY
7. *Leucosticte tephrocotis* — [Nigel Voaden](https://www.inaturalist.org/photos/2816193), CC BY
8. *Myadestes townsendi* — [Laurel Meredyk](https://www.inaturalist.org/photos/231753603), CC BY
9. *Turdus torquatus* — [Ani Sarkisyan](https://www.inaturalist.org/photos/108414038), CC BY
10. *Calliope tschebaiewi* — [Rejoice Gassah](https://www.inaturalist.org/photos/175690522), CC BY
11. *Loxia curvirostra* — [Jason Alexander](https://www.inaturalist.org/photos/257080568), CC BY
12. *Cardellina pusilla* — [Paul Roots](https://www.inaturalist.org/photos/24621521), CC BY

</details>

### 每個目各一隻

![每個目各一隻](previews/orders.jpg)

<details><summary>照片作者（由左至右、由上至下）</summary>

1. *Struthio camelus* — [Andrew Allen](https://www.inaturalist.org/photos/55506762), CC BY
2. *Dromaius novaehollandiae* — [CK2AZ](https://www.inaturalist.org/photos/121143193), CC BY
3. *Apteryx australis* — [Mark Anderson](https://www.inaturalist.org/photos/1795821), CC BY-SA
4. *Rhea pennata* — [Thibaud Aronson](https://www.inaturalist.org/photos/359489448), CC BY-SA
5. *Tinamotis pentlandii* — [iNaturalist](https://www.inaturalist.org/photos/243646625), CC0
6. *Somateria fischeri* — [Nigel Voaden](https://www.inaturalist.org/photos/2946643), CC BY
7. *Phasianus colchicus* — [John Krampl](https://www.inaturalist.org/photos/127255695), CC BY
8. *Phoenicopterus chilensis* — [Thibaud Aronson](https://www.inaturalist.org/photos/64524005), CC BY-SA
9. *Tachybaptus dominicus* — [Laura Clark](https://www.inaturalist.org/photos/223776589), CC BY
10. *Crinifer piscator* — [Christoph Moning](https://www.inaturalist.org/photos/94968069), CC BY
11. *Eupodotis caerulescens* — [Brian du Preez](https://www.inaturalist.org/photos/15201068), CC BY-SA
12. *Geococcyx californianus* — [Jody Shugart](https://www.inaturalist.org/photos/8844788), CC BY
13. *Monias benschi* — [Nigel Voaden](https://www.inaturalist.org/photos/3717210), CC BY
14. *Pterocles alchata* — [Mourad Harzallah](https://www.inaturalist.org/photos/176603239), CC BY
15. *Hemiphaga novaeseelandiae* — [Jon Sullivan](https://www.inaturalist.org/photos/1196415), CC BY
16. *Opisthocomus hoazin* — [Nicolas Olejnik](https://www.inaturalist.org/photos/2987824), CC BY
17. *Laterallus rogersi* — [Brian Gratwicke](https://www.inaturalist.org/photos/104246), CC BY
18. *Larus michahellis* — [Chris Sulots](https://www.inaturalist.org/photos/248836478), CC BY
19. *Rhynochetos jubatus* — [Lennart Hudel](https://www.inaturalist.org/photos/33484568), CC BY
20. *Phaethon lepturus* — [iNaturalist](https://www.inaturalist.org/photos/102189130), CC0
21. *Gavia immer* — [Jamie O'Neill](https://www.inaturalist.org/photos/251343258), CC BY
22. *Aptenodytes forsteri* — [mattward](https://www.inaturalist.org/photos/251293817), CC BY-SA
23. *Pterodroma magentae* — [John Barkla](https://www.inaturalist.org/photos/1251791), CC BY
24. *Ephippiorhynchus senegalensis* — [Wynand Uys](https://www.inaturalist.org/photos/13753257), CC BY
25. *Nannopterum auritum* — [Peter Abrahamsen](https://www.inaturalist.org/photos/255454786), CC BY
26. *Ardea herodias* — [mostbittern](https://www.inaturalist.org/photos/134213334), CC BY
27. *Caprimulgus europaeus* — [Dmitry Galitsyn](https://www.inaturalist.org/photos/426714858), CC BY
28. *Nyctibius griseus* — [William Stephens](https://www.inaturalist.org/photos/63558513), CC BY
29. *Podargus papuensis* — [Andrew Allen](https://www.inaturalist.org/photos/52277094), CC BY
30. *Aegotheles crinifrons* — [Jason Alexander](https://www.inaturalist.org/photos/526365190), CC BY
31. *Archilochus colubris* — [Blake Ross](https://www.inaturalist.org/photos/239401590), CC BY
32. *Surnia ulula* — [Laurel Meredyk](https://www.inaturalist.org/photos/251510806), CC BY
33. *Vultur gryphus* — [Ezequiel Racker](https://www.inaturalist.org/photos/202029519), CC BY
34. *Buteo lineatus* — [Don Loarie](https://www.inaturalist.org/photos/14603656), CC BY
35. *Coracias caudatus* — [Tony Eales](https://www.inaturalist.org/photos/298432395), CC BY-SA
36. *Pteroglossus bailloni* — [Júlio Castellain](https://www.inaturalist.org/photos/112488961), CC BY
37. *Daptrius albogularis* — [Jeff Young](https://www.inaturalist.org/photos/12549808), CC BY
38. *Strigops habroptilus* — [M Rutherford](https://www.inaturalist.org/photos/154022742), CC BY
39. *Pica pica* — [bitsnbirds](https://www.inaturalist.org/photos/199815492), CC BY

</details>

## 裡面有什麼

| | |
|---|---|
| `data/species.json` | 每種一筆記錄，最完整的資料：分類、鳥名、編號、分布、形態、保育等級，以及照片、認定依據和檢查記錄。欄位標準和花叔的`data/`一致，說明見[data/README.md](data/README.md)（1209種） |
| `data/species.csv` | 同上，攤平成表格，方便用Excel開啟 |
| `data/names.csv` | 1209種鳥、43種語言的鳥名（英文CC BY 4.0，其他語言CC BY 3.0） |
| `data/field-guide.zh-Hans.json` | 325種鳥的中文圖鑑筆記（CC BY-SA 4.0） |
| `docs/` | 網站：15種語言，每種鳥一個頁面 |
| `ios/` | 離線iOS App原始碼 |
| `scripts/、site/` | 採集、篩選、出圖和建站的腳本（MIT） |

## 涵蓋情況

- 照片：1209種全部都有，每張都有照片頁、原圖尺寸、授權和授權連結。163張CC0照片的攝影師放棄了署名，iNaturalist也不提供名字，我們不替他們補名字，只留作者主頁連結。
- 認定：每張至少3人、跨至少3個月，中位數是5人、3個月，沒有異議。
- 編號：iNaturalist物種編號、eBird、Avibase 1209種全有；Wikidata 1194種，GBIF 1176種。
- 鳥名、分布、形態、保育等級原樣取自花叔的資料，我們沒有改動，所以缺的地方和他一樣，例如體長只有616種有。

## 照片怎麼選的，品質如何

**物種對不對，由人決定。** 照片來自iNaturalist的野外研究級觀察，至少3個帳號目前認定為這個物種，認定跨至少3個不同月份，沒有人給出別的物種。原圖長邊至少1200像素，授權只收CC0、CC BY、CC BY-SA。

**畫面先由模型初篩，再逐張看。** 偵測模型只看畫面裡有幾隻鳥、鳥多大、有沒有人手，不判斷物種。之後逐張看圖，排除了367張：被遮擋、只拍到局部、死鳥、家禽、手繪畫、拍錯的鳥等，每張都寫了原因，見[docs/eye-check.csv](docs/eye-check.csv)。

- **還有9749種沒有入選。** 其中5929種沒有一筆觀察做到3人認定、跨3個月；2448種還沒做構圖檢查，正在做；879種沒有一張畫面清楚的單隻鳥照片；400種原圖太小；90種分類範圍變了，暫不收；另有3種因學名對不上或看圖排除。每一項的計數見[docs/stats.json](docs/stats.json)。

這些是真實照片，但物種是網友鑑定的，不是鳥類學家逐張核對的。當作一張可靠的參考照來用；涉及細節辨識，請以圖鑑為準。 和花叔版誰錯得少，要等兩版公開後比較各自被指出的錯誤。在那之前只能說物種依據更強，不能說效果更好。

發現錯圖，歡迎[提issue](../../issues/new/choose)；網站上每種鳥都有填好鳥名的回報連結。鳥友的糾錯，是這個專案最需要的貢獻。

## 署名與撤下

每張照片的頁面、作者和授權寫在`data/species.json`的`photo`裡。如果照片是你拍的，而你不希望被收錄，請用「攝影師撤回照片」issue表單告訴我們，我們會在7天內換掉，以後也不再使用。

## 怎麼用

單張照片可以直接引用，連結格式是：

```
https://inaturalist-open-data.s3.amazonaws.com/photos/<photoId>/original.jpg
```

編號在`data/species.csv`的`photoUrl`欄。署名寫攝影師，並註明來自iNaturalist；網站上每種鳥都有現成的引用文字。

只想要資料，可以這樣拉：

```bash
git clone --filter=blob:none --sparse https://github.com/flychicken067/bird-human-picks
cd bird-human-picks && git sparse-checkout set data
```

## 致謝

- 照片和鑑定：iNaturalist的攝影師和鑑定者，逐張寫在`data/species.json`裡。照片本身不在倉庫中。
- 分類、鳥名、編號、分布、形態：[huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)，花叔，MIT。中文圖鑑筆記同出該倉庫，CC BY-SA 4.0。
- AviList Core Team. 2026. AviList: The Global Avian Checklist, v2026，CC BY 4.0；IOC世界鳥類名錄v15.2，CC BY 3.0；AVONET，Tobias等，2022，CC BY 4.0；Wikidata，CC0。


[BUILD.md](BUILD.md) · [RULES.md](RULES.md) · [PARITY.md](PARITY.md) · [NOTICE.md](NOTICE.md)
