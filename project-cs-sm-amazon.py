#Amazon Employees Database

print('Amazon Employees Database')
import sqlite3 as x
q=x.connect('sm12c.db')
cur=q.cursor()
d={'s':[1,2,3,4,5],'n':['Andrea Bell','Naomi Ward','Salil Singh','Nikitha Green','Percy Vere'],'ar':['Bristol','Warton','Cardigan','Skelton','London'],'p':['7450098033','7036210126','7399157138','7911250314','7508017277'],'a':['Backwell','Carnforth','Ambleston','Haxby','Wembley']}
d3={'s':'sno','n':'name','ar':'area','p':'phone_no','a':'address','sm':'manager_sno','sl':'sal'}
l7=[[1,'Andrea Bell','2','25000'],[2,'Naomi Ward','NULL','35000'],[3,'Salil Singh','2','30000'],[4,'Nikitha Green','1','20000'],[5,'Percy Vere','3','15000']]
#1--sno int primary key,2--name char(10),3--manager sno char(10),4--sal char(10)

def show(d):#formatting dict
    k=len(d['s'])
    print('s.no.\t\t','name\t\t\t','area\t\t\t','phone_no\t','address',end='\n'+('-'*100)+'\n')
    for i in range(k):
        for j in d:
            e=d[j][i]
            if type(e)==str and len(e)<=8 and j!='p':
                print(e,end='\t\t\t')
            elif j=='p':print(e,end='\t')
            else:
                print(e,end='\t\t')
        print()

def SHOW(l):#formatting nested list
    print('s.no.\t\t','name\t\t\t','manager s.no.\t\t','salary\t',end='\n'+('-'*80)+'\n')
    for i in range(len(l)):
        for j in l[i]:
            if type(j)==str and len(j)<=8:
                print(j,end='\t\t\t')
            else:
                print(j,end='\t\t')
        print()

def sh(k='t11'):#to see access data already in sql(if any)
    cur.execute('select * from "%s";'%str(k))
    r=cur.fetchall()
    return(r)


def sql():#dumping initial data into sql
    d={'s':[1,2,3,4,5],'n':['Andrea Bell','Naomi Ward','Salil Singh','Nikitha Green','Percy Vere'],'ar':['Bristol','Warton','Cardigan','Skelton','London'],'p':['7450098033','7036210126','7399157138','7911250314','7508017277'],'a':['Backwell','Carnforth','Ambleston','Haxby','Wembley']}
    for i in range(len(d['s'])):
        l=[]
        for j in d:
            l.append(d[j][i])
        cur.execute("insert into t11 values(%d,'%s','%s','%s','%s');"%tuple(l))
    l7=[[1,'Andrea Bell','2','25000'],[2,'Naomi Ward','NULL','35000'],[3,'Salil Singh','2','30000'],[4,'Nikitha Green','1','20000'],[5,'Percy Vere','3','15000']]
    for j in range(i+1):
        cur.execute("insert into t111 values(%d,'%s','%s','%s');"%tuple(l7[j]))
def rev():#revamp
    d={'s':[1,2,3,4,5],'n':['Andrea Bell','Naomi Ward','Salil Singh','Nikitha Green','Percy Vere'],'ar':['Bristol','Warton','Cardigan','Skelton','London'],'p':['7450098033','7036210126','7399157138','7911250314','7508017277'],'a':['Backwell','Carnforth','Ambleston','Haxby','Wembley']}
    l7=[[1,'Andrea Bell','2','25000'],[2,'Naomi Ward','NULL','35000'],[3,'Salil Singh','2','30000'],[4,'Nikitha Green','1','20000'],[5,'Percy Vere','3','15000']]
    cur.execute("drop table if exists t11")
    cur.execute("create table t11(sno int primary key,name char(16),area char(16),phone_no char(16),address char(16))")
    cur.execute("drop table if exists t111")
    cur.execute("create table t111(sno int primary key,name char(16),manager_sno char(16),sal char(16))")
    sql()
    return d,l7
