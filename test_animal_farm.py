"""
Test Suite for Animal Farm Challenge
=====================================

This test suite demonstrates that:
1. All requirements are met
2. The design handles runtime changes elegantly (Checkpoint Question 1)
3. The design is easily extensible with new animals (Checkpoint Question 2)
"""

import pytest
from animal_farm import (
    Animal, Bird, Dog,
    FlyAction, CrowAction, BarkAction, ChaseAction,
    GuardDuty, LayEggsDuty, HerdDuty,
    Action, Duty
)


# ============================================================================
# TEST: Basic Animal Requirements
# ============================================================================

class TestBasicAnimalRequirements:
    """Test that all basic requirements are met."""
    
    def test_every_animal_can_eat(self):
        """Requirement: Every animal can eat."""
        bird = Bird("Tweety", FlyAction(), LayEggsDuty())
        dog = Dog("Buddy", BarkAction(), GuardDuty())
        
        bird.make_hungry()
        dog.make_hungry()
        
        assert "eating" in bird.eat().lower()
        assert "eating" in dog.eat().lower()
        assert not bird.is_hungry
        assert not dog.is_hungry
    
    def test_every_animal_can_sleep(self):
        """Requirement: Every animal can sleep."""
        bird = Bird("Tweety", FlyAction(), LayEggsDuty())
        dog = Dog("Buddy", BarkAction(), GuardDuty())
        
        bird.make_sleepy()
        dog.make_sleepy()
        
        assert "sleeping" in bird.sleep().lower()
        assert "sleeping" in dog.sleep().lower()
        assert not bird.is_sleepy
        assert not dog.is_sleepy
    
    def test_every_animal_has_a_name(self):
        """Requirement: Every Animal has a name."""
        bird = Bird("Tweety")
        dog = Dog("Buddy")
        
        assert bird.name == "Tweety"
        assert dog.name == "Buddy"
    
    def test_every_animal_has_legs(self):
        """Requirement: Every Animal has legs."""
        bird = Bird("Tweety")
        dog = Dog("Buddy")
        
        assert bird.legs == 2  # Birds have 2 legs
        assert dog.legs == 4   # Dogs have 4 legs
    
    def test_animal_cannot_perform_duty_when_hungry(self):
        """Requirement: No animal can perform their duty if they are hungry."""
        dog = Dog("Buddy", BarkAction(), GuardDuty())
        dog.make_hungry()
        
        result = dog.perform_duty()
        assert "hungry" in result.lower()
        assert "❌" in result
    
    def test_animal_cannot_perform_duty_when_sleepy(self):
        """Requirement: No animal can perform their duty if they are sleepy."""
        dog = Dog("Buddy", BarkAction(), GuardDuty())
        dog.make_sleepy()
        
        result = dog.perform_duty()
        assert "sleepy" in result.lower()
        assert "❌" in result
    
    def test_animal_can_perform_duty_when_not_hungry_or_sleepy(self):
        """Animals can perform duty when they are neither hungry nor sleepy."""
        dog = Dog("Buddy", BarkAction(), GuardDuty())
        
        result = dog.perform_duty()
        assert "❌" not in result
        assert "guarding" in result.lower()
    
    def test_every_animal_has_one_action_at_a_time(self):
        """Requirement: Every Animal can have only a single action at a time."""
        bird = Bird("Tweety", FlyAction())
        
        # Bird has one action
        assert bird.perform_action() == "Tweety is flying high in the sky! 🦅"
        
        # Change to a different action (replaces the previous one)
        bird.set_action(CrowAction())
        assert "Cock-a-doodle-doo" in bird.perform_action()
    
    def test_every_animal_has_one_duty_at_a_time(self):
        """Requirement: Every Animal can have only a single duty at a time."""
        dog = Dog("Rex", BarkAction(), GuardDuty())
        
        # Dog has one duty
        assert "guarding" in dog.perform_duty().lower()
        
        # Change to a different duty (replaces the previous one)
        dog.set_duty(HerdDuty())
        assert "herding" in dog.perform_duty().lower()
    
    def test_every_animal_must_have_a_duty(self):
        """Requirement: Every Animal must have a duty."""
        # Animal without duty should raise error when trying to perform
        dog = Dog("Buddy", BarkAction())  # No duty assigned
        
        with pytest.raises(ValueError, match="has no duty assigned"):
            dog.perform_duty()
    
    def test_every_animal_must_perform_an_action(self):
        """Requirement: Every Animal must perform an action."""
        # Animal without action should raise error when trying to perform
        bird = Bird("Tweety")  # No action assigned
        
        with pytest.raises(ValueError, match="has no action assigned"):
            bird.perform_action()


