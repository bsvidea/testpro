import csv

with open("student_data.csv","a",newline='') as file:
    write=csv.writer(file)
    write.writerows([[4,"Dev",21,"3rd","CSE"]])
    file.close()
print("new data uploaded")
