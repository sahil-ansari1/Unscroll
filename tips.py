import random

tips = [
    "Stretch for 2 minutes instead of scrolling!",
    "Hydrate yourself — drink a glass of water.",
    "Look away from your screen for 20 seconds!",
    "Take a deep breath and relax your mind.",
    "Read a page of a book instead of Instagram.",
    "Walk a few steps — your body needs it!",
    "Organize your desk or phone files.",
    "Write one small goal for today.",
    "Call a friend instead of scrolling reels.",
    "Uninstall one useless app now!"
]

def get_tip():
    return random.choice(tips)

if __name__ == "__main__":
    print("Your Unscroll Tip:")
    print(get_tip())
  
