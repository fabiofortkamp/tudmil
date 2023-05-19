import sys
import pathlib 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

OUTPUT_FILENAME = "output.png"
FIG_SIZE_CM = 10
FIG_SIZE_IN = FIG_SIZE_CM / 2.54

def read_input_filename() -> str:
    """Reads the input filename from the command line.
    
    Returns:
        str: The input filename.
    """
    return sys.argv[-1]


def initialize_figure_and_axes() -> tuple[Figure, Axes]:
    """Initializes the figure and axes for the plot.
    
    Returns:
        fig: The figure object.
        ax: The axes object.
    
    """
    fig, ax = plt.subplots(figsize=(FIG_SIZE_IN, FIG_SIZE_IN))
    ax.set_xlim(-FIG_SIZE_CM/2, FIG_SIZE_CM/2)
    ax.set_ylim(-FIG_SIZE_CM/2, FIG_SIZE_CM/2)
    return fig


def read_lines_from_file(filename) -> list[str]:
    """Reads the lines from the input file.
    
    Args:
        filename: The name of the input file.
    
    Returns:
        list[str]: The lines from the input file.
    """
    with open(filename,'r') as f:
        lines = f.readlines()
    return lines

def parse_command_from_single_line(line: str) -> tuple[str,str]:
    """Parses a single line from the input file.
    
    Example:
        >>> parse_command_from_single_line("P 3 # comment")
        ('P', '3')
        >>> parse_command_from_single_line('W 10 invalid')
        ('W', '10')
        >>> parse_command_from_single_line('U')
        ('U', '')
    
    Args:
        line: A single line from the input file.
    
    Returns:
        tuple[str,str]: The command and the argument.
    """
    
    
    fields = line.split()
    
    command = fields[0]
    
    try:
        argument = fields[1]
    except IndexError:
        argument = ""
    
    return command, argument

def parse_commands(lines):
    
    return [parse_command_from_single_line(line) for line in lines]


linewidth = 1
def select_pen_size(fig, argument):
    global linewidth
    linewidth = int(argument)
    
x_curr, y_curr = 0, 0
def pen_down(fig, argument):
    global x_curr, y_curr
    x_curr, y_curr = 0, 0
    
def pen_up(fig, argument):
    pass

def draw_north(fig, argument):
    global x_curr, y_curr
    x_new, y_new = x_curr, y_curr + int(argument)
    fig.gca().plot([x_curr, x_new], [y_curr, y_new], linewidth=linewidth, color='black')
    x_curr, y_curr = x_new, y_new
    
def draw_east(fig, argument):
    global x_curr, y_curr
    x_new, y_new = x_curr + int(argument), y_curr
    fig.gca().plot([x_curr, x_new], [y_curr, y_new], linewidth=linewidth, color='black')
    x_curr, y_curr = x_new, y_new
    
def draw_south(fig, argument):
    global x_curr, y_curr
    x_new, y_new = x_curr, y_curr - int(argument)
    fig.gca().plot([x_curr, x_new], [y_curr, y_new], linewidth=linewidth, color='black')
    x_curr, y_curr = x_new, y_new
    
def draw_west(fig, argument):
    global x_curr, y_curr
    x_new, y_new = x_curr - int(argument), y_curr
    fig.gca().plot([x_curr, x_new], [y_curr, y_new], linewidth=linewidth, color='black')
    x_curr, y_curr = x_new, y_new

COMMANDS = {
    "P": select_pen_size,
    "D": pen_down,
    "U": pen_up,
    "N": draw_north,
    "E": draw_east,
    "S": draw_south,
    "W": draw_west,
}

def execute_instruction(fig, instruction):
    command, argument = instruction
    COMMANDS[command](fig, argument)

fig = initialize_figure_and_axes()
filename = read_input_filename()
lines = read_lines_from_file(filename)
instructions = parse_commands(lines)
for instruction in instructions: 
    execute_instruction(fig, instruction)    

fig.savefig(OUTPUT_FILENAME, dpi=600)