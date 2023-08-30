# -- Bring to you by Vihaan Mody
# -- Enjoy the script!

from clint.textui.colored import blue, yellow, cyan, magenta, red
from pyfiglet import figlet_format

def Banner():
    print(cyan(figlet_format("CalcCLI", "slant"), bold=True), end="")
    print(yellow("A Creative Calculator", bold=True) + magenta(" v1.0"))

def Calculate(operation, x, y):
    return eval(f"{x}{operation}{y}")

def Main():
    try:
        Operation = int(input(f"""
{yellow("[")}\033[95m1\033[m{yellow("]")}{blue(" Basic Operations")}
{yellow("[")}\033[95m2\033[m{yellow("]")}{blue(" Number-Theoretic & Representation Functions")}
{yellow("[")}\033[95m3\033[m{yellow("]")}{blue(" Mathematical Constants")}
{yellow("[")}\033[95m4\033[m{yellow("]")}{blue(" Power & Logarithmic Functions")}
{yellow("[")}\033[95m5\033[m{yellow("]")}{blue(" Trigonometric Functions")}
{yellow("[")}\033[95m6\033[m{yellow("]")}{blue(" Angular Conversion")}
{yellow("[")}\033[95m7\033[m{yellow("]")}{blue(" Hyperbolic Functions")}
\033[95mOption\033[m>"""))
    except ValueError:
        exit(red("Invalid Option"))
    except KeyboardInterrupt:
        exit()
    except Exception as Error:
        exit(Error)
    
    if Operation > 7 or Operation <= 0:
        exit(red("Out Of Option Range"))
    elif Operation == 1:
            try:
                Operation = int(input(f"""
{yellow("[")}\033[95m1\033[m{yellow("]")}{blue(" Addition")}
{yellow("[")}\033[95m2\033[m{yellow("]")}{blue(" Subtraction")}
{yellow("[")}\033[95m3\033[m{yellow("]")}{blue(" Multiplication")}
{yellow("[")}\033[95m4\033[m{yellow("]")}{blue(" Division")}
\033[95mOption\033[m>"""))
            except ValueError:
                exit(red("Invalid Option"))
            except KeyboardInterrupt:
                exit()
            except Exception as Error:
                exit(Error)
            if Operation == 1:
                x = int(input("Enter number x: "))
                y = int(input("Enter number y: "))
                print(Calculate("+", x, y))
                input("Back>")
                import calccli

Banner()
Main()
