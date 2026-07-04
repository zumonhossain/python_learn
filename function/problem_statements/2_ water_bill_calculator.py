def water_bill(units_consumed, rate_per_unit):
    print("Units Used :", units_consumed);
    print("Rate :", "¥", rate_per_unit, "/unit");
    print("Total Bill :", "¥", units_consumed * rate_per_unit);
water_bill(120, 5);
print("-----------------------")
water_bill(300, 5);