region_a = [88, 74, 95, 61];
region_b = [79, 91, 85, 70];
top_finalists = region_a.sort(reverse=True);
region_a.extend(region_b);
print("All scores:", region_a);
print("Top 3 finalists:", top_finalists);
if region_a > 90:
    print("A score above 90 made it to the podium!");
else:
    print("No score above 90 this season");