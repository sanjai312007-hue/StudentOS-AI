"""
Mock data for StudentOS AI — used until real AI/DB integration.
Provides realistic data for all modules to showcase functionality.
"""
import datetime
import random

# ─── Student Profile ──────────────────────────────────────────────
STUDENT_PROFILE = {
    "id": "STU001",
    "name": "Sanjai R",
    "email": "sanjai@studentos.ai",
    "college": "Anna University",
    "department": "Computer Science & Engineering",
    "semester": 6,
    "cgpa": 8.75,
    "skills": ["Python", "Machine Learning", "Data Structures", "SQL", "React", "FastAPI"],
    "career_goal": "AI Engineer",
    "avatar": "🎓",
    "study_streak": 12,
    "total_quizzes": 47,
    "total_study_hours": 234,
}

# ─── Dashboard Stats ──────────────────────────────────────────────
DASHBOARD_STATS = {
    "study_hours_today": 3.5,
    "study_hours_week": 22,
    "quizzes_completed": 47,
    "avg_quiz_score": 82,
    "assignments_pending": 3,
    "resume_ats_score": 78,
    "streak_days": 12,
    "learning_progress": 68,
    "rank": 5,
    "total_students": 120,
}

# ─── Upcoming Events ──────────────────────────────────────────────
UPCOMING_EVENTS = [
    {"title": "DBMS Assignment", "due": "2 days", "type": "assignment", "priority": "high", "subject": "DBMS"},
    {"title": "OS Mid-Term Exam", "due": "5 days", "type": "exam", "priority": "high", "subject": "OS"},
    {"title": "Python Project Submission", "due": "7 days", "type": "project", "priority": "medium", "subject": "Python"},
    {"title": "ML Lab Report", "due": "10 days", "type": "assignment", "priority": "low", "subject": "Machine Learning"},
    {"title": "Data Structures Quiz", "due": "3 days", "type": "quiz", "priority": "medium", "subject": "DSA"},
]

# ─── Today's Schedule ──────────────────────────────────────────────
TODAYS_SCHEDULE = [
    {"time": "09:00 AM", "subject": "Python", "duration": "2 hrs", "type": "study", "status": "completed", "color": "#6C63FF"},
    {"time": "11:30 AM", "subject": "DBMS", "duration": "1.5 hrs", "type": "study", "status": "completed", "color": "#FF6B6B"},
    {"time": "02:00 PM", "subject": "Operating Systems", "duration": "2 hrs", "type": "study", "status": "in_progress", "color": "#4ECDC4"},
    {"time": "04:30 PM", "subject": "Machine Learning", "duration": "1 hr", "type": "revision", "status": "upcoming", "color": "#FFE66D"},
    {"time": "06:00 PM", "subject": "DSA Practice", "duration": "1.5 hrs", "type": "practice", "status": "upcoming", "color": "#A78BFA"},
]

# ─── Monthly Study Heatmap ────────────────────────────────────────
MONTHLY_STUDY_HEATMAP = {
    "weeks": [f"W{i}" for i in range(1, 9)],
    "hours": [[random.randint(0, 5) for _ in range(7)] for _ in range(8)]
}

# ─── Weekly Quiz Scores ───────────────────────────────────────────
WEEKLY_SCORES = {
    "weeks": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"],
    "Python":  [68, 72, 75, 78, 81, 85, 88, 92],
    "DBMS":    [55, 60, 63, 67, 70, 72, 75, 78],
    "OS":      [40, 45, 48, 52, 55, 58, 61, 65],
    "ML":      [60, 65, 70, 74, 78, 83, 87, 91],
    "DSA":     [50, 55, 58, 62, 65, 68, 72, 76],
}