try:#to keep dict,list updated after program is closed
    t,t2=sh(),sh('t111')
    if len(t)>0:
        d1,l7={},[]
        for i in t2:
            l7.append(list(i))
        for i in d:
            d1[i]=[]
        for i in t:
            d1['s'].append(i[0])
            d1['n'].append(i[1])
            d1['ar'].append(i[2])
            d1['p'].append(i[3])
            d1['a'].append(i[4])
        d=d1
    else:
        temp=rev()
        d=temp[0]
        l7=temp[1]
except:
    temp=rev()
    d=temp[0]
    l7=temp[1]

def di(x,key1,bo=False):#sorting
    t1=tuple(d[x])
    t=tuple(sorted(t1,key=key1,reverse=bo))
    l0=[]
    for i in t:
        k=t1.index(i)
        l0.append(k)
    for i in d:
        l=d[i]
        l1=[]
        for j in l0:
            k=l[j]
            l1.append(k)
        d[i]=l1
    return(d)
def dii(x):#filter
    j=input('\t\tenter parameter\n\t\t')
    d1,l,l1,t={},[],d[x],()
    for i in d[x]:
        if j.lower() in i.lower():
            l.append(i)
    for h in l:
        t+=(l1.index(h),)
    for i in d:
        d1[i]=[]
        for j in range(len(d[i])):
            if j in t:
                d1[i].append(d[i][j])
    return(d1)
def sear(x1):
    d0={}
    if x1 in d['s']:
        k=(d['s']).index(x1)
        for i in d:
            l5=[]
            l5.append(d[i][k])
            d0[i]=l5
        show(d0)
