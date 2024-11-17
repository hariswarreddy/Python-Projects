#Employee Management System
#Designer :- Bontha Hariswar Reddy
employee_details = dict()    #Creating Empty Dictionary
while True:
    print("----------EMPLOYEE MANAGEMENT SYSTEM------------")
    print("1.INSERT NEW EMPLOYEE RECORD")
    print("2.DISPLAY ALL EMPLOYEE RECORDS")
    print("3.SEARCH EMPLOYEE RECORD")
    print("4.UPDATE EMPLOYEE RECORD")
    print("5.DELETE EMPLOYEE RECORD")
    print("6.EXIT")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("-----------INSERT NEW EMPLOYEE RECORD-----------")
        employee_id=(input("Enter employee id:"))
        employee_name=input("Enter employee name:")
        employee_dept=input("Enter employee department:")
        employee_salary=float(input("Enter employee salary:"))
        employee_details.update({employee_id:{"employee_name":employee_name,"employee_dept":employee_dept,"employee_salary":employee_salary}})
    elif choice==2:
        print("-----------DISPLAY ALL EMPLOYEE RECORDS-----------")
        for i in employee_details.items():
            print("%20s %20s %20s %20f"%(i[0],i[1]["employee_name"],i[1]["employee_dept"],i[1]["employee_salary"]))
    elif choice==3:
        print("-----------SEARCH EMPLOYEE RECORD WITH USER NAME-----------")
        employee_id=(input("Enter employee id:"))
        print(employee_details.get(employee_id))
    elif choice==4:
        print("-----------UPDATE EMPLOYEE RECORD-----------")
        employee_id=(input("Enter employee id:"))
        employee_name=input("Enter employee name:")
        employee_dept=input("Enter employee department:")
        employee_salary=int(input("Enter employee salary:"))
        employee_details.update({employee_id:{"employee_name":employee_name,"employee_dept":employee_dept,"employee_salary":employee_salary}})
    elif choice==5:
        print("-----------DELETE EMPLOYEE RECORD-----------")
        employee_id=(input("Enter employee id:"))
        employee_details.pop(employee_id)
    elif choice==6:
        print("-----------EXIT-----------")
        break
    else:
        print("Invalid choice!!!")