# ─── AI Tutor Responses ──────────────────────────────────────────
AI_TUTOR_RESPONSES = {
    "binary search": {
        "definition": "**Binary Search** is a searching algorithm that finds the position of a target value within a **sorted array**. It works by repeatedly dividing the search interval in half.",
        "example": """Consider a sorted array: `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`\n\nSearching for **23**:\n- Step 1: Mid = 16 → 23 > 16, search right half\n- Step 2: Mid = 56 → 23 < 56, search left half\n- Step 3: Mid = 23 → **Found!** ✅""",
        "code": """```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid          # Found!
        elif arr[mid] < target:
            left = mid + 1      # Search right half
        else:
            right = mid - 1     # Search left half
    
    return -1  # Not found

# Example usage
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
result = binary_search(arr, 23)
print(f"Element found at index: {result}")  # Output: 5
```""",
        "complexity": "| Case | Time Complexity | Space Complexity |\n|:---|:---|:---|\n| **Best** | O(1) | O(1) |\n| **Average** | O(log n) | O(1) |\n| **Worst** | O(log n) | O(1) |",
        "interview_questions": [
            "What is the prerequisite for Binary Search?",
            "How does Binary Search differ from Linear Search?",
            "Can Binary Search be applied to linked lists?",
            "Implement Binary Search recursively.",
            "What is the time complexity of Binary Search? Prove it.",
        ],
    },
    "default": {
        "definition": "I can help you understand any Computer Science concept! Try asking about:\n- **Data Structures**: Arrays, Linked Lists, Trees, Graphs, Stacks, Queues\n- **Algorithms**: Sorting, Searching, Dynamic Programming, Greedy\n- **OS Concepts**: Deadlocks, Memory Management, Process Scheduling\n- **DBMS**: Normalization, SQL Joins, ACID Properties\n- **ML**: Linear Regression, Neural Networks, Decision Trees",
        "example": "Type a topic above to get started! 🚀",
        "code": "",
        "complexity": "",
        "interview_questions": [],
    },
}

