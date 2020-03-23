# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/family-planning.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("State-wise [ India ] Current use of family planning methods :");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")


# Question - C : print available states/UT

df1 = df['India-States-Union Territories']

print('---------------------------------------------')
print('Available data for following State and UT  : ')
print('---------------------------------------------')
print(df1)
print('---------------------------------------------')


# Question - D : Using any method

plt.title('Question - D : Using any method ')
plt.xlabel("State/UT sl no. --- >")
plt.ylabel("Number of uses --- >")
    
df_any_total = df['Any method - Total']

plt.plot(df_any_total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Any method - Total ")

df_any_rural = df['Any method - Rural']
                     
plt.plot(df_any_rural,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Any method - Rural")
            
df_any_urban = df['Any method - Urban']

plt.plot(df_any_urban,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Any method - Urban")

plt.legend()
plt.show()

# Question - E : Using any " MODERN " method

plt.title('Question - E : Using any " MODERN " method')
plt.xlabel("State/UT sl no. --- >")
plt.ylabel("Number of uses --- >")
    
df_any_mod_total = df['Any modern method - Total']

plt.plot(df_any_mod_total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Any modern method - Total")

df_any_mod_rural = df['Any modern method - Rural']
                     
plt.plot(df_any_mod_rural,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Any modern method - Rural")
            
df_any_mod_urban = df['Any modern method - Urban']

plt.plot(df_any_mod_urban,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3]  Any modern method - Urban")

plt.legend()
plt.show()

# Question - F : Sterilisation ( Female + Male )

plt.title('Question - F : Sterilisation ( Female + Male )')
plt.xlabel("State/UT sl no. --- >")
plt.ylabel("Number of uses --- >")
    
df_ste_total = df['Sterilisation - Total']

plt.plot(df_ste_total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Sterilisation - Total")

df_ste_rural = df['Sterilisation - Rural']
                     
plt.plot(df_ste_rural,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Sterilisation - Rural")
            
df_ste_urban = df['Sterilisation - Urban']

plt.plot(df_ste_urban,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Sterilisation - Urban")

plt.legend()
plt.show()

# Question - G : Female Sterilisation

plt.title('Question - G : Female Sterilisation')
plt.xlabel("State/UT sl no. --- >")
plt.ylabel("Number of uses --- >")
    
df_ste_female_total = df['Female sterilization - Total']

plt.plot(df_ste_female_total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Female sterilization - Total")

df_ste_female_rural = df['Female sterilization - Rural']
                     
plt.plot(df_ste_female_rural,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Female sterilization - Rural")
            
df_ste_female_urban = df['Female sterilization - Urban']

plt.plot(df_ste_female_urban,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Female sterilization - Urban")

plt.legend()
plt.show()

# Question - H : Male Sterilisation

plt.title('Question - H : Male Sterilisation')
plt.xlabel("State/UT sl no. --- >")
plt.ylabel("Number of uses --- >")
    
df_ste_male_total = df['Male sterilisation - Total']

plt.plot(df_ste_male_total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Male sterilisation - Total")

df_ste_male_rural = df['Male sterilisation - Rural']
                     
plt.plot(df_ste_male_rural,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Male sterilisation - Rural")
            
df_ste_male_urban = df['Male sterilisation - Urban']

plt.plot(df_ste_male_urban,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Male sterilisation - Urban")

plt.legend()
plt.show()

# Question - I : IUD/PPIUD

plt.title('Question - I : IUD/PPIUD')
plt.xlabel("State/UT sl no. --- >")
plt.ylabel("Number of uses --- >")
    
df_iud_total = df['IUD/PPIUD - Total']

plt.plot(df_iud_total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] IUD/PPIUD - Total")

df_iud_rural = df['IUD/PPIUD - Rural']
                     
plt.plot(df_ste_male_rural,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] IUD/PPIUD - Rural")
            
df_iud_urban = df['IUD/PPIUD - Urban']

plt.plot(df_iud_urban,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] IUD/PPIUD - Urban")

plt.legend()
plt.show()

# Question - J : Pill using

plt.title('Question - J : Pill using')
plt.xlabel("State/UT sl no. --- >")
plt.ylabel("Number of uses --- >")
    
df_pill_total = df['Pill - Total']

plt.plot(df_pill_total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Pill - Total")

df_pill_rural = df['Pill - Rural']
                     
plt.plot(df_pill_rural,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Pill - Rural")
            
df_pill_urban = df['Pill - Urban']

plt.plot(df_pill_urban,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Pill - Urban")

plt.legend()
plt.show()

# Question - K : Condom use

plt.title('Question - K : Condom use')
plt.xlabel("State/UT sl no. --- >")
plt.ylabel("Number of uses --- >")
    
df_condom_total = df['Condom - Total']

plt.plot(df_condom_total,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Condom - Total")

df_condom_rural = df['Condom - Rural']
                     
plt.plot(df_condom_rural,
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Condom - Rural")
            
df_condom_urban = df['Condom - Urban']

plt.plot(df_condom_urban,
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Condom - Urban")

plt.legend()
plt.show()


