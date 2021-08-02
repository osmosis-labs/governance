intended_total_aps = 1000000
gauge_ids = """0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
37
38
39
43
44
45
64
65
66
124
125
126"""

aps = """10000
182720
34260
11420
16000
3000
1000
91360
17130
5710
91360
17130
5710
54880
10290
3430
54880
10290
3430
14640
2745
915
14640
2745
915
14640
2745
915
14640
2745
915
73120
13710
4570
73120
13710
4570
48000
9000
3000
48000
9000
3000"""

gauge_ids = gauge_ids.splitlines()
aps = aps.splitlines()
assert sum([int(x) for x in aps]) == intended_total_aps
gauge_string = ",".join(gauge_ids)
aps_string = ",".join(aps)
print("gauge_string: ", gauge_string)
print("aps_string: ", aps_string)