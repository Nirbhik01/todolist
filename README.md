
# 📝 Django To-Do List Web App

## 📌 Introduction

This is a simple To-Do List web application built using **Django** (Python web framework) for the backend and **HTML, CSS, and JavaScript** for the frontend. The app allows users to:

- Add tasks with labels, status, and due dates
- View all tasks
- Filter tasks by label, status, or due date
- Delete tasks

### 🔧 Technologies and Tools Used:

- **Python 3**
- **Django**
- **HTML5, CSS3, JavaScript (Vanilla)**
- **JSON (for data exchange)**
- **SQLite** (default Django database)

---

## ⚠️ Challenges Faced

While developing the app, I encountered a few interesting challenges:

- **Invoking Django Views from JavaScript**: To add, delete, or fetch tasks, I had to call Django view functions through `fetch()` API calls from the frontend. These needed to send and receive data in **JSON** format, so understanding how to parse JSON on both ends was crucial.
  
- **Handling Asynchronous Data**: The app uses the `fetch()` function to make asynchronous requests. It was tricky to make sure data was fetched and handled properly — especially after performing actions like adding or deleting tasks, where the page shouldn’t reload.

- **Creating DOM Elements Dynamically**: After a user adds a task, the task appears immediately in the list. I learned how to **create and insert elements using JavaScript** to reflect changes without a page reload.

---

## ✅ Conclusion

Through this project, I learned how to:

- Use **Django models and views** to manage data
- Connect Django backend with frontend using **AJAX-like `fetch()` calls**
- Work with **JSON** data to send and receive information between client and server
- Dynamically render and update content on the page using **DOM manipulation**
- Implement **filtering and task management logic**

It was a great experience to build a full-stack mini project and see how everything — from forms to filtering and deleting — comes together in a real-world web app!

---