# ─── Quiz Questions ───────────────────────────────────────────────
QUIZ_QUESTIONS = {
    "Python": [
        {
            "question": "What is the output of `print(type([]))`?",
            "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
            "answer": 0,
            "explanation": "An empty `[]` creates a list object in Python. The `type()` function returns the class type of the object.",
            "difficulty": "Beginner",
        },
        {
            "question": "Which of the following is used to define a decorator in Python?",
            "options": ["@decorator", "#decorator", "!decorator", "$decorator"],
            "answer": 0,
            "explanation": "In Python, decorators are defined using the `@` symbol followed by the decorator function name, placed above the function definition.",
            "difficulty": "Intermediate",
        },
        {
            "question": "What does the `yield` keyword do in Python?",
            "options": [
                "Pauses function execution and returns a generator",
                "Terminates the function immediately",
                "Raises an exception",
                "Creates a new thread",
            ],
            "answer": 0,
            "explanation": "`yield` turns a function into a generator. It pauses the function, saves its state, and returns a value. The function resumes from where it left off when `next()` is called.",
            "difficulty": "Intermediate",
        },
        {
            "question": "Which data structure uses LIFO (Last In, First Out) principle?",
            "options": ["Stack", "Queue", "Array", "Linked List"],
            "answer": 0,
            "explanation": "A Stack follows the LIFO principle — the last element added is the first one removed. Think of a stack of plates!",
            "difficulty": "Beginner",
        },
        {
            "question": "What is the time complexity of `dict.get(key)` in Python?",
            "options": ["O(1)", "O(n)", "O(log n)", "O(n²)"],
            "answer": 0,
            "explanation": "Python dictionaries use hash tables internally, so average-case lookup is O(1) — constant time.",
            "difficulty": "Intermediate",
        },
        {
            "question": "What is a lambda function in Python?",
            "options": [
                "An anonymous inline function",
                "A function with multiple return values",
                "A function that runs in parallel",
                "A function that modifies global variables",
            ],
            "answer": 0,
            "explanation": "Lambda functions are small anonymous functions defined with the `lambda` keyword. Example: `square = lambda x: x**2`",
            "difficulty": "Beginner",
        },
        {
            "question": "Which module is used for regular expressions in Python?",
            "options": ["re", "regex", "regexp", "match"],
            "answer": 0,
            "explanation": "The `re` module provides support for regular expressions in Python. Use `re.match()`, `re.search()`, `re.findall()` etc.",
            "difficulty": "Beginner",
        },
        {
            "question": "What is the difference between `deepcopy` and `copy`?",
            "options": [
                "deepcopy creates independent copies of nested objects, copy doesn't",
                "copy is faster but deepcopy is more accurate",
                "There is no difference",
                "deepcopy only works with lists",
            ],
            "answer": 0,
            "explanation": "`copy.copy()` creates a shallow copy (nested objects are still referenced). `copy.deepcopy()` recursively copies all nested objects, creating a fully independent clone.",
            "difficulty": "Advanced",
        },
        {
            "question": "What is GIL in Python?",
            "options": [
                "Global Interpreter Lock — prevents true multi-threading",
                "Generic Input Library",
                "Graph Integration Layer",
                "General Import Loader",
            ],
            "answer": 0,
            "explanation": "The GIL (Global Interpreter Lock) is a mutex in CPython that allows only one thread to execute Python bytecode at a time. This limits true parallelism in multi-threaded programs.",
            "difficulty": "Advanced",
        },
        {
            "question": "Which method is called when an object is created in Python?",
            "options": ["__init__", "__new__", "__create__", "__start__"],
            "answer": 0,
            "explanation": "`__init__` is the constructor method called after the object is created. `__new__` actually creates the object, but `__init__` initializes its attributes.",
            "difficulty": "Beginner",
        },
    ],
    "DBMS": [
        {
            "question": "What does ACID stand for in database transactions?",
            "options": [
                "Atomicity, Consistency, Isolation, Durability",
                "Atomicity, Concurrency, Isolation, Durability",
                "Accuracy, Consistency, Isolation, Durability",
                "Atomicity, Consistency, Integration, Durability",
            ],
            "answer": 0,
            "explanation": "ACID properties ensure reliable database transactions: Atomicity (all or nothing), Consistency (valid state), Isolation (concurrent independence), Durability (permanent).",
            "difficulty": "Beginner",
        },
        {
            "question": "Which normal form eliminates transitive dependencies?",
            "options": ["3NF", "1NF", "2NF", "BCNF"],
            "answer": 0,
            "explanation": "Third Normal Form (3NF) eliminates transitive dependencies — where a non-key attribute depends on another non-key attribute.",
            "difficulty": "Intermediate",
        },
        {
            "question": "What is a foreign key?",
            "options": [
                "A field that references the primary key of another table",
                "The first column of every table",
                "A unique identifier for each row",
                "An encrypted key for security",
            ],
            "answer": 0,
            "explanation": "A foreign key establishes a relationship between two tables by referencing the primary key of another table.",
            "difficulty": "Beginner",
        },
        {
            "question": "Which type of JOIN returns all rows from both tables?",
            "options": ["FULL OUTER JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN"],
            "answer": 0,
            "explanation": "FULL OUTER JOIN returns all rows from both tables, with NULLs where there's no match.",
            "difficulty": "Intermediate",
        },
        {
            "question": "What is deadlock in DBMS?",
            "options": [
                "When two or more transactions wait indefinitely for each other's locks",
                "When a database crashes",
                "When a query takes too long",
                "When data is corrupted",
            ],
            "answer": 0,
            "explanation": "Deadlock occurs when two or more transactions are waiting for each other to release locks, creating a circular dependency. None can proceed.",
            "difficulty": "Intermediate",
        },
    ],
    "Operating Systems": [
        {
            "question": "What is a process in an operating system?",
            "options": [
                "A program in execution",
                "A stored file",
                "A hardware component",
                "A type of memory",
            ],
            "answer": 0,
            "explanation": "A process is a program that is currently being executed. It includes the program code, current activity, and allocated resources.",
            "difficulty": "Beginner",
        },
        {
            "question": "Which scheduling algorithm may cause starvation?",
            "options": [
                "Shortest Job First (SJF)",
                "Round Robin",
                "First Come First Serve (FCFS)",
                "None of the above",
            ],
            "answer": 0,
            "explanation": "SJF can cause starvation for long processes if shorter processes keep arriving. The long process may never get CPU time.",
            "difficulty": "Intermediate",
        },
        {
            "question": "What is virtual memory?",
            "options": [
                "A technique that uses disk space as an extension of RAM",
                "Memory inside the CPU",
                "Read-only memory",
                "Cloud storage",
            ],
            "answer": 0,
            "explanation": "Virtual memory allows the OS to use disk space to simulate additional RAM, enabling processes to use more memory than physically available.",
            "difficulty": "Beginner",
        },
        {
            "question": "What is thrashing in operating systems?",
            "options": [
                "Excessive paging causing severe performance degradation",
                "A type of virus",
                "Fast context switching",
                "Memory overflow",
            ],
            "answer": 0,
            "explanation": "Thrashing occurs when the OS spends more time swapping pages in and out of memory than executing processes, drastically reducing performance.",
            "difficulty": "Advanced",
        },
        {
            "question": "Which of the following is NOT a necessary condition for deadlock?",
            "options": [
                "Preemption",
                "Mutual Exclusion",
                "Hold and Wait",
                "Circular Wait",
            ],
            "answer": 0,
            "explanation": "The four necessary conditions for deadlock are: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Preemption actually prevents deadlock!",
            "difficulty": "Intermediate",
        },
    ],
    "Machine Learning": [
        {
            "question": "Which algorithm is used for classification AND regression?",
            "options": [
                "Decision Tree",
                "K-Means",
                "Apriori",
                "PCA",
            ],
            "answer": 0,
            "explanation": "Decision Trees can be used for both classification (predict categories) and regression (predict continuous values) tasks.",
            "difficulty": "Beginner",
        },
        {
            "question": "What is overfitting in machine learning?",
            "options": [
                "Model performs well on training data but poorly on test data",
                "Model performs poorly on all data",
                "Model takes too long to train",
                "Model uses too much memory",
            ],
            "answer": 0,
            "explanation": "Overfitting occurs when a model learns the noise in training data instead of the actual pattern, leading to poor generalization on new data.",
            "difficulty": "Beginner",
        },
        {
            "question": "Which technique is used to prevent overfitting?",
            "options": [
                "All of the above",
                "Regularization (L1/L2)",
                "Dropout",
                "Cross-validation",
            ],
            "answer": 0,
            "explanation": "Regularization, Dropout, Cross-validation, Early stopping, and Data augmentation are all techniques to prevent overfitting.",
            "difficulty": "Intermediate",
        },
        {
            "question": "What does the 'K' in K-Nearest Neighbors represent?",
            "options": [
                "Number of nearest neighbors to consider",
                "Number of clusters",
                "Number of features",
                "Number of iterations",
            ],
            "answer": 0,
            "explanation": "In KNN, 'K' is the number of closest data points (neighbors) used to make a prediction. Choosing the right K is crucial for model performance.",
            "difficulty": "Beginner",
        },
        {
            "question": "What is the vanishing gradient problem?",
            "options": [
                "Gradients become extremely small during backpropagation in deep networks",
                "The model disappears from memory",
                "Training data gets corrupted",
                "Loss function becomes zero",
            ],
            "answer": 0,
            "explanation": "In deep neural networks, gradients can become exponentially small as they propagate backward through layers, causing earlier layers to learn very slowly or not at all.",
            "difficulty": "Advanced",
        },
    ],
}

