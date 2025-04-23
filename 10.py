cet = {"soham", "joshep", "smaya", "kyra", "ravi"}
jee = {"adi", "soham", "kyra", "neev", "meera"}
neet = {"joshep", "neev", "kyra", "pradip", "tina"}

unionexample=cet|jee|neet
intersectionexpmale=jee&neet
diffexmple1=jee-neet
diffexmple2=neet-jee
symetricdiff=cet^neet

print("cet",cet)
print("jee",jee)
print("neet",neet)
print("union",unionexample)
print("intersection",intersectionexpmale)
print("diifernce1:",diffexmple1,"diifernce2:",diffexmple2)
print("symetic differnce",symetricdiff)


