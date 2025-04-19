def calculate_thai_tax(income_thb):
    brackets = [
        (150000, 0.00),
        (300000, 0.05),
        (500000, 0.10),
        (750000, 0.15),
        (1000000, 0.20),
        (2000000, 0.25),
        (5000000, 0.30),
        (float('inf'), 0.35)
    ]

    tax = 0.0
    prev_limit = 0.0

    for limit, rate in brackets:
        if income_thb > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income_thb - prev_limit) * rate
            break

    return (round(income_thb/5.08),round((income_thb-tax)/5.08),round(tax/5.08),round(100*(1-((income_thb-tax)/income_thb))))

x1=800000*5.08
print(calculate_thai_tax(x1))