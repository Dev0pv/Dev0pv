import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

class ImageRenamerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("DesiNite")
        self.master.set_theme('arc')

        self.tabs = ttk.Notebook(master)
        self.load_image_tab = ttk.Frame(self.tabs)
        self.wallpaper_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.load_image_tab, text="Load Image")
        self.tabs.add(self.wallpaper_tab, text="Wallpaper")

        self.tabs.pack(fill=tk.BOTH, expand=True)

        self.load_image_label = tk.Label(self.load_image_tab, text="Browse and Rename Image:")
        self.load_image_label.pack(pady=10)

        self.browse_button = ttk.Button(self.load_image_tab, text="Browse BMP", command=self.browse_image)
        self.browse_button.pack(pady=10)

        self.rename_button = ttk.Button(self.load_image_tab, text="Rename Image", command=self.rename_image)
        self.rename_button.pack(pady=10)

        self.change_load_screen_button = ttk.Button(self.load_image_tab, text="Change Load Screen", command=self.change_load_screen)
        self.change_load_screen_button.pack(pady=10)

        self.reset_load_image_button = ttk.Button(self.load_image_tab, text="Reset", command=self.reset_load_image)
        self.reset_load_image_button.pack(pady=10)

        self.wallpaper_label = tk.Label(self.wallpaper_tab, text="Browse and Rename Wallpaper:")
        self.wallpaper_label.pack(pady=10)

        self.browse_wallpaper_button = ttk.Button(self.wallpaper_tab, text="Browse JPG", command=self.browse_wallpaper)
        self.browse_wallpaper_button.pack(pady=10)

        self.rename_wallpaper_button = ttk.Button(self.wallpaper_tab, text="Rename Wallpaper", command=self.rename_wallpaper)
        self.rename_wallpaper_button.pack(pady=10)

        self.apply_wallpaper_button = ttk.Button(self.wallpaper_tab, text="Apply Wallpaper", command=self.apply_wallpaper)
        self.apply_wallpaper_button.pack(pady=10)

        self.reset_wallpaper_button = ttk.Button(self.wallpaper_tab, text="Reset", command=self.reset_wallpaper)
        self.reset_wallpaper_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", fg="green", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.bmp")])
        if file_path:
            self.selected_image = file_path
            print(f"Selected Image: {self.selected_image}")

    def rename_image(self):
        if hasattr(self, 'selected_image'):
            new_name = os.path.join(os.path.dirname(self.selected_image), "Splash.bmp")
            try:
                if os.path.exists(new_name):
                    raise FileExistsError(f"Target file {new_name} already exists.")

                os.rename(self.selected_image, new_name)
                self.selected_image = new_name
                print(f"Image renamed to {new_name}")
                self.set_result_message("Image renamed successfully", "green")
            except FileExistsError as e:
                print(f"Error renaming image: {e}")
                self.set_result_message("Error renaming image: File already exists", "red")
            except Exception as e:
                print(f"Error renaming image: {e}")
                self.set_result_message("Error renaming image", "red")
        else:
            print("Please browse an image first.")
            self.set_result_message("Please browse an image first.", "red")

    def change_load_screen(self):
        if hasattr(self, 'selected_image'):
            splash_folder_path = "C:/Program Files/Epic Games/Fortnite/FortniteGame/Content/Splash"
            try:
                for file_name in os.listdir(splash_folder_path):
                    file_path = os.path.join(splash_folder_path, file_name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)

                shutil.copy(self.selected_image, splash_folder_path)
                print(f"Load screen changed successfully.")
                self.set_result_message("Load screen changed successfully", "green")
            except FileExistsError as e:
                print(f"Error changing load screen: {e}")
                self.set_result_message("Error changing load screen: File already exists", "red")
            except Exception as e:
                print(f"Error changing load screen: {e}")
                self.set_result_message("Error changing load screen", "red")
        else:
            print("Please browse an image first.")
            self.set_result_message("Please browse an image first.", "red")

    def reset_load_image(self):
        if hasattr(self, 'selected_image'):
            original_name = os.path.join(os.path.dirname(self.selected_image), "Splash_original.bmp")
            try:
                if os.path.exists(original_name):
                    raise FileExistsError(f"Target file {original_name} already exists.")

                os.rename(self.selected_image, original_name)
                self.selected_image = original_name
                print(f"Image reset to {original_name}")
                self.set_result_message("Image reset successfully", "green")
            except FileExistsError as e:
                print(f"Error resetting image: {e}")
                self.set_result_message("Error resetting image: File already exists", "red")
            except Exception as e:
                print(f"Error resetting image: {e}")
                self.set_result_message("Error resetting image", "red")
        else:
            print("No image to reset.")
            self.set_result_message("No image to reset.", "red")

    def browse_wallpaper(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])
        if file_path:
            self.selected_wallpaper = file_path
            print(f"Selected Wallpaper: {self.selected_wallpaper}")

    def rename_wallpaper(self):
        if hasattr(self, 'selected_wallpaper'):
            new_name = os.path.join(os.path.dirname(self.selected_wallpaper), "94B6B9B00327C76C152A04591443D1E70429F4B0.jpg")
            try:
                if os.path.exists(new_name):
                    raise FileExistsError(f"Target file {new_name} already exists.")

                os.rename(self.selected_wallpaper, new_name)
                self.selected_wallpaper = new_name
                print(f"Wallpaper renamed to {new_name}")
                self.set_result_message("Wallpaper renamed successfully", "green")
            except FileExistsError as e:
                print(f"Error renaming wallpaper: {e}")
                self.set_result_message("Error renaming wallpaper: File already exists", "red")
            except Exception as e:
                print(f"Error renaming wallpaper: {e}")
                self.set_result_message("Error renaming wallpaper", "red")
        else:
            print("Please browse a wallpaper first.")
            self.set_result_message("Please browse a wallpaper first.", "red")

    def apply_wallpaper(self):
        if hasattr(self, 'selected_wallpaper'):
            wallpaper_folder_path = "C:/Users/micha/AppData/Local/FortniteGame/Saved/PersistentDownloadDir/CMS/Files/6351768D512008CF544EF39C31E1C66EF0565806"
            try:
                existing_path = os.path.join(wallpaper_folder_path, "94B6B9B00327C76C152A04591443D1E70429F4B0.jpg")
                if os.path.exists(existing_path):
                    os.remove(existing_path)

                shutil.copy(self.selected_wallpaper, wallpaper_folder_path)
                print(f"Wallpaper changed successfully.")
                self.set_result_message("Wallpaper changed successfully", "green")
            except FileExistsError as e:
                print(f"Error changing wallpaper: {e}")
                self.set_result_message("Error changing wallpaper: File already exists", "red")
            except Exception as e:
                print(f"Error changing wallpaper: {e}")
                self.set_result_message("Error changing wallpaper", "red")
        else:
            print("Please browse a wallpaper first.")
            self.set_result_message("Please browse a wallpaper first.", "red")

    def reset_wallpaper(self):
        if hasattr(self, 'selected_wallpaper'):
            original_name = os.path.join(os.path.dirname(self.selected_wallpaper), "94B6B9B00327C76C152A04591443D1E70429F4B0_original.jpg")
            try:
                if os.path.exists(original_name):
                    raise FileExistsError(f"Target file {original_name} already exists.")

                os.rename(self.selected_wallpaper, original_name)
                self.selected_wallpaper = original_name
                print(f"Wallpaper reset to {original_name}")
                self.set_result_message("Wallpaper reset successfully", "green")
            except FileExistsError as e:
                print(f"Error resetting wallpaper: {e}")
                self.set_result_message("Error resetting wallpaper: File already exists", "red")
            except Exception as e:
                print(f"Error resetting wallpaper: {e}")
                self.set_result_message("Error resetting wallpaper", "red")
        else:
            print("No wallpaper to reset.")
            self.set_result_message("No wallpaper to reset.", "red")

    def set_result_message(self, message, color):
        self.result_label.config(text=message, fg=color)

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = ImageRenamerApp(root)
    root.mainloop()
