from src.table import Table

table = Table("test", 5, 0)

table.put(1,None,0,'11111',[1,2,3,4,5])
table.put(2,1,0,'11111',[6,7,8,9,10])
table.put(3,1,0,'11111',[14,15,11,12,13])
r = table.get(1,'11111')
print(r)