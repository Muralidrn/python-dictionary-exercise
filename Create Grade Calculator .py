student={'Math': 90, 'Science': 80, 'English': 70,"history":48,"geography":55}
print(student.values())
print(sum(student.values()))
avg=sum(student.values())/len(student)
print(f"avg : {avg}")
print(f"Grade A" if avg>=70 else "Grade B" if avg >=50 else " Grade C")
