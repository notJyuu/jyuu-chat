def cetr2012(income):
    # -----------------------------
    # Federal Tax Brackets
    # -----------------------------
    federal_bracket_1 = 42707
    federal_bracket_2 = 85414
    federal_bracket_3 = 132406

    federal_rate_1 = 0.15
    federal_rate_2 = 0.22
    federal_rate_3 = 0.26
    federal_rate_4 = 0.29

    federal_tax = 0

    if income <= federal_bracket_1:
        federal_tax = income * federal_rate_1
    elif income <= federal_bracket_2:
        federal_tax = federal_bracket_1 * federal_rate_1
        federal_tax += (income - federal_bracket_1) * federal_rate_2
    elif income <= federal_bracket_3:
        federal_tax = federal_bracket_1 * federal_rate_1
        federal_tax += (federal_bracket_2 - federal_bracket_1) * federal_rate_2
        federal_tax += (income - federal_bracket_2) * federal_rate_3
    else:
        federal_tax = federal_bracket_1 * federal_rate_1
        federal_tax += (federal_bracket_2 - federal_bracket_1) * federal_rate_2
        federal_tax += (federal_bracket_3 - federal_bracket_2) * federal_rate_3
        federal_tax += (income - federal_bracket_3) * federal_rate_4

    # -----------------------------
    # Ontario Tax Brackets
    # -----------------------------
    ontario_bracket_1 = 39020
    ontario_bracket_2 = 78043
    ontario_bracket_3 = 500000

    ontario_rate_1 = 0.0505
    ontario_rate_2 = 0.0915
    ontario_rate_3 = 0.1116
    ontario_rate_4 = 0.1216

    ontario_tax = 0

    if income <= ontario_bracket_1:
        ontario_tax = income * ontario_rate_1
    elif income <= ontario_bracket_2:
        ontario_tax = ontario_bracket_1 * ontario_rate_1
        ontario_tax += (income - ontario_bracket_1) * ontario_rate_2
    elif income <= ontario_bracket_3:
        ontario_tax = ontario_bracket_1 * ontario_rate_1
        ontario_tax += (ontario_bracket_2 - ontario_bracket_1) * ontario_rate_2
        ontario_tax += (income - ontario_bracket_2) * ontario_rate_3
    else:
        ontario_tax = ontario_bracket_1 * ontario_rate_1
        ontario_tax += (ontario_bracket_2 - ontario_bracket_1) * ontario_rate_2
        ontario_tax += (ontario_bracket_3 - ontario_bracket_2) * ontario_rate_3
        ontario_tax += (income - ontario_bracket_3) * ontario_rate_4

    # -----------------------------
    # Total & Effective Rate
    # -----------------------------
    total_tax = federal_tax + ontario_tax
    effective_rate = (total_tax / income) * 100

    return effective_rate


def cetr2020(income):
    # -----------------------------
    # Federal Tax Brackets (2020)
    # -----------------------------
    federal_bracket_1 = 48535
    federal_bracket_2 = 97069
    federal_bracket_3 = 150473
    federal_bracket_4 = 214368

    federal_rate_1 = 0.15
    federal_rate_2 = 0.205
    federal_rate_3 = 0.26
    federal_rate_4 = 0.29
    federal_rate_5 = 0.33

    federal_tax = 0

    if income <= federal_bracket_1:
        federal_tax = income * federal_rate_1
    elif income <= federal_bracket_2:
        federal_tax = federal_bracket_1 * federal_rate_1
        federal_tax += (income - federal_bracket_1) * federal_rate_2
    elif income <= federal_bracket_3:
        federal_tax = federal_bracket_1 * federal_rate_1
        federal_tax += (federal_bracket_2 - federal_bracket_1) * federal_rate_2
        federal_tax += (income - federal_bracket_2) * federal_rate_3
    elif income <= federal_bracket_4:
        federal_tax = federal_bracket_1 * federal_rate_1
        federal_tax += (federal_bracket_2 - federal_bracket_1) * federal_rate_2
        federal_tax += (federal_bracket_3 - federal_bracket_2) * federal_rate_3
        federal_tax += (income - federal_bracket_3) * federal_rate_4
    else:
        federal_tax = federal_bracket_1 * federal_rate_1
        federal_tax += (federal_bracket_2 - federal_bracket_1) * federal_rate_2
        federal_tax += (federal_bracket_3 - federal_bracket_2) * federal_rate_3
        federal_tax += (federal_bracket_4 - federal_bracket_3) * federal_rate_4
        federal_tax += (income - federal_bracket_4) * federal_rate_5

    # -----------------------------
    # Ontario Tax Brackets (2020)
    # -----------------------------
    ontario_bracket_1 = 44740
    ontario_bracket_2 = 89482
    ontario_bracket_3 = 150000
    ontario_bracket_4 = 220000

    ontario_rate_1 = 0.0505
    ontario_rate_2 = 0.0915
    ontario_rate_3 = 0.1116
    ontario_rate_4 = 0.1216
    ontario_rate_5 = 0.1316

    ontario_tax = 0

    if income <= ontario_bracket_1:
        ontario_tax = income * ontario_rate_1
    elif income <= ontario_bracket_2:
        ontario_tax = ontario_bracket_1 * ontario_rate_1
        ontario_tax += (income - ontario_bracket_1) * ontario_rate_2
    elif income <= ontario_bracket_3:
        ontario_tax = ontario_bracket_1 * ontario_rate_1
        ontario_tax += (ontario_bracket_2 - ontario_bracket_1) * ontario_rate_2
        ontario_tax += (income - ontario_bracket_2) * ontario_rate_3
    elif income <= ontario_bracket_4:
        ontario_tax = ontario_bracket_1 * ontario_rate_1
        ontario_tax += (ontario_bracket_2 - ontario_bracket_1) * ontario_rate_2
        ontario_tax += (ontario_bracket_3 - ontario_bracket_2) * ontario_rate_3
        ontario_tax += (income - ontario_bracket_3) * ontario_rate_4
    else:
        ontario_tax = ontario_bracket_1 * ontario_rate_1
        ontario_tax += (ontario_bracket_2 - ontario_bracket_1) * ontario_rate_2
        ontario_tax += (ontario_bracket_3 - ontario_bracket_2) * ontario_rate_3
        ontario_tax += (ontario_bracket_4 - ontario_bracket_3) * ontario_rate_4
        ontario_tax += (income - ontario_bracket_4) * ontario_rate_5

    # -----------------------------
    # Total & Effective Rate
    # -----------------------------
    total_tax = federal_tax + ontario_tax
    effective_rate = (total_tax / income) * 100

    return effective_rate


# 2020 effective tax rate on minimum wage * avg work hours
income = 17.6 * 255 * 8
rate = cetr2020(income)
print(f"Effective tax rate on ${income:,.0f} in 2020 is {rate:.2f}%")


# 2025 effective tax rate on minimum wage * avg work hours
income = 10 * 255 * 8 
rate = cetr2012(income)
print(f"Effective tax rate on ${income:,.0f} in 2012 is {rate:.2f}%")



