# Background for input pages, mute button, home page
# With zoomed image
# With scrollbar
# Two invigilators
#timer
import tkinter as tk
import pygame
from PIL import Image, ImageTk
import cv2
import threading
import time
from playsound import playsound
from tkinter import Label, Tk

# Initialize the main Tkinter window
root = tk.Tk()
root.configure(bg='#E9D2B7')
root.attributes('-fullscreen', True)


def video():

    # Create a Canvas to hold the video frame and the button
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Initialize video capture
    cap = cv2.VideoCapture(r"C:\Users\Siddi.Harshini\OneDrive\文档\clg video.mp4")

    # Create a label to hold the video frame
    lbl = tk.Label(canvas)
    lbl.pack()

    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (1450, 920))
            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to ImageTk format
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            # Update the label with the new image
            lbl.imgtk = imgtk
            lbl.config(image=imgtk)
            # Call this function again after a delay
            lbl.after(1, update_frame)
        else:
            cap.release()
            create_num_branches_page()

    def play_audio():
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load background music
        pygame.mixer.music.load(r"C:\Users\Siddi.Harshini\Downloads\background-inspiring-207551.mp3")

        # Set the volume for background music (0.0 to 1.0)
        pygame.mixer.music.set_volume(1.0)

        # Start playing background music
        pygame.mixer.music.play(-1)  # -1 loops the music indefinitely

    # Start updating the frame
    update_frame()

    # Start audio playback in a separate thread
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.daemon = True  # Ensure the thread exits when the main program does
    audio_thread.start()

    button_start = tk.Button(canvas, text='Start', command=home_page, font=('Arial', 20))
    canvas.create_window(600, 600, window=button_start, anchor='nw')

# Variables and configuration
rows, cols = 5, 9
cell_width, cell_height = 60, 60
padding = 40
steps, delay = 20, 100  # animation steps and delay in milliseconds
background_color = '#E9D2B7'

# Center position calculation
center_row, center_col = rows // 2, cols // 2
center_x = center_col * (cell_width + padding) + cell_width // 2
center_y = center_row * (cell_height + padding) + cell_height // 2

images = {}


# Load images
def load_image(path, width=None, height=None):
    image = Image.open(path)
    if width and height:
        image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)


# Load specific images
invisilator_photo = load_image(r"C:\Users\Siddi.Harshini\Downloads\Screenshot__54_-removebg-preview.png", cell_width + 20, cell_height + 20)
invisilator_photo1 = load_image(r"C:\Users\Siddi.Harshini\Downloads\Screenshot__54_-removebg-preview.png", cell_width + 20, cell_height + 20)
paper_photo = load_image(r"C:\Users\Siddi.Harshini\Downloads\book_new-removebg-preview (1).png", cell_width, cell_height)
bench_photo = load_image(r"C:\Users\Siddi.Harshini\Downloads\table_new-removebg-preview.png", cell_width, cell_height)
pen_image = load_image(r"C:\Users\Siddi.Harshini\Downloads\pen_image-removebg-preview (1).png", cell_width, cell_height)

options = [
    r"C:\Users\Siddi.Harshini\Downloads\cse_student_with_pen-removebg-preview.png",
    r"C:\Users\Siddi.Harshini\Downloads\it_pen-removebg-preview.png",
    r"C:\Users\Siddi.Harshini\Downloads\ece_stupen-removebg-preview.png",
    r"C:\Users\Siddi.Harshini\Downloads\eee_student_with_pen-removebg-preview (1).png",
    r"C:\Users\Siddi.Harshini\Downloads\aiml_pen-removebg-preview.png",
    r"C:\Users\Siddi.Harshini\Downloads\extra_student1-removebg-preview (1).png",
    r"C:\Users\Siddi.Harshini\Downloads\extra_student2-removebg-preview.png",
    r"C:\Users\Siddi.Harshini\Downloads\extra_student3-removebg-preview.png",
    r"C:\Users\Siddi.Harshini\Downloads\extra_student4-removebg-preview.png",
    r"C:\Users\Siddi.Harshini\Downloads\extra_student5-removebg-preview.png",
]

