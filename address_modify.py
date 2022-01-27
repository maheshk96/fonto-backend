import pandas as pd
import numpy as np

# concat the various column data into a single column data for ease in parsing
df = pd.read_csv('sample_addresses.csv', names = ['Address','Val1','Val2'])
df['Val2'] = df['Val2'].fillna(0)
df['Val2'] = df['Val2'].astype('int')
df['Val2'] = df['Val2'].replace(0,'')
df = df.fillna('')
df['Addr'] = df['Address'].astype('str') + ' ' + df['Val1'].astype('str') + ' ' + df['Val2'].astype('str')

#Create dictionary to store postcode and state code as key-value pair
post_state_codes = dict(zip(text['postcode'].astype(str), text['state_code']))
#Create dictionary to store place + state and postcode code as key-value pair
place_post_codes = dict(zip((text['place_name'] + ' ' + text['state_code']), text['postcode'].astype(str)))
#sets to store state and post codes
state_codes = set(text['state_code'])
postcodes = set(text['postcode'])

outfile = open("new_file.csv","w")

#function to map and add the required place, state and post codes to a new column
def funcheck(sample):
  #splitting the data list
  wordlist = sample.split()

  postcode = None
  statecode = None
  place_name = None
  street = None
  if wordlist[-1] in post_state_codes:
      postcode = wordlist[-1]
      statecode = post_state_codes[postcode]
      wordlist = wordlist[:-1]
  
  if wordlist[-1] in state_codes:
      if statecode is None:
          statecode = wordlist[-1]
      # else:
      #   assert (statecode == wordlist[-1]), 'Statecode: {}, word: {}, Postcode: {}, Sample: {}'.format(statecode, wordlist[-1], postcode, sample)
  elif statecode is not None:
      wordlist.append(statecode)

  #iterating through the key-value pairing to seperate out the street value and place_name. 
  for place, std in place_post_codes.items():
      index = ' '.join(wordlist).lower().find(' ' + place.lower())
      if index != -1:
          street = ' '.join(wordlist)[:index]
          if postcode is None:
              postcode = std
          # else:
          #   assert (postcode == std), 'Postcode: {}, std: {}, Place: {}'.format(postcode, std, place)

          place_name = ' '.join(place.split()[:-1])
  

  # return the comma separated values or the string that is not found in the txt file.
  if postcode is None:
    return sample
  else:
    return ', '.join([street, place_name, statecode, postcode])


col_list = []
for i in range(df.shape[0]):
    col_list.append(funcheck(df.loc[i,'Addr']))
res = pd.DataFrame(col_list)
res
res.to_csv('python_solution.csv', encoding='utf-8', index=False)