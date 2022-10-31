# Password generator using string and secrets module 

import string, secrets 

Characters = string.ascii_letters + string.digits 

Password = ''.join(secrets.choice(Characters) for i in range (8))

print ("Your Generated Password Is >>> ", Password)
