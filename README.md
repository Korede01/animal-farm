# Animal Farm Challenge - Solution

A Python implementation of an object-oriented farm animal system demonstrating SOLID principles, design patterns, and clean code architecture.

## 🎯 Solution Overview

This solution implements a **flexible and extensible** animal farm system using the **Strategy Pattern** to address the key requirements and checkpoint questions.

### Key Features

✅ All required features implemented:
- Every animal can eat and sleep
- Animals have names and legs
- Birds have 2 legs, Dogs have 4 legs
- Some birds can fly, some can crow
- Some dogs can bark, some can chase sheep
- Animals cannot perform duties when hungry or sleepy
- Each animal has one action and one duty at a time

✅ **Runtime Flexibility** (Checkpoint Q1):
- Actions and duties can be changed at runtime without creating new instances
- Uses Strategy Pattern for swappable behaviors

✅ **Easy Extensibility** (Checkpoint Q2):
- New animals, actions, and duties can be added without modifying existing code
- Follows Open/Closed Principle

## 🏗️ Architecture & Design

### Design Patterns Used

**Strategy Pattern**: Actions and Duties are separate strategy classes that can be composed with animals and swapped at runtime. This is the key to answering both checkpoint questions.

```
Animal (Context)
    ├── has-a Action (Strategy)
    │   ├── FlyAction
    │   ├── CrowAction
    │   ├── BarkAction
    │   └── ChaseAction
    │
    └── has-a Duty (Strategy)
        ├── GuardDuty
        ├── LayEggsDuty
        └── HerdDuty
```

### SOLID Principles Applied

1. **Single Responsibility**: Each class has one clear purpose
   - `Animal`: Manages state and coordinates behaviors
   - `Action` classes: Define specific actions
   - `Duty` classes: Define specific duties

2. **Open/Closed**: Open for extension, closed for modification
   - New animals can be added by extending `Animal`
   - New actions/duties can be added by implementing interfaces
   - No need to modify existing code

3. **Liskov Substitution**: All actions and duties are interchangeable
   - Any `Action` can be used with any `Animal`
   - Any `Duty` can be used with any `Animal`

4. **Interface Segregation**: Small, focused interfaces
   - `Action` has only `perform()` and `get_name()`
   - `Duty` has only `execute()` and `get_name()`

5. **Dependency Inversion**: Depend on abstractions, not concretions
   - `Animal` depends on abstract `Action` and `Duty`, not concrete implementations

## 📁 Files

- **`animal_farm.py`**: Core implementation with all classes
- **`test_animal_farm.py`**: Comprehensive test suite (pytest)
- **`demo.py`**: Interactive demonstration
- **`README.md`**: This file
- **`THOUGHT_PROCESS.md`**: Detailed explanation of design decisions

## 🚀 Quick Start

### Run the Basic Example

```bash
python animal_farm.py
```

### Run the Interactive Demo

```bash
python demo.py
```

This will demonstrate:
- Basic animal creation and usage
- State management (hungry/sleepy)
- Runtime action/duty changes (Checkpoint Q1)
- Adding new animal types (Checkpoint Q2)
- Realistic farm scenario

### Run the Test Suite

```bash
# Install pytest if needed
pip install pytest

# Run tests
pytest test_animal_farm.py -v
```

Expected output: All tests passing ✅

## 💡 Usage Examples

### Basic Usage

```python
from animal_farm import Bird, Dog, FlyAction, BarkAction, GuardDuty, LayEggsDuty

# Create a flying bird
eagle = Bird("Eddie", FlyAction(), LayEggsDuty())
print(eagle.perform_action())  # "Eddie is flying high in the sky! "
print(eagle.perform_duty())    # "Eddie has laid fresh eggs! "

# Create a guard dog
rex = Dog("Rex", BarkAction(), GuardDuty())
print(rex.perform_action())    # "Rex barks loudly: Woof woof! "
print(rex.perform_duty())      # "Rex is guarding the farm vigilantly! "
```

### Runtime Flexibility (Checkpoint Q1)

```python
from animal_farm import Dog, BarkAction, ChaseAction, GuardDuty

# Create a dog that barks
dog = Dog("Duke", BarkAction(), GuardDuty())
print(dog.perform_action())  # "Duke barks loudly: Woof woof! "

# Change action at runtime - no need to create new instance!
dog.set_action(ChaseAction())
print(dog.perform_action())  # "Duke is chasing sheep across the field! "
```

