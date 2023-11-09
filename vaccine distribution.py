site = input('Vaccination site? ').upper()
total_cost = 0  # set total to 0 so it has starting point
vaccine_table = [] 
result = []  
while(3):  # three for three types of vaccines
    vacc_type = input('Vaccine type? ').upper()
    if vacc_type != '':
        vaccine_table.append(vacc_type)
        vacc_no = int(input('Number of vaccines requested? '))
        shipping_fee = float(input('Shipping fee per 100 doses? '))
        cost = (vacc_no * shipping_fee) /100
        total_cost += cost   # adds cost up each time
        vacc_no = str(vacc_no)
        vaccine_table.append(vacc_no)
        cost_round = ('%.2f' % cost)  # format cost to 2dp
        cost = str(cost_round)
        vaccine_table.append(cost)  # add vacc_type, vacc_no and cost 
    else:  # ends loop when name of vaccine is empty
        break

for z in range(0, len(vaccine_table), 3):  # splits the list into 3
    result.append(vaccine_table[z:z +3])  # (type,no and cost)
    
vat = total_cost / 6  # calculate vat standard rate
cash_paid = int(input('Cash paid? ')) 
change = cash_paid - total_cost 

space = " "  # easier to format than pressing spacebar 
print(f'VACCINES2U{space*16}SHIPPING ORDER')
print('VAT GB123456789 {1: >{0}}'.format(24, site))  # indicate a start and end
print('')  
print(f'Vaccine{space*19}Qty.{space*6}Cost')
for row in result:  # prints to number of columns needed
    print('{: <15} {: >14} {: >9}'.format(*row))  
print('')  # now format all money values to 2dp
print('TOTAL {1: >{0}}'.format(34, ('%.2f' % total_cost)))  
print('VAT INCLUDED IN TOTAL{1: >{0}}'.format(19, ('%.2f' %vat)))
print('CASH PAID{1: >{0}}'.format(31, ('%.2f' % cash_paid)))
print('CHANGE{1: >{0}}'.format(34, ('%.2f' % change)))

