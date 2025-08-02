**TO DO LIST**

The project is a **To-Do List Reminder application** developed using **Python**. It provides a simple and user-friendly interface that allows users to manage their daily tasks with time-based reminders. The graphical interface is built using the **Tkinter** library, while **threading** is used to handle background countdown timers for each task. Users can input a task description along with a time duration in hours. Once submitted, each task is assigned a unique ID and begins counting down in real time. The task list on the interface displays all active tasks along with their remaining time in hours. When the time for a task runs out, the application automatically removes it from the list and displays a pop-up notification using **`tk.messagebox`**, reminding the user that the time for that task is up.

The application supports additional features such as updating and deleting tasks. Users can select an existing task, modify its text or time, and save the changes. The interface includes dedicated input fields for editing and buttons for updating and saving changes. The real-time countdown functionality is handled through **threading.Timer**, which decreases the remaining seconds for each task every second. The task list is refreshed continuously to reflect the updated time or any changes made by the user.

Internally, the application uses a **dictionary** to store tasks with their corresponding details like text and remaining time. It also makes use of **Tkinter variables** such as `StringVar` and `DoubleVar` to manage the state of the input fields. The application demonstrates effective use of **event-driven programming**, **multi-threading**, and **GUI design**. Overall, it serves as a lightweight yet functional desktop tool for personal task management and is a good example of integrating timers and reminders in Python applications.

**TIC TAC TOE**

The project is a **Tic-Tac-Toe game application** built using **Python** and the **Tkinter** library for the graphical user interface. It allows users to play either in **Player vs Player** mode or against a simple **Bot**. The game presents a classic 3x3 grid where players take turns marking cells with "X" or "O". The interface includes buttons for selecting the game mode and displays the current score of both players.

In **Player vs Player** mode, two users take alternate turns. In **Bot mode**, the user plays as "X" and the bot randomly selects an available cell to place "O". The game checks for a win condition after each move by examining rows, columns, and diagonals. If a player wins, a pop-up window appears to announce the winner and asks if the user wants to play again. If all cells are filled without a winner, the game declares a draw and offers the same restart option.

The game uses a **2D list** to store the current state of the board and updates both the backend and frontend (button labels) after every move. The **score** for each player is tracked and displayed in real time. The game flow is handled through event-driven programming with `tk.Button` callbacks for each cell.

This project demonstrates the use of GUI components such as buttons, labels, and message boxes, along with fundamental programming concepts like **game logic**, **event handling**, and **state management**. It provides an engaging and interactive user experience while showcasing the basics of building a desktop game application in Python. The random bot move logic adds a simple form of AI, making it suitable for beginners learning game development and GUI programming.

