import subprocess
import os
def users():
    task = subprocess.Popen("ls -1 /var/cpanel/users", shell=True, stdout=subprocess.PIPE)
    data = task.stdout.read()
    f = open("users.txt","w+")
    f.write(data)
    f.close()
    f = open("users.txt","r")
    users = []
    for i in f.readlines():
        users.append(i.replace('\n',''))
    f.close()
    return users

def inst_id(user):
    task = subprocess.Popen("/usr/local/cpanel/3rdparty/bin/php /usr/local/cpanel/whostmgr/docroot/cgi/softaculous/cli.php -u --user=%s --list=1" % user, shell=True, stdout=subprocess.PIPE)
    data = task.stdout.read()
    f = open("users.txt","w+")
    f.write(data)
    f.close()
    myList = []
    f = open("users.txt","r")
    for i in f.readlines():
        if len(i) >=2:
            st=i.strip(' \t\n\r')
            if st[2].isdigit():
                myList.append(st.split('|')[1])
    f.close()
    return myList

def upgrade(user,scripts):
    for i in scripts:
        script = i.strip(' \t\n\r')
        task = subprocess.Popen("/usr/local/cpanel/3rdparty/bin/php /usr/local/cpanel/whostmgr/docroot/cgi/softaculous/cli.php -u --user=%s --insid=%s" %(user,script), shell=True, stdout=subprocess.PIPE)
        data = task.stdout.read()
        print data


def main():
    for i in users():
        print ("Update user: %s\n" % i)
        upgrade(i,inst_id(i))


if __name__== "__main__":
    main()