# Load background image
background_image_path = r"C:\Users\Siddi.Harshini\OneDrive\文档\class room background.jpg"
background_image = load_image(background_image_path, root.winfo_screenwidth(), root.winfo_screenheight())

# Load background image
background_image1_path = r"C:\Users\Siddi.Harshini\Downloads\branch names background.jpg"
background_image1 = load_image(background_image1_path, root.winfo_screenwidth(), root.winfo_screenheight())

# Load background image
background_image3_path = r"C:\Users\Siddi.Harshini\OneDrive\Pictures\Screenshots\Screenshot (55).png"
background_image3 = load_image(background_image3_path, root.winfo_screenwidth(), root.winfo_screenheight())


def mute():
    def toggle_audio():
        if pygame.mixer.music.get_volume() > 0:
            pygame.mixer.music.set_volume(0)
            mute.config(text="Unmute")
        else:
            pygame.mixer.music.set_volume(0.1)
            mute.config(text="Mute")

    mute = tk.Button(root, text="Mute", command=toggle_audio, font=("Arial", 20), bg='red', fg='black', padx=10, pady=5)
    mute.pack(pady=5)


# Functions to handle the Tkinter application flow
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


def home_page():
    clear_window()

    # Load background music
    pygame.mixer.music.load(r"C:\Users\Siddi.Harshini\Downloads\background-inspiring-207551.mp3")
    pygame.mixer.music.set_volume(0.1)  # Reduce volume to 10%
    pygame.mixer.music.play(-1)  # -1 loops the music indefinitely

    # Load background image
    background_image2_path = r"C:\Users\Siddi.Harshini\OneDrive\文档\home page.jpg"
    background_image2 = load_image(background_image2_path, root.winfo_screenwidth(), root.winfo_screenheight())

    canvas1 = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas1.pack(fill='both', expand=True)
    canvas1.create_image(0, 0, image=background_image2, anchor='nw')

    # Keep a reference to the image
    root.background_image2 = background_image2

    room_button = tk.Button(root, text="Add Classroom", command=create_num_branches_page, font=("Arial", 20), bg="lightblue",
                            fg="black", padx=10, pady=5)
    canvas1.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 4 + 200, window=room_button)

    Quit_button = tk.Button(root, text="Quit", command=exit, font=("Arial", 20),
                            bg="lightblue",
                            fg="black", padx=10, pady=5)
    canvas1.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 4 + 300, window=Quit_button)


def create_canvas():
    global canvas, canvas_width, canvas_height

    canvas_ = tk.Canvas(root, bg='#E9D2B7', highlightthickness=0, borderwidth=0)
    canvas_.pack(fill=tk.BOTH, expand=True)

    '''canvas_.create_image(0, 0, anchor=tk.NW, image=background_image1)'''

    canvas_width = cols * (cell_width + padding) - padding
    canvas_height = rows * (cell_height + padding) - padding
    canvas = tk.Canvas(canvas_, width=canvas_width, height=canvas_height, bg='#E9D2B7', highlightthickness=0,
                       borderwidth=0)
    canvas.pack()
    draw_grid()


def create_num_branches_page():
    clear_window()

    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill='both', expand=True)
    canvas.create_image(0, 0, image=background_image, anchor='nw')

    label = tk.Label(root, text="Enter number of branches:", font=("Arial", 20), bg="#2F7673", fg='white')
    canvas.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 4, window=label)

    global num_branches_var
    num_branches_var = tk.IntVar(value=1)
    num_branches_spinbox = tk.Spinbox(root, from_=1, to=10, textvariable=num_branches_var, font=("Arial", 20))
    canvas.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 4 + 50,
                         window=num_branches_spinbox)

    next_button = tk.Button(root, text="Next", command=create_branch_name_entries, font=("Arial", 20),
                            fg="black", padx=10, pady=5)
    canvas.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 4 + 100, window=next_button)

    mute()


