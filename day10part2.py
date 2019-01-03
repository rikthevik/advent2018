#!/usr/bin/env python3

""" https://adventofcode.com/2018/day/2 """

inputstr = """
position=<-30580, -10081> velocity=< 3,  1>
position=< 20644, -51044> velocity=<-2,  5>
position=<-51060, -40809> velocity=< 5,  4>
position=< 10386, -10077> velocity=<-1,  1>
position=< 10387, -40807> velocity=<-1,  4>
position=<-20305, -20315> velocity=< 2,  2>
position=< 51359,  20655> velocity=<-5, -2>
position=< 30860,  20655> velocity=<-3, -2>
position=< 51386,  51377> velocity=<-5, -5>
position=<-20297,  30900> velocity=< 2, -3>
position=<-10112, -30558> velocity=< 1,  3>
position=< 10427,  10414> velocity=<-1, -1>
position=<-51031,  41143> velocity=< 5, -4>
position=<-10079,  30895> velocity=< 1, -3>
position=< 30873,  20653> velocity=<-3, -2>
position=<-20315,  51378> velocity=< 2, -5>
position=<-30590,  51382> velocity=< 3, -5>
position=< 10422,  30894> velocity=<-1, -3>
position=<-30571, -51048> velocity=< 3,  5>
position=< 10414,  10411> velocity=<-1, -1>
position=<-30585,  10406> velocity=< 3, -1>
position=<-30566,  30894> velocity=< 3, -3>
position=< 41153,  10409> velocity=<-4, -1>
position=< 30868,  10411> velocity=<-3, -1>
position=< 30876, -20315> velocity=<-3,  2>
position=< 41143,  10411> velocity=<-4, -1>
position=< 10379, -10077> velocity=<-1,  1>
position=<-51066, -20320> velocity=< 5,  2>
position=<-51026,  20657> velocity=< 5, -2>
position=<-40825, -20319> velocity=< 4,  2>
position=< 51383, -51044> velocity=<-5,  5>
position=< 30864,  10406> velocity=<-3, -1>
position=<-51028, -20315> velocity=< 5,  2>
position=<-51058,  20648> velocity=< 5, -2>
position=< 20636,  41138> velocity=<-2, -4>
position=<-51033, -10081> velocity=< 5,  1>
position=<-20299, -51053> velocity=< 2,  5>
position=< 41116, -40808> velocity=<-4,  4>
position=< 41159, -40805> velocity=<-4,  4>
position=<-40824, -30563> velocity=< 4,  3>
position=< 20625, -20315> velocity=<-2,  2>
position=<-51035,  41143> velocity=< 5, -4>
position=< 41151,  30896> velocity=<-4, -3>
position=<-10107,  51382> velocity=< 1, -5>
position=<-10076,  30891> velocity=< 1, -3>
position=< 20678,  10405> velocity=<-2, -1>
position=< 51402, -20324> velocity=<-5,  2>
position=< 30902,  30894> velocity=<-3, -3>
position=<-51044,  20657> velocity=< 5, -2>
position=<-10099, -10079> velocity=< 1,  1>
position=< 41146,  30898> velocity=<-4, -3>
position=< 30892,  51384> velocity=<-3, -5>
position=<-51057,  20653> velocity=< 5, -2>
position=< 41162,  20652> velocity=<-4, -2>
position=<-10088, -10080> velocity=< 1,  1>
position=< 10425,  20652> velocity=<-1, -2>
position=<-30564,  30895> velocity=< 3, -3>
position=<-20329, -40810> velocity=< 2,  4>
position=< 41119,  30897> velocity=<-4, -3>
position=<-40825, -20317> velocity=< 4,  2>
position=< 41162,  30895> velocity=<-4, -3>
position=<-40813,  10405> velocity=< 4, -1>
position=<-30537,  30900> velocity=< 3, -3>
position=<-20299,  30897> velocity=< 2, -3>
position=< 20661, -30559> velocity=<-2,  3>
position=<-20339, -20317> velocity=< 2,  2>
position=<-30558, -51052> velocity=< 3,  5>
position=< 51349,  51377> velocity=<-5, -5>
position=<-30598, -40807> velocity=< 3,  4>
position=< 41151,  51377> velocity=<-4, -5>
position=<-40798, -30565> velocity=< 4,  3>
position=<-51082,  10410> velocity=< 5, -1>
position=<-51082,  41134> velocity=< 5, -4>
position=<-30593,  30893> velocity=< 3, -3>
position=<-10099, -20321> velocity=< 1,  2>
position=<-51028, -40807> velocity=< 5,  4>
position=<-40793,  41143> velocity=< 4, -4>
position=<-10104, -30565> velocity=< 1,  3>
position=< 51348,  41134> velocity=<-5, -4>
position=<-20318, -40808> velocity=< 2,  4>
position=<-30550, -30564> velocity=< 3,  3>
position=< 10406,  20657> velocity=<-1, -2>
position=<-30582,  51386> velocity=< 3, -5>
position=< 20652,  30891> velocity=<-2, -3>
position=< 51396,  51381> velocity=<-5, -5>
position=< 10382, -30560> velocity=<-1,  3>
position=< 20642, -10072> velocity=<-2,  1>
position=< 51398, -30567> velocity=<-5,  3>
position=< 30873, -51052> velocity=<-3,  5>
position=< 20646, -51048> velocity=<-2,  5>
position=< 10403, -30559> velocity=<-1,  3>
position=<-30593, -30564> velocity=< 3,  3>
position=<-51044, -40803> velocity=< 5,  4>
position=<-10078, -30563> velocity=< 1,  3>
position=<-40840, -40805> velocity=< 4,  4>
position=< 51375, -30562> velocity=<-5,  3>
position=<-20355, -40806> velocity=< 2,  4>
position=<-40793, -51053> velocity=< 4,  5>
position=<-30545,  51386> velocity=< 3, -5>
position=< 41163,  30900> velocity=<-4, -3>
position=< 51379,  41138> velocity=<-5, -4>
position=< 10392, -51053> velocity=<-1,  5>
position=<-10051,  51386> velocity=< 1, -5>
position=<-10056,  30894> velocity=< 1, -3>
position=<-40832, -40806> velocity=< 4,  4>
position=<-10055,  30900> velocity=< 1, -3>
position=< 30884,  30895> velocity=<-3, -3>
position=<-20339,  30895> velocity=< 2, -3>
position=<-40804, -30564> velocity=< 4,  3>
position=<-51047, -40807> velocity=< 5,  4>
position=<-51071, -10075> velocity=< 5,  1>
position=< 10414, -10074> velocity=<-1,  1>
position=< 30892,  10407> velocity=<-3, -1>
position=< 51402, -30565> velocity=<-5,  3>
position=<-40840, -30566> velocity=< 4,  3>
position=< 10403, -51047> velocity=<-1,  5>
position=<-10093, -30563> velocity=< 1,  3>
position=< 10390, -20319> velocity=<-1,  2>
position=< 10385,  51381> velocity=<-1, -5>
position=< 41119,  41141> velocity=<-4, -4>
position=< 30868,  41141> velocity=<-3, -4>
position=<-10099, -20320> velocity=< 1,  2>
position=<-20315,  10408> velocity=< 2, -1>
position=< 30893, -51049> velocity=<-3,  5>
position=<-10112,  41138> velocity=< 1, -4>
position=<-20307, -20317> velocity=< 2,  2>
position=<-51081,  20648> velocity=< 5, -2>
position=<-40781,  51377> velocity=< 4, -5>
position=< 41152,  41138> velocity=<-4, -4>
position=<-51036, -40808> velocity=< 5,  4>
position=< 41130, -20324> velocity=<-4,  2>
position=< 51351, -20319> velocity=<-5,  2>
position=< 41111, -51053> velocity=<-4,  5>
position=< 30860,  10408> velocity=<-3, -1>
position=< 10400, -30567> velocity=<-1,  3>
position=<-20354, -30566> velocity=< 2,  3>
position=<-30590, -20315> velocity=< 3,  2>
position=<-51056, -40810> velocity=< 5,  4>
position=<-30594, -30566> velocity=< 3,  3>
position=< 20674,  30891> velocity=<-2, -3>
position=<-40801, -20315> velocity=< 4,  2>
position=<-51055, -10073> velocity=< 5,  1>
position=< 51359,  51385> velocity=<-5, -5>
position=< 41111,  30894> velocity=<-4, -3>
position=<-51071,  41134> velocity=< 5, -4>
position=<-51042,  10408> velocity=< 5, -1>
position=< 10390,  20656> velocity=<-1, -2>
position=< 51351,  41143> velocity=<-5, -4>
position=< 41135, -10073> velocity=<-4,  1>
position=< 20654,  41135> velocity=<-2, -4>
position=< 30880,  20652> velocity=<-3, -2>
position=< 30916, -30558> velocity=<-3,  3>
position=< 10422,  30897> velocity=<-1, -3>
position=< 30901,  20653> velocity=<-3, -2>
position=< 10433, -20315> velocity=<-1,  2>
position=< 30889, -20318> velocity=<-3,  2>
position=< 51378, -20316> velocity=<-5,  2>
position=<-30593,  20657> velocity=< 3, -2>
position=<-10096, -30558> velocity=< 1,  3>
position=< 20675,  51386> velocity=<-2, -5>
position=<-10071, -40805> velocity=< 1,  4>
position=< 51403, -20315> velocity=<-5,  2>
position=<-40824,  30895> velocity=< 4, -3>
position=< 51406,  41134> velocity=<-5, -4>
position=<-51083, -40809> velocity=< 5,  4>
position=<-30569, -51048> velocity=< 3,  5>
position=<-20331, -10076> velocity=< 2,  1>
position=<-20342, -10079> velocity=< 2,  1>
position=< 10417, -30560> velocity=<-1,  3>
position=< 41139,  30891> velocity=<-4, -3>
position=<-20342,  41139> velocity=< 2, -4>
position=< 51383,  30899> velocity=<-5, -3>
position=< 41135, -10081> velocity=<-4,  1>
position=<-20331, -40803> velocity=< 2,  4>
position=< 51363,  10405> velocity=<-5, -1>
position=< 51398, -40801> velocity=<-5,  4>
position=< 10425, -10072> velocity=<-1,  1>
position=< 41161,  10409> velocity=<-4, -1>
position=<-30590,  41142> velocity=< 3, -4>
position=<-20339, -10081> velocity=< 2,  1>
position=<-10112, -40803> velocity=< 1,  4>
position=< 20638,  10405> velocity=<-2, -1>
position=< 51354, -20321> velocity=<-5,  2>
position=< 20675, -30563> velocity=<-2,  3>
position=< 10374, -51049> velocity=<-1,  5>
position=<-10056,  20655> velocity=< 1, -2>
position=< 20661, -40809> velocity=<-2,  4>
position=< 41119,  41139> velocity=<-4, -4>
position=< 10377, -40805> velocity=<-1,  4>
position=< 51351,  20651> velocity=<-5, -2>
position=<-40825,  30892> velocity=< 4, -3>
position=<-10064, -30567> velocity=< 1,  3>
position=<-30589,  20652> velocity=< 3, -2>
position=<-51047,  20649> velocity=< 5, -2>
position=<-40782,  10414> velocity=< 4, -1>
position=<-10080,  41140> velocity=< 1, -4>
position=< 51354,  51385> velocity=<-5, -5>
position=< 30902,  10411> velocity=<-3, -1>
position=< 30909, -30567> velocity=<-3,  3>
position=< 20646,  30900> velocity=<-2, -3>
position=<-40793,  20656> velocity=< 4, -2>
position=<-10084, -20316> velocity=< 1,  2>
position=<-51082, -40805> velocity=< 5,  4>
position=<-10064,  10406> velocity=< 1, -1>
position=< 41155, -30563> velocity=<-4,  3>
position=< 10414,  10406> velocity=<-1, -1>
position=<-10051, -51044> velocity=< 1,  5>
position=< 41127, -51048> velocity=<-4,  5>
position=<-40809, -51052> velocity=< 4,  5>
position=<-40836, -10074> velocity=< 4,  1>
position=< 30864,  41139> velocity=<-3, -4>
position=<-10055,  30891> velocity=< 1, -3>
position=< 41151, -51044> velocity=<-4,  5>
position=<-20323, -51047> velocity=< 2,  5>
position=< 30918, -30567> velocity=<-3,  3>
position=<-20323, -51049> velocity=< 2,  5>
position=< 20636, -40806> velocity=<-2,  4>
position=< 41122, -20324> velocity=<-4,  2>
position=< 10422, -51051> velocity=<-1,  5>
position=< 10402, -40802> velocity=<-1,  4>
position=< 51362, -30567> velocity=<-5,  3>
position=<-40792,  41143> velocity=< 4, -4>
position=< 51366,  10405> velocity=<-5, -1>
position=< 20666,  41134> velocity=<-2, -4>
position=<-10080,  30898> velocity=< 1, -3>
position=<-40781, -20324> velocity=< 4,  2>
position=<-30580, -10081> velocity=< 3,  1>
position=< 20641, -40803> velocity=<-2,  4>
position=< 10382,  30895> velocity=<-1, -3>
position=< 30902, -20318> velocity=<-3,  2>
position=<-51082, -10076> velocity=< 5,  1>
position=<-51076,  51382> velocity=< 5, -5>
position=< 51386, -30567> velocity=<-5,  3>
position=< 30873, -10081> velocity=<-3,  1>
position=<-40825,  10411> velocity=< 4, -1>
position=<-20354,  51382> velocity=< 2, -5>
position=< 41152, -30563> velocity=<-4,  3>
position=<-20318,  20657> velocity=< 2, -2>
position=< 30892,  20652> velocity=<-3, -2>
position=< 30889,  20655> velocity=<-3, -2>
position=< 51346, -20322> velocity=<-5,  2>
position=<-10062, -10081> velocity=< 1,  1>
position=<-20329,  20657> velocity=< 2, -2>
position=< 30887,  20657> velocity=<-3, -2>
position=< 30903, -20322> velocity=<-3,  2>
position=<-30571,  30896> velocity=< 3, -3>
position=<-40839, -40810> velocity=< 4,  4>
position=<-10075,  10413> velocity=< 1, -1>
position=< 51386, -30564> velocity=<-5,  3>
position=<-10064, -51044> velocity=< 1,  5>
position=<-10088,  51382> velocity=< 1, -5>
position=< 10374,  51382> velocity=<-1, -5>
position=< 51351,  51385> velocity=<-5, -5>
position=< 51350,  41135> velocity=<-5, -4>
position=< 30880,  30891> velocity=<-3, -3>
position=<-30561, -40801> velocity=< 3,  4>
position=<-20323, -20318> velocity=< 2,  2>
position=<-40793, -51046> velocity=< 4,  5>
position=<-40785,  30899> velocity=< 4, -3>
position=< 51386,  41136> velocity=<-5, -4>
position=<-10103,  30895> velocity=< 1, -3>
position=<-10104,  51384> velocity=< 1, -5>
position=< 30892, -30566> velocity=<-3,  3>
position=<-30566, -40810> velocity=< 3,  4>
position=<-20307,  51384> velocity=< 2, -5>
position=<-10061, -51049> velocity=< 1,  5>
position=<-51084, -30562> velocity=< 5,  3>
position=< 51359,  20655> velocity=<-5, -2>
position=<-51071, -51046> velocity=< 5,  5>
position=<-10107, -20315> velocity=< 1,  2>
position=<-51079,  20651> velocity=< 5, -2>
position=<-30550, -20322> velocity=< 3,  2>
position=< 30897, -20322> velocity=<-3,  2>
position=<-10062,  51377> velocity=< 1, -5>
position=<-20319, -20317> velocity=< 2,  2>
position=< 10403, -30566> velocity=<-1,  3>
position=< 30916, -30563> velocity=<-3,  3>
position=<-40809,  41136> velocity=< 4, -4>
position=<-51028, -20316> velocity=< 5,  2>
position=<-10088, -20316> velocity=< 1,  2>
position=<-20307,  41139> velocity=< 2, -4>
position=< 51381, -40806> velocity=<-5,  4>
position=<-51034, -10072> velocity=< 5,  1>
position=<-51043,  41138> velocity=< 5, -4>
position=<-40817,  20655> velocity=< 4, -2>
position=< 20673, -30562> velocity=<-2,  3>
position=<-10091, -40810> velocity=< 1,  4>
position=<-51072,  20652> velocity=< 5, -2>
position=< 30909,  41143> velocity=<-3, -4>
position=< 20649,  10406> velocity=<-2, -1>
position=<-10080,  30895> velocity=< 1, -3>
position=< 41151, -30561> velocity=<-4,  3>
position=<-10107, -10076> velocity=< 1,  1>
position=<-10096, -20322> velocity=< 1,  2>
position=<-30542,  41138> velocity=< 3, -4>
position=<-30553, -10072> velocity=< 3,  1>
position=< 30897, -10080> velocity=<-3,  1>
position=< 20662,  41134> velocity=<-2, -4>
position=<-51074,  20652> velocity=< 5, -2>
position=< 20667, -10081> velocity=<-2,  1>
position=< 51387, -10077> velocity=<-5,  1>
position=< 41148, -51053> velocity=<-4,  5>
position=<-40841,  41140> velocity=< 4, -4>
position=<-40784, -10081> velocity=< 4,  1>
position=<-20347, -40802> velocity=< 2,  4>
position=< 30900, -10081> velocity=<-3,  1>
position=< 51375,  10413> velocity=<-5, -1>
position=<-51050,  51377> velocity=< 5, -5>
position=<-51042, -10078> velocity=< 5,  1>
position=<-30585,  20649> velocity=< 3, -2>
position=<-51044, -30562> velocity=< 5,  3>
position=<-30542,  30899> velocity=< 3, -3>
position=<-30558, -40805> velocity=< 3,  4>
position=<-51044, -30559> velocity=< 5,  3>
position=< 41155,  51381> velocity=<-4, -5>
position=< 41155, -10077> velocity=<-4,  1>
position=<-40798,  51384> velocity=< 4, -5>
position=< 51399, -40810> velocity=<-5,  4>
position=<-10068, -30566> velocity=< 1,  3>
position=< 10431,  20657> velocity=<-1, -2>
position=<-10088,  20651> velocity=< 1, -2>
position=< 20676, -20324> velocity=<-2,  2>
position=< 30908,  20656> velocity=<-3, -2>
position=<-51027, -30563> velocity=< 5,  3>
position=<-40817,  41135> velocity=< 4, -4>
position=< 30889,  10406> velocity=<-3, -1>
position=<-20310, -30567> velocity=< 2,  3>
position=< 20630, -30564> velocity=<-2,  3>
position=< 30917, -10077> velocity=<-3,  1>
position=<-10075, -20321> velocity=< 1,  2>
position=<-51027,  20652> velocity=< 5, -2>
position=<-51064, -40806> velocity=< 5,  4>
position=< 51382,  10411> velocity=<-5, -1>
position=<-40813, -20319> velocity=< 4,  2>
position=< 10387, -20320> velocity=<-1,  2>
position=< 41143,  30895> velocity=<-4, -3>
position=< 30919,  51381> velocity=<-3, -5>
position=< 41151,  10406> velocity=<-4, -1>
position=<-51079,  10411> velocity=< 5, -1>
position=<-20307, -51045> velocity=< 2,  5>
position=<-30550, -51049> velocity=< 3,  5>
position=< 20657,  30893> velocity=<-2, -3>
position=<-40828,  51386> velocity=< 4, -5>
position=< 20649,  41139> velocity=<-2, -4>
position=<-30542,  30892> velocity=< 3, -3>
position=<-10053, -51044> velocity=< 1,  5>
position=< 41121,  30895> velocity=<-4, -3>
position=< 20642, -51053> velocity=<-2,  5>
position=< 30900,  10407> velocity=<-3, -1>
position=< 41111,  41136> velocity=<-4, -4>
position=< 10422,  10408> velocity=<-1, -1>
position=< 51391, -51044> velocity=<-5,  5>
position=<-20352, -51048> velocity=< 2,  5>
position=< 51367, -20324> velocity=<-5,  2>
position=< 41135,  20657> velocity=<-4, -2>
position=< 41159, -20321> velocity=<-4,  2>
position=< 20652,  51382> velocity=<-2, -5>
position=<-51055, -30558> velocity=< 5,  3>
position=< 51346,  30894> velocity=<-5, -3>
position=<-30562,  41138> velocity=< 3, -4>
position=<-51084,  30897> velocity=< 5, -3>
position=<-20339, -20324> velocity=< 2,  2>
position=< 51382, -40810> velocity=<-5,  4>
position=<-10112, -51046> velocity=< 1,  5>
position=< 30884, -10077> velocity=<-3,  1>
position=<-40785,  30891> velocity=< 4, -3>
position=<-20315,  10412> velocity=< 2, -1>
position=<-30590,  30892> velocity=< 3, -3>
position=<-10072,  41143> velocity=< 1, -4>
position=< 51362,  41137> velocity=<-5, -4>
position=<-10052,  30895> velocity=< 1, -3>
position=< 10424, -51049> velocity=<-1,  5>
position=<-30574,  10411> velocity=< 3, -1>
position=< 30878, -40806> velocity=<-3,  4>
position=< 30920,  51386> velocity=<-3, -5>
position=<-30582, -10078> velocity=< 3,  1>
position=< 51370,  41142> velocity=<-5, -4>
position=<-10099, -30567> velocity=< 1,  3>
position=< 30916,  41135> velocity=<-3, -4>
position=< 30884, -30565> velocity=<-3,  3>
position=< 10423, -51053> velocity=<-1,  5>
position=<-30572,  30900> velocity=< 3, -3>
position=< 30893, -51053> velocity=<-3,  5>
position=<-30582,  51383> velocity=< 3, -5>
position=<-20355, -30559> velocity=< 2,  3>
position=< 10417, -20322> velocity=<-1,  2>
position=< 10422,  41135> velocity=<-1, -4>
position=< 20630, -10076> velocity=<-2,  1>
position=<-51057, -51053> velocity=< 5,  5>
position=< 41163,  10414> velocity=<-4, -1>
"""

