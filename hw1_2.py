lines=[]
with open("C:/Users/USER/Downloads/kobe.csv","r") as file:
	r=file.readline()
	for line in file:
		lines.append(line.split(","))
def f(dic):
	l=[]
	for key,val in dic.items():
		l+=[(val,key)]
	return l
print("#1")#1
s=[0,0]
s_in=[0,0]
for i in range(len(lines)):
	if lines[i][15]=="HOU\n":
		if lines[i][10][0]=="2":
			s[0]+=1
			if lines[i][9]!="0":
				s_in[0]+=1
		else:
			s[1]+=1
			if lines[i][9]!="0":
				s_in[1]+=1
	else:
		continue
print("two: %.2f"%(s_in[0]/s[0]))#平均兩分球命中率
print("three: %.2f"%(s_in[1]/s[1]))#平均三分球命中率
print("#2")#2
dic,dic_in={},{}
dic[lines[0][15][:3]],dic_in[lines[0][15][:3]]=1,int(lines[0][9])*int(lines[0][10][0])
for i in range(1,len(lines)):
	game_id,opp=lines[i][2],lines[i][15][:3]
	if game_id==lines[i-1][2]:
		dic_in[lines[i][15][:3]]+=int(lines[i][9])*int(lines[i][10][0])
	else:
		if opp in dic:
			dic[opp]+=1
			dic_in[opp]+=int(lines[i][9])*int(lines[i][10][0])
		else:
			dic[opp]=1
			dic_in[opp]=int(lines[i][9])*int(lines[i][10][0])
for key in dic.keys():
	dic[key]=dic_in[key]/dic[key]
l=f(dic)
l.sort()
for i in range(5):
	print(l[i][1],": %.3f"%(l[i][0]))
print("#3")#3
dic={}
dic_oppo={}
for i in range(len(lines)):
	game_id,time,score,oppo,second,playoff,period=lines[i][2],int(lines[i][3]),int(lines[i][9])*int(lines[i][10][0]),lines[i][15][:3],int(lines[i][7]),lines[i][5],lines[i][4]
	if playoff=="1" and period=="4":
		if (time<3) or (time==3 and second==0) :
			if game_id in dic:
				dic[game_id]+=score
			else:
				dic[game_id]=score
				dic_oppo[game_id]=oppo
		else:
			continue
	else:
		continue
l=f(dic)
l.sort(reverse=True)
for i in range(5):
	print(dic_oppo[l[i][1]],l[i][1],":",l[i][0])
print("#4")#4
dic,dic_in={},{}
for i in range(len(lines)):
	action,minute,second,period,playoff,season,shot=lines[i][0],int(lines[i][3]),int(lines[i][7]),lines[i][4],lines[i][5],lines[i][6],lines[i][9]
	if (action=='Jump Shot') and (period=='4') and (playoff=='1'):
		if minute<1 or (minute==1 and second==0):
			if season in dic:
				dic[season]+=1
				if shot=='1':
					dic_in[season]+=1
			else:
				dic[season]=1
				if shot=='1':
					dic_in[season]=1
				else:
					dic_in[season]=0
		else:
			continue
	else:
		continue
for key in dic.keys():
	dic[key]=round(dic_in[key]/dic[key],4)
ans=f(dic)
for i in range(len(ans)):
	print(ans[i][1],ans[i][0])
print("#5")#5
dic,dic_in={},{}
for i in range(len(lines)):
	game_id,shot,opp,date=lines[i][2],lines[i][9],lines[i][-1][:3],lines[i][-3]
	if (game_id,opp,date) in dic:
		dic[(game_id,opp,date)]+=1
		if shot=="1":
			dic_in[(game_id,opp,date)]+=1
	else:
		dic[(game_id,opp,date)]=1
		if shot=="1":
			dic_in[(game_id,opp,date)]=1
		else:
			dic_in[(game_id,opp,date)]=0
for key in dic.keys():
	dic[key]=round(dic_in[key]/dic[key],2)
t=True
all_,right,length=[],[],[]
for key in dic.keys():
	if dic[key]>=0.33:
		right+=[(key,dic[key])]
	else:
		all_+=[right]
		right=[]
for i in range(len(all_)):
	length+=[(len(all_[i]),i)]
length.sort(reverse=True)
for i in range(3):
	print('from',all_[length[i][1]][0][0][2],'to',all_[length[i][1]][-1][0][2],length[i][0])
print("#6")#6
up,down,plus,minus,dic,dic_in,ans={},{},{},{},{},{},[]
for i in range(len(lines)):
	game_id,period,score,opp,date,shot=lines[i][2],lines[i][4],int(lines[i][9])*int(lines[i][10][0]),lines[i][15][:3],lines[i][-3],lines[i][9]
	if (game_id,opp,date) in dic:
		dic[(game_id,opp,date)]+=1
		dic_in[(game_id,opp,date)]+=int(shot)
		if period=='1' or period=='2':
			up[(game_id,opp,date)]+=score
		if period=='3' or period=='4':
			if (game_id,opp,date) in down:
				down[(game_id,opp,date)]+=score
			else:
				down[(game_id,opp,date)]=score
	else:
		dic[(game_id,opp,date)]=1
		dic_in[(game_id,opp,date)]=int(shot)
		if period=='1' or period=='2':
			up[(game_id,opp,date)]=score
		if period=='3' or period=='4':
			down[(game_id,opp,date)]=score
for key in up.keys():
	if key not in down:
		down[key]=0
for key in down.keys():
	if key not in up:
		up[key]=0
for key in dic.keys():
	dic[key]=round(dic_in[key]/dic[key],4)
	plus[key]=up[key]+down[key]
	minus[key]=up[key]-down[key]
for key in minus.keys():
	if minus[key]>0:
		ans+=[(dic[key],key)]
ans.sort()
ans1=ans[:3]
ans1.sort(reverse=True)
for i in range(3):
	print('日期:',ans1[i][1][2],'對手:',ans1[i][1][1],'得分差:',minus[ans1[i][1]],'該場得分:',plus[ans1[i][1]],'命中率:',ans1[i][0])
print('#7')#7
dic_score,dic_loose,no_in={},{},0
for i in range(len(lines)):
	game_id,opp,shot,date,score=lines[i][2],lines[i][-1][:3],int(lines[i][9]),lines[i][-3],int(lines[i][9])*int(lines[i][10][0])
	if (game_id,opp,date) in dic_score:
		dic_score[(game_id,opp,date)]+=score
		dic_loose[(game_id,opp,date)]+=[shot]
	else:
		dic_score[(game_id,opp,date)]=score
		dic_loose[(game_id,opp,date)]=[shot]
for key in dic_loose.keys():
	maxx,i=0,0
	while i <len(dic_loose[key])-1:
		if dic_loose[key][i]==1:
			del dic_loose[key][i]
			i=0
		else:
			if dic_loose[key][i+1]==0:
				i+=1
			else:
				if i+1>maxx:
					maxx=i+1
					del dic_loose[key][:i+1]
				else:
					del dic_loose[key][:i+1]
				i=0
	dic_loose[key]=maxx
ans=f(dic_loose)
ans.sort(reverse=True)
for i in range(3):
	print('日期:',ans[i][1][2],'對手:',ans[i][1][1],'連續失手:',ans[i][0],'得分:',dic_score[ans[i][1]])





