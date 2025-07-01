import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Scans the text and yields all floating-point numbers found.

    Parameters:
        text (str): The input text containing numbers.

    Yields:
        float: The next floating-point number found in the text.
    """
    pattern = r'\d+\.\d+'
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculates the total sum of floating-point numbers in the text,
    using the generator function provided.

    Parameters:
        text (str): The input text containing numbers.
        func (Callable): A function returning a generator of floats.

    Returns:
        float: The sum of all numbers found in the text.
    """
    return sum(func(text))



# ======= Usage Example =======

if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}") # Outputs: 'Загальний дохід: 1351.46'