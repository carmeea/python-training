# Sales Report Processing
sales = [120, 150, 170, 100]
# a - total sales for the quarter
total_sales = sum(sales)
print(total_sales)
# b- average sales per month
len_sales = len(sales)
avg_sales = (total_sales/len_sales)
print(avg_sales)
#c 
print("This is the total number of sales: {:.2f}".format(total_sales),"\nThis is the average of sales per month: {:.2f}".format(avg_sales))
print("OR")
print("This is the total number of sales: %.2f"%total_sales,"\nThis is the average of sales per month: %.2f"%avg_sales)