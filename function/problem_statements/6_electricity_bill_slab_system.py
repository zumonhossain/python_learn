def electricity_bill(units):
    if units <= 100:
        return units * 3;
    elif units <= 300:
        return (100 * 3) + (units - 100) * 5;
    else:
        return (100 * 3) + (200 * 5) + (units - 300) * 7;

bill = electricity_bill(80);
print(f"Bill: ¥{bill}");

bill = electricity_bill(200);
print(f"Bill: ¥{bill}");

bill = electricity_bill(450);
print(f"Bill: ¥{bill}");