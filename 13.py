Name=input("What's your name")
name_length=(len(Name))
if name_length<3:
    print("Name must be at least 3 characters")
    
elif name_length>50:
    print('Name can be a maximum of 25 characters')
          
else:
    print('Name looks good')
