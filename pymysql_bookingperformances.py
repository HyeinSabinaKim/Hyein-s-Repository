import pymysql.cursors

class A:
    connection = pymysql.connect(host = 'astronaut.snu.ac.kr', port = 3306, user = 'BDE-2018-08', password = 'a137a0f25f98', db = 'BDE-2018-08', charset = 'utf8', autocommit = True, cursorclass = pymysql.cursors.DictCursor)
    def f1():
        cursor=A.connection.cursor() 
        sql = "select * from buildings"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("-"*80)
        print("id".ljust(7),end="")
        print("name".ljust(20),end="")
        print("location".ljust(20),end="")
        print("capacity".ljust(15),end="")
        print("assigned".ljust(10))
        print("-"*80)
        for i in range(len(result)):
            print(str(result[i]['id']).ljust(7),end="")
            print(result[i]['name'].ljust(20),end="")
            print(result[i]['location'].ljust(20),end="")
            print(str(result[i]['capacity']).ljust(15),end="")
            print(str(result[i]['assigned']).ljust(10))
            
    def f2():
        cursor=A.connection.cursor() 
        sql = "select * from performances"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("-"*80)
        print("id".ljust(7),end="")
        print("name".ljust(20),end="")
        print("type".ljust(20),end="")
        print("price".ljust(15),end="")
        print("booked".ljust(10))
        print("-"*80)
        for i in range(len(result)):
            print(str(result[i]['id']).ljust(7),end="")
            print(result[i]['name'].ljust(20),end="")
            print(result[i]['type'].ljust(20),end="")
            print(str(result[i]['price']).ljust(15),end="")
            print(str(result[i]['booked']).ljust(10))
  
    def f3():
        cursor=A.connection.cursor() 
        sql = "select * from audiences"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("-"*80)
        print("id".ljust(7),end="")
        print("name".ljust(20),end="")
        print("gender".ljust(20),end="")
        print("age".ljust(15))
        print("-"*80)
        for i in range(len(result)):
            print(str(result[i]['id']).ljust(7),end="")
            print(result[i]['name'].ljust(20),end="")
            print(result[i]['gender'].ljust(20),end="")
            print(str(result[i]['age']).ljust(15))
            
    def f4():
        f4_a = input("Building name: ")[:200]
        f4_b = input("Building location: ")[:200]
        f4_c = input("Building capacity: ")
        cursor=A.connection.cursor() 
        sql = "insert into buildings (name, location, capacity,assigned) values(%s,%s,%s,%s)"
        cursor.execute(sql,(f4_a,f4_b,f4_c,0))
        result = cursor.fetchall()
        print("A building is successfully inserted")
    
    def f5():
        cursor=A.connection.cursor() 
        while True:
            f5_a = input("Building ID: ")[:200]
            sql = "select * from buildings where id = %s"
            cursor.execute(sql,(f5_a))
            result = cursor.fetchall()
            if result == ():
                print("There is no such building. Please write another building number.")
            else:
                break
        sql = "delete from buildings where id = %s"
        cursor.execute(sql,(f5_a))
        result = cursor.fetchall()
        print("A building is successfully deleted")
        
        
    def f6():
        f6_a = input("Performance name: ")[:200]
        f6_b = input("Performance type: ")[:200]
        f6_c = input("Performance price: ")
        cursor=A.connection.cursor() 
        sql = "insert into performances (name, type, price,booked) values(%s,%s,%s,%s)"
        cursor.execute(sql,(f6_a,f6_b,f6_c,0))
        result = cursor.fetchall()
        print("A performance is successfully inserted")

    def f7():
        cursor=A.connection.cursor() 
        while True:
            f7_a = input("Performance ID: ")
            sql = "select * from performances where id = %s"
            cursor.execute(sql,(f7_a))
            result = cursor.fetchall()
            if result == ():
                print("There is no such performance. Please write another performance number.")
            else:
                break
        sql = "delete from performances where id = %s"
        cursor.execute(sql,(f7_a))
        result = cursor.fetchall()
        print("A performance is successfully deleted")
        
    def f8():
        f8_a = input("Audience name: ")[:200]
        f8_b = input("Audience gender: ")[:200]
        f8_c = input("Audience age: ")
        cursor=A.connection.cursor() 
        sql = "insert into audiences (name, gender,age) values(%s,%s,%s)"
        cursor.execute(sql,(f8_a,f8_b,f8_c))
        result = cursor.fetchall()
        print("An audience is successfully inserted")

    def f9():
        cursor=A.connection.cursor() 
        while True:
            f9_a = input("Audience ID: ")
            sql = "select * from audiences where id = %s"
            cursor.execute(sql,(f9_a))
            result = cursor.fetchall()
            if result == ():
                print("There is no such audience. Please write another audience number.")
            else:
                break
        sql = "delete from audiences where id = %s"
        cursor.execute(sql,(f9_a))
        result = cursor.fetchall()
        print("An audience is successfully deleted")
        
        
    def f10():
        cursor=A.connection.cursor() 
        while True:
            f10_a = input("Building ID: ")
            sql = "select * from buildings where id = %s"
            cursor.execute(sql,(f10_a))
            result = cursor.fetchall()
            if result == ():
                print("There is no such building. Please write another building number.")
            else:
                break       
        while True:
            f10_b = input("Performance ID: ")
            sql = "select * from assigned where performance_id = %s"
            cursor.execute(sql,(f10_b))
            result = cursor.fetchall()
            if result != ():
                print("Already assigned to other builiding. Select another performance.")
            else:
                break
        sql = "insert into assigned (building_id, performance_id) values (%s,%s)"
        cursor.execute(sql,(f10_a,f10_b))
        sql = "update buildings set assigned = assigned+1 where id = %s"
        cursor.execute(sql,(f10_a))
        result = cursor.fetchall() 
        print("Successfully assigned a performance")
  
    def f11():
        cursor = A.connection.cursor()
        while True:
            f11_a = input("Performance ID: ")
            sql = "select * from assigned where performance_id = %s"
            cursor.execute(sql,(f11_a))
            result = cursor.fetchall()
            if result == ():
                print("The performance has not been assigned to any location.")
                print("Please select another performance.")
            else:
                break
        f11_b = input("Audience ID: ")    
        while True:
            f11_c = input("Seat number: ")
            seat = list(map(lambda x: int(x),f11_c.split(",")))
            sql = "select capacity from buildings where id = (select building_id from assigned where performance_id = %s)"
            cursor.execute(sql,(f11_a))
            capacity = cursor.fetchall()[0]['capacity']
            if set(seat) < set(list(range(1,capacity+1))):
                sql = "select distinct seat_no from booked where performance_id = %s"
                cursor.execute(sql,(f11_a))
                result = cursor.fetchall()
                seat_lst = []
                for i in result:
                    seat_lst.append(i['seat_no'])
                if set(seat).intersection(set(seat_lst)) != set():
                    print("Sorry, at least one of the seats is taken already.")
                    print("Please assign other seats.")
                else:
                    break
            else:
                print("Sorry, you've written a seat number out of the building's capacity.")
                print("Please rewrite your desired seat numbers.")             
        for i in range(len(seat)):
            sql = "insert into booked values (%s,%s,%s)"
            cursor.execute(sql,(f11_a,f11_b,seat[i]))
        sql = "update performances set booked = booked+%s where id = %s"
        cursor.execute(sql,(len(seat),f11_a))
        sql = "select price from performances where id = %s"
        cursor.execute(sql,(f11_a))
        result = cursor.fetchall()[0]
        print("Successfully booked a performance")
        print("Total ticket price is " + str(len(seat)*result['price']))
  
    def f12():
        cursor = A.connection.cursor()
        while True:
            f12_a = input("Building ID: ")
            sql = "select id from buildings where id = %s"
            cursor.execute(sql,(f12_a))
            result = cursor.fetchall()
            if result == ():
                print("You've written a wrong building number. Please write another builidng number.")
            else:
                break
        sql = "select * from performances where id in (select performance_id from assigned where building_id = %s)"
        cursor.execute(sql,(f12_a))
        result = cursor.fetchall()
        print("-"*80)
        print("id".ljust(7),end="")
        print("name".ljust(20),end="")
        print("type".ljust(20),end="")
        print("price".ljust(15),end="")
        print("booked".ljust(10))
        print("-"*80)
        for i in range(len(result)):
            print(str(result[i]['id']).ljust(7),end="")
            print(result[i]['name'].ljust(20),end="")
            print(result[i]['type'].ljust(20),end="")
            print(str(result[i]['price']).ljust(15),end="")
            print(str(result[i]['booked']).ljust(10))
                    
    def f13():
        cursor = A.connection.cursor()
        while True:
            f13_a = input("Performance ID: ")
            sql = "select id from performances where id = %s"
            cursor.execute(sql,(f13_a))
            result = cursor.fetchall()
            if result == ():
                print("You've written a wrong performance number. Please write another performance number.")
            else:
                break
        sql = "select * from audiences where id in (select audience_id from booked where performance_id= %s)"
        cursor.execute(sql,(f13_a))
        result = cursor.fetchall()
        print("-"*80)
        print("id".ljust(7),end="")
        print("name".ljust(20),end="")
        print("gender".ljust(20),end="")
        print("age".ljust(15))
        print("-"*80)
        for i in range(len(result)):
            print(str(result[i]['id']).ljust(7),end="")
            print(result[i]['name'].ljust(20),end="")
            print(result[i]['gender'].ljust(20),end="")
            print(str(result[i]['age']).ljust(15))
            
    def f14():
        cursor = A.connection.cursor()
        while True:
            f14_a = input("Performance ID: ")
            sql = "select * from assigned where performance_id = %s"
            cursor.execute(sql,(f14_a))
            result = cursor.fetchall()
            if result == ():
                print("The performance has not been assigned to any location, or it does not exist.")
                print("Please select another performance.")
            else:
                break    
        sql = "select capacity from buildings where id = (select building_id from assigned where performance_id = %s)"
        cursor.execute(sql,(f14_a))
        result = cursor.fetchall()[0]
        capacity = result['capacity']
        sql = "select seat_no, audience_id from booked where performance_id = %s"
        cursor.execute(sql,(f14_a))
        result = cursor.fetchall()
        print("-"*80)
        print("seat_number".ljust(40),end="")
        print("audience_id".ljust(30))
        print("-"*80)
        for i in range(capacity):
            if result[i]['seat_no'] == i+1:
                print(str(i+1).ljust(40),end="")
                print(str(result[i]['audience_id']).ljust(30))
            else:
                print(str(i+1).ljust(30))
        print("-"*80)
            
print("="*80)
print("1. print all buildings")
print("2. print all performances")
print("3. print all audiences")
print("4. insert a new building")
print("5. remove a building")
print("6. insert a new performance")
print("7. remove an audience")
print("8. insert a new audience")
print("9. remove an audience")
print("10. assign a performance to a building")
print("11. book a performance")
print("12. print all performances assigned to a building")
print("13. print all audiences who booked for a performance")
print("14. print ticket booking status of a performance")
print("15. exit")
print("="*80)
while True:
    a = input("Select your action: ")
    if a == "15":
        print("Bye!")
        exit()
    else:
        eval("A.f" + a + "()")