# ─── Flashcard Decks ──────────────────────────────────────────────
FLASHCARD_DECKS = {
    "Data Structures": [
        {"front": "What is a Stack?", "back": "A **LIFO** (Last In, First Out) data structure. Elements are added and removed from the same end (top).\n\n**Operations**: push(), pop(), peek()\n**Time**: O(1) for all operations"},
        {"front": "What is a Queue?", "back": "A **FIFO** (First In, First Out) data structure. Elements are added at rear and removed from front.\n\n**Operations**: enqueue(), dequeue(), front()\n**Time**: O(1) for all operations"},
        {"front": "What is a Binary Tree?", "back": "A tree where each node has **at most 2 children** (left and right).\n\n**Types**: Full, Complete, Perfect, Balanced\n**Traversals**: Inorder, Preorder, Postorder"},
        {"front": "What is a Hash Table?", "back": "A data structure that maps **keys to values** using a hash function.\n\n**Average Time**: O(1) for insert, delete, search\n**Worst Case**: O(n) due to collisions"},
        {"front": "What is a Linked List?", "back": "A linear data structure where elements are stored in **nodes**, each pointing to the next.\n\n**Types**: Singly, Doubly, Circular\n**Advantage**: Dynamic size, efficient insert/delete"},
        {"front": "What is a Graph?", "back": "A collection of **vertices (nodes)** connected by **edges**.\n\n**Types**: Directed, Undirected, Weighted\n**Representations**: Adjacency Matrix, Adjacency List"},
        {"front": "What is a Heap?", "back": "A complete binary tree where parent is **greater (Max-Heap)** or **smaller (Min-Heap)** than children.\n\n**Used for**: Priority Queues, Heap Sort\n**Time**: O(log n) insert, O(1) find min/max"},
        {"front": "What is a Trie?", "back": "A tree-like data structure for storing **strings** efficiently.\n\n**Used for**: Autocomplete, Spell checking\n**Time**: O(m) where m = length of string"},
    ],
    "Python Concepts": [
        {"front": "What is a List Comprehension?", "back": "A concise way to create lists.\n\n```python\nsquares = [x**2 for x in range(10)]\n```\n\nEquivalent to a for-loop but more Pythonic."},
        {"front": "What is *args and **kwargs?", "back": "`*args` — Variable positional arguments (tuple)\n`**kwargs` — Variable keyword arguments (dict)\n\n```python\ndef func(*args, **kwargs):\n    print(args)    # (1, 2, 3)\n    print(kwargs)  # {'a': 4}\n```"},
        {"front": "What is a Generator?", "back": "A function that uses `yield` to return values **lazily** (one at a time).\n\n**Memory efficient** — doesn't store all values.\n\n```python\ndef count_up(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1\n```"},
        {"front": "What is the GIL?", "back": "**Global Interpreter Lock** — a mutex in CPython.\n\nAllows only **one thread** to execute Python bytecode at a time.\n\n**Workaround**: Use `multiprocessing` for CPU-bound tasks."},
        {"front": "Mutable vs Immutable?", "back": "**Mutable**: Can be changed after creation\n→ list, dict, set\n\n**Immutable**: Cannot be changed\n→ int, float, str, tuple, frozenset"},
        {"front": "What is a Decorator?", "back": "A function that **wraps another function** to extend its behavior.\n\n```python\ndef timer(func):\n    def wrapper(*args):\n        start = time.time()\n        result = func(*args)\n        print(f'Took {time.time()-start}s')\n        return result\n    return wrapper\n\n@timer\ndef slow_func():\n    time.sleep(1)\n```"},
    ],
    "Machine Learning": [
        {"front": "Supervised vs Unsupervised Learning?", "back": "**Supervised**: Labeled data → Predicts output\n→ Classification, Regression\n\n**Unsupervised**: No labels → Finds patterns\n→ Clustering, Dimensionality Reduction"},
        {"front": "What is Gradient Descent?", "back": "An optimization algorithm that **minimizes the loss function** by iteratively moving in the direction of steepest descent.\n\n**Learning Rate (α)** controls step size.\n\n**Types**: Batch, Stochastic, Mini-batch"},
        {"front": "Bias vs Variance Tradeoff?", "back": "**High Bias**: Underfitting — model too simple\n**High Variance**: Overfitting — model too complex\n\n**Goal**: Find the sweet spot (balanced model)"},
        {"front": "What is Cross-Validation?", "back": "A technique to evaluate model performance by **splitting data into K folds**.\n\nTrain on K-1 folds, test on 1 fold. Repeat K times.\n\n**K-Fold CV** reduces overfitting and gives robust estimates."},
        {"front": "Precision vs Recall?", "back": "**Precision** = TP / (TP + FP) → How many predicted positives are correct?\n\n**Recall** = TP / (TP + FN) → How many actual positives were found?\n\n**F1 Score** = Harmonic mean of both"},
    ],
}

