given_ratings = [3.8, 4.5, 2.9, 4.8, 4.1];
ranked_shorted = sorted(given_ratings, reverse=True);
print("Highest:", max(given_ratings), "|","Lowest:", min(given_ratings));
print("Ranked", ranked_shorted,);
if given_ratings >= 4.5: 
	print("Top restaurant qualifies for Featured badge!");
else:
	print("No featured badge this week"); 



