# Automated Seating Arrangement and Monitoring System for Examination Halls

## 📽️ Project Demo  
🔗 [Watch the Demo](https://youtu.be/Y75aUXawpTM)  

## Overview  
This **Python-based project** automates the process of:  
- ✅ **Seating arrangement**  
- ✅ **Paper distribution**  
- ✅ **Invigilator movement**  

The system is built using **Tkinter** for GUI visualization and **multithreading** for timed operations.  
It features an interactive interface that dynamically places students, distributes papers, and simulates invigilator patrolling.  

---

## Features  
- **Automated Student Seating**: Arranges students in a **grid format**, ensuring fair placement based on branch-wise distribution.  
- **Paper Distribution Animation**: Simulates animated paper movement to each student's seat.  
- **Invigilator Movement Simulation**: Two invigilators follow predefined paths to patrol the examination hall.  
- **Countdown Timer**: A **20-second timer** with an **audio alert** for start and end times.  
- **User Interface Controls**:  
  - 🎯 **Seat allocation**  
  - 📜 **Paper distribution**  
  - 👮 **Invigilator movement**  
  - 🔊 **Mute/unmute button** for background sounds  
  - ❌ **Exit button** to close the application  
- **Graphical Enhancements**: Uses images for students, invigilators, and papers for a **visually appealing interface**.  

---

## Implementation Details  

### 1️⃣ Student Seating Arrangement  
- Uses a **grid-based layout** to ensure proper student spacing.  
- If the number of columns is divisible by the number of branches, students are arranged **systematically**; otherwise, a **round-robin approach** is used.  

### 2️⃣ Paper Distribution  
- After seating is arranged, papers are **animated** to move from a central position to each student's desk.  

### 3️⃣ Invigilator Movement  
- Two invigilators **patrol in a zigzag path**:  
  - Moves **left to right** in even rows  
  - Moves **right to left** in odd rows  
- The movement is **animated smoothly**.  

### 4️⃣ Countdown Timer with Sound Alerts  
- **20-second timer** displayed using Tkinter labels.  
- Runs in a **separate thread** to prevent UI freezing.  
- 🎵 **School bell sound** plays at the **start and end** of the timer.  

### 5️⃣ GUI Design  
- **Top Frame**: Buttons for **seating, paper distribution, invigilator movement**.  
- **Bottom Frame**: ❌ **Exit button**.  
- **Left Frame**: ⏳ **Countdown timer & audio toggle**.  
- **Right Frame**: 📸 **Student details & images**.  
- Uses **Tkinter buttons, labels, and images** for an **interactive experience**.  

---

## Technologies Used  
- **Python** 🐍  
- **Tkinter** (for GUI) 🎨  
- **Pygame** (for audio management) 🔊  
- **Threading** (to handle countdown timers) ⏳  
- **OpenCV** (optional, for image processing) 📷  