### Easy Extensibility (Checkpoint Q2)

```python
from animal_farm import Animal, Action, Duty

# Add a new action
class MeowAction(Action):
    def perform(self, animal_name: str) -> str:
        return f"{animal_name} meows! "
    
    def get_name(self) -> str:
        return "Meow"

# Add a new animal type
class Cat(Animal):
    def __init__(self, name: str, action: Action = None, duty: Duty = None):
        super().__init__(name, legs=4, action=action, duty=duty)

# Use it immediately!
cat = Cat("Whiskers", MeowAction(), CatchMiceDuty())
print(cat.perform_action())  # "Whiskers meows! "
```

### State Management

```python
from animal_farm import Dog, BarkAction, GuardDuty

dog = Dog("Buddy", BarkAction(), GuardDuty())

# Dog gets hungry
dog.make_hungry()
print(dog.perform_duty())  # "Buddy is too hungry to perform duty!"

# Feed the dog
print(dog.eat())           # "Buddy is eating... nom nom nom! "
print(dog.perform_duty())  # "Buddy is guarding the farm vigilantly! "
```

## 🧪 Test Coverage

The test suite covers:

✅ All basic requirements\
✅ Bird-specific requirements (2 legs, fly, crow)\
✅ Dog-specific requirements (4 legs, bark, chase)\
✅ State management (hungry/sleepy blocking duties)\
✅ Runtime flexibility\
✅ Extensibility\
✅ Edge cases\
✅ Integration scenarios\

## 🎓 Design Rationale

### Why Strategy Pattern?

The Strategy Pattern was chosen because:

1. **Runtime Flexibility**: Behaviors can be changed at runtime by swapping strategy objects
2. **Open/Closed Principle**: New behaviors can be added without modifying existing classes
3. **Composition over Inheritance**: More flexible than creating subclasses for every combination
4. **Testability**: Each strategy can be tested independently

### Alternative Approaches Considered

1. **Inheritance-based**: Creating `FlyingBird`, `CrowingBird`, `BarkingDog`, etc.
   - ❌ Leads to class explosion
   - ❌ Makes runtime changes impossible

2. **Method overriding**: Override methods in each subclass
   - ❌ Violates Open/Closed Principle
   - ❌ Harder to add new behaviors

3. **Flag-based**: Use boolean flags like `can_fly`, `can_bark`
   - ❌ Leads to complex conditional logic
   - ❌ Violates Single Responsibility

The Strategy Pattern is the cleanest solution that addresses both checkpoint questions perfectly.

## 📊 Checkpoint Questions Answered

### Question 1: Runtime Changes

**How well does the design fare with changes for example updating the action for an animal in run time?**

**Answer**: Excellently! The Strategy Pattern makes this trivial:

```python
dog.set_action(new_action)  # Changes behavior instantly
dog.set_duty(new_duty)      # Changes duty instantly
```

No need to:
- Create a new instance
- Modify the class definition
- Restart the application

### Question 2: Adding New Animals

**How well does the design fare with changes creating a new animal?**

**Answer**: Very easy! Just inherit from `Animal` and optionally create new actions/duties:

```python
class Cat(Animal):  # 3 lines to add a new animal!
    def __init__(self, name: str, action=None, duty=None):
        super().__init__(name, legs=4, action=action, duty=duty)
```

No existing code needs to be modified. This is the **Open/Closed Principle** in action.

## 👨‍💻 Code Quality Features

- ✅ **Type hints**: All methods use type annotations
- ✅ **Docstrings**: Every class and method is documented
- ✅ **Clean code**: Follows PEP 8 style guide
- ✅ **DRY principle**: No code duplication
- ✅ **Error handling**: Validates preconditions with clear error messages

## 🏆 Production-Ready Features

This solution demonstrates backend engineering best practices:

- **Separation of Concerns**: Clear boundaries between classes
- **Testability**: Every component can be tested independently
- **Maintainability**: Easy to understand and modify
- **Scalability**: Can easily grow with new requirements
- **Documentation**: Well-commented and explained
- **Defensive Programming**: Validates state before operations
