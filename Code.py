class Solution(object):
   def validIPAddress(self, IP):
      def isIPv4(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False
      if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
         return "IPv4"

ob = Solution()
print("Enter 10 ip addresses: ")
lis = []
every = []
for x in range(10):
    lis.append(input("Enter address {}: ".format(x + 1)))
    print(ob.validIPAddress(lis[x]))
    ipa=lis[x]
    parts = ipa.split('.')

    #decimal
    every.append(ipa)

    # Binary
    bin2='0b'
    for part in parts:
        bin2 += format(int(part),'08b')
    every.append(bin2)

    #Octal
    oct2 = '0o'
    for part in parts:
      oct2 += format(int(part), '04o')
    every.append(oct2)

    # Hexadecimal
    hex2='0x'
    for part in parts:
        hex2 += format(int(part),'02x')
    every.append(hex2)

dic = {1:"first", 2:"second", 3:"third", 4:"fourth", 5:"fifth", 6:"sixth", 7:"seventh", 8:"eighth", 9:"ninth", 10:"tenth"}
f = open("conversion.txt", "w")
for i in range(len(every)):
   f.write(every[i])
   f.write("\n")

f.close()
f = open("conversion.txt")
for i in range(len(every) // 4):
   print("The " + dic[i+1] + "IP address in Decimal, Binary, Octal and hexadecimal format is \n" + f.readline() + " " + f.readline() + " " + f.readline() + " " + f.readline())
f.close()