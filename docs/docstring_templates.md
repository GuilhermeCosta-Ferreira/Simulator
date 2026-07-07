# Python Docstring Templates

Use these templates when adding documentation to modules, classes, functions, and methods.

General rules:

* Keep the first line short and action-oriented.
* Explain **why** the object exists, not only what the code already says.
* Do not document `self` or `cls`.
* Document public APIs carefully.
* Private helpers only need docstrings when their behavior is non-obvious.
* Keep placeholders like `<...>` only while drafting. Replace them before committing.

---

## 1. Module Docstring

Place this at the top of the `.py` file, before imports.

```python
"""<Short description of what this module provides>.

This module defines <main responsibility of the file>. It is used by
<part of the system / workflow> to <reason this module exists>.

Main components:
    <ClassOrFunctionName>: <short purpose>.
    <ClassOrFunctionName>: <short purpose>.

Notes:
    <Important assumptions, limitations, or design decisions, if any>.
"""
```

### Minimal version

```python
"""<Domain> module for <project/system name>.

Defines <main class/functionality> used to <main purpose>.
"""
```

---

## 2. Class Docstring

Place this immediately under the class definition.

```python
class <ClassName>:
    """<Short description of what this class represents>.

    <ClassName> is responsible for <main responsibility>. It should be used
    when <usage context>. This class should not be responsible for
    <explicit non-responsibility, if useful>.

    Attributes:
        <attribute_name>: <description of the attribute>.
        <attribute_name>: <description of the attribute>.

    Examples:
        <Short example only if it improves clarity>.
    """
```

### Dataclass version

```python
@dataclass
class <ClassName>:
    """<Short description of the data or behavior represented by this class>.

    This class stores <state/data> and provides <behavior>. It is used by
    <system component> during <workflow/simulation step/process>.

    Attributes:
        <field_name>: <description of the field>.
        <field_name>: <description of the field>.
    """
```

---

## 3. Function Docstring

Use this for standalone functions.

```python
def <function_name>(<args>) -> <return_type>:
    """<Short description of what the function does>.

    <Optional longer explanation of the function's behavior, assumptions,
    side effects, or algorithm. Include this only when useful.>

    Args:
        <arg_name>: <description of the argument>.
        <arg_name>: <description of the argument>.

    Returns:
        <Description of the returned value>.

    Raises:
        <ExceptionType>: <When this exception is raised>.
    """
```

### Minimal function version

```python
def <function_name>(<args>) -> <return_type>:
    """<Short description of what the function does>.

    Args:
        <arg_name>: <description>.

    Returns:
        <description>.
    """
```

### Function with no return value

```python
def <function_name>(<args>) -> None:
    """<Short description of the side effect or action performed>.

    Args:
        <arg_name>: <description>.
    """
```

---

## 4. Method Docstring

Use this for methods inside classes.

Do not document `self`.

```python
class <ClassName>:
    def <method_name>(self, <args>) -> <return_type>:
        """<Short description of what this method does>.

        This method <explain how it changes or uses the object>. It should be
        called when <usage context>.

        Args:
            <arg_name>: <description of the argument>.
            <arg_name>: <description of the argument>.

        Returns:
            <Description of the returned value>.

        Raises:
            <ExceptionType>: <When this exception is raised>.
        """
```

### Method that updates internal state

```python
class <ClassName>:
    def <method_name>(self, <args>) -> None:
        """Update <part of the object state>.

        This method modifies <specific fields/state> according to
        <rule/input/process>.

        Args:
            <arg_name>: <description of the argument>.
        """
```

### Method that performs one simulation step

```python
class <ClassName>:
    def step(self, dt: float, context: "<ContextType>") -> None:
        """Advance the object by one simulation step.

        Updates the internal state using the elapsed simulation time and the
        shared simulation context.

        Args:
            dt: Simulation time step.
            context: Shared simulation context for the current run.
        """
```

---

## 5. Abstract Method Docstring

Use this in base classes and interfaces.

```python
class <BaseClassName>:
    def <method_name>(self, <args>) -> <return_type>:
        """<Short description of the required behavior>.

        Implementations must <contract that subclasses must satisfy>. This
        method is called by <caller/system component> during <workflow>.

        Args:
            <arg_name>: <description of the argument>.

        Returns:
            <Description of what implementations must return>.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError
```

---

## 6. Property Docstring

Use this for computed properties.

```python
@property
def <property_name>(self) -> <return_type>:
    """Return <description of computed value>.

    The value is computed from <source fields/data>. It does not modify the
    object state.
    """
```

---

## 7. Example for a Node Module

```python
"""Health module for simulation nodes.

Defines the node-attached module responsible for storing and updating
health-related state during a simulation.
"""

from dataclasses import dataclass
from typing import ClassVar

from .node_module import NodeModule


@dataclass
class HealthModule(NodeModule):
    """Store and update health-related state for a simulation node.

    This module represents health as a continuous value attached to a node.
    It is used in simulations where entities can age, recover, degrade, or
    become inactive due to health conditions.

    Attributes:
        health: Current health value of the node.
        age: Current age of the represented entity.
    """

    name: ClassVar[str] = "health"

    health: float
    age: float

    def apply(self, dt: float) -> None:
        """Apply one health update step.

        Updates the health module using the elapsed simulation time.

        Args:
            dt: Simulation time step.
        """
```