# ─── Study Plans ──────────────────────────────────────────────────
STUDY_PLAN = {
    "Monday": [
        {"subject": "Python", "duration": "2 hrs", "time": "09:00 - 11:00", "type": "Theory + Practice", "color": "#6C63FF", "priority": "high"},
        {"subject": "DBMS", "duration": "1.5 hrs", "time": "14:00 - 15:30", "type": "Theory", "color": "#FF6B6B", "priority": "medium"},
        {"subject": "DSA Practice", "duration": "2 hrs", "time": "17:00 - 19:00", "type": "Problem Solving", "color": "#A78BFA", "priority": "high"},
    ],
    "Tuesday": [
        {"subject": "Operating Systems", "duration": "2 hrs", "time": "09:00 - 11:00", "type": "Theory", "color": "#4ECDC4", "priority": "high"},
        {"subject": "Machine Learning", "duration": "2 hrs", "time": "14:00 - 16:00", "type": "Theory + Code", "color": "#FFE66D", "priority": "high"},
        {"subject": "Python Practice", "duration": "1 hr", "time": "18:00 - 19:00", "type": "Coding", "color": "#6C63FF", "priority": "medium"},
    ],
    "Wednesday": [
        {"subject": "DBMS", "duration": "2 hrs", "time": "09:00 - 11:00", "type": "SQL Practice", "color": "#FF6B6B", "priority": "high"},
        {"subject": "DSA", "duration": "2 hrs", "time": "14:00 - 16:00", "type": "Algorithms", "color": "#A78BFA", "priority": "high"},
        {"subject": "OS Practice", "duration": "1.5 hrs", "time": "17:00 - 18:30", "type": "Numericals", "color": "#4ECDC4", "priority": "medium"},
    ],
    "Thursday": [
        {"subject": "Machine Learning", "duration": "2 hrs", "time": "09:00 - 11:00", "type": "Model Building", "color": "#FFE66D", "priority": "high"},
        {"subject": "Python", "duration": "1.5 hrs", "time": "14:00 - 15:30", "type": "Advanced Topics", "color": "#6C63FF", "priority": "medium"},
        {"subject": "Quiz Review", "duration": "1 hr", "time": "17:00 - 18:00", "type": "Revision", "color": "#FF9F43", "priority": "low"},
    ],
    "Friday": [
        {"subject": "DSA", "duration": "2 hrs", "time": "09:00 - 11:00", "type": "Graph Algorithms", "color": "#A78BFA", "priority": "high"},
        {"subject": "DBMS", "duration": "1.5 hrs", "time": "14:00 - 15:30", "type": "Normalization", "color": "#FF6B6B", "priority": "medium"},
        {"subject": "Mock Test", "duration": "2 hrs", "time": "16:00 - 18:00", "type": "Full Test", "color": "#FF9F43", "priority": "high"},
    ],
    "Saturday": [
        {"subject": "Project Work", "duration": "3 hrs", "time": "10:00 - 13:00", "type": "Coding", "color": "#2ED573", "priority": "high"},
        {"subject": "Weak Topics", "duration": "2 hrs", "time": "15:00 - 17:00", "type": "Revision", "color": "#FF4757", "priority": "high"},
    ],
    "Sunday": [
        {"subject": "Revision", "duration": "2 hrs", "time": "10:00 - 12:00", "type": "Week Review", "color": "#FF9F43", "priority": "medium"},
        {"subject": "Rest & Relax", "duration": "—", "time": "Afternoon", "type": "Break", "color": "#2ED573", "priority": "low"},
    ],
}

