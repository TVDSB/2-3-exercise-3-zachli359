import pytest
import student 



def test_simple_number():
    input_values=['7']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert 7 == output[1]

def test_all_num():
    for i in range(1,100):
        if i % 3 == 0 or i % 5 == 0:
            continue
        input_values=[str(i)]
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert i == output[1]

def test_all_buzz():
    for i in range(5,500,5):
        if i % 15 == 0:
            continue
        input_values=[str(i)]
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert "buzz" in output[1].lower()

def test_all_fizz():
    for i in range(3,500,3):
        if i % 15 == 0:
            continue
        input_values=[str(i)]
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert "fizz" in output[1].lower()

def test_all_fizzbuzz():
    for i in range(15,500,15):
        input_values=[str(i)]
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert "fizz" in output[1].lower() and "buzz" in output[1].lower()
