# Formal Definition of the Pushdown Automaton

## 1. Introduction

A Pushdown Automaton (PDA) is a computational model that consists of a finite control and a stack. It is useful for recognizing nested structures.

In this project, a stack is used to check whether HTML opening and closing tags are correctly matched and nested.

## 2. Components of the PDA

A PDA is formally represented as:

M = (Q, Σ, Γ, δ, q0, Z0, F)

Where:

- Q: Set of states
- Σ: Input alphabet
- Γ: Stack alphabet
- δ: Transition function
- q0: Initial state
- Z0: Initial stack symbol
- F: Set of accepting states

## 3. Application to the Project

### States (Q)

- q0: Read and examine the input.
- qaccept: Input has balanced tags.
- qreject: An error is detected.

These states describe the project's conceptual behavior.

### Input Alphabet (Σ)

The input consists of HTML text containing opening tags, closing tags, and other content.

### Stack Alphabet (Γ)

The stack stores the names of opening tags, such as:

- html
- body
- div
- p
- b

### Initial Stack Symbol (Z0)

The stack starts empty in the Python implementation. Z0 is a theoretical representation that may be used in a formal PDA definition.

### Transition Function (δ)

1. When an opening tag is encountered, push its name onto the stack.
2. When a closing tag is encountered, compare its name with the top of the stack.
3. If the names match, pop the opening tag.
4. If the stack is empty when a closing tag is encountered, reject the input.
5. If the tag names do not match, reject the input.
6. At the end of the input, accept if the stack is empty; otherwise, reject.

HTML void tags such as `br` and `img` are ignored by the stack because they do not require closing tags.

## 4. Example

Input:

<html><body><b>Hello</b></body></html>

Stack operations:

1. Read <html> → Push html
2. Read <body> → Push body
3. Read <b> → Push b
4. Read </b> → Pop b
5. Read </body> → Pop body
6. Read </html> → Pop html

The stack is empty at the end.

Result: BALANCED

## 5. Example of Invalid Input

Input:

<div><b>Hello</div></b>

The stack contains div and b when the closing tag </div> is encountered.

The top of the stack is b, which does not match div.

Result: IMBALANCED

## 6. Conclusion

This project demonstrates the practical use of a stack-based PDA concept to check the matching and nesting of HTML tags.

Note: The implementation is a simplified educational checker, not a complete HTML/XML parser.