import pymssql
import socket
import json
from _sqlite3 import OperationalError



conn = pymssql.connect(host = "localhost", port = '1433', user = 'sa', password = '412765442', database = 'summer',charset="utf8",as_dict=True)
cur = conn.cursor()

if not cur:
    raise(NameError,"error")

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost', 8002))  
sock.listen(5)
print('open success!!')
while True:
    connection, address = sock.accept()
    print('the client ip is '+str(address))
    bufin = connection.recv(1024).decode('UTF_8')
    
    while True:
        try:
            if(bufin=='1'):
                bufin = connection.recv(1024).decode('UTF_8')
                bufin_new = json.loads(bufin)
                username = (bufin_new["username"])
                password = (bufin_new["password"])
                operation = "select * from person where username = '%s' and password = '%s'" % (username,password)
                
                num = 0
                cur.execute(operation)
                for row in cur.fetchall():
                    num = num + 1
                if(num!=0):
                    connection.send(b'1')
                    print(str(row) + 'login success!')
                    username = (bufin_new["username"])
                    password = (bufin_new["password"])
                else:
                    connection.send(b'0')
                break
            
            if(bufin=='2'):
                bufin = connection.recv(1024).decode('utf_8')
                bufin_new = json.loads(bufin)
                username = (bufin_new["username"])
                password = (bufin_new["password"])
                phoneno = (bufin_new["phoneno"])
                address = (bufin_new["address"])
                idtype = (bufin_new["idtype"])
                idno = (bufin_new["idno"])
                operation = "insert into account values ('%s','%s',%d,'%s','%s',%d)" % (username,password,phoneno,address,
                                                                                        idtype,idno)
                print(operation)
                try:
                    cur.execute(operation)
                    connection.send(b'1')
                    break
                except:
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
        
    
        


        
