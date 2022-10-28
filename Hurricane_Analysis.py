# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def updating_damages(lst):
  new_lst = []
  for value in lst:
    if value != 'Damages not recorded':
      if value[-1] == 'M':
        new_lst.append((float(value[:-1]) * conversion['M']))
      elif value[-1] == 'B':
        new_lst.append((float(value[:-1]) * conversion['B']))
    elif value == 'Damages not recorded':
      new_lst.append('Damages not recorded')
  return new_lst

new_damages = updating_damages(damages)

# 2 
# Create a Table
# Create and view the hurricanes dictionary

def hurricanes():
  hurricanes = {}
  for i in range(len(names)):
    hurricanes[names[i]] = {'Name': names[i], 
                            'Month': months[i],
                            'Year': years[i],
                            'Max Sustained Wind': max_sustained_winds[i],
                            'Areas Affected': areas_affected[i],
                            'Damage': new_damages[i],
                            'Deaths': deaths[i]}
  return hurricanes
print(dict(hurricanes()))
hurr = dict(hurricanes())

# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key

def y_hurricanes():
  y_hurricanes = {}
  for hurricane in hurr.values():
    current_year = hurricane['Year']
    current_cane = hurricane
    if hurricane['Year'] not in y_hurricanes:
      y_hurricanes[current_year] = []
      y_hurricanes[current_year].append(hurricane)
    elif hurricane['Year'] in y_hurricanes:
      y_hurricanes[hurricane['Year']].append(hurricane)
  return y_hurricanes

#print(dict(y_hurricanes()))

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
     
def affectedareas():
  areaofhurricanes = {}
  for hurricane in hurr.values():
    for area in hurricane['Areas Affected']:
      if area not in areaofhurricanes:
        areaofhurricanes[area] = 1
      elif area in areaofhurricanes:
        areaofhurricanes[area] += 1
  return areaofhurricanes

#print(dict(affectedareas()))

affected_areas_count = dict(affectedareas())

# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in

def max_area():
  max_area = 'Central America'
  max_area_count = 0
  for area in affected_areas_count.keys():
    if affected_areas_count[area] > max_area_count:
      max_area = area
      max_area_count = affected_areas_count[area]
  return f'The area affected by the most hurricanes is {max_area}, it often {max_area_count} times.'
  
#print(max_area())

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths

def max_mortality():
  max_mortality_cane = 'Central America'
  max_mortality = 0
  for hurricane in hurr.values():
    if hurricane['Deaths'] > max_mortality:
      max_mortality_cane = hurricane['Name']
      max_mortality = hurricane['Deaths']
  return f'The most lethal hurricane was the {max_mortality_cane}, caused {max_mortality} deaths.'
  
#print(max_mortality())

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key

def hurricanes_by_mor():
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurr.values():
    if hurricane['Deaths'] <= 0:
      hurricanes_by_mortality[0].append(hurricane)
    elif hurricane['Deaths'] > 0 and hurricane['Deaths'] <= 99:
      hurricanes_by_mortality[1].append(hurricane)
    elif hurricane['Deaths'] >= 100 and hurricane['Deaths'] <= 499:
      hurricanes_by_mortality[2].append(hurricane)
    elif hurricane['Deaths'] >= 500 and hurricane['Deaths'] <= 999:
      hurricanes_by_mortality[3].append(hurricane)
    elif hurricane['Deaths'] >= 1000 and hurricane['Deaths'] <= 9999:
      hurricanes_by_mortality[4].append(hurricane) 
    elif hurricane['Deaths'] >= 10000:
      hurricanes_by_mortality[5].append(hurricane)
  return hurricanes_by_mortality

#print(hurricanes_by_mor())

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

def max_damage():
  max_damage_cane = 'Cuba I'
  max_damage = 0
  for hurricane in hurr.values():
    if hurricane['Damage'] != 'Damages not recorded':
      if hurricane['Damage'] > max_damage:
        max_damage_cane = hurricane['Name']
        max_damage = hurricane['Damage']
        return f'The hurricane that caused the greatest damage was {max_damage_cane}, and the cost was {max_damage}'
  
print(max_damage())

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def hurricanes_by_dam():
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurr.values():
    if hurricane['Damage'] != 'Damages not recorded':
      if hurricane['Damage'] <= 0:
        hurricanes_by_damage[0].append(hurricane)
      elif hurricane['Damage'] > 0 and hurricane['Damage'] <= 99999999:
        hurricanes_by_damage[1].append(hurricane)
      elif hurricane['Damage'] >= 100000000 and hurricane['Damage'] <= 999999999:
        hurricanes_by_damage[2].append(hurricane)
      elif hurricane['Damage'] >= 1000000000 and hurricane['Damage'] <= 9999999999:
        hurricanes_by_damage[3].append(hurricane)
      elif hurricane['Damage'] >= 10000000000 and hurricane['Damage'] <= 99999999999:
        hurricanes_by_damage[4].append(hurricane) 
      elif hurricane['Damage'] >= 50000000000:
        hurricanes_by_damage[5].append(hurricane)
  return hurricanes_by_damage
  
# categorize hurricanes in new dictionary with damage severity as key

print(hurricanes_by_dam())
