"""
Animal Farm Test
================

This project implements a flexible animal farm system using the Strategy Pattern
for maximum extensibility and runtime flexibility.

Design Decisions:
- Strategy Pattern: Actions and Duties are separate, swappable objects
- Open/Closed Principle: Easy to add new animals, actions, duties without modifying existing code
- State Management: Animals track hungry/sleepy states that affect duty execution
- Composition over Inheritance: Behaviors are composed rather than inherited

Author: Erinle Oluwakorede Olatunde
Date: 2025-11-24
"""

from abc import ABC, abstractmethod
from typing import Optional


# ============================================================================
# STRATEGY PATTERN: Action Classes
# ============================================================================

class Action(ABC):
    """Abstract base class for all animal actions."""
    
    @abstractmethod
    def perform(self, animal_name: str) -> str:
        """
        Returns:
            String description of the action performed
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the name of this action."""
        pass


class FlyAction(Action):
    """Action for flying (typically for birds)."""
    
    def perform(self, animal_name: str) -> str:
        return f"{animal_name} is flying high in the sky! 🦅"
    
    def get_name(self) -> str:
        return "Fly"


class CrowAction(Action):
    """Action for crowing (for roosters and similar birds)."""
    
    def perform(self, animal_name: str) -> str:
        return f"{animal_name} crows: Cock-a-doodle-doo!"
    
    def get_name(self) -> str:
        return "Crow"


class BarkAction(Action):
    """Action for barking (for dogs)."""
    
    def perform(self, animal_name: str) -> str:
        return f"{animal_name} barks loudly: Woof woof!"
    
    def get_name(self) -> str:
        return "Bark"


class ChaseAction(Action):
    """Action for chasing sheep (for herding dogs)."""
    
    def perform(self, animal_name: str) -> str:
        return f"{animal_name} is chasing sheep across the field!"
    
    def get_name(self) -> str:
        return "Chase Sheep"


# ============================================================================
# STRATEGY PATTERN: Duty Classes
# ============================================================================

class Duty(ABC):
    """Abstract base class for all animal duties."""
    
    @abstractmethod
    def execute(self, animal_name: str) -> str:
        """
        Returns:
            String description of the duty executed
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the name of this duty."""
        pass


class GuardDuty(Duty):
    """Duty for guarding the farm."""
    
    def execute(self, animal_name: str) -> str:
        return f"{animal_name} is guarding the farm vigilantly!"
    
    def get_name(self) -> str:
        return "Guard"


class LayEggsDuty(Duty):
    """Duty for laying eggs."""
    
    def execute(self, animal_name: str) -> str:
        return f"{animal_name} has laid an egg!"
    
    def get_name(self) -> str:
        return "Lay Eggs"


class HerdDuty(Duty):
    """Duty for herding sheep."""
    
    def execute(self, animal_name: str) -> str:
        return f"{animal_name} is herding sheep together!"
    
    def get_name(self) -> str:
        return "Herd Sheep"


# ============================================================================
# BASE ANIMAL CLASS
# ============================================================================

