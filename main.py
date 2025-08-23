import os, sys
import inspect as ins
import time
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
import my_math
import my_math_tests
import mm_test
from my_math_tests import TestLineEq
import unittest


load_dotenv()
giga = GigaChat(
    credentials=os.getenv('GIGACHAT_CREDENTIALS')
)

def extract_unittest_section(text):
    """
    Extract the part of a string from "import unittest" to "unittest.main"

    Args:
        text (str): The input string containing unittest code

    Returns:
        str: The extracted section from "import unittest" to "unittest.main"
    """
    start_marker = "import unittest"
    end_marker = "unittest.main()"

    # Find the start position
    start_pos = text.find(start_marker)
    if start_pos == -1:
        return "ERROR: Start marker 'import unittest' not found"

    # Find the end position
    end_pos = text.find(end_marker, start_pos)
    if end_pos == -1:
        return "ERROR: End marker 'unittest.main()' not found"

    # Extract the section (include the end marker)
    end_pos += len(end_marker)
    extracted_section = text[start_pos:end_pos]

    return extracted_section


def test_writer_agent(sources, tests):
    s_name = ins.getmodule(sources).__name__
    ts_name = ins.getmodule(tests).__name__
    chat = Chat(
            messages=[
                Messages(
                    role=MessagesRole.SYSTEM,
                    content=(f'Напиши тест для Python-функций из модуля {s_name}: {ins.getsource(sources)}, '
                             'используя unittests. Выведи ТОЛЬКО код модуля с тестами. coding=utf-8')
                )
            ]
        )
    i = 1
    while i:
        response = giga.chat(chat)
        answer = response.choices[0].message.content
        print('---------- Реплика модели: ---------------')
        code_for_testModule = extract_unittest_section(answer)
        if code_for_testModule[0:5] != 'ERROR: ':
            with open(f"{ts_name}.py", "w", encoding="utf-8") as file:
                file.write(str(code_for_testModule))
            print(f'Код полученный от модели записан в файл {ts_name}')
            print(25 * '-', ' Запускаем тесты ', 25 * '-')
            errors = run_tests()
            print(f'Всего ошибок и падений {errors}')
        else:
            print('ОШИБКА: В ответе модели код не найден')
        print("-------------------------")
        question = input("Введите уточнения (0 для выхода): ")
        if question == "0":
            break
        chat.messages.append(
            Messages(
                role=MessagesRole.USER,
                content=question
            )
        )


# Run tests from my_math_tests.py
def run_tests():
    """Run all tests from my_math_tests.py"""
    print("Running tests from my_math_tests.py...")
    print("=" * 50)
    time.sleep(0.01)
    
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestLineEq)
    
    # Run the tests
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    time.sleep(0.01)
    
    print("=" * 50)
    # print(f"Tests run: {result.testsRun}")
    # print(f"Failures: {len(result.failures)}")
    # print(f"Errors: {len(result.errors)}")
    
    # if result.failures:
    #     print("\nFailures:")
    #     for test, traceback in result.failures:
    #         print(f"  {test}: {traceback}")
    #
    # if result.errors:
    #     print("\nErrors:")
    #     for test, traceback in result.errors:
    #         print(f"  {test}: {traceback}")
    
    return len(result.failures) + len(result.errors)


test_writer_agent(my_math, mm_test)