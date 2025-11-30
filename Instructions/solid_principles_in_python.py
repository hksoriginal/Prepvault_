SOLID_PR = """


# SOLID Principles in Python with Examples

## 1. Single Responsibility Principle (SRP)
A class should have one, and only one, reason to change. This means that a class should only have one job or responsibility.

### Example:
```python
# Before SRP: A class handling both file operations and user notifications
class FileManager:
    def save_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
    
    def notify_user(self, message):
        print(f"Notification: {message}")

# After SRP: Separation of responsibilities into two classes
class FileManager:
    def save_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)

class Notifier:
    def notify_user(self, message):
        print(f"Notification: {message}")
```

---

## 2. Open/Closed Principle (OCP)
Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification. This means you should be able to add new functionality without changing existing code.

### Example:
```python
# Before OCP: A class with hardcoded payment methods
class PaymentProcessor:
    def process(self, payment_type):
        if payment_type == "credit_card":
            print("Processing credit card payment")
        elif payment_type == "paypal":
            print("Processing PayPal payment")

# After OCP: Using polymorphism to extend without modification
class PaymentMethod:
    def process(self):
        raise NotImplementedError

class CreditCardPayment(PaymentMethod):
    def process(self):
        print("Processing credit card payment")

class PayPalPayment(PaymentMethod):
    def process(self):
        print("Processing PayPal payment")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method
    
    def process(self):
        self.payment_method.process()
```

---

## 3. Liskov Substitution Principle (LSP)
Subtypes must be substitutable for their base types. This means that objects of a derived class should be able to replace objects of the base class without affecting the correctness of the program.

### Example:
```python
# Violating LSP: A subclass that changes the behavior of the base class
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")

# Correct LSP: A better hierarchy that adheres to LSP
class Bird:
    def move(self):
        print("Moving")

class FlyingBird(Bird):
    def move(self):
        print("Flying")

class Ostrich(Bird):
    def move(self):
        print("Running")
```

---

## 4. Interface Segregation Principle (ISP)
Clients should not be forced to depend on methods they do not use. This means that no client should be forced to implement an interface it doesn’t use.

### Example:
```python
# Violating ISP: A class implementing methods it doesn't need
class WorkerInterface:
    def work(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError

class Robot(WorkerInterface):
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError("Robots don't eat")

# Correct ISP: Split interfaces
class Workable:
    def work(self):
        raise NotImplementedError

class Eatable:
    def eat(self):
        raise NotImplementedError

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")
```

---

## 5. Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. Both should depend on abstractions. Also, abstractions should not depend on details. Details should depend on abstractions.

### Example:
```python
# Before DIP: High-level class depends on a low-level class
class LightBulb:
    def turn_on(self):
        print("LightBulb: ON")
    
    def turn_off(self):
        print("LightBulb: OFF")

class Switch:
    def __init__(self, light_bulb: LightBulb):
        self.light_bulb = light_bulb
    
    def operate(self, state):
        if state == "ON":
            self.light_bulb.turn_on()
        else:
            self.light_bulb.turn_off()

# After DIP: High-level class depends on abstraction
class Switchable:
    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: ON")
    
    def turn_off(self):
        print("LightBulb: OFF")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device
    
    def operate(self, state):
        if state == "ON":
            self.device.turn_on()
        else:
            self.device.turn_off()
```
"""
