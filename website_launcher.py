import tkinter as tk
from tkinter import messagebox
import webbrowser
import time
import json
import os

class WebsiteLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Launcher")
        self.root.geometry("400x500")
        
        # List to store website entries
        self.website_entries = []
        
        # Create and pack widgets
        tk.Label(root, text="Enter websites to launch:", font=('Arial', 12)).pack(pady=10)
        
        # Frame for website entries
        self.entries_frame = tk.Frame(root)
        self.entries_frame.pack(pady=5, padx=10)
        
        # Add initial website entry
        self.add_website_entry()
        
        # Buttons
        tk.Button(root, text="Add Website", command=self.add_website_entry).pack(pady=5)
        tk.Button(root, text="Launch Websites", command=self.launch_websites).pack(pady=5)
        tk.Button(root, text="Save URLs", command=self.save_urls).pack(pady=5)
        tk.Button(root, text="Load URLs", command=self.load_urls).pack(pady=5)
        
        # Status label
        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack(pady=5)
        
    def add_website_entry(self):
        """Add a new website entry field with a remove button"""
        frame = tk.Frame(self.entries_frame)
        frame.pack(fill='x', pady=2)
        
        entry = tk.Entry(frame, width=40)
        entry.pack(side='left', padx=5)
        
        remove_btn = tk.Button(frame, text="X", command=lambda f=frame, e=entry: self.remove_entry(f, e))
        remove_btn.pack(side='left')
        
        self.website_entries.append(entry)
        
    def remove_entry(self, frame, entry):
        """Remove a website entry field"""
        if len(self.website_entries) > 1:
            self.website_entries.remove(entry)
            frame.destroy()
        else:
            messagebox.showwarning("Warning", "You must keep at least one website entry!")
            
    def launch_websites(self):
        """Launch the websites in Chrome"""
        websites = [entry.get().strip() for entry in self.website_entries if entry.get().strip()]
        
        if not websites:
            messagebox.showwarning("Warning", "Please enter at least one website!")
            return
            
        # Add https:// if not present
        websites = ['https://' + site if not site.startswith(('http://', 'https://')) else site 
                   for site in websites]
        
        try:
            # Use default browser instead of forcing Chrome
            # Open first website in new window
            webbrowser.open_new(websites[0])
            time.sleep(1)
            
            # Open remaining websites in new tabs
            for site in websites[1:]:
                webbrowser.open_new_tab(site)
                time.sleep(0.5)
                
            self.status_label.config(text="Websites launched successfully!", fg="green")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def save_urls(self):
        """Save URLs to a JSON file"""
        urls = [entry.get().strip() for entry in self.website_entries if entry.get().strip()]
        if urls:
            try:
                with open('saved_urls.json', 'w') as f:
                    json.dump(urls, f)
                self.status_label.config(text="URLs saved successfully!", fg="green")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save URLs: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No URLs to save!")
            
    def load_urls(self):
        """Load URLs from JSON file"""
        try:
            if os.path.exists('saved_urls.json'):
                with open('saved_urls.json', 'r') as f:
                    urls = json.load(f)
                
                # Clear existing entries
                for entry in self.website_entries:
                    entry.master.destroy()
                self.website_entries.clear()
                
                # Add loaded URLs
                for url in urls:
                    self.add_website_entry()
                    self.website_entries[-1].insert(0, url)
                    
                self.status_label.config(text="URLs loaded successfully!", fg="green")
            else:
                messagebox.showinfo("Info", "No saved URLs found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load URLs: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteLauncher(root)
    root.mainloop()