list_of_headlines = ["oldest news 1","oldest news 2","New Ai Law Passed","Budget Cuts Announced","School Reform Bill",]
recent = list_of_headlines[-3:];
print("Total headlines:", len(list_of_headlines), "|", "Showing:", len(recent) );
if len(list_of_headlines) >= 3:
	print("1:", recent[0].title());
	print("2:", recent[1].title());
	print("3:", recent[2].title());
else:
	print("Not enough news yet");