# ============================================================================
# TEST: Bird Specific Requirements
# ============================================================================

class TestBirdRequirements:
    """Test bird-specific requirements."""
    
    def test_birds_have_2_legs(self):
        """Requirement: Birds have 2 legs."""
        bird1 = Bird("Tweety", FlyAction())
        bird2 = Bird("Roger", CrowAction())
        
        assert bird1.legs == 2
        assert bird2.legs == 2
    
    def test_some_birds_can_fly(self):
        """Requirement: Some birds can fly (Not all birds can fly)."""
        flying_bird = Bird("Eagle", FlyAction(), LayEggsDuty())
        
        result = flying_bird.perform_action()
        assert "flying" in result.lower()
    
    def test_some_birds_can_crow(self):
        """Requirement: Some birds can Crow (for example a rooster)."""
        rooster = Bird("Roger", CrowAction(), LayEggsDuty())
        
        result = rooster.perform_action()
        assert "cock-a-doodle-doo" in result.lower()


# ============================================================================
# TEST: Dog Specific Requirements
# ============================================================================

class TestDogRequirements:
    """Test dog-specific requirements."""
    
    def test_dogs_have_4_legs(self):
        """Requirement: All dogs have 4 legs."""
        dog1 = Dog("Buddy", BarkAction())
        dog2 = Dog("Rex", ChaseAction())
        
        assert dog1.legs == 4
        assert dog2.legs == 4
    
    def test_some_dogs_can_bark(self):
        """Requirement: Some dogs can Bark."""
        barking_dog = Dog("Buddy", BarkAction(), GuardDuty())
        
        result = barking_dog.perform_action()
        assert "bark" in result.lower() or "woof" in result.lower()
    
    def test_some_dogs_can_chase_sheep(self):
        """Requirement: Some dogs can Chase sheep."""
        herding_dog = Dog("Rex", ChaseAction(), HerdDuty())
        
        result = herding_dog.perform_action()
        assert "chase" in result.lower() or "chasing" in result.lower()
        assert "sheep" in result.lower()


# ============================================================================
# TEST: Checkpoint Question 1 - Runtime Changes
# ============================================================================

class TestRuntimeFlexibility:
    """
    Checkpoint Question 1: How well does the design fare with changes 
    for example updating the action for an animal in run time.
    
    Answer: The Strategy Pattern makes this trivial!
    """
    
    def test_change_action_at_runtime(self):
        """Animals can change their action at runtime."""
        dog = Dog("Rex", BarkAction(), GuardDuty())
        
        # Initially barks
        result1 = dog.perform_action()
        assert "bark" in result1.lower() or "woof" in result1.lower()
        
        # Change to chasing at runtime
        dog.set_action(ChaseAction())
        result2 = dog.perform_action()
        assert "chase" in result2.lower() or "chasing" in result2.lower()
        
        # The action changed successfully!
    
    def test_change_duty_at_runtime(self):
        """Animals can change their duty at runtime."""
        dog = Dog("Rex", BarkAction(), GuardDuty())
        
        # Initially guards
        result1 = dog.perform_duty()
        assert "guard" in result1.lower()
        
        # Change to herding at runtime
        dog.set_duty(HerdDuty())
        result2 = dog.perform_duty()
        assert "herd" in result2.lower()
        
        # The duty changed successfully!
    
    def test_bird_can_change_from_flying_to_crowing(self):
        """A bird can change from flying to crowing at runtime."""
        bird = Bird("Tweety", FlyAction(), LayEggsDuty())
        
        # Initially flies
        assert "flying" in bird.perform_action().lower()
        
        # Learn to crow instead
        bird.set_action(CrowAction())
        assert "cock-a-doodle-doo" in bird.perform_action().lower()


# ============================================================================
# TEST: Checkpoint Question 2 - Extensibility
# ============================================================================

