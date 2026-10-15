import re

from stack import Stack


VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr",
    "img", "input", "link", "meta", "param",
    "source", "track", "wbr"
}


def check_balance(html):
    opening_tags_count = 0
    stack = Stack()

    pattern = r"<!--.*?-->|<![^>]*>|<\s*(/?)\s*([a-zA-Z][a-zA-Z0-9:-]*)\b[^>]*>"

    for match in re.finditer(pattern, html, re.DOTALL):
        token = match.group(0)

        # Ignore comments and declarations
        if token.startswith("<!--") or token.startswith("<!"):
            continue

        is_closing = match.group(1) == "/"
        tag = match.group(2).lower()

        if is_closing:
            if stack.is_empty():
                return {
                "balanced": False,"error": f"Unexpected closing tag </{tag}>","opening_tags_count": opening_tags_count
                }

            opening_tag = stack.peek()

            if opening_tag != tag:
                return {
                    "balanced": False,
                    "error": (
                        f"Closing tag </{tag}> does not match "
                        f"opening tag <{opening_tag}>"
                    ),
                    "opening_tags_count": opening_tags_count
                }
            

            stack.pop()

        else:
            if tag in VOID_TAGS or token.rstrip().endswith("/>"):
                continue

            stack.push(tag)
            opening_tags_count += 1

    if not stack.is_empty():
        return {
            "balanced": False,
            "error": f"Unclosed tag <{stack.peek()}>",
            "opening_tags_count": opening_tags_count
        }

    return {
        "balanced": True,
        "error": None,
        "opening_tags_count": opening_tags_count
}