while True:
    print('''\n0.Revamp database
1.add
2.show
3.update
4.delete
5.search
6.filter
7.sort
8.exit\n''')
    x=int(input('enter option\n'))
    d=di('s',None)
    if x==0:#revamp
        temp=rev()
        d=temp[0]
        l7=temp[1]
    elif x==1:#add records-(sql)
        l,l1=[],[]
        k=int(input('\tenter s.no.\n\t'))
        if k not in d['s']:
            for i in d:
                if i=='s':
                    (d[i]).append(k)
                    l1.append(d[i][-1])
                else:
                    (d[i]).append(input('\tenter '+d3[i]+'(upto 15 char)\n\t')[:15])
                l.append(d[i][-1])
            l1.append(d['n'][-1])
            l1.append(input('\tenter manager S.No.(upto 15 char)\n\t')[:15])
            l1.append(input('\tenter Salary(upto 7 char)\n\t')[:7])
            l7.append(l1)
            cur.execute("insert into t11 values(%d,'%s','%s','%s','%s');"%tuple(l))
            cur.execute("insert into t111 values(%d,'%s','%s','%s');"%tuple(l1))
        else:
            print('ERROR\nS.No. already exists')
    elif x==2:#show records--[format]
        print('''\t1.employee personal data
\t2.manager and salaries
\t3.both''')
        we=int(input('\t\tenter option\n\t\t'))
        if we==1:
            show(d)
        elif we==2:
            SHOW(l7)
        else:
            show(d)
            SHOW(l7)

    elif x==3:#update records-(sql)
        x1=input('''\n\n\tenter what is to be updated:
    serial number                       s
    name                                n
    phone                               p
    area                                ar
    address                             a
    manager\'s serial number             sm
    salary                              sl
    cancel                              c\n\t''')
        if x1 in ('s','n','p','ar','a','sm','sl'):
            if x1!='sm' and x1!='sl':
                l,L=d.get(x1),d.get('s')
                if x1!='s':
                    print('\t',d3[x1],d3['s'],sep='\t\t')
                    print()
                    for i in range(len(l)):
                        if len(l[i])>8:
                            print('\t\t',l[i],L[i],sep='\t')
                        else:print('\t',l[i],L[i],sep='\t\t')
                else:
                    print('\t\t','sno')
                    print()
                    for i in range(len(l)):
                        print('\t\t',L[i])
                k=int(input('\t\tenter serial number of element to be updated\n\t\t'))
                if k not in L:print('serial number not found')
                else:
                    r=L.index(k)
                    blanc=0
                    if x1=='s':
                        bleu=int(input('\n\t\tenter updated element\n\t\t'))
                        if bleu not in l:
                            l[r]=bleu
                        else:
                            blanc=1
                            print('Serial number already exists. Please enter Unique serial number')
                    else:
                        l[r]=input('\n\t\tenter updated element\n\t\t')
                    tr=l[r]
                    if x1=='s':
                        if blanc==0:
                            for iu in range(len(l7)):
                                if l7[iu][0]==k:
                                    l7[iu][0]=tr
                    elif x1=='n':
                        for iu in l7:
                            if iu[0]==k:
                                iu[1]=l[r]
                    d[x1]=l
                    cur.execute(f"UPDATE t11 SET {d3[x1]}=? WHERE sno=?", (tr, k))
            else:
                if x1=='sm':
                    print('',d3['s'],d3['sm'],sep='\t\t')
                    print()
                    for it in l7:
                        print('',it[0],it[2],sep='\t\t')
                    k=int(input('\t\tenter serial number of element to be updated\n\t\t'))
                    tr=input('\n\t\tenter updated element\n\t\t')
                    for ih in l7:
                        if ih[0]==k:
                            ih[2]=tr
                elif x1=='sl':
                    print('',d3['s'],d3['sl'],sep='\t\t')
                    print()
                    for ij in l7:
                        print('',ij[0],ij[3],sep='\t\t')
                    k=int(input('\t\tenter serial number of element to be updated\n\t\t'))
                    tr=input('\n\t\tenter updated element\n\t\t')
                    for ir in l7:
                        if ir[0]==k:
                            ir[3]=tr                
        if x1 in ('s','n','sm','sl') and k in d['s']:
            cur.execute(f"UPDATE t111 SET {d3[x1]}=? WHERE sno=?", (tr, k)) 
        else:
            pass

    elif x==4:#delete records-(sql)
        print(d['s'],d['n'])
        x1=int(input('\tenter S.No.\n\t'))
        if x1 in d['s']:
            for ie in l7:
                if ie[0]==x1:
                    l7.remove(ie)
            l=d['s']
            k=l.index(x1)
            for j in d:
                l1=d[j]
                l1.pop(k)  
            cur.execute("delete from t11 where sno='%d'"%(x1))
            cur.execute("delete from t111 where sno='%d'"%(x1))
        else:
            print('S.No. doesn\'t exist')

    elif x==5:#search records--[format]
        x1=int(input('\tenter S.No.\n\t'))
        sear(x1)
        if x1 in d['s']:
            for ii in l7:
                if ii[0]==x1:
                    SHOW([ii])
                    if ii[-2]!='NULL':
                        bo=input('show records of manager? y/n \n\t')
                        if bo=='y':
                            n=int(ii[-2])
                            sear(n)
                        elif bo=='n':
                            pass           
        else:
            print('\t\tS.No. not found')

    elif x==6:#filter through records--[format]
        while True:
            print('''\t1.by character in name
\t2.by ph number
\t3.by area
\t4.Exit Filter''')
            a=int(input('\tenter option\n\t'))
            if a==1:
                show(dii('n'))
            elif a==2:
                show(dii('p'))
            elif a==3:
                show(dii('ar'))
            elif a==4:break

    elif x==7:#sort the records--[format]
        while True:
            print('''\t1.by length of name
\t2.by alphabetical order of name
\t3.by phone number
\t4.Exit Sort''')
            a=int(input('\tenter option\n\t'))
            if a in (1,2,3):
                bo=int(input('''\t\t1.acsending
\t\t2.descending\n\t\t'''))
                if bo==1:b=False
                elif bo==2:b=True
            if a==1:
                d=di('n',len,b)
                show(d)
            elif a==2:
                d=di('n',None,b)
                show(d)
            elif a==3:
                d=di('p',None,b)
                show(d)
            elif a==4:break

    elif x==8:#exit
        break
    else:#invalid input
        print('error')
    q.commit()
cur.close()
q.close()
