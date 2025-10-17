#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
try:
    from view.gui_viewer import AuthViewerApp
except ImportError as e:
    print("ERRO DE IMPORTAÇÃO: Não foi possível encontrar os módulos.")
    sys.exit(1)


def main():
    root = tk.Tk()
    app = AuthViewerApp(root) 
    root.mainloop()

if __name__ == '__main__':
    main()