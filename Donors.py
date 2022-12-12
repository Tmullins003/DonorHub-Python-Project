"""
Goal: create a program where the end-user can continuously append data in an Excel sheet. In this case we will be
recreating a donor-hub for Vagabond Missions. Where the missionaries or Development Officers can dp the following
functions:
    1. Show Fund % to end-user goal
    2. Fund life expectancy(when will I hit 0)
    3. Show and Separate One Time Gifts and Recurring Gifts
    4. Calculate total sum of funds
    5. Suggest yearly/monthly/bi-weekly/weekly income
    6. be able to read and write donors info

"""

'''
df = pd.DataFrame(columns=["Donor ID", "Donor Name", "Amount Donated"])
donorInput = int(input("Enter how many NEW donors: "))

for _ in range(donorInput):
    donorID = int(input("Enter Donor ID: "))
    donorName = input("Enter Donor Name: ")
    donorGift = int(input("Enter Amount Donated: "))
    df1 = pd.DataFrame(data=[[donorID, donorName, donorGift]], columns=["Donor ID", "Donor Name", "Amount Donated"])
    df = pd.concat([df, df1], axis=0)

df.index = range(len(df.index))

print(df)
df.to_excel(r'D:\CodingProjects\DonorProject\Donors.xlsx', sheet_name='Sheet 1', index=False)  # writes to Excel file
this could be used to write to a new sheet and then combine to the old sheet therefore creating a continuous updated sheet
'''
# Right now were going to focus on just reading from a given xlsx then worry about appending it from a user later

import pandas as pd

donor_file = pd.read_excel('D:\CodingProjects\DonorProject\Donors.xlsx', sheet_name='RCG', index_col='Donor ID')
donor_file2 = pd.read_excel('D:\CodingProjects\DonorProject\Donors.xlsx', sheet_name='OTG', index_col='Donor ID')
df = pd.DataFrame(donor_file)
df2 = pd.DataFrame(donor_file2)
print(df,'\n\n', df2)
t1 = df['Gift Amount'].sum()
t2 = df2['Gift Amount'].sum()
fundTotal = (df['Gift Amount'].sum() * 12) + df2['Gift Amount'].sum()
print('Yearly Sum:', fundTotal)
print('Monthly Sum:', fundTotal / 12)
print('Bi-Weekly Sum:', fundTotal / 26)
print('Weekly Sum:', fundTotal / 52)