from collections import namedtuple
n,Students,marks=int(input()),namedtuple("Student",input()),0
for i in range(n):
        marks+=int(Students(*input().split()).MARKS)
print(marks/n)