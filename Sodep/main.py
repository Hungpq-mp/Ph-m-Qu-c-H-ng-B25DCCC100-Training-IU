with open('SODEP.INP','r') as n:
    n = n.read().strip()
tong = 0
for i in n:
    tong += int(i)

if tong % 10 == 9: 
    anw = "1"
else:
    anw ="0"
with open("SODEP.OUT","w") as f:
    f.write(anw)
