def calculate_monthly_payments_equal_principal(principal, annual_interest_rate, loan_years):

    number_of_payments = loan_years * 12

    monthly_interest_rate = annual_interest_rate / 12

    monthly_principal = principal / number_of_payments

    monthly_payments = []
    remaining_principal = principal


    for i in range(number_of_payments):
        monthly_interest = remaining_principal * monthly_interest_rate
        monthly_payments.append(monthly_principal + monthly_interest)
        remaining_principal -= monthly_principal

    return monthly_payments

principal = 202315050415
annual_interest_rate = 0.05
loan_years = 10

monthly_payments = calculate_monthly_payments_equal_principal(principal, annual_interest_rate, loan_years)

print(
    f"如果你贷款 {principal} 元，年利率 {annual_interest_rate * 100:.2f}%，贷款期限 {loan_years} 年，每月需要还款的金额如下:")
for i, payment in enumerate(monthly_payments, start=1):
    print(f"第 {i} 个月需还款: {payment:.2f} 元")
