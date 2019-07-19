Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from threading import *
>>> class EvenNumberThread:
	def displayEvenNumbers(self):
		for i in range(0,100):
			if i%2==0:
				print(i)

	
>>> class OddNumberThread:
	def displayOddNumbers(self):
		for i in range(0,100):
			if i%2!=0:
				print(i)

				
>>> class MainThread:
	def displayNumbers(self):
		for i in range(0,100):
			print(i)

			
>>> object=EvenNumberThread()
>>> t1=Thread(target=object.displayEvenNumbers)
>>> t1.start()
>>> 0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98

>>> object=OddNumberThread()
>>> t2=Thread(target=object.displayOddNumbers)
>>> t2.start()
1
>>> 
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99

>>> object=MainThread()
>>> t3=Thread(target=object.displayNumbers)
>>> t3.start()
0
>>> 
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
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
