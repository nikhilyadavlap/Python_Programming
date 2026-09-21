"""Q2. At an airport, a traveler is allowed entry into the flight only if he clears the following checks:
1.Baggage Check  
2.Immigration Check  
3.Security Check  
The logic for the check methods are given below: 
check_baggage (baggage_weight)  
• returns True if baggage_weight is greater than or equal to 0 and less than or equal to 40. Otherwise returns False.  
check_immigration (expiry_year)  
• returns True if expiry_year is greater than or equal to 2030 and less than or equal to 2050. Otherwise returns False.  
check_security(noc_status)  
• returns True if noc_status is 'valid' or 'VALID', for all other values return False.  
traveler()  
• Initialize the traveler Id and traveler name and invoke the functions check_baggage(), check_immigration() and check_security() by passing required arguments.  
Refer the table below for values of arguments.  

       Variable            Value
       traveler_id         1001
       traveler_name       Jim
       baggage_weight      35
       expiry_year         2019
       noc_status          VALID

• If all values of check_baggage(), check_immigration() and check_security() are true,   
- display traveler_id and traveler_name  
- display "Allow Traveler to fly!"  
Otherwise,  
- display traveler_id and traveler_name  
- display "Detain Traveler for Re-checking!  
Invoke the traveler() function. Modify the values of different variables in traveler() function and observe the output."""

#CODE:

def check_baggage(weight):
    return weight >= 0 and weight <= 40

def check_immigration(year):
    return year >= 2030 and year <= 2050

def check_security(status):
    return status.lower() == "valid"

def traveler():
    traveler_id = input("Enter Traveler ID: ")
    traveler_name = input("Enter Traveler Name: ")
    baggage = float(input("Enter Baggage Weight: "))
    year = int(input("Enter Passport Expiry Year: "))
    status = input("Enter NOC Status: ")

    if check_baggage(baggage) and check_immigration(year) and check_security(status):
        print(traveler_id)
        print(traveler_name)
        print("Allow Traveler to fly!")

    else:
        print(traveler_id)
        print(traveler_name)
        print("Detain Traveler for Re-checking!")

traveler()
