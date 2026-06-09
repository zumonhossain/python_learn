# Department names
departments = ['Engineering', 'Business', 'Arts']

courses = [
    [   
        ["Algorithms", 3, 30, 28],
        ["Networks", 3, 25, 25],
        ["Databases", 2, 35, 10],
        ["AI Basics", 4, 20, 20]
    ],
    [   
        ["Marketing", 3, 40, 38],
        ["Finance", 3, 30, 30],
        ["Management", 2, 35, 20],
        ["Economics", 4, 25, 25]
    ],
    [   
        ["History", 3, 30, 15],
        ["Philosophy", 3, 20, 20],
        ["Literature", 2, 25, 10],
        ["Fine Arts", 4, 20, 18]
    ]
]

print("============================================")
print("UNIVERSITY COURSE CATALOG")
print("============================================")

d = 0

while d < len(courses):
