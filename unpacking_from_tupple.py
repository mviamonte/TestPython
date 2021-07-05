work_hours = [("Abby", 100), ("Billy", 8400),("Cassie",800)]
def employee_check(work_hours):
  max_hours = 0
  employee_of_month=""
  for employee, hours in work_hours:
    if max_hours < hours:
      max_hours = hours
      employee_of_month = employee
  #else:
   # continue
  return (employee_of_month, max_hours)
results = employee_check(work_hours)
#print (max_hours,employee_of_month)
#print (results)
name,hours = employee_check(work_hours)
print (name)
print (hours)