# ─── Performance Analytics ────────────────────────────────────────
WEEKLY_SCORES = {
    "weeks": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"],
    "Python": [65, 70, 72, 78, 82, 85, 88, 92],
    "DBMS": [60, 62, 68, 72, 75, 80, 82, 90],
    "OS": [45, 48, 50, 52, 55, 58, 60, 50],
    "ML": [70, 75, 78, 80, 85, 88, 90, 95],
    "DSA": [55, 60, 65, 70, 72, 75, 78, 82],
}

SUBJECT_ACCURACY = {
    "subjects": ["Python", "DBMS", "OS", "ML", "DSA"],
    "accuracy": [92, 90, 50, 95, 82],
    "colors": ["#6C63FF", "#FF6B6B", "#4ECDC4", "#FFE66D", "#A78BFA"],
}

STUDY_HOURS_DISTRIBUTION = {
    "subjects": ["Python", "DBMS", "OS", "ML", "DSA", "Projects"],
    "hours": [45, 32, 28, 40, 38, 20],
    "colors": ["#6C63FF", "#FF6B6B", "#4ECDC4", "#FFE66D", "#A78BFA", "#2ED573"],
}

MONTHLY_STUDY_HEATMAP = [
    [2, 3, 0, 4, 3, 2, 1],
    [3, 4, 2, 3, 4, 3, 0],
    [4, 3, 3, 5, 4, 2, 1],
    [3, 5, 4, 3, 5, 4, 2],
]

# ─── Resume Data ──────────────────────────────────────────────────
RESUME_DATA = {
    "name": "Sanjai R",
    "email": "sanjai@email.com",
    "phone": "+91-9876543210",
    "linkedin": "linkedin.com/in/sanjai-r",
    "github": "github.com/sanjai-r",
    "summary": "Aspiring AI Engineer with strong foundation in Python, Machine Learning, and Full-Stack Development. Experienced in building AI-powered applications using LangChain, RAG, and modern web technologies.",
    "education": [
        {
            "degree": "B.Tech Computer Science & Engineering",
            "college": "Anna University",
            "year": "2022 - 2026",
            "cgpa": "8.75 / 10",
        }
    ],
    "skills": {
        "Languages": ["Python", "JavaScript", "SQL", "Java"],
        "AI/ML": ["TensorFlow", "Scikit-learn", "LangChain", "OpenAI API", "FAISS"],
        "Web": ["React.js", "FastAPI", "Streamlit", "Flask"],
        "Tools": ["Git", "Docker", "PostgreSQL", "MongoDB"],
    },
    "projects": [
        {
            "name": "StudentOS AI",
            "description": "AI-powered academic operating system with RAG-based PDF chat, quiz generator, and performance analytics.",
            "tech": "Python, Streamlit, FastAPI, LangChain, FAISS",
        },
        {
            "name": "Smart Resume Analyzer",
            "description": "NLP-based resume parser that extracts skills and matches them with job descriptions.",
            "tech": "Python, spaCy, Streamlit",
        },
    ],
    "experience": [
        {
            "role": "AI/ML Intern",
            "company": "Tech Solutions Pvt Ltd",
            "duration": "May 2025 - Jul 2025",
            "description": "Built ML models for customer churn prediction. Improved accuracy by 15% using ensemble methods.",
        }
    ],
    "certifications": [
        "Google Data Analytics Professional Certificate",
        "IBM AI Engineering Professional Certificate",
        "LangChain for LLM Application Development",
    ],
}

