q1= """1. Which type of Programming does Python support?
a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned"""
q2="""2. Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom?"""

q3="""Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned"""

q4="""4. Which of the following is the correct extension of the Python file?
a) .python
b) .pl
c) .py
d) .p"""
q5="""5. Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted"""
questions={q1:"d",q2:"c",q3:"b",q4:"c",q5:"a"}
name=input("enter your name")
print("Hello",name,"welcome to python quiz world")
score=0
for i in questions:
    print(i)
    ans=input("enter any answer a/b/c/d:")
    if ans==questions[i]:
        print("right answer, you got 5 point")
        score=score+1
    else:
        print("worng answer, you got 0 point")
        score=score-1
print("final score is:",score)
