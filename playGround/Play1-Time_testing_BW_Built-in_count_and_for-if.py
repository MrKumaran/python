# conclusion foe this inbuilt count is faster than for loop
import time as t

listOne = [22, 41, 39, 88, 100, 39, 58, 45, 87, 60, 92, 70, 92, 60, 18,
51, 38, 42, 93, 69, 21, 8, 84, 37, 22, 63, 12, 81, 54, 63, 91, 54, 39, 37, 60, 39, 15, 35, 10, 69, 75, 94, 79, 49, 2,
100, 49, 50, 67, 59, 8, 56, 60, 39, 6, 89, 1, 63, 29, 41, 80, 37, 33, 7, 45, 95, 72, 96, 91, 13, 61, 29, 44, 3, 94,
56, 46, 24, 44, 33, 13, 1, 77, 70, 37, 60, 90, 7, 66, 66, 82, 98, 56, 39, 12, 91, 24, 73, 47, 87, 89, 15, 95, 81, 79,
28, 19, 27, 26, 2, 54, 87, 2, 29, 9, 73, 85, 31, 94, 9, 18, 80, 27, 71, 97, 47, 68, 30, 10, 90, 71, 56, 24, 21, 1,
100, 4, 88, 41, 15, 11, 21, 64, 2, 3, 75, 7, 16, 43, 45, 15, 62, 89, 47, 11, 84, 97, 15, 32, 7, 81, 93, 67, 33, 99,
32, 47, 87, 53, 90, 93, 9, 24, 57, 44, 82, 14, 49, 93, 9, 36, 27, 8, 25, 34, 23, 41, 48, 100, 58, 68, 43, 34, 23, 52,
53, 8, 11, 30, 87, 77, 44, 29, 85, 47, 76, 65, 82, 51, 83, 76, 86, 38, 68, 47, 23, 69, 8, 10, 98, 67, 77, 34, 2, 66,
65, 16, 8, 11, 9, 46, 34, 46, 48, 45, 69, 10, 45, 10, 43, 55, 97, 52, 15, 19, 24, 64, 94, 9, 14, 4, 72, 88, 93, 86,
58, 48, 48, 59, 18, 68, 86, 46, 1, 41, 26, 4, 29, 79, 85, 71, 61, 8, 76, 40, 22, 12, 50, 14, 39, 99, 73, 18, 46, 29,
55, 69, 10, 27, 23, 82, 20, 88, 69, 48, 37, 18, 19, 55, 84, 64, 4, 23, 80, 21, 54, 69, 73, 49, 44, 58, 88, 93, 5, 89,
68, 32, 13, 74, 7, 81, 90, 28, 98, 17, 76, 28, 70, 17, 18, 83, 77, 8, 97, 36, 94, 5, 8, 88, 6, 68, 19, 94, 3, 68, 18,
69, 32, 70, 51, 18, 100, 9, 50, 73, 74, 8, 6, 10, 24, 28, 81, 31, 77, 78, 17, 92, 98, 76, 74, 98, 42, 33, 83, 68, 45,
1, 65, 76, 27, 81, 70, 70, 79, 65, 3, 99, 45, 67, 80, 47, 56, 37, 94, 82, 73, 36, 8, 16, 95, 44, 35, 33, 43, 55, 100,
91, 77, 82, 28, 9, 45, 18, 81, 58, 61, 81, 65, 46, 16, 73, 12, 10, 31, 66, 94, 100, 11, 59, 21, 62, 94, 2, 27, 60,
85, 30, 23, 39, 44, 55, 1, 24, 22, 26, 5, 13, 50, 42, 96, 91, 3, 59, 21, 68, 33, 48, 33, 34, 2, 22, 47, 32, 14, 43,
90, 82, 56, 52, 99, 24, 9, 33, 33, 56, 28, 1, 30, 62, 14, 55, 18, 69, 11, 35, 100, 26, 60, 7, 54, 5, 71, 78, 46, 31,
61, 26, 19, 74, 6, 20, 59, 53, 28, 39, 77, 100, 76, 7, 5, 79, 57, 87, 92, 13, 36, 37, 34, 65, 54, 56, 82, 64, 11, 36,
63, 11, 2, 12, 45, 32, 62, 13, 52, 49, 40, 20, 39, 87, 77, 74, 30, 26, 77, 52, 66, 62, 83, 15, 73, 75, 19, 92, 7, 59,
37, 15, 47, 54, 55, 36, 70, 98, 45, 21, 87, 4, 8, 92, 63, 2, 97, 35, 41, 91, 74, 92, 7, 41, 48, 13, 51, 95, 21, 67,
11, 30, 80, 51, 53, 10, 92, 64, 52, 49, 1, 27, 98, 84, 37, 99, 65, 87, 99, 66, 1, 85, 95, 16, 28, 81, 65, 9, 12, 56,
2, 17, 91, 64, 52, 3, 33, 48, 72, 34, 84, 9, 4, 74, 40, 75, 42, 77, 64, 43, 11, 14, 16, 90, 66, 76, 22, 38, 92, 97,
64, 21, 32, 53, 57, 56, 90, 70, 88, 69, 38, 79, 57, 80, 48, 67, 74, 45, 47, 9, 49, 16, 75, 27, 99, 11, 64, 47, 8, 6,
17, 73, 22, 48, 6, 95, 32, 85, 92, 9, 33, 15, 35, 59, 20, 81, 65, 90, 57, 24, 90, 95, 90, 61, 48, 71, 46, 72, 4, 17,
21, 48, 82, 68, 34, 72, 4, 57, 59, 34, 22, 18, 23, 78, 92, 34, 12, 10, 39, 48, 58, 85, 53, 64, 33, 50, 100, 11, 51,
40, 60, 11, 85, 50, 68, 85, 65, 98, 15, 23, 5, 18, 24, 59, 22, 80, 9, 19, 68, 47, 20, 95, 88, 49, 91, 56, 91, 18, 90,
94, 31, 27, 71, 14, 71, 83, 61, 97, 37, 76, 77, 25, 52, 79, 58, 58, 19, 17, 12, 25, 87, 58, 61, 98, 13, 31, 4, 55, 5,
75, 2, 83, 63, 94, 35, 62, 98, 20, 6, 89, 78, 81, 79, 6, 47, 39, 90, 1, 18, 51, 91, 42, 95, 93, 55, 31, 7, 22, 97,
63, 92, 28, 89, 71, 36, 96, 42, 64, 18, 88, 77, 51, 56, 51, 23, 58, 50, 47, 33, 93, 93, 15, 81, 30, 81, 85, 70, 88,
100, 49, 79, 52, 37, 54, 28, 92, 46, 86, 86, 93, 20, 31, 26, 16, 34, 92, 62, 58, 10, 10, 100, 54, 95, 39, 78, 60, 67,
8, 94, 29, 23, 5, 49, 75, 66, 31, 51, 41, 64, 77, 40, 52, 40, 23, 33, 86, 100, 80, 56, 59, 44, 79, 56, 6, 21, 9, 6,
24, 18, 68, 3, 82, 74, 93, 52, 8, 85, 73, 80, 80, 75, 51, 72, 15, 56, 80, 85, 2, 26, 53, 68, 74, 60, 51, 11, 40, 67,
60, 75, 49, 28, 34, 14, 95, 73, 14, 26, 11, 37, 20, 78, 1, 27, 60, 4, 54, 57, 53, 58, 62, 14, 65, 51, 9, 59, 99, 18,
53, 93, 36, 86, 98, 5, 72, 52, 41, 77, 60, 98, 22, 4, 35, 17, 9, 43, 68, 4, 74, 32, 64, 25, 10, 65, 22, 41, 39, 88,
100, 39, 58, 45, 87, 60, 92, 70, 92, 60, 18, 6, 82, 51, 38, 42, 93, 69, 21, 8, 84, 37, 22, 63, 12, 81, 54, 63, 91,
54, 39, 37, 60, 39, 15, 35, 10, 69, 75, 94, 79, 49, 2, 100, 49, 50, 67, 59, 8, 56, 60, 39, 6, 89, 1, 63, 29, 41, 80,
37, 33, 7, 45, 95, 72, 96, 91, 13, 61, 29, 44, 3, 94, 56, 46, 24, 44, 33, 13, 1, 77, 70, 37, 60, 90, 7, 66, 66, 82,
98, 56, 39, 12, 91, 24, 73, 47, 87, 89, 15, 95, 81, 79, 28, 19, 27, 26, 2, 54, 87, 2, 29, 9, 73, 85, 31, 94, 9, 18,
80, 27, 71, 97, 47, 68, 30, 10, 90, 71, 56, 24, 21, 1, 100, 4, 88, 41, 15, 11, 21, 64, 2, 3, 75, 7, 16, 43, 45, 15,
62, 89, 47, 11, 84, 97, 15, 32, 7, 81, 93, 67, 33, 99, 32, 47, 87, 53, 90, 93, 9, 24, 57, 44, 82, 14, 49, 93, 9, 36,
27, 8, 25, 34, 23, 41, 48, 100, 58, 68, 43, 34, 23, 52, 53, 8, 11, 30, 87, 77, 44, 29, 85, 47, 76, 65, 82, 51, 83,
76, 86, 38, 68, 47, 23, 69, 8, 10, 98, 67, 77, 34, 2, 66, 65, 16, 8, 11, 9, 46, 34, 46, 48, 45, 69, 10, 45, 10, 43,
55, 97, 52, 15, 19, 24, 64, 94, 9, 14, 4, 72, 88, 93, 86, 58, 48, 48, 59, 18, 68, 86, 46, 1, 41, 26, 4, 29, 79, 85,
71, 61, 8, 76, 40, 22, 12, 50, 14, 39, 99, 73, 18, 46, 29, 55, 69, 10, 27, 23, 82, 20, 88, 69, 48, 37, 18, 19, 55,
84, 64, 4, 23, 80, 21, 54, 69, 73, 49, 44, 58, 88, 93, 5, 89, 68, 32, 13, 74, 7, 81, 90, 28, 98, 17, 76, 28, 70, 17,
18, 83, 77, 8, 97, 36, 94, 5, 8, 88, 6, 68, 19, 94, 3, 68, 18, 69, 32, 70, 51, 18, 100, 9, 50, 73, 74, 8, 6, 10, 24,
28, 81, 31, 77, 78, 17, 92, 98, 76, 74, 98, 42, 33, 83, 68, 45, 1, 65, 76, 27, 81, 70, 70, 79, 65, 3, 99, 45, 67, 80,
47, 56, 37, 94, 82, 73, 36, 8, 16, 95, 44, 35, 33, 43, 55, 100, 91, 77, 82, 28, 9, 45, 18, 81, 58, 61, 81, 65, 46,
16, 73, 12, 10, 31, 66, 94, 100, 11, 59, 21, 62, 94, 2, 27, 60, 85, 30, 23, 39, 44, 55, 1, 24, 22, 26, 5, 13, 50, 42,
96, 91, 3, 59, 21, 68, 33, 48, 33, 34, 2, 22, 47, 32, 14, 43, 90, 82, 56, 52, 99, 24, 9, 33, 33, 56, 28, 1, 30, 62,
14, 55, 18, 69, 11, 35, 100, 26, 60, 7, 54, 5, 71, 78, 46, 31, 61, 26, 19, 74, 6, 20, 59, 53, 28, 39, 77, 100, 76, 7,
5, 79, 57, 87, 92, 13, 36, 37, 34, 65, 54, 56, 82, 64, 11, 36, 63, 11, 2, 12, 45, 32, 62, 13, 52, 49, 40, 20, 39, 87,
77, 74, 30, 26, 77, 52, 66, 62, 83, 15, 73, 75, 19, 92, 7, 59, 37, 15, 47, 54, 55, 36, 70, 98, 45, 21, 87, 4, 8, 92,
63, 2, 97, 35, 41, 91, 74, 92, 7, 41, 48, 13, 51, 95, 21, 67, 11, 30, 80, 51, 53, 10, 92, 64, 52, 49, 1, 27, 98, 84,
37, 99, 65, 87, 99, 66, 1, 85, 95, 16, 28, 81, 65, 9, 12, 56, 2, 17, 91, 64, 52, 3, 33, 48, 72, 34, 84, 9, 4, 74, 40,
75, 42, 77, 64, 43, 11, 14, 16, 90, 66, 76, 22, 38, 92, 97, 64, 21, 32, 53, 57, 56, 90, 70, 88, 69, 38, 79, 57, 80,
48, 67, 74, 45, 47, 9, 49, 16, 75, 27, 99, 11, 64, 47, 8, 6, 17, 73, 22, 48, 6, 95, 32, 85, 92, 9, 33, 15, 35, 59,
20, 81, 65, 90, 57, 24, 90, 95, 90, 61, 48, 71, 46, 72, 4, 17, 21, 48, 82, 68, 34, 72, 4, 57, 59, 34, 22, 18, 23, 78,
92, 34, 12, 10, 39, 48, 58, 85, 53, 64, 33, 50, 100, 11, 51, 40, 60, 11, 85, 50, 68, 85, 65, 98, 15, 23, 5, 18, 24,
59, 22, 80, 9, 19, 68, 47, 20, 95, 88, 49, 91, 56, 91, 18, 90, 94, 31, 27, 71, 14, 71, 83, 61, 97, 37, 76, 77, 25,
52, 79, 58, 58, 19, 17, 12, 25, 87, 58, 61, 98, 13, 31, 4, 55, 5, 75, 2, 83, 63, 94, 35, 62, 98, 20, 6, 89, 78, 81,
79, 6, 47, 39, 90, 1, 18, 51, 91, 42, 95, 93, 55, 31, 7, 22, 97, 63, 92, 28, 89, 71, 36, 96, 42, 64, 18, 88, 77, 51,
56, 51, 23, 58, 50, 47, 33, 93, 93, 15, 81, 30, 81, 85, 70, 88, 100, 49, 79, 52, 37, 54, 28, 92, 46, 86, 86, 93, 20,
31, 26, 16, 34, 92, 62, 58, 10, 10, 100, 54, 95, 39, 78, 60, 67, 8, 94, 29, 23, 5, 49, 75, 66, 31, 51, 41, 64, 77,
40, 52, 40, 23, 33, 86, 100, 80, 56, 59, 44, 79, 56, 6, 21, 9, 6, 24, 18, 68, 3, 82, 74, 93, 52, 8, 85, 73, 80, 80,
75, 51, 72, 15, 56, 80, 85, 2, 26, 53, 68, 74, 60, 51, 11, 40, 67, 60, 75, 49, 28, 34, 14, 95, 73, 14, 26, 11, 37,
20, 78, 1, 27, 60, 4, 54, 57, 53, 58, 62, 14, 65, 51, 9, 59, 99, 18, 53, 93, 36, 86, 98, 5, 72, 52, 41, 77, 60, 98,
22, 4, 35, 17, 9, 43, 68, 4, 74, 32, 64, 25, 10, 65]

start = t.time()
print(listOne.count(69))
stop =t.time()
print(stop-start)
start = t.time()
count = 0
for i in listOne:
    if i == 69:
        count =  count + 1
print(count)
stop =t.time()
print(stop-start)