# grocery/tests/test_grocery.py

import io
import tempfile
from pytest import raises
from grocery import read_grocery_file

def test_bad_grocery_type():
    csv_data = """apple,1.0,foo"""

    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w') as tmp_file:
        # Write the CSV data to the temporary file
        tmp_file.write(csv_data)
        tmp_file.flush()

        # Pass the file path to the function
        with raises(KeyError):
            read_grocery_file(tmp_file.name)

def test_bad_price():
    csv_data = """apple,foo,fruit"""

    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w') as tmp_file:
        # Write the CSV data to the temporary file
        tmp_file.write(csv_data)
        tmp_file.flush()

        # Pass the file path to the function
        with raises(ValueError):
            read_grocery_file(tmp_file.name)