import json, re, collections, itertools, os

def display(positions):
    for row, points in itertools.groupby(sorted(positions, key=lambda p: (p.y, p.x)), key=lambda p: p.y):
        print(list(points)) 


def main():
    positions = []
    velocities = []
    f = open("part10.html", "w")
    for l in inputstr.strip().splitlines():
        left, right = l.split("> velocity=<")
        pos = [ int(s.strip()) for s in left[10:].split(",") ]
        vel = [ int(s.strip()) for s in right[:-1].split(",") ]
        positions.append(pos)
        velocities.append(vel)
    
    horiz_values = [ p[0] for p in positions ]
    horiz_offset = min(horiz_values)
    total_width = max(horiz_values) - min(horiz_values)
    horiz_scale = 800.0 / total_width * 0.5

    vert_values = [ p[1] for p in positions ]
    vert_offset = min(vert_values)
    total_height = max(vert_values) - min(vert_values)
    vert_scale = 800.0 / total_height * 0.5

    for p in positions:
        p[0] = (p[0] - horiz_offset) * horiz_scale
        p[1] = (p[1] - vert_offset) * vert_scale

    for p in velocities:
        p[0] *= horiz_scale
        p[1] *= vert_scale

    info = {}

    print("width", total_width, "height", total_height)


    print('''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Canvas tutorial</title>
    <script type="text/javascript">
      var ctx;
      var positions = %s;
      var velocities = %s;
      var info = %s;
      function draw() {
        var canvas = document.getElementById('tutorial');
        ctx = canvas.getContext('2d');
        alert('hello');
        drawPositions();
        setInterval(loop, 100);
      }
      function loop() {
        console.log("looping");
        move();
        drawPositions();
      }
      function move() {
        for (var i=0; i < positions.length; ++i) {
            positions[i][0] += velocities[i][0] * 120;
            positions[i][1] += velocities[i][1] * 120;
        }
      }
      function drawPositions() {
        ctx.clearRect(0, 0, 800, 800);
        for (var i=0; i < positions.length; ++i) {
          ctx.fillRect(positions[i][0], positions[i][1], 2, 2);
        }
      }
    </script>
    <style type="text/css">
      canvas { border: 1px solid black; }
    </style>
  </head>
  <body onload="draw();">
    <canvas id="tutorial" width="400" height="400"></canvas>
  </body>
</html>
''' % (json.dumps(positions), json.dumps(velocities), json.dumps(info)), file=f)
    os.system("open part10.html")






if __name__ == '__main__':
    main()
