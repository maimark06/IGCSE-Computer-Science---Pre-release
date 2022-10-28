#Lists
ticket_type=['adult','child','senior','family','group']
cost_1day=[20.00,12.00,16.00,60.00,15.00]
cost_2day=[30.00,18.00,24.00,90.00,22.50]
ext_attraction=['lion feeding','penguin feeding','evening barbecue (two-day tickets only)']
cost_per_person=[2.50,2.00,5.00]
visit_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
#Menu
print('one day visit'.upper().center(60))
print('CATEEGORY - PRICE($)')
for count in range(0,5):
  print(ticket_type[count],'-',cost_1day[count])
print('two day visit'.upper().center(60))
print('CATEEGORY - PRICE($)')
for count in range(0,5):
  print(ticket_type[count],'-',cost_2day[count])
print('extra attraction per person'.upper().center(65))
print('CATEEGORY - PRICE($)')
for count in range(0,3):
  print(ext_attraction[count],'-',cost_per_person[count])
print()
print('1. One-Day Pass')
print('2. Two-Day Pass')

while True:
  tickettype_choice=input('Enter Choice of Pass [1 or 2]: ')
  if tickettype_choice== '1' or tickettype_choice== '2':
    break

print()
print('visiting days'.upper())
for i in range(7):
  print(i+1,'.  ',end='')
  print(visit_days[i])
while True:
  while True:
    try:
      visitdays_choice=int(input('Enter day of your visit [1-7]: '))
      flag=True
    except ValueError:
      print('Please enter an Integer')
      flag=False
    if flag==True:
      break
  if visitdays_choice <= 7 and visitdays_choice >=1:
    break
#calculator
print()
while True:
  try:
    print()
    adults=int(input('Enter number of adults: '))
    seniors=int(input('Enter number of seniors: '))
    childs=int(input('Enter number of children: '))
    flag=True
  except ValueError:
    print('Enter Integer Only')
    flag=False
  if flag==True:
    break

if tickettype_choice =='1':
  print('Extra ticket: lion feeding')
  while True:
    try:
      lionfeed_ticket=int(input('Extra ticket: '))
      flag=True
    except ValueError:
      print('Enter Integers Only')
      flag=False
    if flag==True:
      break
  while True:
    print('Extra ticket: penguin feeding')
    try:
      penguinfeed_ticket=int(input('Extra ticket: '))
      flag=True
    except ValueError:
      print('Enter Integers Only')
      print()
      flag=False
    if flag==True:
      break
  barbecue_ticket=0

if tickettype_choice =='2':
  print('Extra ticket: lion feeding')
  while True:
    try:
      lionfeed_ticket=int(input('Extra ticket: '))
      flag=True
    except ValueError:
      print('Enter Integers Only')
      flag=False
    if flag==True:
      break
  while True:
    print('Extra ticket: penguin feeding')
    try:
      penguinfeed_ticket=int(input('Extra ticket: '))
      flag=True
    except ValueError:
      print('Enter Integers Only')
      print()
      flag=False
    if flag==True:
      break
  while True:
    print('Extra ticket: evening barbecue')
    try:
      barbecue_ticket=int(input('Extra ticket: '))
      flag=True
    except ValueError:
      print('Enter Integers Only')
      print()
      flag=False
    if flag==True:
      break


  
  
  
  
print()
print()
print('Your Choices'.upper().center(60))
if tickettype_choice=='1':
    print_type='One-Day Ticket'
    print_day=visit_days[visitdays_choice-1]
    print_adultcost=cost_1day[0]
    print_seniorcost=cost_1day[1]
    print_childcost=cost_1day[2]
    print_barbecue=0
elif tickettype_choice=='2':
    print_type='Two-Day Ticket'
    print_day=visit_days[visitdays_choice-1] + ' and '+ visit_days[visitdays_choice]
    print_adultcost=cost_2day[0]
    print_seniorcost=cost_2day[1]
    print_childcost=cost_2day[2]
    print_barbecue=5.00
