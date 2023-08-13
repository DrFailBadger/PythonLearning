# function outputs

def format_name(f_name,l_name):
  first = f_name.title()
  last = l_name.title()
  fullname = f"{first} {last}"
  #print(fullname)
  return fullname

capname = format_name("david", "HASASADislop")
print(format_name("david", "HASASADislop"))
print(capname)

# function outputs

def format_name(f_name,l_name):
  if  f_name == "" or l_name == "":
    return "You did not provide a value for first name or last name"
  first = f_name.title()
  last = l_name.title()
  fullname = f"{first} {last}"
  #print(fullname)
  return fullname

#capname = format_name("david", "HASASADislop")
#print(format_name("david", "HASASADislop"))
#print(capname)