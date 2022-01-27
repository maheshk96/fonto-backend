# fonto-backend

The files present in this repo is the python code for the problem of storing the address and other information in the given system. 
This solution required modifying the existing csv file provided with the help of the .txt in order to create the solution csv with the appropriate 
comma seprated string stored.

The problems and assumptions for the given problem : 

1) The 'Chatswood' entry had the postcode stored as '3067' which is matched with the state code of 'Vic'. This is contrary to the entry in the original csv file where the address referenced a 'NSW' address and the 'Chatswood' entry was matched to a postcode of '2067'. For programming purposes, the 'Vic' address is referenced in the final CSV so as to not tamper with the original CSV file provided.
2) The 'Crows Nest' entry had two pincodes return within 'NSW'.
3) The entry for Pensylvania could not be matched with the existing txt file and hence could not return the required value for state or postcode.
4) The 'Freshwater' entry was present in two state codes 'NSW' and 'QLD'. This needed additional effort in order to seperate them out.