def create_branch_name_entries():
    clear_window()

    canvas2 = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas2.pack(fill='both', expand=True)
    canvas2.create_image(0, 0, image=background_image3, anchor='nw')

    global num_branches, branch_names, entries
    num_branches = num_branches_var.get()
    branch_names = [tk.StringVar() for _ in range(num_branches)]
    entries = []

    label = tk.Label(root, text="Enter branch names:", font=("Arial", 20), bg="#2F7673", fg='white')
    canvas2.create_window(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 4 - 75, window=label)

    y_offset = root.winfo_screenheight() // 4 - 25
    for i in range(num_branches):
        entry_label = tk.Label(root, text=f"Branch {i + 1} : ", font=("Arial", 20), bg="#2F7673", fg='white')
        canvas2.create_window(root.winfo_screenwidth() // 2 - 100, y_offset, window=entry_label)

        entry = tk.Entry(root, textvariable=branch_names[i], font=("Arial", 20))
        canvas2.create_window(root.winfo_screenwidth() // 2 + 150, y_offset, window=entry)

        entries.append(entry)

        y_offset += 50

    submit_button = tk.Button(root, text="Submit", command=show_summary, font=("Arial", 20), bg="#2F7673", fg='black',
                              padx=10, pady=5)
    canvas2.create_window(root.winfo_screenwidth() // 2, y_offset + 20, window=submit_button)

    for entry in entries:
        entry.bind("<Return>", focus_next_widget)

    if entries:
        entries[0].focus_set()

    mute()


def focus_next_widget(event):
    widget = event.widget
    idx = entries.index(widget)
    if idx < len(entries) - 1:
        entries[idx + 1].focus()
    else:
        show_summary()
    return "break"


def show_summary():
    clear_window()
    if num_branches < 5:
        frames1()
    else:
        frames2()
    create_canvas()


def animate_move(image_id, start_pos, end_pos, step=0):
    if step <= steps:
        x = start_pos[0] + (end_pos[0] - start_pos[0]) * step / steps
        y = start_pos[1] + (end_pos[1] - start_pos[1]) * step / steps
        canvas.coords(image_id, x, y)
        root.after(delay, animate_move, image_id, start_pos, end_pos, step + 1)


def exit_app():
    root.destroy()


def draw_grid():
    for row in range(rows):
        for col in range(cols):
            x0 = col * (cell_width + padding)
            y0 = row * (cell_height + padding)
            x1 = x0 + cell_width
            y1 = y0 + cell_height
            canvas.create_rectangle(x0, y0, x1, y1, fill='white', outline='')
            canvas.create_image(x0, y0, anchor='nw', image=bench_photo)


def place_images(branch_index):
    branch_name = branch_names[branch_index].get()
    photo = load_image(options[branch_index % len(options)], cell_width, cell_height)
    images[branch_name] = photo

    roll_prefix = chr(97 + branch_index)  # 'a' for branch 0, 'b' for branch 1, etc.
    roll_number = 1  # Initialize the roll number

    if num_branches == 1:
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    target_x = col * (cell_width + padding) + cell_width // 2
                    target_y = row * (cell_height + padding) + cell_height // 2
                    image_id = canvas.create_image(
                        center_col * (cell_width + padding) + cell_width // 2,
                        center_row * (cell_height + padding) + cell_height // 2,
                        image=photo)
                    images[(row, col)] = image_id
                    animate_move(image_id,
                                 (center_col * (cell_width + padding) + cell_width // 2,
                                  center_row * (cell_height + padding) + cell_height // 2),
                                 (target_x, target_y))
                    image_id_pen = canvas.create_image(center_col * (cell_width + padding) + cell_width // 2,
                                                       center_row * (cell_height + padding) + cell_height // 2,
                                                       image=pen_image)
                    animate_move(image_id_pen, (center_col * (cell_width + padding) + cell_width // 2,
                                                center_row * (cell_height + padding) + cell_height // 2),
                                 (target_x, target_y))
                    # Add roll number in the upper-right corner at the edge
                    roll_id = canvas.create_text(target_x + cell_width // 2, target_y - cell_height // 2, text=f"{roll_prefix}{roll_number}", font=("Arial", 12), fill="black", anchor='ne')
                    roll_number += 1
    else:
        if cols % num_branches == 0:
            branch_count = 0
            for row in range(rows):
                if row % 2 == 0:
                    for col in range(cols):
                        if branch_count % len(branch_names) == branch_index:
                            target_x = col * (cell_width + padding) + cell_width // 2
                            target_y = row * (cell_height + padding) + cell_height // 2
                            image_id = canvas.create_image(
                                center_col * (cell_width + padding) + cell_width // 2,
                                center_row * (cell_height + padding) + cell_height // 2,
                                image=photo)
                            animate_move(image_id,
                                         (center_col * (cell_width + padding) + cell_width // 2,
                                          center_row * (cell_height + padding) + cell_height // 2),
                                         (target_x, target_y))
                            image_id_pen = canvas.create_image(center_col * (cell_width + padding) + cell_width // 2,
                                                               center_row * (cell_height + padding) + cell_height // 2,
                                                               image=pen_image)
                            animate_move(image_id_pen, (center_col * (cell_width + padding) + cell_width // 2,
                                                        center_row * (cell_height + padding) + cell_height // 2),
                                         (target_x, target_y))
                            # Add roll number in the upper-right corner at the edge
                            roll_id = canvas.create_text(target_x + cell_width // 2, target_y - cell_height // 2, text=f"{roll_prefix}{roll_number}", font=("Arial", 12), fill="black", anchor='ne')
                            roll_number += 1
                        branch_count += 1
        else:
            for row in range(rows):
                for col in range(cols):
                    if (row * cols + col) % len(branch_names) == branch_index:
                        target_x = col * (cell_width + padding) + cell_width // 2
                        target_y = row * (cell_height + padding) + cell_height // 2
                        image_id = canvas.create_image(
                            center_col * (cell_width + padding) + cell_width // 2,
                            center_row * (cell_height + padding) + cell_height // 2,
                            image=photo)
                        animate_move(image_id,
                                     (center_col * (cell_width + padding) + cell_width // 2,
                                      center_row * (cell_height + padding) + cell_height // 2),
                                     (target_x, target_y))
                        image_id_pen = canvas.create_image(center_col * (cell_width + padding) + cell_width // 2,
                                                           center_row * (cell_height + padding) + cell_height // 2,
                                                           image=pen_image)
                        animate_move(image_id_pen, (center_col * (cell_width + padding) + cell_width // 2,
                                                    center_row * (cell_height + padding) + cell_height // 2),
                                     (target_x, target_y))
                        # Add roll number in the upper-right corner at the edge
                        roll_id = canvas.create_text(target_x + cell_width // 2, target_y - cell_height // 2, text=f"{roll_prefix}{roll_number}", font=("Arial", 12), fill="black", anchor='ne')
                        roll_number += 1


def papers():
    for branch_index in range(num_branches):
        if num_branches == 1:
            for row in range(rows):
                for col in range(cols):
                    if (row + col) % 2 == 0:
                        target_a = col * (cell_width + padding) + cell_width // 2
                        target_b = row * (cell_height + padding) + cell_height // 2
                        image_id_p = canvas.create_image(center_col * (cell_width + padding) + cell_width // 2,
                                                         center_row * (cell_height + padding) + cell_height // 2,
                                                         image=paper_photo)
                        animate_move(image_id_p, (center_col * (cell_width + padding) + cell_width // 2,
                                                  center_row * (cell_height + padding) + cell_height // 2),
                                     (target_a, target_b))
        else:
            if cols % num_branches == 0:
                branch_count_p = 0
                for row in range(rows):
                    if row % 2 == 0:
                        for col in range(cols):
                            if branch_count_p % len(branch_names) == branch_index:
                                target_a = col * (cell_width + padding) + cell_width // 2
                                target_b = row * (cell_height + padding) + cell_height // 2
                                image_id_p = canvas.create_image(center_col * (cell_width + padding) + cell_width // 2,
                                                                 center_row * (
                                                                             cell_height + padding) + cell_height // 2,
                                                                 image=paper_photo)
                                animate_move(image_id_p, (center_col * (cell_width + padding) + cell_width // 2,
                                                          center_row * (cell_height + padding) + cell_height // 2),
                                             (target_a, target_b))
                            branch_count_p += 1
            else:
                for row in range(rows):
                    for col in range(cols):
                        if (row * cols + col) % len(branch_names) == branch_index:
                            target_a = col * (cell_width + padding) + cell_width // 2
                            target_b = row * (cell_height + padding) + cell_height // 2
                            image_id_p = canvas.create_image(center_col * (cell_width + padding) + cell_width // 2,
                                                             center_row * (cell_height + padding) + cell_height // 2,
                                                             image=paper_photo)
                            animate_move(image_id_p, (center_col * (cell_width + padding) + cell_width // 2,
                                                      center_row * (cell_height + padding) + cell_height // 2),
                                         (target_a, target_b))


def animate_invigilator():

    path1 = []
    path2 = []

    for row in range(rows-1):
        if row % 2 == 0:
            # Even row: left to right
            for col in range(cols):
                path1.append((col * (cell_width + padding) + cell_width // 2,
                             row * (cell_height + padding) + cell_height // 2))
        else:
            # Odd row: right to left
            for col in range(cols - 1, -1, -1):
                path1.append((col * (cell_width + padding) + cell_width // 2,
                             row * (cell_height + padding) + cell_height // 2))

    for row in reversed(range(rows-1)):
        if row % 2 == 0:
            # Even row: left to right
            for col in range(cols):
                path2.append((col * (cell_width + padding) + cell_width // 2,
                             row * (cell_height + padding) + cell_height // 2))
        else:
            # Odd row: right to left
            for col in range(cols - 1, -1, -1):
                path2.append((col * (cell_width + padding) + cell_width // 2,
                             row * (cell_height + padding) + cell_height // 2))

    def move_invigilator1(index=0):
        if index < len(path1):
            next_index = (index + 1) % len(path1)
            start_pos = path1[index]
            end_pos = path1[next_index]
            animate_move(invigilator_id1, start_pos, end_pos)
            # Schedule the next move if not at the last cell
            root.after(steps * delay + 1000, move_invigilator1, next_index)

    def move_invigilator2(index=0):
        if index < len(path2):
            next_index = (index + 1) % len(path2)
            start_pos = path2[index]
            end_pos = path2[next_index]
            animate_move(invigilator_id2, start_pos, end_pos)
            # Schedule the next move if not at the last cell
            root.after(steps * delay + 1000, move_invigilator2, next_index)

    invigilator_id1 = canvas.create_image(center_x, center_y, image=invisilator_photo1, anchor='nw')
    move_invigilator1()

    invigilator_id2 = canvas.create_image(center_x, center_y, image=invisilator_photo, anchor='nw')
    move_invigilator2()

def start_timer(timer_label):
    playsound(r"C:\Users\Siddi.Harshini\Downloads\school-bell-199584.mp3")
    def update_timer():
        remaining_time = 20 # 20 seconds
        while remaining_time >= 0:
            mins, secs = divmod(remaining_time, 60)
            hours, mins = divmod(mins, 60)
            timer_label.config(text="{:02d}:{:02d}:{:02d}".format(hours, mins, secs))
            timer_label.update()
            time.sleep(1)
            remaining_time -= 1

        timer_label.config(text="Time's up!")
        playsound(r"C:\Users\Siddi.Harshini\Downloads\school-bell-199584.mp3")  # Adjust the path to your sound file

    timer_thread = threading.Thread(target=update_timer)
    timer_thread.start()

def start_timer1(timer_label):
    playsound(r"C:\Users\Siddi.Harshini\Downloads\school-bell-199584.mp3")
    def update_timer():
        remaining_time = 20 # 20 i8n seconds
        while remaining_time >= 0:
            mins, secs = divmod(remaining_time, 60)
            hours, mins = divmod(mins, 60)
            timer_label.config(text="{:02d}:{:02d}:{:02d}".format(hours, mins, secs))
            timer_label.update()
            time.sleep(1)
            remaining_time -= 1

        timer_label.config(text="Time's up!")
        playsound(r"C:\Users\Siddi.Harshini\Downloads\school-bell-199584.mp3")  # Adjust the path to your sound file

    timer_thread = threading.Thread(target=update_timer)
    timer_thread.start()
def frames1():
    def papers_timer():
        papers()
        start_timer(timer_label)
    def toggle_audio():
        if pygame.mixer.music.get_volume() > 0:
            pygame.mixer.music.set_volume(0)
            mute_button.config(text="Unmute")
        else:
            pygame.mixer.music.set_volume(0.1)
            mute_button.config(text="Mute")

    top_frame = tk.Frame(root, bg='#E9D2B7')
    top_frame.pack(side=tk.TOP, padx=10, pady=10)

    bottom_frame = tk.Frame(root, bg='#E9D2B7')
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    left_frame = tk.Frame(root, bg='#E9D2B7')
    left_frame.pack(side=tk.LEFT, padx=10)

    right_frame = tk.Frame(root, bg='#E9D2B7')
    right_frame.pack(side=tk.RIGHT, padx=10)


    for index, branch_name_var in enumerate(branch_names):
        branch_name = branch_name_var.get()
        button = tk.Button(top_frame, text=branch_name.upper(), command=lambda i=index: place_images(i),
                           font=("Arial", 20), bg="blue", fg="black", padx=10, pady=5)
        button.pack(side='left', padx=5, pady=5)

    paper_button = tk.Button(top_frame, text="Paper", command=papers_timer, font=("Arial", 20), bg='red', fg='black',
                             padx=10, pady=5)
    paper_button.pack(side='left', padx=5, pady=20)

    invigilator_button = tk.Button(top_frame, text="Invigilator", command=animate_invigilator, font=("Arial", 20),
                                   bg='yellow', fg='black', padx=10, pady=5)
    invigilator_button.pack(pady=20)

    timer_label = tk.Label(left_frame, text="", font=("Arial", 20), fg="black", bg="#E9D2B7")
    timer_label.pack()

    '''timer_button = tk.Button(left_frame, text="Timer", command=lambda: start_timer(timer_label), font=("Arial", 20),
                             bg='skyblue', fg='black', padx=10, pady=5)
    timer_button.pack(pady=5)'''

    mute_button = tk.Button(left_frame, text="Mute", command=toggle_audio, font=("Arial", 20), bg='red', fg='black',
                            padx=10, pady=5)
    mute_button.pack(pady=5)

    home = tk.Button(left_frame, text="Home", command=home_page, font=("Arial", 20),bg="blue", fg="black", padx=10, pady=5)
    home.pack(pady=5)


    for index, branch_name_var in enumerate(branch_names):
        branch_name = branch_name_var.get()
        image_path = options[index % len(options)]
        photo = load_image(image_path, cell_width, cell_height)

        label = tk.Label(right_frame, text=f"{branch_name.upper()} Students", bg=background_color, font=("Arial", 20))
        label.pack(side='top', pady=10)

        image_label = tk.Label(right_frame, image=photo, bg='#E9D2B7')
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack(side='top')

    exit_button = tk.Button(bottom_frame, text="Exit", command=exit_app, font=("Arial", 20), bg='#F04444', fg='black', padx=10, pady=5)
    exit_button.pack(pady=20)


def frames2():
    def papers_timer():
        papers()
        start_timer1(timer_label)
    def toggle_audio():
        if pygame.mixer.music.get_volume() > 0:
            pygame.mixer.music.set_volume(0)
            mute_button.config(text="Unmute")
        else:
            pygame.mixer.music.set_volume(0.1)
            mute_button.config(text="Mute")

    top_frame = tk.Frame(root, bg='#E9D2B7')
    top_frame.pack(side=tk.TOP, padx=10, pady=10)

    bottom_frame = tk.Frame(root, bg='#E9D2B7')
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    left_frame = tk.Frame(root, bg='#E9D2B7')
    left_frame.pack(side=tk.LEFT, padx=10)

    right_frame = tk.Frame(root, bg='#E9D2B7')
    right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

    # Create a canvas inside the right frame
    right_canvas = tk.Canvas(right_frame, bg=background_color, width=120, highlightthickness=0)
    right_canvas.pack(side=tk.LEFT, fill=tk.Y)

    # Create a scrollbar for the canvas
    scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=right_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to work with the scrollbar
    right_canvas.configure(yscrollcommand=scrollbar.set)
    right_canvas.bind('<Configure>', lambda e: right_canvas.configure(scrollregion=right_canvas.bbox('all')))

    # Create a frame inside the canvas to hold the content
    right_content = tk.Frame(right_canvas, bg=background_color)
    right_canvas.create_window((180, 0), window=right_content, anchor='nw')

    for index, branch_name_var in enumerate(branch_names):
        branch_name = branch_name_var.get()
        button = tk.Button(top_frame, text=branch_name.upper(), command=lambda i=index: place_images(i),
                           font=("Arial", 20), bg="blue", fg="black", padx=10, pady=5)
        button.pack(side='left', padx=5, pady=5)

    paper_button = tk.Button(top_frame, text="Paper", command=papers_timer, font=("Arial", 20), bg='red', fg='black',
                             padx=10, pady=5)
    paper_button.pack(side='left', padx=5, pady=20)

    invigilator_button = tk.Button(top_frame, text="Invigilator", command=animate_invigilator, font=("Arial", 20),
                                   bg='yellow', fg='black', padx=10, pady=5)
    invigilator_button.pack(pady=20)

    timer_label = tk.Label(left_frame, text="", font=("Arial", 20), fg="black", bg="#E9D2B7")
    timer_label.pack()

    mute_button = tk.Button(left_frame, text="Mute", command=toggle_audio, font=("Arial", 20), bg='red', fg='black',
                            padx=10, pady=5)
    mute_button.pack(pady=5)

    home = tk.Button(left_frame, text="Home", command=home_page, font=("Arial", 20),
                     bg="blue", fg="black", padx=10, pady=5)
    home.pack(pady=5)

    for index, branch_name_var in enumerate(branch_names):
        branch_name = branch_name_var.get()
        image_path = options[index % len(options)]
        photo = load_image(image_path, cell_width, cell_height)

        label = tk.Label(right_content, text=f"{branch_name.upper()} Students", bg=background_color, font=("Arial", 20))
        label.pack(side='top', pady=10)

        image_label = tk.Label(right_content, image=photo, bg='#E9D2B7')
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack(side='top')

    exit_button = tk.Button(bottom_frame, text="Exit", command=exit_app, font=("Arial", 20), bg='#F04444', fg='black',
                            padx=10, pady=5)
    exit_button.pack(pady=20)

    right_canvas.update_idletasks()
    right_canvas.config(scrollregion=right_canvas.bbox('all'))


# Start the application
video()
root.mainloop()



