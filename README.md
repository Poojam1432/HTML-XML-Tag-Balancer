# HTML/XML Tag Balancer Using Pushdown Automaton

## 1. Project Overview

The HTML/XML Tag Balancer is a simple application that checks whether opening and closing tags are properly matched and nested.

It uses the concept of a Pushdown Automaton (PDA) from Theory of Computation. A stack is used to store opening tags and match them with closing tags.

## 2. Objectives

- Understand the practical application of a Pushdown Automaton.
- Implement a stack to manage opening and closing tags.
- Identify mismatched, unexpected, and unclosed tags.
- Test the application using valid and invalid HTML samples.

## 3. Technologies Used

- Python
- Visual Studio Code
- Git and GitHub
- Pytest for automated testing

## 4. Working Principle

1. The user enters an HTML string.
2. The program identifies opening and closing tags.
3. Opening tags are pushed onto the stack.
4. When a closing tag appears, it is compared with the top of the stack.
5. If the tags match, the opening tag is removed.
6. If they do not match, the program reports an error.
7. If the stack is empty at the end, the tags are considered balanced.

## 5. Project Structure

```text
HTML-XML-Tag-Balancer/
├── src/
│   ├── stack.py
│   ├── pda.py
│   └── main.py
├── dataset/
│   └── html_samples.json
├── tests/
│   └── test_pda.py
└── README.md
## 10. Test Cases

The application has been tested using the following inputs:

| Test Case | Input | Expected Result |
|---|---|---|
| 1 | `<div><p>Hello</p></div>` | Balanced |
| 2 | `<div><b>Hello</div></b>` | Imbalanced |
| 3 | `<div><p>Hello</div>` | Imbalanced |
| 4 | `</div>` | Imbalanced |
| 5 | Empty input | Balanced |
| 6 | `<div>Hello<br><img src="photo.jpg"><hr></div>` | Balanced |

Automated tests are also available in the `tests` folder and use the dataset in `dataset/html_samples.json`.

Run the automated tests with:

```bash
py -m pytest tests/test_pda.py -v