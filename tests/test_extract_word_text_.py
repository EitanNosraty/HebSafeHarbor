import pytest

import docx2txt


@pytest
def extract_hello_world():
    my_text = docx2txt.process("hello.docx")
    print(my_text)
    return my_text == "hello world"