ATS_SCORE_DATA = {
    "overall_score": 78,
    "formatting": 85,
    "keywords": 72,
    "grammar": 90,
    "skills_match": 70,
    "missing_keywords": ["Docker", "Kubernetes", "CI/CD", "AWS", "System Design"],
    "suggestions": [
        "Add more quantifiable achievements (numbers, percentages)",
        "Include 'Docker' and 'AWS' to match industry requirements",
        "Add a 'Publications' or 'Research' section if applicable",
        "Use action verbs: 'Developed', 'Implemented', 'Optimized'",
        "Ensure consistent formatting throughout",
    ],
}

# ─── Internship Recommendations ──────────────────────────────────
INTERNSHIP_RECOMMENDATIONS = [
    {
        "title": "AI/ML Engineering Intern",
        "company": "Google",
        "location": "Bangalore, India",
        "duration": "3 months",
        "stipend": "₹80,000/month",
        "skills_match": 92,
        "required_skills": ["Python", "TensorFlow", "Machine Learning", "Deep Learning"],
        "logo": "🔵",
    },
    {
        "title": "Python Developer Intern",
        "company": "Microsoft",
        "location": "Hyderabad, India",
        "duration": "6 months",
        "stipend": "₹60,000/month",
        "skills_match": 88,
        "required_skills": ["Python", "FastAPI", "SQL", "Git"],
        "logo": "🟦",
    },
    {
        "title": "Data Science Intern",
        "company": "Amazon",
        "location": "Remote",
        "duration": "3 months",
        "stipend": "₹70,000/month",
        "skills_match": 85,
        "required_skills": ["Python", "Pandas", "ML", "SQL"],
        "logo": "🟧",
    },
    {
        "title": "GenAI Research Intern",
        "company": "OpenAI",
        "location": "Remote",
        "duration": "4 months",
        "stipend": "₹1,00,000/month",
        "skills_match": 78,
        "required_skills": ["Python", "LLMs", "LangChain", "PyTorch"],
        "logo": "⬛",
    },
    {
        "title": "Full Stack AI Developer",
        "company": "Infosys",
        "location": "Pune, India",
        "duration": "6 months",
        "stipend": "₹35,000/month",
        "skills_match": 95,
        "required_skills": ["Python", "React", "FastAPI", "SQL"],
        "logo": "🔷",
    },
    {
        "title": "NLP Engineer Intern",
        "company": "Flipkart",
        "location": "Bangalore, India",
        "duration": "3 months",
        "stipend": "₹50,000/month",
        "skills_match": 80,
        "required_skills": ["Python", "NLP", "Transformers", "spaCy"],
        "logo": "🟡",
    },
]

