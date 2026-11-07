# Ivan开源：多人认定的鸟类真实照片库

<img src="previews/header.jpg" alt="人选鸟图网站：每种鸟一张真实照片，每张都经至少3人认定" width="100%">

[English](README.md) · **简体中文** · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

<a href="https://flychicken067.github.io/bird-human-picks/"><img src="docs/assets/og.png" alt="人选鸟图网站：每种鸟一张真实照片，每张都经至少3人认定" width="100%"></a>

**这些照片的完整用法，去[网站](https://flychicken067.github.io/bird-human-picks/)看。** 人选鸟图网站有15种语言，1049种鸟每种一个页面：照片、几个人认定、体型、保护等级、分布、各语言鸟名、引用方式和报错入口，也能和花叔的AI贴纸并排对比。

[Ivan](https://github.com/flychicken067)开源的鸟类真实照片库，起因是想看看：不让AI画、只用人的判断，能把花叔的「huashu-bird-sticker」做到什么程度。每种鸟一张iNaturalist上的野外照片，除上传者本人外，至少3个人在至少3个不同月份认定为同一物种，不算点AI建议给出的鉴定，也没有人给出别的物种。按全球统一鸟类名录[AviList v2026](https://www.avilist.org/)整理，目前1049种、39目141科，和[huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)用同一套编号，可以直接对接。照片全部可以免费商用，每张都记录了作者、授权和认定依据。

> **iNaturalist全量查询已经跑完。** 11011种里有10993种拿到了鉴定数据，另外18种学名对不上。新查到的鸟种还要做构图检查和逐张看图，做完后入选数会增加。花叔版有10973种贴纸，我们目前是其中的1049种。

**授权一句话：** 照片可以免费用于任何用途，包括商用，只要按每张照片自己的授权署名（CC0不用署名，CC BY和CC BY-SA要署名，CC BY-SA改过的要按同样授权分享）。我们整理的数据按CC BY 4.0，代码按MIT，第三方部分见[NOTICE](NOTICE.md)。

## 画廊

10个照片最多、最有代表性的类群，每组12张，同一个属尽量只放一张，优先选认定人数多的；最后是每个目各一只。每张图下面列了摄影师。

### 蜂鸟 · *Trochilidae* — 82种

![蜂鸟](previews/families/trochilidae.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

1. *Archilochus colubris* — [Blake Ross](https://www.inaturalist.org/photos/239401590), CC BY
2. *Sephanoides fernandensis* — [iNaturalist](https://www.inaturalist.org/photos/64734837), CC0
3. *Eulampis jugularis* — [Annika Lindqvist](https://www.inaturalist.org/photos/2906217), CC BY
4. *Anthracothorax nigricollis* — [graciela arballo](https://www.inaturalist.org/photos/468129910), CC BY
5. *Coeligena torquata* — [Kristiina Hurme](https://www.inaturalist.org/photos/1618568), CC BY
6. *Eupetomena macroura* — [iNaturalist](https://www.inaturalist.org/photos/543676913), CC0
7. *Selasphorus platycercus* — [Texas Bird Family](https://www.inaturalist.org/photos/444286145), CC BY
8. *Loddigesia mirabilis* — [Thibaud Aronson](https://www.inaturalist.org/photos/114707728), CC BY-SA
9. *Heliactin bilophus* — [agujaceratops](https://www.inaturalist.org/photos/348331475), CC BY
10. *Mellisuga helenae* — [iNaturalist](https://www.inaturalist.org/photos/258810323), CC0
11. *Colibri cyanotus* — [Annika Lindqvist](https://www.inaturalist.org/photos/2383409), CC BY
12. *Chrysolampis mosquitus* — [Inacio Oliveira](https://www.inaturalist.org/photos/474805261), CC BY

</details>

### 翠鸟、蜂虎、鹦鹉和其他彩色鸟 · *Alcedinidae* · *Meropidae* · *Coraciidae* · *Ramphastidae* · *Megalaimidae* · *Psittacidae* · *Psittaculidae* · *Thraupidae* · *Nectariniidae* · *Paradisaeidae* · *Pipridae* — 36种

![翠鸟、蜂虎、鹦鹉和其他彩色鸟](previews/families/colourful.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

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

### 鸠鸽 · *Columbidae* — 79种

![鸠鸽](previews/families/columbidae.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

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

### 鸭、雁与天鹅 · *Anatidae* — 75种

![鸭、雁与天鹅](previews/families/anatidae.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

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

### 雉鸡、鹑与冢雉 · *Phasianidae* · *Odontophoridae* · *Numididae* · *Megapodiidae* · *Cracidae* — 104种

![雉鸡、鹑与冢雉](previews/families/phasianidae.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

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

### 鸮 · *Strigidae* · *Tytonidae* — 41种

![鸮](previews/families/owls.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

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

### 猛禽 · *Accipitridae* · *Falconidae* · *Cathartidae* — 32种

![猛禽](previews/families/raptors.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

1. *Buteo lineatus* — [Don Loarie](https://www.inaturalist.org/photos/14603656), CC BY
2. *Astur cooperii* — [Becky Matsubara](https://www.inaturalist.org/photos/43282408), CC BY
3. *Icthyophaga vocifer* — [Wynand Uys](https://www.inaturalist.org/photos/20939777), CC BY
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

### 鹭、鹮与鹳 · *Ardeidae* · *Threskiornithidae* · *Ciconiidae* — 63种

![鹭、鹮与鹳](previews/families/herons.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

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

### 鹬、鸻与鸥 · *Scolopacidae* · *Charadriidae* · *Laridae* · *Recurvirostridae* · *Haematopodidae* — 101种

![鹬、鸻与鸥](previews/families/shorebirds.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

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

### 鸣禽：鹟、鸫、莺、霸鹟与鸦 · *Muscicapidae* · *Turdidae* · *Parulidae* · *Tyrannidae* · *Icteridae* · *Corvidae* · *Paridae* · *Fringillidae* · *Estrildidae* — 52种

![鸣禽：鹟、鸫、莺、霸鹟与鸦](previews/families/songbirds.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

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

### 每个目各一只

![每个目各一只](previews/orders.jpg)

<details><summary>照片作者（从左到右、从上到下）</summary>

1. *Struthio camelus* — [Andrew Allen](https://www.inaturalist.org/photos/55506762), CC BY
2. *Dromaius novaehollandiae* — [CK2AZ](https://www.inaturalist.org/photos/121143193), CC BY
3. *Apteryx australis* — [Mark Anderson](https://www.inaturalist.org/photos/1795821), CC BY-SA
4. *Rhea pennata* — [Thibaud Aronson](https://www.inaturalist.org/photos/359489448), CC BY-SA
5. *Tinamotis pentlandii* — [iNaturalist](https://www.inaturalist.org/photos/243646625), CC0
6. *Somateria fischeri* — [Nigel Voaden](https://www.inaturalist.org/photos/2946643), CC BY
7. *Phasianus colchicus* — [John Krampl](https://www.inaturalist.org/photos/127255695), CC BY
8. *Phoenicopterus chilensis* — [Thibaud Aronson](https://www.inaturalist.org/photos/64524005), CC BY-SA
9. *Podiceps gallardoi* — [Ezequiel Racker](https://www.inaturalist.org/photos/213999760), CC BY
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

## 里面有什么

| | |
|---|---|
| `data/species.json` | 每种一条记录，最完整的数据：分类、鸟名、编号、分布、形态、保护等级，以及照片、认定依据和检查记录。字段标准和花叔的`data/`一致，说明见[data/README.md](data/README.md)（1049种） |
| `data/species.csv` | 同上，摊平成表格，方便用Excel打开 |
| `data/names.csv` | 1049种鸟、43种语言的鸟名（英文CC BY 4.0，其他语言CC BY 3.0） |
| `data/field-guide.zh-Hans.json` | 289种鸟的中文图鉴笔记（CC BY-SA 4.0） |
| `docs/` | 网站：15种语言，每种鸟一个页面 |
| `ios/` | 离线iOS App源码 |
| `scripts/、site/` | 采集、筛选、出图和建站的脚本（MIT） |

## 覆盖情况

- 照片：1049种全部有，每张都有照片页、原图尺寸、授权和授权链接。143张CC0照片的摄影师放弃了署名，iNaturalist也不给名字，我们不替他们补名字，只留作者主页链接。
- 认定：每张至少3人、跨至少3个月，中位数是4人、3个月，没有异议。
- 编号：iNaturalist物种编号、eBird、Avibase 1049种全有；Wikidata 1034种，GBIF 1021种。
- 鸟名、分布、形态、保护等级原样取自花叔的数据，我们没有改动，所以缺的地方和他一样，比如体长只有540种有。

## 照片怎么选的，质量如何

**物种对不对，由人决定。** 照片来自iNaturalist的野外研究级观测，至少3个账号当前认定为这个物种，认定跨至少3个不同月份，没有人给出别的物种。原图长边至少1200像素，授权只收CC0、CC BY、CC BY-SA。上传者本人的鉴定和点AI建议给出的鉴定都不算。

**画面先由模型初筛，再逐张看。** 检测模型只看画面里有几只鸟、鸟多大、有没有人手，不判断物种。之后逐张看图，排除了370张：被遮挡、只拍到局部、死鸟、家禽、手绘画、拍错的鸟等，每张都写了原因，见[docs/eye-check.csv](docs/eye-check.csv)。

- **还有9909种没有入选。** 其中6067种没有一条观测做到3人认定、跨3个月；3728种还没按新规则复核；22种没有一张画面清楚的单只鸟照片；90种分类范围变了，暂不收；另有2种因学名对不上或看图排除。每一项的计数见[docs/stats.json](docs/stats.json)。

这些是真实照片，但物种是网友鉴定的，不是鸟类学家逐张核对的。当作一张可靠的参考照来用；涉及细节辨识，请以图鉴为准。 和花叔版谁错得少，要等两版公开后比较各自被人指出的错误。在那之前只能说物种依据更强，不能说效果更好。

发现错图，欢迎[提issue](../../issues/new/choose)；网站上每种鸟都有填好鸟名的报错链接。鸟友的纠错，是这个项目最需要的贡献。

## 署名与撤下

每张照片的页面、作者和授权写在`data/species.json`的`photo`里。如果照片是你拍的，而你不希望被收录，请用「摄影师撤回照片」issue表单告诉我们，我们会在7天内换掉，以后也不再使用。

## 怎么用

单张照片可以直接引用，链接格式是：

```
https://inaturalist-open-data.s3.amazonaws.com/photos/<photoId>/original.jpg
```

编号在`data/species.csv`的`photoUrl`列。署名写摄影师，并注明来自iNaturalist；网站上每种鸟都有现成的引用文字。

只想要数据，可以这样拉：

```bash
git clone --filter=blob:none --sparse https://github.com/flychicken067/bird-human-picks
cd bird-human-picks && git sparse-checkout set data
```

## 致谢

- 照片和鉴定：iNaturalist的摄影师和鉴定者，逐张写在`data/species.json`里。照片本身不在仓库中。
- 分类、鸟名、编号、分布、形态：[huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)，花叔，MIT。中文图鉴笔记同出该仓库，CC BY-SA 4.0。
- AviList Core Team. 2026. AviList: The Global Avian Checklist, v2026，CC BY 4.0；IOC世界鸟类名录v15.2，CC BY 3.0；AVONET，Tobias等，2022，CC BY 4.0；Wikidata，CC0。


[BUILD.md](BUILD.md) · [RULES.md](RULES.md) · [PARITY.md](PARITY.md) · [NOTICE.md](NOTICE.md)
