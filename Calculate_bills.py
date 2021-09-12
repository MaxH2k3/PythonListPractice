def cal_bills(TotalAmount, bills):
    work_job = [("waiter", 200000), ("sailer", 200000), ("grab", 200000), ("shipper", 150000)]
    SumBills = 0
    Part_Time_Job = []
    for index in range(0, len(bills)):
        SumBills += bills[index][1]
    Change_Money = TotalAmount - SumBills
    if bills == []:
    	print("This month you have any bills")
    else:
	    if Change_Money > 0:
	        print("This month enough, greet!, change: ", Change_Money)
	    elif Change_Money == 0:
	        print("You should use save money more, change: ", Change_Money)
	    else:
	        print("This month not enough to pay bills, change: ", Change_Money)
	        for i in range(0, len(work_job)):
	            if Change_Money >= 0:
	                break
	            Change_Money = Change_Money + work_job[i][1]
	            Part_Time_Job.append(work_job[i])
	        print("I have some job for you to ear money to pay your bills this month: ", Part_Time_Job)


#Exemple 1
TotalAmount = 1500000
bills = [("Electric", 200000), ("Water", 60000), ("Food", 1500000), ("Entertainment", 200000), ("House", 500000), ("Another", 300000)]
cal_bills(TotalAmount, bills)

#Exemple 2
TotalAmount = 10000
bills = []
cal_bills(TotalAmount, bills)

#Exemple 3
TotalAmount = 0
bills = []
cal_bills(TotalAmount, bills)
