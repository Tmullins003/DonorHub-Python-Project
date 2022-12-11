"""
Goal: create a program where the end-user can continuously append data in an Excel sheet. In this case we will be
recreating a donorhub for Vagabond Missions. Where the missionaries or Development Officers can insert new donor
information. It will also do the following functions
    1. Show Fund % to end-user goal
    2. Fund life expectancy(when will I hit 0)
    3. Show and Separate One Time Gifts and Recurring Gifts
    4. Calculate total sum of funds
    5. Suggest yearly/monthly/bi-weekly/weekly income
    6. be able to read and write donors info

"""
import pandas as pd

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
