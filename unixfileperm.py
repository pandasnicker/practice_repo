
perms = {'0':'---'
         ,'1':'--x'
         ,'2':'-w-'
         ,'3':'-wx'
         ,'4':'r--'
         ,'5':'r-x'
         ,'6':'rw-'
         ,'7':'rwx'
         }

def printUnixStylePerms(permsissionStr):
   res = ''
   for i in permsissionStr:
      res += perms.get(i)
   return res