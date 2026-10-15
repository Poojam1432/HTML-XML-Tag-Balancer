# PDA State Diagram
## HTML/XML Tag Balancer

### States

- q0: Process the input and perform stack operations.
- qaccept: All tags are balanced, and the stack is empty.
- qreject: A tag mismatch or unexpected closing tag is detected, or opening tags remain at the end.

### State Diagram

```text
                 START
                   |
                   v
             +-----------+
             |    q0     |
             |  Process  |
             |   Tags    |
             +-----------+
               /       \
              /         \
     Tags balanced    Error detected
     Stack is empty        |
            |              v
            v        +-------------+
       +---------+   |   qreject   |
       | qaccept |   | Imbalanced  |
       | Balanced|   +-------------+
       +---------+