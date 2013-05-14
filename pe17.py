#leaving 1000 for the time being
one = 191 #unit digit + hundred d of 3d + 1000
two = 190 
three = 190
four = 190
five = 190
six = 190
seven = 190
eight = 190
nine = 190
ten = 10
eleven = 10
twelve = 10
thirteen = 10
fourteen = 10
fifteen = 10
sixteen = 10
seventeen = 10
eighteen = 10
nineteen = 10 
twenty = 100 
thirty = 100
forty = 100
fifty = 100
sixty = 100
seventy = 100
eighty = 100
ninety = 100
hundred = 900
nd = 891
thousand = 1

total = one*3 + two*3 + three*5 + four*4 + five*4 + six*3 + seven*5 + eight*5 + nine*4 
total = total + ten*3 + eleven*6 + twelve*6 + thirteen*8 + fourteen*8 + fifteen*7 + sixteen*7 + seventeen*9 + eighteen*8 + nineteen*8 
total = total + twenty*6 + thirty*6 + forty*5 + fifty*5 + sixty*5 + seventy*7 + eighty*6 + ninety*6 + hundred*7 + nd*3 + thousand*8

print total    




