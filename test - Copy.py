import pretty_midi as pm

mdir = 'target.mid'

#test = pm.PrettyMidi(mdir)
xsocre = []
with open(mdir,'r') as f:
    templist = f.split('\n')
    templist.pop()
    for line in templist:
        xscore.append([float(i) for i in line.split(',')])
for each in xscore:
    each.append(each[1].round())
print(xscore)
raise
'''
[[0,1.0000,1.45,66,80,2.214,tempo1,3.1223,tempo2,duration,timelenth],
[],
[]]
'''
frame = 0.125
t = 0
note_index = 0
c_ins = 0
FLAG = True
result = []
while FLAG:
    if xscore[note_index][0] == -3:
        break
    if xscore[note_index][0] != c_ins:
        c_ins+=1
        t = 0
    InerFLAG = True
    while InerFLAG:
        if t>=xscore[note_index][****] and t<=xscore[note_index][****]:
            result.append([c_ins])
            note_index+=1
        if xscore[note_index][0] != c_ins:
            if xscore[note_index][0] == -3:
                FLAG = False
            else:
                
            InerFLAG = False
    if t-int(t) == 0:
        pass
    elif t-int(t) ==
        
        result.append([t,start])
    elif t-int(t) == 0.5:
        pass
    elif t-int(t) == 0.25 or t-int(t) == 0.75:
        pass
    else:
        raise

    t+=frame

frame = 0.225
t = 0
note_index = 0
c_ins = 0
FLAG = True
result = []
while FLAG:
    if xscore[note_index][0] == -3:
        break
    if xscore[note_index][0] != c_ins:
        c_ins+=1
        t = 0
        
        
    if t-int(t) == 0:
        interval = 0.13
        if 
        result.append([t,start])
        
    elif t-int(t) == 0.5:
        pass
    elif t-int(t) == 0.25 or t-int(t) == 0.75:
        pass
    
    else:
        raise

    
