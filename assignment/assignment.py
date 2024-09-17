# #1.Dictionary
print("\n--------------------------------------------")
print("|         -Solution of Dictionary-         |")
print("--------------------------------------------")
courses = {
    "CSE101":{
        "course name":"Introduction to Programming",
        "credits":3,
        "instructor":"Dr.Alice"
    },
    "CSE102":{
        "course name":"Data Structures",
        "credits":4,
        "instructor":"Dr.Bob"
    },
    "CSE103":{
        "course name":"Database Systems",
        "credits":3,
        "instructor":"Dr.Carol"
    }
}
print("The Original Data Set")
for key,value in courses.items():
    print(f"Course: {key}")
    for innerKey,innerValue in courses[key].items():
        print(f"{innerKey}: {innerValue}")
    print("-----------------\n")
#print(courses)
# courses.update([1][2],"Dr.Bob Jr.")
courses["CSE102"]["instructor"] = "Dr.Bob Jr."
for key,value in courses.items():
    if(key == "CSE102"):
        for innerKey in courses[key].keys():
            if(innerKey == "instructor"):
                courses[key][innerKey] = "Dr.Bob Jr."
print("After updadting the instructor's name for CSE102 to Dr. Bob Jr.")
for key,value in courses.items():
    print(f"Course: {key}")
    for innerKey,innerValue in courses[key].items():
        print(f"{innerKey}: {innerValue}")
    print("-----------------\n")
#print(courses)
print("After adding new course: CSE104")
courses["CSE104"] = {
    "course name" : "Algorithms",
    "credits":4,
    "instructor":"Dr.Dave"
}
for key,value in courses.items():
    print(f"Course: {key}")
    for innerKey,innerValue in courses[key].items():
        print(f"{innerKey}: {innerValue}")
    print("-----------------\n")

courses.pop("CSE101")
print("After deleting  course: CSE101")
for key,value in courses.items():
    print(f"Course: {key}")
    for innerKey,innerValue in courses[key].items():
        print(f"{innerKey}: {innerValue}")
    print("-----------------\n")
print("\n--------------------------------------------")
print("|         -Solution of String-             |")
print("--------------------------------------------")
#2.Strings 
sentence = "Learning Python is fun and rewarding."
subStr = sentence[-28:-15]
print(subStr)
sentence = sentence.replace("rewarding","exciting",-1)
print("Ater modifying the sentence with exciting: ")
print(sentence)
n = len(sentence)
sentence = sentence.title()
print(sentence)

#List
print("\n--------------------------------------------")
print("|          -Solution of List-              |")
print("--------------------------------------------")
customers = ["Alice","Bob","Charlie","David","Eve"]

print(f"\nThe third customer in the list: {customers[2]}")
print("\n-----------------\n")
customers[1] = "Ben"
print("After Upgrading Bob to Ben:> ")
for customer in customers:
    print(customer,end=',')
print("\n-----------------\n")
#Adding new customer in the list at the end
customers.append("Frank")
print("After adding Frank to the customer list:> ")
for customer in customers:
    print(customer,end=',')
print("\n-----------------\n")
#Removed David from the list
customers.pop(3)
print("After removing David from  the customer list:> ")
for customer in customers:
    print(customer,end=',')
print("\n-----------------\n")
customers.sort()
print("After sorting  the customer list:> ")
for customer in customers:
    print(customer,end=',')
print("\n-----------------\n")
print("The final  customer list:> ")
for customer in customers:
    print(customer,end=',')

print("\n--------------------------------------------")
print("|       -Solution of Control Flow-          |")
print("--------------------------------------------")

grades = [85,78,92,45,33,67,88,41]


#Solution of 4.b
print("\nInitial Scores and grades => ")

def findGrade(grades):
    for mark in grades:
        if(mark>=80):
            print(f"student mark: {mark}, Grade: A")
        elif(mark>=60):
            print(f"student mark: {mark}, Grade: B")
        elif(mark>=40):
            print(f"student mark: {mark}, Grade: C")
        else:
            print(f"student mark: {mark}, Grade: F")

findGrade(grades)
def boost_grades(grade):
    return grade+(grade*.05)
boosted_list = map(boost_grades,grades)
grades = list(boosted_list)
print("\nAfter boosting grade by 5% => ")
findGrade(grades)

def myFilter(grade):
    return grade >= 90

print("\nAfter Filtering by 90+ scores => ")
newList = list(filter(myFilter,grades))
for grade in newList:
    print(grade)

    
print("\n--------------------------------------------")
print("|             -Tuple and Set-              |")
print("--------------------------------------------")

books = (
    ("To Kill a Mochingbird","Harper Lee",1960),
    ("1984","George Orwell",1949),
    ("The Great Gatsby","F.Scott Fitzgerald",1925)
)

tags = {"classic","dystopian","novel","literature"}
print("\nPrinting 2nd's tupple 2nd element => ")
print(books[1][1])
tempList = list(books)
tempList.append(("Brave New World","Aldous Huxley",1932))
books = tuple(tempList)
ThirdBook = books[2]
ThirdBookName = ThirdBook[0]
ThirdBookAuthor = ThirdBook[1]
ThirdBookPubYear = ThirdBook[2]
print()
print("Third Book information")
print(f"Book Name: {ThirdBookName},")
print(f"Book Author: {ThirdBookAuthor},")
print(f"Published: {ThirdBookPubYear}\n")
i = 1
print("All Books Title")
for item in books:
    print(f"Book {i}: {item[0]}")
    i = i+1
#adding "sci-fi" new tag into the tag set
tags = tags | {"sci-fi"}
print("\nAfter added 'sci-fi' tag into the tags set")
for tag in tags:
    print(tag)

print("\nAfter removing 'novel' tag from the tags set")
tags.remove("novel")
for tag in tags:
    print(tag)
