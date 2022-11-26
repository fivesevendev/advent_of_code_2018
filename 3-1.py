#AOC-2018-3-1


import timeit, sys, time


testData = [
    ("#1", 1, 3, 4, 4),
    ("#2", 3, 1, 4, 4),
    ("#3", 5, 5, 2, 2),
]

data = [("#1",126,902,29,28),("#2",84,482,15,11),("#3",603,530,17,10),("#4",316,302,16,12),("#5",739,983,28,10),("#6",753,122,20,29),("#7",530,554,12,26),("#8",455,60,25,10),("#9",915,465,13,22),("#10",981,813,15,14),("#11",299,473,24,22),("#12",647,679,25,12),("#13",898,700,14,27),("#14",622,745,25,29),("#15",312,156,10,20),("#16",480,316,13,22),("#17",735,160,14,14),("#18",82,713,11,17),("#19",691,670,19,17),("#20",14,968,19,20),("#21",3,271,27,21),("#22",341,788,23,15),("#23",564,771,27,16),("#24",676,166,25,12),("#25",530,172,10,22),("#26",730,277,28,10),("#27",437,739,16,17),("#28",261,722,13,11),("#29",935,122,13,23),("#30",676,16,15,15),("#31",915,319,23,20),("#32",737,810,16,25),("#33",767,147,16,15),("#34",778,895,21,23),("#35",17,739,18,15),("#36",662,424,14,27),("#37",336,934,27,27),("#38",541,934,27,26),("#39",621,3,16,25),("#40",714,196,25,12),("#41",6,628,10,28),("#42",192,379,16,22),("#43",89,747,10,20),("#44",419,789,22,24),("#45",241,910,25,18),("#46",743,873,28,10),("#47",581,836,23,27),("#48",574,119,27,13),("#49",432,573,10,19),("#50",886,620,23,21),("#51",446,167,15,14),("#52",326,634,29,13),("#53",29,457,11,24),("#54",410,189,13,24),("#55",811,933,28,28),("#56",287,650,15,11),("#57",240,519,26,16),("#58",598,695,22,26),("#59",836,344,13,4),("#60",261,140,22,14),("#61",739,88,12,15),("#62",295,891,17,25),("#63",246,861,17,11),("#64",719,844,11,28),("#65",669,597,15,20),("#66",718,364,17,25),("#67",388,535,21,11),("#68",475,504,10,25),("#69",359,621,13,11),("#70",153,446,29,14),("#71",166,540,13,24),("#72",135,369,22,12),("#73",302,878,18,23),("#74",829,215,18,26),("#75",81,483,14,11),("#76",950,458,22,23),("#77",576,757,20,28),("#78",558,235,22,26),("#79",290,761,26,12),("#80",315,610,16,13),("#81",652,917,18,26),("#82",916,117,27,10),("#83",16,85,25,18),("#84",397,636,23,27),("#85",771,627,28,28),("#86",824,897,27,12),("#87",852,605,29,16),("#88",197,838,21,11),("#89",876,397,10,15),("#90",9,916,28,21),("#91",591,978,29,20),("#92",744,611,27,10),("#93",459,62,16,29),("#94",87,622,14,16),("#95",161,738,20,22),("#96",506,264,29,20),("#97",633,742,17,25),("#98",413,226,21,11),("#99",840,441,20,21),("#100",37,7,25,19),("#101",21,711,29,14),("#102",438,190,27,21),("#103",633,113,14,22),("#104",277,26,26,17),("#105",135,462,18,17),("#106",46,783,26,27),("#107",353,702,19,26),("#108",711,975,12,5),("#109",555,4,12,22),("#110",384,841,11,26),("#111",433,35,23,21),("#112",680,260,5,7),("#113",330,256,12,11),("#114",705,394,17,22),("#115",898,116,13,12),("#116",376,813,12,24),("#117",349,826,28,23),("#118",684,67,22,27),("#119",973,758,24,12),("#120",183,924,19,15),("#121",186,196,24,15),("#122",697,188,27,15),("#123",868,343,25,15),("#124",172,340,14,13),("#125",899,203,12,4),("#126",403,194,16,29),("#127",607,285,16,10),("#128",296,924,10,14),("#129",735,72,25,21),("#130",120,678,27,23),("#131",747,771,26,23),("#132",657,537,23,26),("#133",402,632,29,12),("#134",862,571,26,22),("#135",881,873,26,10),("#136",354,820,29,18),("#137",173,742,15,20),("#138",417,32,14,15),("#139",688,681,22,15),("#140",800,269,19,25),("#141",880,821,10,23),("#142",477,579,22,27),("#143",846,583,28,26),("#144",391,236,28,23),("#145",672,950,16,11),("#146",560,796,25,20),("#147",38,781,20,19),("#148",664,694,14,10),("#149",67,337,20,11),("#150",101,924,16,29),("#151",19,532,13,12),("#152",846,757,23,21),("#153",321,832,15,14),("#154",76,905,12,3),("#155",174,628,26,22),("#156",239,298,10,21),("#157",698,71,24,28),("#158",444,163,16,26),("#159",661,699,20,29),("#160",703,126,11,15),("#161",626,58,27,27),("#162",85,74,14,10),("#163",834,430,21,16),("#164",815,119,19,24),("#165",471,242,27,17),("#166",98,696,14,29),("#167",98,573,24,20),("#168",97,211,15,24),("#169",519,805,15,13),("#170",718,630,17,7),("#171",559,661,22,16),("#172",662,480,13,24),("#173",105,536,14,13),("#174",618,746,15,29),("#175",951,232,12,28),("#176",659,602,27,15),("#177",612,761,15,19),("#178",953,469,24,15),("#179",285,518,15,12),("#180",677,258,18,12),("#181",562,417,14,25),("#182",712,522,23,26),("#183",506,775,13,20),("#184",264,516,24,24),("#185",97,113,19,21),("#186",390,588,10,25),("#187",427,361,23,15),("#188",217,509,26,21),("#189",239,662,18,14),("#190",121,368,18,26),("#191",940,852,10,14),("#192",867,882,20,15),("#193",413,266,27,21),("#194",838,469,24,29),("#195",837,76,14,24),("#196",528,418,29,21),("#197",295,341,18,14),("#198",345,609,19,21),("#199",522,265,28,12),("#200",190,416,21,10),("#201",408,347,13,11),("#202",856,162,27,19),("#203",797,439,26,17),("#204",265,143,27,19),("#205",761,102,11,21),("#206",933,693,11,11),("#207",251,801,21,14),("#208",364,695,26,10),("#209",33,781,28,13),("#210",696,697,29,19),("#211",501,555,10,11),("#212",73,452,24,18),("#213",91,291,25,18),("#214",396,499,24,10),("#215",86,85,22,15),("#216",418,475,16,25),("#217",603,901,11,23),("#218",15,955,20,17),("#219",107,355,28,28),("#220",258,550,28,15),("#221",265,399,27,17),("#222",496,757,15,28),("#223",423,491,21,24),("#224",228,829,15,25),("#225",188,519,28,24),("#226",566,622,18,17),("#227",929,856,25,14),("#228",596,303,18,20),("#229",633,110,26,26),("#230",419,544,24,29),("#231",380,389,19,11),("#232",157,364,18,21),("#233",866,294,20,21),("#234",899,710,22,23),("#235",455,493,23,26),("#236",802,123,20,26),("#237",781,384,11,15),("#238",649,763,15,13),("#239",889,878,20,15),("#240",820,508,23,12),("#241",95,561,14,13),("#242",580,418,20,18),("#243",12,341,27,11),("#244",734,191,28,11),("#245",473,499,13,10),("#246",386,879,26,10),("#247",711,691,10,29),("#248",916,443,18,10),("#249",360,378,22,18),("#250",29,518,25,18),("#251",426,914,24,19),("#252",746,287,26,16),("#253",792,219,15,23),("#254",780,977,18,18),("#255",530,79,12,25),("#256",597,698,16,24),("#257",933,305,23,23),("#258",596,695,11,18),("#259",235,834,27,17),("#260",302,273,14,15),("#261",412,451,25,10),("#262",870,205,14,15),("#263",291,384,18,27),("#264",35,309,27,21),("#265",357,506,28,14),("#266",968,439,14,29),("#267",184,185,28,17),("#268",387,931,16,12),("#269",631,660,26,22),("#270",469,555,16,24),("#271",361,497,14,14),("#272",403,355,11,12),("#273",159,371,11,23),("#274",393,483,24,19),("#275",535,347,14,24),("#276",44,135,21,16),("#277",380,634,22,14),("#278",876,287,13,28),("#279",265,870,13,23),("#280",583,138,24,27),("#281",364,99,20,29),("#282",507,415,24,21),("#283",693,861,29,17),("#284",318,938,28,19),("#285",704,584,19,12),("#286",369,922,12,17),("#287",512,548,25,21),("#288",723,788,29,20),("#289",434,605,15,29),("#290",302,293,22,27),("#291",901,17,13,18),("#292",217,880,25,21),("#293",795,623,10,28),("#294",433,102,10,22),("#295",490,799,16,27),("#296",897,34,29,29),("#297",359,644,20,26),("#298",252,549,23,22),("#299",102,370,26,13),("#300",184,545,20,24),("#301",704,481,13,18),("#302",881,705,19,15),("#303",184,342,27,14),("#304",853,725,14,28),("#305",220,390,12,20),("#306",417,52,21,14),("#307",743,618,26,16),("#308",320,254,29,19),("#309",791,971,11,25),("#310",104,57,11,21),("#311",600,748,14,27),("#312",11,278,26,17),("#313",360,798,14,28),("#314",212,106,29,21),("#315",812,24,14,14),("#316",550,1,29,11),("#317",702,548,19,20),("#318",190,911,6,7),("#319",85,64,24,15),("#320",915,479,13,26),("#321",550,868,26,29),("#322",832,855,21,10),("#323",443,887,23,20),("#324",978,169,15,12),("#325",957,745,21,29),("#326",218,149,19,17),("#327",452,857,22,18),("#328",470,19,29,20),("#329",425,134,16,19),("#330",622,753,25,22),("#331",466,155,29,15),("#332",288,0,20,11),("#333",133,919,8,3),("#334",202,459,26,25),("#335",613,805,28,22),("#336",784,123,11,17),("#337",527,413,26,28),("#338",955,509,12,21),("#339",255,138,13,25),("#340",387,247,29,25),("#341",41,701,27,15),("#342",108,891,26,24),("#343",515,466,24,20),("#344",106,108,11,22),("#345",36,691,14,26),("#346",303,463,19,16),("#347",890,882,14,17),("#348",37,23,25,25),("#349",535,665,25,11),("#350",737,935,15,17),("#351",318,792,18,11),("#352",885,331,17,13),("#353",384,224,11,19),("#354",433,557,22,20),("#355",586,463,14,11),("#356",595,958,11,15),("#357",697,39,20,17),("#358",402,612,23,27),("#359",881,695,26,18),("#360",92,75,11,11),("#361",741,739,17,27),("#362",205,388,15,23),("#363",292,260,21,12),("#364",35,426,10,21),("#365",314,459,12,27),("#366",834,678,17,29),("#367",956,102,12,19),("#368",750,410,22,11),("#369",531,161,19,15),("#370",643,654,11,12),("#371",309,248,23,26),("#372",898,335,19,19),("#373",379,180,7,7),("#374",680,720,13,26),("#375",744,660,13,14),("#376",445,135,11,25),("#377",67,622,23,17),("#378",664,830,29,22),("#379",283,933,16,15),("#380",46,835,29,27),("#381",876,311,26,25),("#382",925,703,18,22),("#383",573,664,23,27),("#384",529,120,28,10),("#385",892,201,24,10),("#386",202,394,16,15),("#387",716,854,23,13),("#388",333,462,15,21),("#389",520,448,15,19),("#390",924,613,18,21),("#391",548,344,22,17),("#392",520,383,17,17),("#393",955,932,15,22),("#394",377,268,11,25),("#395",119,45,5,7),("#396",425,547,14,24),("#397",785,673,15,20),("#398",475,489,18,24),("#399",765,981,17,10),("#400",942,414,10,16),("#401",373,641,23,16),("#402",950,862,12,10),("#403",580,193,10,24),("#404",556,827,18,20),("#405",515,271,12,24),("#406",939,69,15,11),("#407",578,101,12,11),("#408",633,157,28,16),("#409",652,173,15,25),("#410",275,191,28,13),("#411",383,481,19,19),("#412",158,47,12,22),("#413",800,158,29,13),("#414",783,762,27,13),("#415",707,98,23,27),("#416",433,132,29,20),("#417",973,460,16,23),("#418",681,56,16,15),("#419",13,653,29,15),("#420",183,399,19,28),("#421",507,359,16,11),("#422",804,649,18,29),("#423",7,508,14,14),("#424",857,501,24,13),("#425",157,441,24,18),("#426",802,606,11,26),("#427",739,275,9,15),("#428",138,287,20,28),("#429",656,658,29,26),("#430",815,275,11,17),("#431",156,233,14,15),("#432",962,759,20,19),("#433",564,667,20,26),("#434",833,957,15,21),("#435",708,752,16,18),("#436",54,315,28,10),("#437",779,124,17,12),("#438",186,480,28,18),("#439",359,639,27,28),("#440",307,213,15,28),("#441",549,324,20,22),("#442",307,312,24,14),("#443",164,638,23,21),("#444",223,377,23,22),("#445",474,582,16,20),("#446",105,62,25,26),("#447",693,65,16,25),("#448",497,631,3,9),("#449",299,315,24,10),("#450",350,371,13,8),("#451",557,945,28,15),("#452",459,890,12,25),("#453",483,592,15,18),("#454",929,201,25,11),("#455",217,827,17,24),("#456",456,851,18,27),("#457",568,141,24,10),("#458",901,568,10,16),("#459",401,475,18,16),("#460",434,119,11,16),("#461",379,752,24,16),("#462",437,794,15,27),("#463",913,581,17,29),("#464",219,603,13,21),("#465",443,106,3,5),("#466",782,619,22,26),("#467",116,95,15,26),("#468",85,720,3,3),("#469",39,854,18,17),("#470",699,943,20,12),("#471",962,496,22,20),("#472",314,214,16,18),("#473",715,834,18,17),("#474",727,69,20,25),("#475",295,966,27,19),("#476",290,792,24,11),("#477",706,73,23,29),("#478",591,349,17,18),("#479",105,709,12,22),("#480",469,69,22,26),("#481",868,647,28,19),("#482",732,182,12,23),("#483",469,843,15,29),("#484",320,843,28,23),("#485",240,40,26,10),("#486",715,261,19,12),("#487",670,287,25,25),("#488",921,246,11,22),("#489",567,943,11,15),("#490",70,754,23,22),("#491",715,628,25,12),("#492",591,580,19,25),("#493",527,492,17,15),("#494",186,897,25,29),("#495",306,321,22,23),("#496",366,841,22,12),("#497",923,105,22,12),("#498",458,335,23,17),("#499",373,774,23,10),("#500",85,321,12,22),("#501",405,61,26,21),("#502",169,328,29,21),("#503",662,373,17,20),("#504",693,767,23,20),("#505",437,98,21,20),("#506",685,25,21,29),("#507",195,133,16,11),("#508",736,654,13,27),("#509",344,686,13,25),("#510",622,580,11,18),("#511",563,874,18,23),("#512",610,527,10,17),("#513",313,218,26,10),("#514",435,442,18,12),("#515",418,546,28,21),("#516",883,886,15,25),("#517",446,205,12,11),("#518",73,875,13,24),("#519",362,349,14,12),("#520",555,230,13,28),("#521",71,616,20,22),("#522",647,683,24,25),("#523",613,265,22,13),("#524",157,290,25,25),("#525",444,493,21,16),("#526",658,824,12,14),("#527",9,90,14,10),("#528",475,546,12,29),("#529",285,15,25,26),("#530",10,250,25,29),("#531",229,305,26,25),("#532",54,696,18,20),("#533",89,526,28,15),("#534",578,427,27,12),("#535",374,279,21,28),("#536",931,428,10,25),("#537",478,19,25,19),("#538",464,851,14,21),("#539",673,685,22,29),("#540",438,134,18,14),("#541",628,839,29,27),("#542",109,368,16,21),("#543",273,866,11,24),("#544",105,536,16,11),("#545",897,543,11,27),("#546",43,598,14,15),("#547",676,772,18,24),("#548",718,950,10,20),("#549",487,809,21,17),("#550",799,860,29,27),("#551",79,628,16,26),("#552",725,803,20,10),("#553",56,274,13,19),("#554",75,868,20,24),("#555",258,789,19,16),("#556",562,789,14,13),("#557",41,859,14,10),("#558",162,820,19,27),("#559",918,819,25,29),("#560",61,513,14,28),("#561",442,397,20,14),("#562",589,360,26,19),("#563",97,52,25,14),("#564",985,579,15,22),("#565",576,130,21,22),("#566",196,130,17,15),("#567",845,404,18,18),("#568",372,175,25,24),("#569",937,256,29,20),("#570",541,716,28,24),("#571",590,798,27,15),("#572",89,47,26,12),("#573",448,23,11,27),("#574",126,358,12,13),("#575",238,615,13,16),("#576",309,251,13,25),("#577",369,863,20,14),("#578",285,467,20,12),("#579",598,294,25,27),("#580",700,264,23,24),("#581",310,432,21,17),("#582",379,543,13,27),("#583",671,432,14,26),("#584",315,206,14,11),("#585",413,344,19,22),("#586",757,519,12,14),("#587",792,110,19,26),("#588",458,141,22,28),("#589",791,696,22,29),("#590",663,177,19,29),("#591",269,656,28,15),("#592",475,775,20,19),("#593",29,158,23,14),("#594",910,430,26,20),("#595",623,186,21,25),("#596",674,735,28,11),("#597",165,322,26,25),("#598",604,589,24,19),("#599",246,666,26,27),("#600",689,797,22,18),("#601",181,933,21,15),("#602",729,230,23,28),("#603",85,734,11,25),("#604",833,537,21,11),("#605",585,733,11,21),("#606",288,450,25,27),("#607",237,345,25,16),("#608",191,503,18,28),("#609",293,751,23,19),("#610",401,51,28,20),("#611",871,570,27,14),("#612",716,730,16,10),("#613",601,623,18,24),("#614",350,355,27,15),("#615",367,477,15,23),("#616",930,255,17,18),("#617",860,843,23,10),("#618",400,643,27,16),("#619",433,720,22,27),("#620",620,962,15,23),("#621",122,153,15,16),("#622",452,791,16,17),("#623",310,168,24,15),("#624",276,468,13,10),("#625",610,905,14,10),("#626",608,4,29,21),("#627",478,86,21,22),("#628",244,560,26,21),("#629",466,392,21,11),("#630",835,482,11,23),("#631",601,864,14,25),("#632",763,909,25,27),("#633",428,571,20,25),("#634",761,886,24,19),("#635",322,864,13,21),("#636",84,507,28,16),("#637",37,146,25,16),("#638",706,507,11,20),("#639",703,474,23,28),("#640",703,386,12,11),("#641",164,910,26,21),("#642",698,729,10,4),("#643",353,287,23,22),("#644",597,540,22,20),("#645",698,689,17,10),("#646",382,289,11,10),("#647",61,234,10,14),("#648",218,608,17,26),("#649",916,662,13,16),("#650",956,499,15,17),("#651",556,949,28,15),("#652",106,51,26,15),("#653",432,530,25,22),("#654",373,270,18,29),("#655",871,398,14,17),("#656",768,609,29,24),("#657",642,59,12,27),("#658",268,333,13,25),("#659",556,202,25,19),("#660",306,925,16,26),("#661",445,628,23,24),("#662",471,386,15,24),("#663",136,820,15,17),("#664",568,103,23,18),("#665",787,107,11,19),("#666",67,922,14,23),("#667",980,173,7,3),("#668",679,228,18,18),("#669",960,118,27,15),("#670",515,925,13,16),("#671",354,785,11,28),("#672",551,955,10,22),("#673",23,74,26,21),("#674",776,51,20,28),("#675",288,8,15,27),("#676",114,700,24,28),("#677",822,374,26,27),("#678",522,553,17,29),("#679",198,836,18,29),("#680",840,904,18,13),("#681",92,778,17,20),("#682",921,327,12,21),("#683",44,675,14,21),("#684",923,237,11,15),("#685",593,709,10,16),("#686",227,611,21,23),("#687",75,336,20,15),("#688",309,261,28,27),("#689",743,835,21,16),("#690",903,585,26,24),("#691",260,413,16,11),("#692",585,962,16,29),("#693",221,899,23,15),("#694",917,62,29,21),("#695",958,656,12,22),("#696",736,756,14,25),("#697",596,292,10,16),("#698",133,811,22,28),("#699",892,872,23,16),("#700",259,714,27,22),("#701",261,725,23,19),("#702",62,950,16,22),("#703",418,414,21,14),("#704",182,663,21,16),("#705",823,89,22,11),("#706",209,968,15,26),("#707",554,546,11,10),("#708",73,186,15,24),("#709",816,574,19,26),("#710",336,446,25,20),("#711",596,45,12,24),("#712",448,378,26,17),("#713",606,807,26,27),("#714",813,9,28,29),("#715",346,361,17,29),("#716",641,958,18,19),("#717",493,766,17,13),("#718",592,550,18,25),("#719",377,599,29,18),("#720",142,893,18,14),("#721",549,532,19,27),("#722",656,846,28,12),("#723",2,956,29,17),("#724",527,977,19,15),("#725",100,902,20,19),("#726",630,266,13,28),("#727",549,102,14,22),("#728",472,868,12,17),("#729",59,306,29,23),("#730",176,828,18,13),("#731",753,394,29,19),("#732",702,729,27,14),("#733",57,538,15,18),("#734",956,912,12,28),("#735",102,24,12,26),("#736",303,488,5,18),("#737",188,626,23,25),("#738",193,197,25,16),("#739",410,458,12,17),("#740",964,492,16,24),("#741",77,623,19,15),("#742",767,111,12,15),("#743",54,288,13,13),("#744",228,102,14,22),("#745",301,486,10,26),("#746",856,655,19,11),("#747",185,177,19,23),("#748",57,764,21,19),("#749",374,754,21,23),("#750",236,33,20,27),("#751",619,786,22,24),("#752",281,84,22,28),("#753",297,792,23,16),("#754",388,938,16,17),("#755",898,330,20,29),("#756",142,38,18,25),("#757",414,481,13,29),("#758",31,282,14,17),("#759",670,219,12,14),("#760",36,421,13,19),("#761",953,786,20,10),("#762",531,407,22,29),("#763",83,342,18,19),("#764",415,532,27,26),("#765",595,923,28,15),("#766",106,109,25,18),("#767",491,629,14,16),("#768",613,980,10,14),("#769",876,45,21,22),("#770",723,767,15,17),("#771",590,358,14,27),("#772",41,695,23,28),("#773",43,657,18,11),("#774",37,592,24,14),("#775",790,747,18,14),("#776",84,174,11,26),("#777",924,165,10,23),("#778",832,450,15,10),("#779",709,49,28,25),("#780",803,849,26,17),("#781",294,25,10,25),("#782",955,623,26,18),("#783",149,467,11,20),("#784",618,130,13,12),("#785",440,121,10,13),("#786",301,13,22,24),("#787",610,70,21,29),("#788",189,518,25,21),("#789",675,434,15,25),("#790",342,348,21,20),("#791",960,115,12,26),("#792",666,314,15,27),("#793",951,438,28,13),("#794",75,908,15,23),("#795",792,839,19,24),("#796",227,144,20,11),("#797",606,149,17,29),("#798",322,260,29,15),("#799",556,826,19,29),("#800",794,559,26,21),("#801",614,877,18,19),("#802",831,700,22,18),("#803",705,490,29,23),("#804",74,900,24,13),("#805",99,519,20,14),("#806",468,597,16,27),("#807",566,633,17,14),("#808",223,866,11,11),("#809",722,504,21,12),("#810",943,863,16,19),("#811",709,341,27,10),("#812",568,746,27,13),("#813",103,295,13,10),("#814",734,155,17,14),("#815",946,672,27,17),("#816",840,845,22,26),("#817",382,659,26,28),("#818",731,631,16,14),("#819",727,630,21,19),("#820",789,345,11,21),("#821",695,689,27,17),("#822",271,649,16,22),("#823",707,795,18,29),("#824",650,475,21,13),("#825",531,531,28,28),("#826",566,317,23,17),("#827",53,827,27,27),("#828",646,555,27,12),("#829",691,843,11,19),("#830",258,855,23,21),("#831",409,187,10,29),("#832",482,630,11,15),("#833",295,459,15,22),("#834",977,592,11,20),("#835",85,404,13,22),("#836",409,49,29,11),("#837",549,609,22,22),("#838",555,688,28,26),("#839",912,307,29,16),("#840",796,862,21,10),("#841",143,372,22,17),("#842",368,871,20,16),("#843",54,475,15,20),("#844",606,443,28,10),("#845",643,837,24,14),("#846",180,817,29,15),("#847",177,751,17,11),("#848",647,969,25,22),("#849",759,509,13,11),("#850",606,620,21,24),("#851",827,885,18,28),("#852",608,885,13,21),("#853",790,868,29,25),("#854",465,352,11,19),("#855",627,643,23,16),("#856",333,341,19,11),("#857",265,718,28,17),("#858",200,448,10,27),("#859",344,826,27,13),("#860",957,103,10,16),("#861",148,309,27,29),("#862",367,514,15,29),("#863",945,241,24,15),("#864",459,508,26,20),("#865",696,599,11,12),("#866",185,159,29,19),("#867",818,370,27,17),("#868",973,453,13,29),("#869",553,243,24,29),("#870",391,472,18,28),("#871",527,352,13,24),("#872",426,267,22,14),("#873",0,248,14,21),("#874",747,190,13,14),("#875",312,722,15,15),("#876",350,353,18,27),("#877",116,103,13,17),("#878",148,245,23,23),("#879",473,355,24,19),("#880",287,551,22,12),("#881",854,608,27,22),("#882",131,270,15,26),("#883",638,472,15,20),("#884",793,338,10,13),("#885",844,939,17,14),("#886",694,727,27,11),("#887",464,791,28,10),("#888",9,590,24,16),("#889",560,83,23,24),("#890",747,278,29,14),("#891",74,763,11,11),("#892",255,474,22,21),("#893",349,300,27,29),("#894",856,298,28,12),("#895",164,232,25,18),("#896",537,104,14,25),("#897",19,741,12,8),("#898",424,43,16,11),("#899",676,153,14,18),("#900",769,656,23,17),("#901",883,905,17,19),("#902",770,350,21,28),("#903",8,961,18,19),("#904",457,849,26,13),("#905",185,758,16,10),("#906",878,583,18,18),("#907",433,734,29,27),("#908",511,279,19,24),("#909",673,423,20,15),("#910",890,470,28,24),("#911",531,538,14,17),("#912",90,778,20,11),("#913",914,221,11,29),("#914",330,871,20,23),("#915",305,609,24,14),("#916",836,747,13,22),("#917",733,937,29,11),("#918",824,451,28,12),("#919",308,306,11,19),("#920",622,626,11,28),("#921",181,362,22,18),("#922",834,962,15,11),("#923",59,246,20,23),("#924",855,868,19,29),("#925",476,779,17,21),("#926",460,256,15,12),("#927",688,742,14,23),("#928",160,560,28,19),("#929",470,456,12,23),("#930",553,780,15,23),("#931",377,700,23,11),("#932",760,761,27,22),("#933",105,68,18,11),("#934",36,648,29,22),("#935",508,405,25,25),("#936",76,360,27,29),("#937",113,130,19,28),("#938",517,383,12,15),("#939",406,892,23,27),("#940",522,575,17,12),("#941",778,765,11,11),("#942",227,868,3,6),("#943",0,922,18,23),("#944",55,683,15,19),("#945",755,648,19,14),("#946",735,271,21,23),("#947",454,852,22,14),("#948",338,936,21,19),("#949",348,920,22,17),("#950",906,447,29,14),("#951",519,919,28,12),("#952",243,946,26,27),("#953",194,641,26,23),("#954",900,332,15,21),("#955",11,672,14,28),("#956",829,706,23,20),("#957",174,14,20,22),("#958",876,295,29,17),("#959",338,637,18,29),("#960",40,697,19,21),("#961",61,489,15,18),("#962",300,856,23,11),("#963",862,202,29,20),("#964",852,507,21,16),("#965",404,51,22,12),("#966",585,453,15,12),("#967",113,513,21,23),("#968",615,130,20,19),("#969",359,802,17,14),("#970",706,183,29,18),("#971",702,542,23,21),("#972",205,494,17,18),("#973",271,491,14,25),("#974",449,9,23,17),("#975",240,627,15,29),("#976",720,551,15,28),("#977",259,351,10,16),("#978",849,546,21,22),("#979",17,667,16,28),("#980",598,752,18,19),("#981",600,910,19,18),("#982",738,833,17,29),("#983",790,652,17,24),("#984",87,76,5,3),("#985",923,866,22,18),("#986",307,742,21,26),("#987",348,369,18,14),("#988",847,851,11,23),("#989",618,298,26,17),("#990",812,629,10,24),("#991",698,119,26,25),("#992",763,882,23,29),("#993",954,817,29,19),("#994",777,722,26,27),("#995",408,8,18,16),("#996",717,535,10,22),("#997",944,783,22,14),("#998",714,577,28,17),("#999",223,955,27,21),("#1000",608,64,17,20),("#1001",819,394,29,27),("#1002",733,506,14,21),("#1003",712,383,28,25),("#1004",897,939,13,29),("#1005",681,702,22,23),("#1006",146,372,26,14),("#1007",512,277,20,19),("#1008",682,86,25,26),("#1009",540,694,20,26),("#1010",171,764,20,10),("#1011",682,710,22,13),("#1012",657,789,4,10),("#1013",963,207,20,21),("#1014",846,111,23,19),("#1015",373,306,16,19),("#1016",616,642,19,12),("#1017",783,439,24,16),("#1018",87,352,10,4),("#1019",128,156,29,11),("#1020",447,758,13,23),("#1021",669,735,15,14),("#1022",196,501,24,22),("#1023",29,22,25,26),("#1024",693,275,29,18),("#1025",319,175,29,26),("#1026",614,130,29,29),("#1027",654,785,12,25),("#1028",219,834,15,21),("#1029",73,853,11,22),("#1030",469,707,29,25),("#1031",632,852,18,12),("#1032",722,195,11,21),("#1033",183,853,24,27),("#1034",372,499,28,25),("#1035",863,375,25,18),("#1036",689,130,27,24),("#1037",690,604,22,12),("#1038",361,197,16,13),("#1039",66,458,15,13),("#1040",974,766,14,21),("#1041",791,381,20,17),("#1042",513,789,18,18),("#1043",296,795,14,11),("#1044",725,204,24,10),("#1045",122,894,13,27),("#1046",891,95,19,27),("#1047",76,397,14,16),("#1048",205,516,14,14),("#1049",882,639,29,13),("#1050",855,106,11,15),("#1051",834,341,18,11),("#1052",736,191,28,27),("#1053",471,483,24,21),("#1054",525,973,28,21),("#1055",574,179,18,17),("#1056",656,918,18,20),("#1057",829,190,14,27),("#1058",673,373,13,11),("#1059",260,587,16,18),("#1060",333,385,26,18),("#1061",817,157,18,14),("#1062",522,178,26,19),("#1063",576,938,16,29),("#1064",879,436,11,17),("#1065",486,447,22,23),("#1066",303,429,21,11),("#1067",517,786,23,25),("#1068",475,474,25,11),("#1069",632,657,15,24),("#1070",2,948,15,12),("#1071",741,198,27,25),("#1072",467,62,18,27),("#1073",561,501,17,13),("#1074",271,513,21,26),("#1075",656,333,15,14),("#1076",27,325,12,18),("#1077",183,396,25,22),("#1078",656,825,21,28),("#1079",285,558,23,20),("#1080",287,95,22,24),("#1081",31,470,4,5),("#1082",880,633,19,19),("#1083",44,154,21,26),("#1084",956,490,15,23),("#1085",901,674,23,10),("#1086",932,299,12,14),("#1087",313,726,16,24),("#1088",474,394,15,11),("#1089",764,122,16,17),("#1090",568,298,10,20),("#1091",720,277,28,27),("#1092",128,885,23,16),("#1093",906,111,25,23),("#1094",477,639,22,24),("#1095",34,36,21,15),("#1096",510,274,20,21),("#1097",800,960,23,29),("#1098",861,163,16,15),("#1099",868,647,26,20),("#1100",355,404,29,11),("#1101",947,226,17,11),("#1102",816,580,13,19),("#1103",615,572,16,14),("#1104",914,612,16,26),("#1105",897,944,23,12),("#1106",287,920,22,15),("#1107",726,816,27,28),("#1108",248,139,18,21),("#1109",425,56,13,16),("#1110",635,305,10,13),("#1111",260,347,22,10),("#1112",263,596,18,15),("#1113",69,470,29,13),("#1114",949,783,17,20),("#1115",10,58,25,23),("#1116",669,941,22,25),("#1117",798,218,27,24),("#1118",893,561,14,26),("#1119",117,42,11,18),("#1120",433,100,29,24),("#1121",969,210,3,13),("#1122",497,708,17,25),("#1123",598,118,20,15),("#1124",892,327,13,25),("#1125",943,639,25,12),("#1126",443,401,17,10),("#1127",103,207,17,11),("#1128",877,789,22,12),("#1129",440,142,11,23),("#1130",571,880,29,29),("#1131",618,802,25,13),("#1132",432,355,27,12),("#1133",743,427,21,15),("#1134",140,121,25,14),("#1135",156,33,22,18),("#1136",659,464,20,20),("#1137",301,457,23,13),("#1138",69,746,22,26),("#1139",285,16,10,21),("#1140",567,478,16,26),("#1141",875,820,11,23),("#1142",156,213,21,23),("#1143",92,52,21,24),("#1144",629,745,18,10),("#1145",347,689,13,23),("#1146",925,875,15,14),("#1147",449,426,11,22),("#1148",274,883,25,23),("#1149",612,917,23,29),("#1150",664,676,19,20),("#1151",855,164,14,13),("#1152",225,898,29,13),("#1153",365,475,11,19),("#1154",784,722,19,22),("#1155",160,755,15,12),("#1156",33,956,18,26),("#1157",294,844,14,27),("#1158",779,723,27,14),("#1159",226,893,21,17),("#1160",519,646,23,21),("#1161",392,655,26,11),("#1162",754,77,14,28),("#1163",246,860,20,13),("#1164",187,350,26,16),("#1165",328,706,17,11),("#1166",840,941,19,11),("#1167",222,670,27,18),("#1168",723,98,28,26),("#1169",450,59,15,12),("#1170",531,151,29,21),("#1171",730,727,16,17),("#1172",626,751,17,15),("#1173",177,446,18,25),("#1174",469,760,28,29),("#1175",565,195,19,16),("#1176",196,414,24,21),("#1177",283,0,17,10),("#1178",207,528,16,23),("#1179",300,196,24,27),("#1180",223,901,29,27),("#1181",749,881,27,26),("#1182",584,24,20,24),("#1183",265,556,13,26),("#1184",31,337,25,14),("#1185",271,396,27,12),("#1186",701,184,28,20),("#1187",799,589,20,14),("#1188",453,864,29,26),("#1189",927,972,14,25),("#1190",103,61,16,10),("#1191",103,909,13,7),("#1192",600,40,17,17),("#1193",264,371,24,15),("#1194",317,730,12,28),("#1195",477,788,17,24),("#1196",547,262,18,19),("#1197",186,5,13,23),("#1198",218,934,29,29),("#1199",101,77,10,11),("#1200",202,692,18,29),("#1201",67,618,21,24),("#1202",421,407,20,13),("#1203",755,501,20,14),("#1204",784,621,25,12),("#1205",246,709,20,15),("#1206",433,42,22,27),("#1207",571,940,20,29),("#1208",420,262,20,14),("#1209",433,623,17,18),("#1210",708,207,24,26),("#1211",702,34,15,11),("#1212",495,413,14,18),("#1213",939,785,15,11),("#1214",919,301,24,26),("#1215",302,478,20,26),("#1216",175,913,12,14),("#1217",96,329,15,19),("#1218",309,253,16,19),("#1219",186,160,21,28),("#1220",276,658,17,10),("#1221",428,137,7,12),("#1222",881,457,27,26),("#1223",174,32,25,17),("#1224",469,460,20,26),("#1225",725,930,28,23),("#1226",3,498,12,29),("#1227",470,141,27,25),("#1228",205,505,20,26),("#1229",500,355,25,22),("#1230",68,932,18,29),("#1231",32,42,23,25),("#1232",723,66,29,12),("#1233",329,336,29,26),("#1234",184,834,21,16),("#1235",475,141,29,13),("#1236",911,829,18,17),("#1237",94,944,23,26),("#1238",840,515,14,27),("#1239",631,747,11,4),("#1240",566,679,23,29),("#1241",591,751,18,10),("#1242",746,650,10,13),("#1243",357,729,16,14),("#1244",329,224,19,13),("#1245",406,187,22,14),("#1246",747,193,9,5),("#1247",256,506,27,22),("#1248",250,706,25,12),("#1249",333,166,19,10),("#1250",283,633,25,29),("#1251",587,809,18,25),("#1252",109,360,15,18),("#1253",631,135,17,11),("#1254",68,476,17,16),("#1255",964,631,26,24),("#1256",880,40,18,14),("#1257",166,818,21,17),("#1258",611,872,19,19),("#1259",303,177,29,11),("#1260",189,848,24,19),("#1261",5,578,10,18),("#1262",146,116,25,14),("#1263",586,337,19,29),("#1264",151,630,27,23),("#1265",527,295,24,24),("#1266",928,230,23,10),("#1267",155,535,26,11),("#1268",536,880,25,27),("#1269",145,262,10,23),("#1270",191,364,21,29),("#1271",108,65,21,14),("#1272",843,176,19,18),("#1273",32,266,23,19),("#1274",837,699,22,10),("#1275",519,497,22,16),("#1276",408,620,10,24),("#1277",524,637,12,15),("#1278",211,715,16,18),("#1279",305,268,16,12),("#1280",788,758,18,26),("#1281",397,747,24,25),("#1282",353,188,12,11),("#1283",738,673,25,26),("#1284",284,363,10,13),("#1285",296,220,28,10),("#1286",86,523,23,18),("#1287",325,29,18,10),("#1288",629,450,22,19),("#1289",176,856,10,14),("#1290",190,413,23,11),("#1291",323,304,27,10),("#1292",969,612,27,26),("#1293",177,391,22,25),("#1294",862,423,24,24),("#1295",19,171,23,28),("#1296",769,349,23,13),("#1297",589,24,18,27),("#1298",388,209,21,16),("#1299",88,619,13,17),("#1300",723,738,27,23),("#1301",748,606,15,21),("#1302",404,2,13,16),("#1303",946,393,10,23),("#1304",290,979,29,19),("#1305",880,782,21,21),("#1306",5,273,15,13),("#1307",394,263,22,25),("#1308",135,223,25,11),("#1309",54,28,11,24),("#1310",78,614,12,26),("#1311",829,744,26,13),("#1312",656,145,17,13),("#1313",62,149,10,23),("#1314",757,532,20,13),("#1315",600,863,11,10),("#1316",862,331,20,28),("#1317",125,351,29,12),("#1318",439,626,24,23),("#1319",781,630,26,16),("#1320",195,485,26,12),("#1321",319,136,26,23),("#1322",298,478,21,10),("#1323",315,934,10,20),("#1324",138,478,28,10),("#1325",736,943,22,15),("#1326",49,695,11,16),("#1327",545,271,22,11),("#1328",491,543,28,16),("#1329",569,973,28,22),("#1330",147,192,19,28),("#1331",715,317,26,25),("#1332",145,449,19,24),("#1333",916,176,24,29),("#1334",390,654,12,24),("#1335",865,571,25,29),("#1336",412,362,20,19),("#1337",570,792,29,11),("#1338",139,467,29,13),("#1339",748,113,28,15),("#1340",591,828,27,16),("#1341",694,479,21,26),("#1342",118,362,13,18),("#1343",740,434,15,24),("#1344",686,60,5,7),("#1345",567,627,19,15),("#1346",28,280,18,10),("#1347",665,675,29,12),("#1348",103,512,16,14),("#1349",394,856,23,27),("#1350",860,365,22,23),("#1351",335,31,3,5),("#1352",773,755,10,27),("#1353",920,969,16,22),("#1354",79,854,10,28),("#1355",935,219,26,28),("#1356",562,441,12,22),("#1357",254,517,14,23),("#1358",466,521,17,17),("#1359",926,210,11,12),("#1360",208,456,28,10),("#1361",346,125,24,28),("#1362",593,968,10,20),("#1363",952,482,10,14),("#1364",706,971,24,14),("#1365",37,695,14,14),("#1366",741,831,25,27),("#1367",508,73,25,12),("#1368",212,385,22,29),("#1369",61,754,14,28),("#1370",782,52,29,21),("#1371",622,190,16,12),("#1372",209,614,21,21),("#1373",369,713,20,29)]


def numFind(n):
    count = 0
    cloth = [['.' for a in range(1000)] for b in range(1000)]
    for claim in n:
        for row in range(claim[2], claim[2] + claim[4]):
            for col in range(claim[1], claim[1] + claim[3]):
                if cloth[row][col] == ".":
                    cloth[row][col] = "#"
                elif cloth[row][col] == "#":
                    cloth[row][col] = "X"
    for sqIn in cloth:
        count += sqIn.count("X")
    return count


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(">>>>>", time.asctime(), "<<<<<\n")
    n = data
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print("\n>>>>>", time.asctime(), "<<<<<")