class TestExtensibility:
    """
    Checkpoint Question 2: How well does the design fare with changes 
    creating a new animal.
    
    Answer: Very easy! Just create new classes. No modification to existing code needed.
    """
    
    def test_add_new_animal_type_cat(self):
        """Demonstrate adding a completely new animal type: Cat."""
        
        # Step 1: Create new actions for cats
        class MeowAction(Action):
            def perform(self, animal_name: str) -> str:
                return f"{animal_name} meows: Meow meow! 🐱"
            
            def get_name(self) -> str:
                return "Meow"
        
        class PurrAction(Action):
            def perform(self, animal_name: str) -> str:
                return f"{animal_name} purrs contentedly! 😺"
            
            def get_name(self) -> str:
                return "Purr"
        
        # Step 2: Create new duty for cats
        class CatchMiceDuty(Duty):
            def execute(self, animal_name: str) -> str:
                return f"{animal_name} is catching mice in the barn! 🐭"
            
            def get_name(self) -> str:
                return "Catch Mice"
        
        # Step 3: Create new Cat class (without modifying ANY existing code!)
        class Cat(Animal):
            """Cats have 4 legs."""
            def __init__(self, name: str, action: Action = None, duty: Duty = None):
                super().__init__(name, legs=4, action=action, duty=duty)
        
        # Step 4: Use the new animal!
        cat = Cat("Whiskers", MeowAction(), CatchMiceDuty())
        
        assert cat.name == "Whiskers"
        assert cat.legs == 4
        assert "meow" in cat.perform_action().lower()
        assert "mice" in cat.perform_duty().lower()
        
        # Can also change actions at runtime
        cat.set_action(PurrAction())
        assert "purr" in cat.perform_action().lower()
        
        # Success! We added a new animal without touching existing code!
    
    def test_add_new_action_to_existing_animal(self):
        """Adding new actions to existing animals is trivial."""
        
        # Create a new action
        class SingAction(Action):
            def perform(self, animal_name: str) -> str:
                return f"{animal_name} sings beautifully! 🎵"
            
            def get_name(self) -> str:
                return "Sing"
        
        # Use it with existing Bird class (no modification needed!)
        singing_bird = Bird("Melody", SingAction(), LayEggsDuty())
        
        assert "sing" in singing_bird.perform_action().lower()
    
    def test_add_new_duty_to_existing_animal(self):
        """Adding new duties to existing animals is trivial."""
        
        # Create a new duty
        class PlowFieldDuty(Duty):
            def execute(self, animal_name: str) -> str:
                return f"{animal_name} is plowing the field! 🚜"
            
            def get_name(self) -> str:
                return "Plow Field"
        
        # Could be used with any animal (open for extension!)
        # For example, if we later add an Ox class
        dog = Dog("Strong", BarkAction(), PlowFieldDuty())
        assert "plow" in dog.perform_duty().lower()


# ============================================================================
# TEST: Edge Cases and Integration
# ============================================================================

class TestEdgeCases:
    """Test various edge cases and integration scenarios."""
    
    def test_animal_state_transitions(self):
        """Test that state transitions work correctly."""
        dog = Dog("Buddy", BarkAction(), GuardDuty())
        
        # Initially not hungry or sleepy
        assert not dog.is_hungry
        assert not dog.is_sleepy
        
        # Make hungry
        dog.make_hungry()
        assert dog.is_hungry
        
        # Eat to resolve hunger
        dog.eat()
        assert not dog.is_hungry
        
        # Make sleepy
        dog.make_sleepy()
        assert dog.is_sleepy
        
        # Sleep to resolve sleepiness
        dog.sleep()
        assert not dog.is_sleepy
    
    def test_duty_blocked_by_multiple_states(self):
        """Test that duty is blocked when hungry OR sleepy."""
        dog = Dog("Buddy", BarkAction(), GuardDuty())
        
        # Can perform when neither hungry nor sleepy
        result = dog.perform_duty()
        assert "❌" not in result
        
        # Cannot perform when hungry
        dog.make_hungry()
        result = dog.perform_duty()
        assert "❌" in result
        
        # Eat but become sleepy
        dog.eat()
        dog.make_sleepy()
        result = dog.perform_duty()
        assert "❌" in result
        
        # Sleep and should work again
        dog.sleep()
        result = dog.perform_duty()
        assert "❌" not in result
    
    def test_get_status_provides_comprehensive_info(self):
        """The get_status method provides useful information."""
        bird = Bird("Tweety", FlyAction(), LayEggsDuty())
        
        status = bird.get_status()
        
        assert "Tweety" in status
        assert "Bird" in status
        assert "2" in status  # 2 legs
        assert "Fly" in status  # Action name
        assert "Lay Eggs" in status  # Duty name


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == "__main__":
    # Run with pytest for detailed output
    pytest.main([__file__, "-v", "--tb=short"])
