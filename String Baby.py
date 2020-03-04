a = " The Irish general election concludes with no party holding a majority of seats in Dáil Éireann. South Korean film Parasite wins four Academy Awards," \
    " including Best Picture and Best Director for Bong Joon-ho (pictured). A mass shooting in Korat, Thailand, leaves 30 people dead and more than 50 others injured." \
    "Two avalanches near the Turkish town of Bahçesaray kill at least 41 people."

b = a.replace(",", "")
c = b.replace(".", "")
d = c.lower()
e = d.split(" ")
f = [e[i] for i in range(0, len(e)) for j in str(e[i]) if j =="c"]
retVal = ""
for i in range(0, len(f)):
    retVal = retVal + f[i] + " "

print(retVal)
