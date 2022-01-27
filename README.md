# fonto-backend

The files present in this repo is the python code for the problem of storing the address and other information in the given system. 
This solution required modifying the existing CSV file provided with the help of the .txt in order to create the solution CSV with the appropriate comma-separated string stored.

The problems and assumptions for the given problem -
1)The 'Chatswood' entry had the postcode stored as '3067' which is matched with the state code of 'Vic'. This is contrary to the entry in the original CSV file where the address referenced an 'NSW' address and the 'Chatswood' entry was matched to a postcode of '2067'. For programming purposes, the 'Vic' address is referenced in the final CSV so as to not tamper with the original CSV file provided.

2)The 'Crows Nest' entry had two pin codes return within 'NSW'.

3)The entry for Pennsylvania could not be matched with the existing txt file and hence could not return the required value for state or postcode.

4)The 'Freshwater' entry was present in two-state codes 'NSW' and 'QLD'. This needed additional effort in order to separate them out.

Design -
The process of writing the code for the given problem is explained in much greater detail through the documentation present in the python code itself. 
The gist of it was to try to separate out the single column of data into individual columns and find the missing data that was present in any of them. 
The next step was to create a wordlist which in turn will be truncated with the data that has been found during the process. 
This complete data is then truncated to form the new CSV file. 

The python file can be run on a development environment with the required .csv and .txt files and the resultant result .csv file mentioned will be created with the required tabular data. 
