import sqlite3  
  
con = sqlite3.connect("staff.db")  
print("Database opened successfully")  
  
con.execute("create table Employees (id VARCHAR PRIMARY KEY , name TEXT NOT NULL, gender TEXT NOT NULL, phn_no INTEGER UNIQUE NOT NULL, dob INTEGER NOT NULL, address TEXT NOT NULL, joining_date INTEGER NOT NULL, dno INTEGER NOT NULL, role TEXT NOT NULL, salary INTEGER NOT NULL ,FOREIGN KEY (dno) REFERENCES Department(Dnumber))" )
con.execute("create table Department(Dnumber INTEGER PRIMARY KEY , Dname TEXT NOT NULL, hod_id VARCHAR NOT NULL, hod_start_date INTEGER NOT NULL,  FOREIGN KEY (hod_id) REFERENCES Employees(id))")
con.execute("create table LeaveRecord(EmployeID INTEGER PRIMARY KEY , Empname TEXT NOT NULL, date DATE NOT NULL ,  Full_day INTEGER NOT NULL, half_day INTEGER NOT NULL , balance INTEGER NOT NULL , remark TEXT NOT NULL, FOREIGN KEY (EmployeID) REFERENCES Employees(id))")
con.execute("create table Teaches(EmpId INTEGER NOT NULL , Cname TEXT NOT NULL, FOREIGN KEY (EmpId) REFERENCES Employees(id))")

                                                                                                                   
print("Table created successfully")  
  
con.close()
  
