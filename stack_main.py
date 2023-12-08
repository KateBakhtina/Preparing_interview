from stack import Stack


def check_brackets(brackets: str) -> bool:
    brackets_dict = dict([("()"), ("[]"), ("{}")])
    brackets_stack = Stack()
    for element in brackets:
        if element in brackets_dict:
            brackets_stack.push(element)
        elif (
            brackets_stack.size() > 0
            and brackets_dict.get(brackets_stack.peek()) == element
        ):
            brackets_stack.pop_element()
        else:
            brackets_stack.push(element)
    return brackets_stack.is_empty()


if __name__ == "__main__":
    print(check_brackets("(((([{}]))))"))
