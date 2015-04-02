# -*- coding: utf8 -*-

import pymssql
import socket
import json



sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost', 8002))  
sock.listen(5)
print('open success!!')
while True:
    connection, address = sock.accept()
    bufin = connection.recv(1024).decode('UTF_8')
    
    
    while True:
        
        try:
            if(bufin=='1'):
                bufin = connection.recv(1024).decode('UTF_8')
                bufin_new = json.loads(bufin)
                username = (bufin_new["username"])
                password = (bufin_new["password"])
                conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
                cur = conn.cursor()
                operation = "select * from person where username = '%s' and password = '%s'" % (username,password)
                num = 0
                cur.execute(operation)
                
                for row in cur.fetchall():
                    num = num + 1
                
                if(num!=0):
                    connection.send(b'1')
                    print(str(row) + 'login success!')
                    conn.close()
                else:
                    connection.send(b'0')
                    conn.close()
                break
            
            
            if(bufin=='2'):
                bufin = connection.recv(1024).decode('gbk')
                bufin_new = json.loads(bufin)
                username = (bufin_new["username"])
                password = (bufin_new["password"])
                phoneno = str(bufin_new["phoneno"])
                address = (bufin_new["address"])
                idtype = (bufin_new["idtype"])
                idno = str(bufin_new["idno"])
                situation = bufin_new["situation"]
                money = bufin_new["money"]
                type = bufin_new["type"]
                    
                if(username=='' or password=='' or idno ==''):
                    connection.send(b'2')
                    break
                conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
                cur = conn.cursor()
                operation1 = "insert into account_0 values ('%s','%s','%s','%s','%s','%s','%s',%d)" % (username,password,phoneno,address,
                                                                                        idtype,idno,situation, money)
                                                                                    
                operation2 = "insert into log values ('%s',%d,'%s',getdate())" % (idno, money, type)
                try:
                    cur.execute(operation1)
                    conn.commit()
                    cur.execute(operation2)
                    conn.commit()
                    conn.close()
                    connection.send(b'1')
                        
                    break
                except:
                    connection.send(b'0')
                        
                    break 
                    
            if(bufin=='3'):
                bufin = connection.recv(1024).decode('gbk')
                bufin_new = json.loads(bufin)
                idno = bufin_new["idno"]
                password = bufin_new["password"]
                new_password = bufin_new["new_password"]
                conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
                cur = conn.cursor()
                num = 0
                operation1 = "select * from account_0 where idno = '%s' and password = '%s'" % (idno,password)
                cur.execute(operation1)
                
                for row in cur.fetchall():
                    num = num + 1
                
                
                
                if(num!=0):
                    try:
                        operation2 = "update account_0 set password = '%s' where idno = '%s'" % (new_password, idno)
                        
                        cur.execute(operation2)
                        conn.commit()
                        conn.close()
                        
                        connection.send(b'1')
                        
                        break
                    except:
                        
                        connection.send(b'0')
                        conn.close()
                        break
                
                else:
                    
                    connection.send(b'0')
                    conn.close()
                    break
            
            if(bufin=='4'):
                bufin = connection.recv(1024).decode('gbk')
                bufin_new = json.loads(bufin)
                idno = bufin_new["idno"]
                password = bufin_new["password"]
                
                conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
                cur = conn.cursor()
                num = 0
                operation1 = "select * from account_0 where idno = '%s' and password = '%s'" % (idno,password)
                cur.execute(operation1)
                
                for row in cur.fetchall():
                    num = num + 1
                    
                if(num!=0):
                    try:
                        operation2 = "update account_0 set situation = '0' where idno = '%s'" % (idno)
                        
                        cur.execute(operation2)
                        conn.commit()
                        conn.close()
                        
                        connection.send(b'1')
                        
                        break
                    except:
                        
                        connection.send(b'0')
                        conn.close()
                        break
                
                else:
                    
                    connection.send(b'0')
                    conn.close()
                    break    
            
            
            if(bufin=='5'):
                bufin = connection.recv(1024).decode('gbk')
                bufin_new = json.loads(bufin)
                idno = bufin_new["idno"]
                money = bufin_new["money"]
                type = bufin_new["type"]
                
                conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
                cur = conn.cursor()
                
                operation1 = "select * from account_0 where idno = '%s'" % (idno)
                cur.execute(operation1)
                num = 0
                for row in cur.fetchall():
                    num += 1
                    flag = int(row['situation'])       #从数据库中取出数据后字符串会有空格！
                
                
                if(num!=0):
                    if(flag!=0):
                        
                        operation2 = "update account_0 set money = money + %d where idno = '%s'" % (money, idno)
                        operation3 = "insert into log values ('%s',%d,'%s',getdate())" % (idno, money, type)
                        cur.execute(operation2)
                        conn.commit()
                        cur.execute(operation3)
                        conn.commit()
                        conn.close()
                        connection.send(b'1')
                        break
                    else:
                        connection.send(b'0')
                        conn.close()
                        break
                else:
                    connection.send(b'2')
                    conn.close()
                    break
                
            if(bufin=='6'):
                bufin = connection.recv(1024).decode('gbk')
                bufin_new = json.loads(bufin)
                idno = bufin_new["idno"]
                password = bufin_new["password"]
                money = bufin_new["money"]
                
                
                conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
                cur = conn.cursor()
                
                operation1 = "select * from account_0 where idno = '%s' and password = '%s'" % (idno, password)
                cur.execute(operation1)
                num = 0
                for row in cur.fetchall():
                    num += 1
                    flag = int(row['situation'])       #从数据库中取出数据后字符串会有空格！
                    leftmoney = row['money']
                
                if(money>leftmoney):
                    connection.send(b'3')
                    conn.close()
                    break
                
                if(num!=0):
                    if(flag!=0):
                        
                        operation2 = "update account_0 set money = money - %d where idno = '%s'" % (money, idno)
                        money = 0 -money
                        operation3 = "insert into log values ('%s',%d,'%s',getdate())" % (idno, money, '取款')
                        cur.execute(operation2)
                        conn.commit()
                        cur.execute(operation3)
                        conn.commit()
                        conn.close()
                        connection.send(b'1')
                        break
                    else:
                        connection.send(b'0')
                        conn.close()
                        break
                else:
                    connection.send(b'2')
                    conn.close()
                    break
                    
                
            if(bufin=='7'):
                bufin = connection.recv(1024).decode('gbk')
                bufin_new = json.loads(bufin)
                idno = bufin_new["idno"]
                password = bufin_new["password"]
            
                conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
                cur = conn.cursor()
                num = 0
                operation1 = "select * from account_0 where idno = '%s' and password = '%s'" % (idno,password)
                cur.execute(operation1)
                
                for row in cur.fetchall():
                    num = num + 1
                    flag = row['money']
                if(num!=0):
                    if(flag==0):
                        operation2 = "delete from account_0 where idno = '%s'"% (idno)
                        cur.execute(operation2)
                        conn.commit()
                        conn.close()
                        connection.send(b'1')
                        break
                    else:
                        
                        connection.send(b'2')
                        conn.close()
                        break
                else:
                    connection.send(b'0')
                    conn.close()
                    break
                    
            if(bufin=='00'):
                username = connection.recv(1024).decode('utf_8')
                conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
                cur = conn.cursor()
                num = 0
                operation1 = "select * from person where username = '%s'" % (username)
                cur.execute(operation1)
                for row in cur.fetchall():
                    num = num + 1
                if(num!=0):
                    operation2 = "update person set password = '' where username = '%s'" % (username)
                    cur.execute(operation2)
                    conn.commit()
                    conn.close()
                    connection.send(b'1')
                    break
                else:
                    conn.commit()
                    conn.close()
                    connection.send(b'0')
                    break
                    
                    
        except socket.timeout: 
            print("time is out")
            break 
        except ConnectionAbortedError:
            print("connection is over!")
            connection.close()
            break
        except ConnectionResetError:
            print("connect is exit!")
            connection.close()
            break
            
    connection.close()
    continue
        
    
        


        
