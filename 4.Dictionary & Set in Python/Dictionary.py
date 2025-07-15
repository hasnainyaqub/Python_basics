info = {
    "name"  : "Hasnain",
    "class" : '11th' ,
    "code" : ["python", "Ai"],
    "topics" : ("dict", "set"),
    "marks" : 85,


}
info["name"] = "Hasnain Yaqoob"
info["surname"] = "Arain"
# print(info)


student = {
    "name" : "Hasnain",
    "marks" : {
        "chem" : 70,
        "phy" : 75,
        "maths" : 85,

    }
}
print(student)
print(student["marks"])
print(student["marks"] ["maths"])
print(student.items())
# print(list(student.keys()))