# ─── Mock Interview Data ─────────────────────────────────────────
MOCK_INTERVIEW_QUESTIONS = {
    "Software Engineer": [
        {"question": "Tell me about yourself.", "category": "Behavioral", "time_limit": 120},
        {"question": "Explain the difference between Stack and Queue.", "category": "Technical", "time_limit": 90},
        {"question": "What is Object-Oriented Programming? Explain its pillars.", "category": "Technical", "time_limit": 120},
        {"question": "Describe a challenging project you worked on.", "category": "Behavioral", "time_limit": 120},
        {"question": "Write a function to reverse a linked list.", "category": "Coding", "time_limit": 180},
        {"question": "What is your approach to debugging?", "category": "Problem Solving", "time_limit": 90},
        {"question": "Explain REST APIs and HTTP methods.", "category": "Technical", "time_limit": 120},
        {"question": "Where do you see yourself in 5 years?", "category": "Behavioral", "time_limit": 90},
    ],
    "AI Engineer": [
        {"question": "Tell me about yourself and your interest in AI.", "category": "Behavioral", "time_limit": 120},
        {"question": "Explain the difference between Supervised and Unsupervised Learning.", "category": "Technical", "time_limit": 120},
        {"question": "What is RAG (Retrieval Augmented Generation)?", "category": "Technical", "time_limit": 120},
        {"question": "How do you handle overfitting in a neural network?", "category": "Technical", "time_limit": 120},
        {"question": "Describe your experience with LLMs.", "category": "Project", "time_limit": 120},
        {"question": "What is the transformer architecture?", "category": "Technical", "time_limit": 150},
        {"question": "How would you build a recommendation system?", "category": "System Design", "time_limit": 180},
        {"question": "What ethical considerations exist in AI?", "category": "Behavioral", "time_limit": 120},
    ],
    "Data Analyst": [
        {"question": "Tell me about yourself.", "category": "Behavioral", "time_limit": 120},
        {"question": "What is the difference between SQL JOIN types?", "category": "Technical", "time_limit": 120},
        {"question": "How do you handle missing data?", "category": "Technical", "time_limit": 90},
        {"question": "Explain the difference between Pandas DataFrame and Series.", "category": "Technical", "time_limit": 90},
        {"question": "Walk me through a data analysis project you completed.", "category": "Project", "time_limit": 150},
        {"question": "What visualization tools have you used?", "category": "Technical", "time_limit": 90},
    ],
    "Python Developer": [
        {"question": "Tell me about yourself.", "category": "Behavioral", "time_limit": 120},
        {"question": "What are Python decorators? Give an example.", "category": "Technical", "time_limit": 120},
        {"question": "Explain list comprehension vs generator expression.", "category": "Technical", "time_limit": 90},
        {"question": "What is the GIL? How does it affect threading?", "category": "Technical", "time_limit": 120},
        {"question": "How would you design a REST API with FastAPI?", "category": "System Design", "time_limit": 150},
        {"question": "What testing frameworks have you used?", "category": "Technical", "time_limit": 90},
    ],
}

INTERVIEW_FEEDBACK_SAMPLE = {
    "overall_score": 89,
    "confidence": 85,
    "communication": 92,
    "technical_accuracy": 88,
    "grammar": 95,
    "categories": {
        "Technical": {"score": 88, "feedback": "Strong technical knowledge. Consider providing more concrete examples."},
        "Behavioral": {"score": 92, "feedback": "Excellent communication. Your STAR method responses were well-structured."},
        "Coding": {"score": 85, "feedback": "Good problem-solving approach. Practice explaining your thought process while coding."},
        "System Design": {"score": 80, "feedback": "Good high-level design. Work on discussing scalability and trade-offs."},
    },
}

# ─── Learning Roadmap ─────────────────────────────────────────────
LEARNING_ROADMAP = {
    "AI Engineer": [
        {"step": 1, "title": "Python Fundamentals", "status": "completed", "progress": 100, "topics": ["Syntax", "OOP", "File Handling", "Libraries"]},
        {"step": 2, "title": "Mathematics for AI", "status": "completed", "progress": 100, "topics": ["Linear Algebra", "Calculus", "Probability", "Statistics"]},
        {"step": 3, "title": "Data Analysis", "status": "completed", "progress": 100, "topics": ["NumPy", "Pandas", "Matplotlib", "Data Cleaning"]},
        {"step": 4, "title": "Machine Learning", "status": "in_progress", "progress": 75, "topics": ["Regression", "Classification", "Clustering", "Ensemble Methods"]},
        {"step": 5, "title": "Deep Learning", "status": "in_progress", "progress": 40, "topics": ["Neural Networks", "CNN", "RNN", "Transfer Learning"]},
        {"step": 6, "title": "NLP & LLMs", "status": "not_started", "progress": 0, "topics": ["Tokenization", "Transformers", "Fine-tuning", "Prompt Engineering"]},
        {"step": 7, "title": "GenAI & RAG", "status": "not_started", "progress": 0, "topics": ["LangChain", "Vector Databases", "RAG Pipeline", "Agents"]},
        {"step": 8, "title": "MLOps & Deployment", "status": "not_started", "progress": 0, "topics": ["Docker", "CI/CD", "Model Serving", "Monitoring"]},
        {"step": 9, "title": "Portfolio & Projects", "status": "not_started", "progress": 0, "topics": ["End-to-End Projects", "Open Source", "Blog Posts"]},
        {"step": 10, "title": "Interview Prep & Internship", "status": "not_started", "progress": 0, "topics": ["DSA", "System Design", "Mock Interviews", "Resume"]},
    ],
}
