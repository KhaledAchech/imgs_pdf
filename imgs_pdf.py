import tkinter as tk
from tkinter import filedialog
from img2pdf import convert

def select_images():
    file_paths = filedialog.askopenfilenames(title="Select Images", 
                filetypes=[("PNG","*.png"),("JPG","*.jpg"),("JPEG","*.jpeg")])
    return list(file_paths)

def main():
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    select_button = tk.Button(frame, text="Select Images", command=lambda: create_pdf(select_images()))
    select_button.pack()
    
    root.mainloop()

def create_pdf(imgs):
    if not imgs:
        print("No images selected.")
        return

    print("Selected Images:")
    for img_path in imgs:
        print(img_path)
        
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not filename:
        print("No file selected.")
        return

    with open(filename, "wb") as file:
        file.write(convert(imgs))

if __name__ == "__main__":
    main()
