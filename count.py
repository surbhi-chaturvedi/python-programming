st=input("enter the string")
vowels=0
consonents=0
digits=0
white_spaces=0
st=st.lower()
for i in range(0,len(st)):
    if(st[i]=='a' or st[i]=='e' or st[i]=='i' or st[i]=='o' or st[i]=='u'):
        vowels=vowels+1
    elif(st[i]>='a'and st[i]<='z'):
        consonents=consonents+1
    elif(st[i]>='0' and st[i]<='9'):
        digits=digits+1
    elif(st[i]==' '):
        white_spaces=white_spaces+1
print("vowels:",vowels)
print("consonents:",consonents)
print("digits:",digits)
print("white_spaces:",white_spaces)
      
