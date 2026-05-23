import time
import random

# User Stats
user_stats = {
    "missions_completed": 0,
    "quiz_score": 0,
    "level": 1
}

def welcome_screen(name):
    """Display welcome screen with animations"""
    print("\n" + "="*50)
    print(f"Hello! Miracle is going on my friend {name}!")
    print("="*50)
    time.sleep(2)
    print(f"Access Granted {name}")
    time.sleep(1)
    print(f"Welcome back my agent {name}!")
    time.sleep(2)
    print(f"\n🎮 Level: {user_stats['level']} | Missions: {user_stats['missions_completed']} | Score: {user_stats['quiz_score']}\n")

def show_menu():
    """Display main menu"""
    print("\n" + "-"*50)
    print("MAIN MENU - Choose Your Adventure:")
    print("-"*50)
    print("1. 🎯 Take a Mission")
    print("2. 🧠 Play Quiz Game")
    print("3. 📊 View Stats")
    print("4. 💪 Special Challenge")
    print("5. 🚪 Exit")
    print("-"*50)
    return input("Enter your choice (1-5): ")

def take_mission(name):
    """Interactive mission system"""
    missions = [
        {
            "title": "Code Master",
            "description": "Write a Python function",
            "reward": 10
        },
        {
            "title": "Debug Detective",
            "description": "Find and fix the bug in the code",
            "reward": 15
        },
        {
            "title": "Algorithm Solver",
            "description": "Solve a logical puzzle",
            "reward": 20
        }
    ]
    
    mission = random.choice(missions)
    print(f"\n🎯 MISSION ACCEPTED: {mission['title']}")
    print(f"📝 Task: {mission['description']}")
    print(f"💰 Reward: {mission['reward']} points")
    
    response = input(f"\n{name}, are you ready to complete this mission? (yes/no): ").lower()
    
    if response == "yes":
        print("\n⏳ Mission in progress...")
        time.sleep(2)
        print("✅ Mission Completed Successfully!")
        user_stats["missions_completed"] += 1
        user_stats["quiz_score"] += mission["reward"]
        print(f"🎉 +{mission['reward']} points earned!")
        
        # Level up logic
        if user_stats["missions_completed"] % 3 == 0:
            user_stats["level"] += 1
            print(f"🚀 LEVEL UP! You are now Level {user_stats['level']}!")
    else:
        print("❌ Mission declined. Better luck next time!")

def play_quiz(name):
    """Interactive quiz game"""
    questions = [
        {
            "question": "What does Python stand for?",
            "options": ["A) Programming Language", "B) A Snake Type", "C) Both A and B"],
            "answer": "C"
        },
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["A) func", "B) def", "C) function"],
            "answer": "B"
        },
        {
            "question": "What is the output of 5 + 3 * 2 in Python?",
            "options": ["A) 16", "B) 11", "C) 20"],
            "answer": "B"
        },
        {
            "question": "Which data type is immutable in Python?",
            "options": ["A) List", "B) Dictionary", "C) Tuple"],
            "answer": "C"
        }
    ]
    
    print("\n" + "="*50)
    print("🧠 PYTHON QUIZ TIME!")
    print("="*50)
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(f"  {option}")
        
        answer = input("Your answer (A/B/C): ").upper()
        
        if answer == q['answer']:
            print("✅ Correct!")
            score += 25
        else:
            print(f"❌ Wrong! Correct answer was {q['answer']}")
        time.sleep(1)
    
    print(f"\n🎯 Quiz Complete! Your Score: {score}/100")
    user_stats["quiz_score"] += score
    print(f"Total Score: {user_stats['quiz_score']}")

def view_stats(name):
    """Display user statistics"""
    print("\n" + "="*50)
    print(f"📊 AGENT {name.upper()}'S STATS")
    print("="*50)
    print(f"🏆 Level: {user_stats['level']}")
    print(f"🎯 Missions Completed: {user_stats['missions_completed']}")
    print(f"⭐ Total Score: {user_stats['quiz_score']}")
    print(f"📈 Average Mission Reward: {user_stats['quiz_score'] // max(user_stats['missions_completed'], 1)}")
    print("="*50)

def special_challenge(name):
    """Special bonus challenge"""
    print("\n" + "="*50)
    print("💪 SPECIAL CHALLENGE: SPEED ROUND")
    print("="*50)
    print("Answer 3 quick questions! Each correct = 50 points!")
    print("="*50)
    
    challenge_questions = [
        ("Is Python interpreted or compiled?", "interpreted"),
        ("What is the Python Package Manager called?", "pip"),
        ("What keyword is used for loops?", "for")
    ]
    
    challenge_score = 0
    for i, (q, ans) in enumerate(challenge_questions, 1):
        user_answer = input(f"\n{i}. {q}\nYour answer: ").lower().strip()
        if user_answer == ans:
            print("✅ Correct!")
            challenge_score += 50
        else:
            print(f"❌ Correct answer: {ans}")
    
    print(f"\n🏅 Challenge Score: {challenge_score}/150")
    user_stats["quiz_score"] += challenge_score

def main():
    """Main game loop"""
    print("\n" + "🔐"*25)
    name = input("Agent, what is your name? ").strip()
    print("🔐"*25)
    
    welcome_screen(name)
    time.sleep(2)
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            take_mission(name)
        elif choice == "2":
            play_quiz(name)
        elif choice == "3":
            view_stats(name)
        elif choice == "4":
            special_challenge(name)
        elif choice == "5":
            print(f"\n👋 Goodbye, Agent {name}! Mission complete!")
            print(f"Final Score: {user_stats['quiz_score']} | Level: {user_stats['level']}")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
