# Ivanオープンソース：複数の人が同定した鳥の実写写真ライブラリ

<img src="previews/header.jpg" alt="Bird Human Picksのサイト：鳥ごとに実写の写真を1枚、どれも3人以上が同定" width="100%">

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · **日本語** · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md)

<a href="https://flychicken067.github.io/bird-human-picks/ja/"><img src="docs/assets/og.png" alt="Bird Human Picksのサイト：鳥ごとに実写の写真を1枚、どれも3人以上が同定" width="100%"></a>

**写真の詳しい使い方は[サイト](https://flychicken067.github.io/bird-human-picks/ja/)で。** 15言語に対応し、1,209種それぞれにページがあります。写真、同定した人数、大きさ、保全状況、分布、各言語の名前、クレジット表記の例、誤りの報告リンク。花叔のAIステッカーと並べて比べることもできます。

[Ivan](https://github.com/flychicken067)によるオープンソースの鳥の実写写真ライブラリです。AIに描かせず人の判断だけで、花叔の「huashu-bird-sticker」をどこまで再現できるかを試すために作りました。種ごとにiNaturalistの野外写真を1枚選び、どれも3人以上が3つ以上の異なる月に同じ種と同定し、別の種を挙げた人はいません。世界共通の鳥類リスト[AviList v2026](https://www.avilist.org/)に従い、現在1,209種、39目145科。[huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)と同じIDを使っているので、そのまま結合できます。写真はすべて商用利用でき、撮影者・ライセンス・同定の根拠を1枚ずつ記録しています。

> **iNaturalistの全件照会が完了しました。** 11,011種のうち10,993種で同定データが取れ、残る18種は学名が一致しませんでした。新しく見つかった種は構図チェックと目視確認がまだで、終われば収録数が増えます。花叔のセットは10,973種のステッカーがあり、私たちは現在そのうち1,209種です。

**ライセンスを一言で：** 写真は商用を含むあらゆる用途に無料で使えます。条件は各写真のライセンスに従ったクレジット表記だけです（CC0は不要、CC BYとCC BY-SAは必要、改変したCC BY-SAは同じライセンスで共有）。整理したデータはCC BY 4.0、コードはMIT、第三者の部分は[NOTICE](NOTICE.md)を参照。

## ギャラリー

写真の多い10グループから各12枚。なるべく1属1枚、同定人数の多いものから選び、最後に各目から1羽ずつ。各プレートの下に撮影者を記載しています。

### ハチドリ · *Trochilidae* — 122種

![ハチドリ](previews/families/trochilidae.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### カワセミ、ハチクイ、オウムなど色鮮やかな鳥 · *Alcedinidae* · *Meropidae* · *Coraciidae* · *Ramphastidae* · *Megalaimidae* · *Psittacidae* · *Psittaculidae* · *Thraupidae* · *Nectariniidae* · *Paradisaeidae* · *Pipridae* — 40種

![カワセミ、ハチクイ、オウムなど色鮮やかな鳥](previews/families/colourful.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### ハト · *Columbidae* — 89種

![ハト](previews/families/columbidae.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### カモ、ガン、ハクチョウ · *Anatidae* — 78種

![カモ、ガン、ハクチョウ](previews/families/anatidae.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### キジ、ウズラ、ツカツクリ · *Phasianidae* · *Odontophoridae* · *Numididae* · *Megapodiidae* · *Cracidae* — 110種

![キジ、ウズラ、ツカツクリ](previews/families/phasianidae.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### フクロウ · *Strigidae* · *Tytonidae* — 44種

![フクロウ](previews/families/owls.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### 猛禽類 · *Accipitridae* · *Falconidae* · *Cathartidae* — 34種

![猛禽類](previews/families/raptors.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### サギ、トキ、コウノトリ · *Ardeidae* · *Threskiornithidae* · *Ciconiidae* — 64種

![サギ、トキ、コウノトリ](previews/families/herons.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### シギ、チドリ、カモメ · *Scolopacidae* · *Charadriidae* · *Laridae* · *Recurvirostridae* · *Haematopodidae* — 115種

![シギ、チドリ、カモメ](previews/families/shorebirds.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### 鳴禽類：ヒタキ、ツグミ、アメリカムシクイ、タイランチョウ、カラス · *Muscicapidae* · *Turdidae* · *Parulidae* · *Tyrannidae* · *Icteridae* · *Corvidae* · *Paridae* · *Fringillidae* · *Estrildidae* — 63種

![鳴禽類：ヒタキ、ツグミ、アメリカムシクイ、タイランチョウ、カラス](previews/families/songbirds.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

### 各目から1羽ずつ

![各目から1羽ずつ](previews/orders.jpg)

<details><summary>撮影者（左から右、上から下）</summary>

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

## 中身

| | |
|---|---|
| `data/species.json` | 1種1レコード、最も完全なデータ：分類、名前、ID、分布、形態、保全状況、そして写真・同定の根拠・チェック記録。花叔の`data/`と同じ項目基準。説明は[data/README.md](data/README.md)（1,209種） |
| `data/species.csv` | 同じ内容を表形式にしたもの |
| `data/names.csv` | 1,209種の43言語の名前（英語CC BY 4.0、他言語CC BY 3.0） |
| `data/field-guide.zh-Hans.json` | 325種の中国語の図鑑メモ（CC BY-SA 4.0） |
| `docs/` | サイト：15言語、種ごとに1ページ |
| `ios/` | オフラインiOSアプリのソース |
| `scripts/、site/` | 収集・選定・プレート作成・サイト生成のスクリプト（MIT） |

## 収録状況

- 写真：1,209種すべてにあり、写真ページ・元画像サイズ・ライセンスとそのURLを記録。CC0の163枚は撮影者が表記を放棄し、iNaturalistも名前を出しません。私たちが名前を補うことはせず、撮影者のプロフィールへのリンクだけを残しています。
- 同定：どの写真も3人以上・3か月以上。中央値は5人・3か月で、異論はありません。
- ID：iNaturalistの分類群ID、eBird、Avibaseは1,209種すべて。Wikidata 1,194種、GBIF 1,176種。
- 名前・分布・形態・保全状況は花叔のデータをそのまま使っており、欠けている所も同じです。たとえば全長があるのは616種だけです。

## 写真の選び方と品質

**種を決めるのは人です。** 写真はiNaturalistの野外の研究用観察から取り、3つ以上のアカウントが現在この種と同定し、同定は3つ以上の異なる月にわたり、別の種を挙げた人はいません。元画像は長辺1200px以上、ライセンスはCC0・CC BY・CC BY-SAのみ。

**画面をモデルで絞り込み、その後1枚ずつ見ます。** 検出モデルは鳥の数・大きさ・人や手の有無だけを見て、種は判断しません。その後すべてを目で確認し、隠れた鳥・一部だけの鳥・死んだ鳥・家禽・絵・別の鳥など367枚を除外しました。理由はすべて[docs/eye-check.csv](docs/eye-check.csv)にあります。

- **まだ9,749種が入っていません。** うち5,929種は3人・3か月の同定がそろった観察がなく、2,448種は構図チェックが未実施で作業中、879種は1羽がはっきり写った写真がなく、400種は元画像が小さく、90種は分類の範囲が変わったため当面除外、残る3種は学名の不一致か目視で除外しました。件数は[docs/stats.json](docs/stats.json)にあります。

実写の写真ですが、種はiNaturalistの利用者が同定したもので、鳥類学者が1枚ずつ確認したものではありません。信頼できる参考写真として使い、細かな識別は図鑑で確かめてください。 花叔版とどちらが誤りが少ないかは、両方を公開した後にそれぞれ指摘された誤りで比べます。それまでは「種の根拠がより強い」とだけ言え、「より良い」とは言えません。

誤った写真を見つけたら[issueを開いて](../../issues/new/choose)ください。サイトの各種ページには鳥の名前入りの報告リンクがあります。バーダーの方からの訂正が、このプロジェクトに最も必要な貢献です。

## クレジットと削除

各写真のページ・撮影者・ライセンスは`data/species.json`の`photo`にあります。ご自身の写真を掲載してほしくない場合は「Remove my photo」のissueフォームでお知らせください。7日以内に差し替え、今後も使いません。

## 使い方

写真は1枚ずつ直接リンクできます。形式は：

```
https://inaturalist-open-data.s3.amazonaws.com/photos/<photoId>/original.jpg
```

番号は`data/species.csv`の`photoUrl`列にあります。撮影者とiNaturalistを表記してください。サイトの各種ページに表記例があります。

データだけを取得するには：

```bash
git clone --filter=blob:none --sparse https://github.com/flychicken067/bird-human-picks
cd bird-human-picks && git sparse-checkout set data
```

## 謝辞

- 写真と同定：iNaturalistの撮影者と同定者。写真ごとに`data/species.json`に記載。写真そのものはリポジトリに含みません。
- 分類・名前・ID・分布・形態：[huashu-bird-sticker](https://github.com/alchaincyf/huashu-bird-sticker)、花叔、MIT。中国語の図鑑メモも同リポジトリから、CC BY-SA 4.0。
- AviList Core Team. 2026. AviList: The Global Avian Checklist, v2026、CC BY 4.0；IOC世界鳥類リストv15.2、CC BY 3.0；AVONET、Tobiasほか、2022、CC BY 4.0；Wikidata、CC0。


[BUILD.md](BUILD.md) · [RULES.md](RULES.md) · [PARITY.md](PARITY.md) · [NOTICE.md](NOTICE.md)
