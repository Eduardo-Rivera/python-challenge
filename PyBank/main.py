import os
import csv

with open ("budget_data.csv", "r") as file:
    budget_data = csv.reader(file)


    #skip header
    next(budget_data)

    #Define variables
    line_counter = 0
    total_sum = 0
    profit_change = 0
    previous = 0
    profit_change_list = []
    months_list = []
   
    
    for i in budget_data:
        #Total number of months
        line_counter += 1            
        
        #Total amount of profit/losses
        total_sum += int(i[1]) 

        #Average of changes    
        profit_change = int(i[1]) - previous 
        previous = int(i[1])     
        profit_change_list.append(profit_change)
        total_change = (sum(profit_change_list[1:87]))
        
        #Greatest increase/decrease
        months = i[0] 
        months_list.append(months) #Month list
    months_list.pop(0) #Remove first month of list
    av_chg = profit_change_list[1:87] #Profit changes list
    my_dict = dict(zip(months_list, av_chg)) #Create dictionary with months and profit changes
    greatest_increase_month = max(my_dict,key=my_dict.get)
    greatest_decrease_month = min(my_dict,key=my_dict.get)
    
    #From average of changes
    avg_change = total_change/85
    avg_change = round(avg_change,2)
    
print("Financial Analysis \n-----------------------")
print(f'Total Months: {line_counter}')
print(f'Total: $ {total_sum}')  
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${my_dict[greatest_increase_month]})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${my_dict[greatest_decrease_month]})')


# output = "Financial Analysis \n \
# ------------------------\n
# ")
# print(f'Total Months: {line_counter}'

output = (
    "Financial Analysis\n"
    "------------------------\n"
    f'Total Months: {line_counter}\n'
    f'Total: $ {total_sum}\n' 
    #calculate avg change in profit/losses over time period
    f'Average Change: ${avg_change}\n'
    f'Greatest Increase in Profits: {greatest_increase_month} (${my_dict[greatest_increase_month]})\n'
    f'Greatest Decrease in Profits: {greatest_decrease_month} (${my_dict[greatest_decrease_month]})')

with open("output.txt", "w") as the_file:
    the_file.write(output)

        