print(f'Choice of Pass: {print_type}')
print(f'Visiting Days: {print_day}')
print(f'Adult(s) - {adults} * ${print_adultcost} = ${adults*print_adultcost}')
print(f'Senior(s) - {seniors} * ${print_seniorcost} = ${seniors*print_seniorcost}')
print(f'Child(s) - {childs} * ${print_childcost} = ${childs*print_childcost}')
print(f'Lion feeding - {lionfeed_ticket} * ${2.50} = ${lionfeed_ticket*2.50}')
print(f'Penguin feeding - {penguinfeed_ticket} * ${2.00} = ${penguinfeed_ticket*2.00}')
print(f'Barbecue feeding - {barbecue_ticket} * ${print_barbecue} = ${barbecue_ticket*print_barbecue}')
total=adults*print_adultcost+seniors*print_seniorcost+childs*print_childcost+lionfeed_ticket*2.50+penguinfeed_ticket*2.00+barbecue_ticket*print_barbecue
print(f'TOTAL - ${total}')



print()
total_member=adults+seniors+childs
if tickettype_choice=='1':
  if total_member >= 6:
    print('Group set option')
    print(f'Total memmbers: {total_member}')
    print('Price per person: $15.00')
    groupprice=total_member*15.0+lionfeed_ticket*2.50+penguinfeed_ticket*2.00+barbecue_ticket*0
    print(f'Group Price: ${groupprice}')
  else:
    print('Group set option')
    print(f'Total memmbers: {total_member}')
    print('Not Available')
    groupprice=999999999999
elif tickettype_choice=='2':
  if total_member >= 6:
    print('Group set option')
    print(f'Total memmbers: {total_member}')
    print('Price per person: $22.50')
    groupprice=total_member*22.50+lionfeed_ticket*2.50+penguinfeed_ticket*2.00+barbecue_ticket*5
    print(f'Group Price: ${groupprice}')
  else:
    print('Group set option')
    print(f'Total memmbers: {total_member}')
    print('Not Available')
    groupprice=999999999999

print()
if tickettype_choice=='1':
    if (adults//2)>0 and (childs//3) >0:
      noadults_notin=adults-(adults//2)*2
      nochilds_notin=(childs)-(childs//3)*3
      familyprice=(adults//2)*60 + noadults_notin*20 + nochilds_notin*12+lionfeed_ticket*2.50+penguinfeed_ticket*2.00+barbecue_ticket*0+seniors*16
      print('Family option')
      print('Price per family packs: $60')
      print(f'Family Price: ${familyprice}')
      print()
    else:
      familyprice=99999999999
      print('Family option')
      print('Price per family packs: $60')
      print('Not Available')
elif tickettype_choice=='2':
    if (adults//2)>0 and (childs//3) >0:
      noadults_notin=(adults)-(adults//2)*2
      nochilds_notin=(childs)-(childs//3)*3
      familyprice=(adults//2)*60 + noadults_notin*30 + nochilds_notin*24+lionfeed_ticket*2.50+penguinfeed_ticket*2.00+barbecue_ticket*5+seniors*24
      print('Family option')
      print('Price per family packs: $60')
      print(f'Family Price: ${familyprice}')
      print()
    else:
      familyprice=99999999999
      print('Family option')
      print('Price per family packs: $60')
      print('Not Available')
      
print()
if total<groupprice and total<familyprice:
  print(f'We recommend the TOTAL package: ${total}')
  print(f'Please purchase: ${total}')
elif groupprice<total and groupprice<familyprice:
  print(f'We recommend the GROUP package: ${groupprice}')
  print(f'Please purchase: ${groupprice}')
elif familyprice<groupprice and familyprice<total:
  print(f'We recommend the FAMILY package: ${familyprice}')
  print(f'Please purchase: ${familyprice}')