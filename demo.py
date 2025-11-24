"""
Animal Farm Demo
================

Interactive demonstration of the Animal Farm system showing:
1. Basic usage and features
2. Runtime flexibility (Checkpoint Question 1)
3. Easy extensibility (Checkpoint Question 2)
"""

from animal_farm import (
    Animal, Bird, Dog,
    FlyAction, CrowAction, BarkAction, ChaseAction,
    GuardDuty, LayEggsDuty, HerdDuty,
    Action, Duty
)


def print_section(title: str):
    """Print a formatted section header."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60 + "\n")


def demo_basic_usage():
    """Demonstrate basic animal creation and usage."""
    print_section("BASIC USAGE DEMONSTRATION")
    
    # Create a flying bird
    eagle = Bird("Eddie the Eagle", FlyAction(), LayEggsDuty())
    print(eagle.get_status())
    print(eagle.perform_action())
    print(eagle.perform_duty())
    
    print("\n" + "-"*60 + "\n")
    
    # Create a guard dog
    guard_dog = Dog("Max", BarkAction(), GuardDuty())
    print(guard_dog.get_status())
    print(guard_dog.perform_action())
    print(guard_dog.perform_duty())


def demo_state_management():
    """Demonstrate state management (hungry/sleepy)."""
    print_section("STATE MANAGEMENT: HUNGRY & SLEEPY")
    
    rooster = Bird("Roger the Rooster", CrowAction(), LayEggsDuty())
    
    print("Roger tries to work...")
    print(rooster.perform_duty())
    
    print("\n🍖 Roger gets hungry...")
    rooster.make_hungry()
    print(rooster.get_status())
    print("\nRoger tries to work while hungry:")
    print(rooster.perform_duty())
    
    print("\n" + rooster.eat())
    print("\nNow Roger can work:")
    print(rooster.perform_duty())
    
    print("\nRoger gets sleepy...")
    rooster.make_sleepy()
    print("\nRoger tries to work while sleepy:")
    print(rooster.perform_duty())
    
    print("\n" + rooster.sleep())
    print("\nRefreshed and ready!")
    print(rooster.perform_duty())


def demo_runtime_changes():
    """Demonstrate runtime flexibility (Checkpoint Question 1)."""
    print_section("⚡ RUNTIME FLEXIBILITY (Checkpoint Q1) ⚡")
    
    print("Creating a versatile farm dog named Bingo...")
    Bingo = Dog("Bingo", BarkAction(), GuardDuty())
    
    print("\nBingo's initial configuration:")
    print(Bingo.get_status())
    
    print("\nBingo performs his action (Bark):")
    print(Bingo.perform_action())
    
    print("\nBingo performs his duty (Guard):")
    print(Bingo.perform_duty())
    
    print("\n" + "~"*60)
    print("⚡ CHANGING ACTION AT RUNTIME...")
    print("~"*60)
    
    Bingo.set_action(ChaseAction())
    print("\nBingo's updated configuration:")
    print(Bingo.get_status())
    
    print("\nBingo now performs his new action (Chase):")
    print(Bingo.perform_action())
    
    print("\n" + "~"*60)
    print("⚡ CHANGING DUTY AT RUNTIME...")
    print("~"*60)
    
    Bingo.set_duty(HerdDuty())
    print("\nBingo's final configuration:")
    print(Bingo.get_status())
    
    print("\nBingo now performs his new duty (Herd):")
    print(Bingo.perform_duty())
    
    print("\nSUCCESS! Bingo's behavior changed at runtime without")
    print("   modifying the Dog class or creating a new instance!")


def demo_extensibility():
    """Demonstrate easy extensibility (Checkpoint Question 2)."""
    print_section("🔧 EXTENSIBILITY (Checkpoint Q2) 🔧")
    
    print("Let's add a completely new animal type: CAT!")
    print("\nStep 1: Define new actions for cats...")
    
    # New actions for cats
    class MeowAction(Action):
        def perform(self, animal_name: str) -> str:
            return f"{animal_name} meows: Meow meow!"
        
        def get_name(self) -> str:
            return "Meow"
    
    class PurrAction(Action):
        def perform(self, animal_name: str) -> str:
            return f"{animal_name} purrs contentedly!"
        
        def get_name(self) -> str:
            return "Purr"
    
    print("MeowAction created")
    print("PurrAction created")
    
    print("\nStep 2: Define new duty for cats...")
    
    # New duty for cats
    class CatchMiceDuty(Duty):
        def execute(self, animal_name: str) -> str:
            return f"{animal_name} is catching mice in the barn! 🐭"
        
        def get_name(self) -> str:
            return "Catch Mice"
    
    print("CatchMiceDuty created")
    
    print("\nStep 3: Create Cat class (inherits from Animal)...")
    
    # New Cat class
    class Cat(Animal):
        """Cats have 4 legs."""
        def __init__(self, name: str, action: Action = None, duty: Duty = None):
            super().__init__(name, legs=4, action=action, duty=duty)
    
    print("Cat class created")
    
    print("\nStep 4: Create and use a cat instance...")
    
    whiskers = Cat("Whiskers", MeowAction(), CatchMiceDuty())
    
    print("\n" + "-"*60)
    print(whiskers.get_status())
    print(whiskers.perform_action())
    print(whiskers.perform_duty())
    
    print("\n" + "-"*60)
    print("Changing Whiskers' action to purring...")
    whiskers.set_action(PurrAction())
    print(whiskers.perform_action())
    
    print("\nSUCCESS! We added a new animal type (Cat) with new")
    print("   actions and duties WITHOUT modifying any existing code!")
    print("   This demonstrates the Open/Closed Principle.")


def demo_farm_scenario():
    """Demonstrate a realistic farm scenario."""
    print_section("REALISTIC FARM SCENARIO")
    
    print("Welcome to Sunny Meadows Farm!\n")
    
    # Create farm animals
    animals = [
        Bird("The Rooster", CrowAction(), LayEggsDuty()),
        Bird("The Hen", FlyAction(), LayEggsDuty()),
        Dog("Bingo", BarkAction(), GuardDuty()),
        Dog("Shep", ChaseAction(), HerdDuty()),
    ]
    
    print("The morning begins...\n")
    
    for animal in animals:
        print("-"*60)
        print(f"\n{animal.name}'s morning routine:")
        print(animal.perform_action())
        print(animal.perform_duty())
        print()
    
    print("-"*60)
    print("\nMid-morning: The animals are getting hungry...")
    
    for animal in animals:
        animal.make_hungry()
        print(f"\n{animal.name}: {animal.perform_duty()}")
    
    print("\nFeeding time!")
    
    for animal in animals:
        print(f"{animal.name}: {animal.eat()}")
    
    print("\nBack to work, everyone!\n")
    
    for animal in animals:
        print(f"{animal.name}: {animal.perform_duty()}")


def main():
    """Run all demonstrations."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "ANIMAL FARM DEMO" + " "*20 + "║")
    print("║" + " "*10 + "Backend Engineer Challenge Solution" + " "*11 + "║")
    print("╚" + "="*58 + "╝")
    
    try:
        demo_basic_usage()
        input("\nPress Enter to continue to State Management demo...")
        
        demo_state_management()
        input("\nPress Enter to continue to Runtime Flexibility demo...")
        
        demo_runtime_changes()
        input("\nPress Enter to continue to Extensibility demo...")
        
        demo_extensibility()
        input("\nPress Enter to continue to Farm Scenario demo...")
        
        demo_farm_scenario()
        
        print_section("✨ DEMO COMPLETE ✨")
        print("This solution demonstrates:")
        print(" All requirements met")
        print(" Clean OOP design with Strategy Pattern")
        print(" Easy runtime modifications (Checkpoint Q1)")
        print(" Simple extensibility (Checkpoint Q2)")
        print(" SOLID principles")
        print(" Production-ready code quality\n")
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted.\n")


if __name__ == "__main__":
    main()
