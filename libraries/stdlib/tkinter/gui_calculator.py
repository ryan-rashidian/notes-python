"""Simple calculator GUI using Tkinter.

Author: Ryan Rashidian
Date: 2025-09-04
"""

from __future__ import annotations

from tkinter import * # type: ignore
import tkinter.ttk as ttk

# Commands
def _button_press(window: Window, value):
    """Append equation command."""
    window.equation_text += str(value)
    window.equation_label.set(window.equation_text) 

def _equals(window: Window):
    """Evaluate equation command."""
    try:
        result = str(eval(window.equation_text))
        window.equation_label.set(result)
        window.equation_text = result

    except SyntaxError:
        window.equation_label.set('SYNTAX ERROR')
        window.equation_text = ''
    except ZeroDivisionError:
        window.equation_label.set('DIVISION ERROR')
        window.equation_text = ''

def _clear(window: Window):
    """Clear equation command."""
    window.equation_label.set('')
    window.equation_text = ''

# GUI
class Window(Tk):
    """Calculator GUI"""

    def __init__(self):
        """Initialize window with Tk"""
        super().__init__()
        self.title('Calculator')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.equation_text = ''
        self.equation_label = StringVar()
        self.label = ttk.Label(
            self,
            textvariable = self.equation_label,
            font = ('', 36),
            background='white',
            anchor='center'
        )
        self.label.grid(row=0, sticky='nsew')

        self.frame = ttk.Frame(self)
        self.frame.config(borderwidth=3, relief='raised')
        self.frame.grid(row=1, sticky='nsew')

        for col in range(4):
            self.frame.columnconfigure(col, weight=1)
        for row in range(5):
            self.frame.rowconfigure(row, weight=1)

        # Load button panel
        self.buttons()

    def buttons(self):
        """Button layout."""
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        buttons_n = []
        for n in numbers:
            button = ttk.Button(
                self.frame,
                text = f'{n}',
                command = lambda x=n: _button_press(self, x)
            )
            buttons_n.append(button)

        buttons_n[1].grid(row=1, column=0, sticky='nsew')
        buttons_n[2].grid(row=1, column=1, sticky='nsew')
        buttons_n[3].grid(row=1, column=2, sticky='nsew')
        buttons_n[4].grid(row=2, column=0, sticky='nsew')
        buttons_n[5].grid(row=2, column=1, sticky='nsew')
        buttons_n[6].grid(row=2, column=2, sticky='nsew')
        buttons_n[7].grid(row=3, column=0, sticky='nsew')
        buttons_n[8].grid(row=3, column=1, sticky='nsew')
        buttons_n[9].grid(row=3, column=2, sticky='nsew')
        buttons_n[0].grid(row=4, column=0, sticky='nsew')

        symbols = ['.', '+', '-', '*', '/']
        buttons_s = {}
        for s in symbols:
            button = ttk.Button(
                self.frame,
                text = f'{s}',
                command = lambda x=s: _button_press(self, x)
            )
            buttons_s[s] = button

        buttons_s['.'].grid(row=4, column=1, sticky='nsew')
        buttons_s['+'].grid(row=1, column=3, sticky='nsew')
        buttons_s['-'].grid(row=2, column=3, sticky='nsew')
        buttons_s['*'].grid(row=3, column=3, sticky='nsew')
        buttons_s['/'].grid(row=4, column=3, sticky='nsew')

        button_equals = ttk.Button(
            self.frame,
            text = '=',
            command = lambda: _equals(self)
        )
        button_equals.grid(row=4, column=2, sticky='nsew')

        button_clear = ttk.Button(
            self.frame,
            text = 'clear',
            command = lambda: _clear(self)
        )
        button_clear.grid(row=0, column=0, columnspan=4, sticky='nsew')

if __name__ == '__main__':
    window = Window()
    window.mainloop()

