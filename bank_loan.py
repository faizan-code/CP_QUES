#Question – : There are two banks – Bank A and Bank B.
# Their interest rates vary. You have received offers
# from both banks in terms of the annual rate of interest,
# tenure, and variations of the rate of interest over
# the entire tenure.You have to choose the offer which
# costs you least interest and reject the other. Do the computation and make a wise choice.
# The loan repayment happens at a monthly frequency and
# Equated Monthly Installment (EMI) is calculated using
# the formula given below :

# EMI = loanAmount * monthlyInterestRate / ( 1 – 1 / (1 + monthlyInterestRate)^(numberOfYears * 12))

# Constraints:
# 1 <= P <= 1000000
# 1 <=T <= 50
# 1<= N1 <= 30
# 1<= N2 <= 30
# Input Format:
# First line: P principal (Loan Amount)
# Second line: T Total Tenure (in years).
# Third Line: N1 is the number of slabs of interest rates for a given period by Bank A. First slab starts from the first year and the second slab starts from the end of the first slab and so on.
# Next N1 line will contain the interest rate and their period.
# After N1 lines we will receive N2 viz. the number of slabs offered by the second bank.
# Next N2 lines are the number of slabs of interest rates for a given period by Bank B. The first slab starts from the first year and the second slab starts from the end of the first slab and so on.
# The period and rate will be delimited by single white space.
 #Output Format: Your decision either Bank A or Bank B.





