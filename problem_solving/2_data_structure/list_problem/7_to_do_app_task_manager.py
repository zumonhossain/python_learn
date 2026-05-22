start_tasks = ['Buy groceries', 'Call doctor', 'Pay bills'];
urgent_task = start_tasks.insert(0, 'Submit report');
remove_tasks = start_tasks.remove('Call doctor');

print(start_tasks[0].upper());
print(start_tasks[1].upper());
print(start_tasks[2].upper());

if len(start_tasks) > 2:
	print("Busy day ahead!");
else:
	print("Light day!");