class Animal:
    """
    Base class for all farm animals.
    
    Every animal has:
    - A name
    - A number of legs
    - The ability to eat and sleep
    - One action and one duty at a time
    - State tracking (hungry, sleepy)
    
    Animals cannot perform duties when hungry or sleepy.
    """
    
    def __init__(self, name: str, legs: int, action: Optional[Action] = None, duty: Optional[Duty] = None):
        """
        Initialize an animal.
        
        Args:
            name: The animal's name
            legs: Number of legs the animal has
            action: The action this animal can perform (optional)
            duty: The duty this animal must perform (optional)
        """
        self._name = name
        self._legs = legs
        self._action = action
        self._duty = duty
        self._is_hungry = False
        self._is_sleepy = False
    
    # Properties
    @property
    def name(self) -> str:
        """Get the animal's name."""
        return self._name
    
    @property
    def legs(self) -> int:
        """Get the number of legs."""
        return self._legs
    
    @property
    def is_hungry(self) -> bool:
        """Check if the animal is hungry."""
        return self._is_hungry
    
    @property
    def is_sleepy(self) -> bool:
        """Check if the animal is sleepy."""
        return self._is_sleepy
    
    # State management methods
    def eat(self) -> str:
        """
        Animal eats and is no longer hungry.
        
        Returns:
            String describing the eating action
        """
        self._is_hungry = False
        return f"{self._name} is eating... nom nom nom! 🍽️"
    
    def sleep(self) -> str:
        """
        Animal sleeps and is no longer sleepy.
        
        Returns:
            String describing the sleeping action
        """
        self._is_sleepy = False
        return f"{self._name} is sleeping..."
    
    def make_hungry(self) -> None:
        """Make the animal hungry."""
        self._is_hungry = True
    
    def make_sleepy(self) -> None:
        """Make the animal sleepy."""
        self._is_sleepy = True
    
    # Action and Duty management (Strategy Pattern in action!)
    def set_action(self, action: Action) -> None:
        """
        Set or change the animal's action at runtime.
        
        This demonstrates the answer to checkpoint question 1:
        "How well does the design fare with changes for example updating 
        the action for an animal in run time."
        
        Args:
            action: The new action for this animal
        """
        self._action = action
    
    def set_duty(self, duty: Duty) -> None:
        """
        Set or change the animal's duty at runtime.
        
        Args:
            duty: The new duty for this animal
        """
        self._duty = duty
    
    def perform_action(self) -> str:
        """
        Perform the animal's action.
        
        Returns:
            String describing the action performed
            
        Raises:
            ValueError: If no action is assigned
        """
        if self._action is None:
            raise ValueError(f"{self._name} has no action assigned!")
        
        return self._action.perform(self._name)
    
    def perform_duty(self) -> str:
        """
        Perform the animal's duty.
        
        NOTE: Animals cannot perform their duty if they are hungry or sleepy!
        
        Returns:
            String describing the duty performed or why it cannot be performed
            
        Raises:
            ValueError: If no duty is assigned
        """
        if self._duty is None:
            raise ValueError(f"{self._name} has no duty assigned!")
        
        # Check preconditions
        if self._is_hungry:
            return f"{self._name} is too hungry to perform duty! Feed them first."
        
        if self._is_sleepy:
            return f"{self._name} is too sleepy to perform duty! Let them sleep first."
        
        return self._duty.execute(self._name)
    
    def get_status(self) -> str:
        """Get a detailed status report of the animal."""
        action_name = self._action.get_name() if self._action else "None"
        duty_name = self._duty.get_name() if self._duty else "None"
        
        states = []
        if self._is_hungry:
            states.append("🍖 Hungry")
        if self._is_sleepy:
            states.append("😴 Sleepy")
        
        state_str = ", ".join(states) if states else "✅ Ready"
        
        return (
            f"\n{'='*50}\n"
            f"🐾 {self._name}\n"
            f"{'='*50}\n"
            f"Type: {self.__class__.__name__}\n"
            f"Legs: {self._legs}\n"
            f"Action: {action_name}\n"
            f"Duty: {duty_name}\n"
            f"State: {state_str}\n"
            f"{'='*50}"
        )


# ============================================================================
# ANIMAL SUBCLASSES
# ============================================================================

class Bird(Animal):
    """
    Bird class - all birds have 2 legs.
    
    Some birds can fly, some can crow (like roosters).
    """
    
    def __init__(self, name: str, action: Optional[Action] = None, duty: Optional[Duty] = None):
        """
        Initialize a bird.
        
        Args:
            name: The bird's name
            action: The action this bird can perform (e.g., FlyAction or CrowAction)
            duty: The duty this bird must perform
        """
        super().__init__(name, legs=2, action=action, duty=duty)


class Dog(Animal):
    """
    Dog class - all dogs have 4 legs.
    
    Some dogs can bark, some can chase sheep.
    """
    
    def __init__(self, name: str, action: Optional[Action] = None, duty: Optional[Duty] = None):
        """
        Initialize a dog.
        
        Args:
            name: The dog's name
            action: The action this dog can perform (e.g., BarkAction or ChaseAction)
            duty: The duty this dog must perform
        """
        super().__init__(name, legs=4, action=action, duty=duty)


# ============================================================================
# EXAMPLE USAGE (demonstrates extensibility)
# ============================================================================

if __name__ == "__main__":
    print("🌾 Welcome to the Animal Farm! 🌾\n")
    
    # Create a rooster that crows and lays eggs
    rooster = Bird(
        name="Roger the Rooster",
        action=CrowAction(),
        duty=LayEggsDuty()
    )
    
    print(rooster.get_status())
    print(rooster.perform_action())
    print(rooster.perform_duty())
    
    print("\n" + "="*50 + "\n")
    
    # Create a guard dog
    guard_dog = Dog(
        name="Rex",
        action=BarkAction(),
        duty=GuardDuty()
    )
    
    print(guard_dog.get_status())
    print(guard_dog.perform_action())
    print(guard_dog.perform_duty())
    
    print("\n" + "="*50)
    print("Making Rex hungry...")
    print("="*50 + "\n")
    
    guard_dog.make_hungry()
    print(guard_dog.get_status())
    print(guard_dog.perform_duty())  # Should fail!
    
    print("\n" + guard_dog.eat())
    print(guard_dog.perform_duty())  # Should work now!
    
    print("\n" + "="*50)
    print("RUNTIME FLEXIBILITY DEMO (Checkpoint Question 1)")
    print("="*50 + "\n")
    
    print("Changing Rex's action from Bark to Chase Sheep at runtime...")
    guard_dog.set_action(ChaseAction())
    print(guard_dog.perform_action())  # Now he chases sheep!
