#!/usr/bin/env python3
"""
ArchWiki Offline Language Selector GUI
Provides language selection interface for archwiki-offline script
# Original Author: Nikhil Singh <nik.singh710@gmail.com>
# Package Maintainer: Semyon5700
"""

import tkinter as tk
from tkinter import ttk
import subprocess
import os
import sys

class ArchWikiLanguageSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ArchWiki Offline - Language Selection")
        self.root.geometry("400x150")
        self.root.resizable(False, False)
        
        self.center_window()
        self.setup_ui()
        self.load_available_languages()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        title_label = ttk.Label(main_frame, text="Select ArchWiki Language", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        lang_label = ttk.Label(main_frame, text="Language:")
        lang_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        
        self.lang_var = tk.StringVar()
        self.lang_combo = ttk.Combobox(main_frame, textvariable=self.lang_var, state="readonly", width=30)
        self.lang_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 10))
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(20, 0))
        
        launch_btn = ttk.Button(button_frame, text="Launch ArchWiki", command=self.launch_archwiki)
        launch_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        cancel_btn = ttk.Button(button_frame, text="Cancel", command=self.root.destroy)
        cancel_btn.pack(side=tk.LEFT)
        
        main_frame.columnconfigure(1, weight=1)
        self.root.bind('<Return>', lambda e: self.launch_archwiki())
    
    def load_available_languages(self):
        wiki_base_dir = "/usr/share/doc/arch-wiki/html"
        languages = ["en"]
        
        if os.path.exists(wiki_base_dir):
            try:
                dirs = [d for d in os.listdir(wiki_base_dir) if os.path.isdir(os.path.join(wiki_base_dir, d))]
                languages.extend(dirs)
            except:
                pass
        
        languages = sorted(list(set(languages)))
        self.lang_combo['values'] = languages
        self.lang_var.set("en")
    
    def launch_archwiki(self):
        selected_lang = self.lang_var.get()
        
        if not selected_lang:
            tk.messagebox.showerror("Error", "Please select a language")
            return
        
        try:
            subprocess.Popen(['archwiki-offline', '-l', selected_lang])
            self.root.destroy()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to launch: {str(e)}")
    
    def run(self):
        self.root.mainloop()

def main():
    if not os.path.exists('/usr/bin/archwiki-offline'):
        print("Error: archwiki-offline script not found")
        sys.exit(1)
    
    app = ArchWikiLanguageSelector()
    app.run()

if __name__ == "__main__":
    main()
