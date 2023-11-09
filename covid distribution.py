import datetime
file = open('contacts.csv')
people = {}
found_address = []
found_people = []

person_tested = input('The person who was tested positive: ')
test_date = input('When was the test? ')

new_test_date = datetime.datetime.strptime(test_date, '%m/%d/%Y')
new_test_date = new_test_date.strftime('%m/%d/%Y')  # convert to mm/dd/yyyy

def convert_time(test_date):
    new_date = datetime.datetime.strptime(test_date, '%m/%d/%Y')
    replaced_month = str(new_date.month)
    num_to_month = [('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'),
           ('5', 'May'), ('6', 'Jun'), ('7', 'Jul'), ('8', 'Aug'),
           ('9', 'Sep'), ('10', 'Oct'), ('11', 'Nov'), 
           ('12', 'Dec')]  
    for number, month in num_to_month:  # ensure num changes to month 
        replaced_month = replaced_month.replace(number, month)
    return new_date, replaced_month


new_date, replaced_month = convert_time(test_date)

def output():
    for line in file:
        user, nhs_no, date, address = line.strip().split(',') 
        if new_test_date == date and person_tested == user:
            found_address.append(address)  # locations to be searched
        elif new_test_date == date and address in found_address:
            phrase = 'should stay at home for next 10 days due to the trip to'
            print('{} {} {} on {:02}, {} {}'.format(user, phrase, 
            address, new_date.day, replaced_month, new_date.year))
            
            
output() 
file.close()  # I used two functions for organised layout of code
