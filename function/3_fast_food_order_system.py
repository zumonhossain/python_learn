def place_order(item, size="Medium", extra_sauce=False):

    if extra_sauce:
        sauce = "Yes";
    else:
        sauce = "No";

    print("Order:", item, "| Size:", size, "| Sauce:", sauce);

place_order("Burger");
place_order("Fries", size="Large");
place_order("Wrap", "Small", True);