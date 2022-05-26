# Take-home challenge: https://github.com/hackbrightacademy/ascii-art-take-home

class Canvas:
    """Create a canvas."""

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.shapes = []

    def add_shape(self, shape):
        """Add a shape to the canvas."""

        self.shapes.append(shape)

    def render(self):
        """Print out the canvas and its shapes."""

        # check if any of the shapes are overlapping
            # most recent shape should be on top

        print(self)

    def clear_shapes(self):
        """Clear all shapes from the canvas."""

        self.shapes = []

class Rectangle:
    """Create a rectangle."""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill = fill_char

    def change_fill_char(self, fill_char):
        """Change the character used to draw the rectangle."""

        self.fill = fill_char

    def move_rectangle(self, axis, num):
        """Move the rectangle along the axis by a given number."""

        axis = axis.lower()

        if axis == "x":
            self.start_x = self.start_x + num
            self.end_x = self.end_x + num

        if axis == "y":
            self.start_y = self.start_y + num
            self.end_y = self.end_y + num


def check_for_overlap(shape1, shape2):
    """Check if two shapes are overlapping.

    If so, most recent shape's fill should overwrite older shape's fill
    where they overlap."""

    pass


def check_if_out_of_bounds(canvas, shape):
    """Check if a shape is out of bounds."""

    pass


#----------------------------------------------------------------------#
#----------------------- Assumptions / Decisions ----------------------#
#----------------------------------------------------------------------#
