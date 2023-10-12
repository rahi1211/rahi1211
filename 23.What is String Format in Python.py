# #
# # EK FUNCATION ATA JISKA NAAM HAI FORMAT WO APKO OPTION DETA HAI KI APKI KOI BE STRING YA KOI BE NUM AP STR KA BEACH ME LE JA SKTE HO
#
# AGR APKO RUN TIME PY KOI VALUE KISI STR KA BEACH ME DALNE HAI TO AP YEH USE KR SKTI HAIN

w="WELLCOME {} TO {} WSCUBETECH".format("HELLO",20)

## JO AP NE PEHLE LIKHA HAI WO JAI GA PEHLE BREAT ME OR DORSA DOSRE ME

print(w)

print()
##2nd option
print()

w="wellcome {1} to {0} wscube".format("hello",20)
print(w)
## yeh index num py be chalta hai

print()
##3rd option


w="wellcome {a:>10} to {b} wscube".format(a="hello",b=20)
print(w)



## apka a ko yeh be bata skti hain ki wo kitne space ka use kre

## yeh agr 10space to 8ka lega asa
## 8space or 10 baki likhe ga
##--------10

##agr asa be chati hain ki 4ider sy or 4oder sy beach aa jai toh be ap kr skti hain
##apko yeh ^ smybol use kren ge yeh yeh andicate deta hai ki yeh  10 na num ka beach me aai ga
##<lessthen symbol yeh deta ha ki sare space left me de dega
##or > graterthen reight me dega