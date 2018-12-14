import csv
import datetime

filepath = "Resources_pyboss/employee_data.csv"
emp=[]
name=None
dob=None
ssn=None
state=None
namemodified=[]
statemodified=[]
first=[]
last=[]
dobmodified=[]
ssnmodified=[]
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
with open(filepath, 'r') as bossdata:
    bossreader = csv.reader(bossdata, delimiter=',')
    bossheader=next(bossreader)
    for row in bossreader:
        emp.append(row[0])
        name=row[1]
        dob=datetime.datetime.strptime(row[2], "%Y-%m-%d")
        ssn="***-**-"+row[3][7:]
        state=row[4]
        namemodified=name.split()
        first.append(namemodified[0])
        last.append(namemodified[1])
        dobmodified.append(datetime.date.strftime(dob,"%m/%d/%y"))
        ssnmodified.append(ssn)
        statemodified.append(us_state_abbrev[state])
finaldata= zip(emp, first, last, dobmodified, ssnmodified, statemodified)

output_file = "Resources_pyboss/output.csv"

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First", "Last", "DOB","SSN", "State"])

    # Write in zipped rows
    writer.writerows(finaldata)

        
        
        
