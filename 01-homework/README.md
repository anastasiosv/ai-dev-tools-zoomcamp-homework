# Introduction to AI-Assisted Development 

In this homework, we'll build an application with AI.

You can use any tool you want: ChatGPT, Claude, GitHub Copilot, Codex, Cursor, Antigravity, etc.

With chat-based applications you will need to copy code back-and-forth, so we recommend that you use an AI assistant in your IDE with agent mode.

We will build a TODO application in Django.

The app should be able to do the following:

- Create, edit and delete TODOs 
- Assign due dates
- Mark TODOs as resolved

You will only need Python to get started (we also recommend that you use `uv`).

You don't need to know Python or Django for doing this homework.


## Question 1: Install Django

We want to install Django. Ask AI to help you with that.

What's the command you used for that?

**Answer:** `uv pip install django`

There could be multiple ways to do it. Put the one that AI suggested in the homework form.


## Question 2: Project and App

Now we need to create a project and an app for that.

Follow the instructions from AI to do it. At some point, you will need to include the app you created in the project.

What's the file you need to edit for that?

**Answer:** `settings.py`

- `settings.py` ✓
- `manage.py`
- `urls.py`
- `wsgi.py`

**Note:** We added `'todos'` to the `INSTALLED_APPS` list in `todo_project/settings.py`.


## Question 3: Django Models

Let's now proceed to creating models - the mapping from python objects to a relational database. 

For the TODO app, which models do we need? Implement them.

**Answer:** We created a single `Todo` model in `todos/models.py` with the following fields:
- `title` (CharField, max_length=200)
- `description` (TextField, optional)
- `due_date` (DateField, optional)
- `resolved` (BooleanField, default=False)
- `created_at` (DateTimeField, auto_now_add=True)

What's the next step you need to take?

**Answer:** Run migrations

- Run the application
- Add the models to the admin panel
- Run migrations ✓
- Create a makefile

**Note:** After defining the model, we ran:
```bash
python manage.py makemigrations todos
python manage.py migrate
```


## Question 4. TODO Logic

Let's now ask AI to implement the logic for the TODO app. Where do we put it? 

**Answer:** `views.py`

- `views.py` ✓
- `urls.py`
- `admin.py`
- `tests.py`

**Note:** We implemented class-based views in `todos/views.py`:
- `TodoListView` - List all TODOs
- `TodoDetailView` - View a single TODO
- `TodoCreateView` - Create a new TODO
- `TodoUpdateView` - Update an existing TODO
- `TodoDeleteView` - Delete a TODO
- `TodoToggleResolvedView` - Toggle the resolved status

We also created `todos/urls.py` to map URLs to these views and included it in the main project's `urls.py`.


## Question 5. Templates

Next step is creating the templates. You will need at least two: the base one and the home one. Let's call them `base.html` and `home.html`.

**Answer:** We created:
- `templates/base.html` - Base template (project-level)
- `todos/templates/todos/todo_list.html` - List view template
- `todos/templates/todos/todo_detail.html` - Detail view template
- `todos/templates/todos/todo_form.html` - Form template (for create and update)
- `todos/templates/todos/todo_confirm_delete.html` - Delete confirmation template

Where do you need to register the directory with the templates? 

**Answer:** `TEMPLATES['DIRS']` in project's `settings.py`

- `INSTALLED_APPS` in project's `settings.py`
- `TEMPLATES['DIRS']` in project's `settings.py` ✓
- `TEMPLATES['APP_DIRS']` in project's `settings.py`
- In the app's `urls.py`

**Note:** We set `'DIRS': [BASE_DIR / 'templates']` in `todo_project/settings.py` to register the project-level templates directory. App-specific templates are automatically discovered via `'APP_DIRS': True`.

## Question 6. Tests

Now let's ask AI to cover our functionality with tests.

- Ask it which scenarios we should cover
- Make sure they make sense
- Let it implement it and run them 

Probably it will require a few iterations to make sure that tests pass and evertyhing is working. 

What's the command you use for running tests in the terminal? 

**Answer:** `python manage.py test`

- `pytest`
- `python manage.py test` ✓
- `python -m django run_tests`
- `django-admin test`

**Note:** We created comprehensive tests in `todos/tests.py` covering:
- Model tests (creation, string representation, default values)
- View tests (list, detail, create, update, delete, toggle resolved)
- All 14 tests pass successfully

## Running the app

Now the application is developed and tested. Run it:

```bash
python manage.py runserver
```

Since we asked AI to test everything, it should just work. If it doesn't, iterate with AI until it works.

**Note:** The application is accessible at `http://127.0.0.1:8000/` (redirects to `/todos/`). 


## Homework URL

Commit your code to GitHub. You can create a repository for this course. Within the repository, create a folder, e.g. "01-todo", where you put the code.

Use the link to this folder in the homework submission form.

**Note:** This project is located in the `01-homework` folder within the repository: `https://github.com/anastasiosv/ai-dev-tools-zoomcamp-homework` 


## Tip

You can copy-paste the homework description into the AI system of your choice. But make sure you understand (and follow) all the steps in the response.


## Submission

Submit your homework here: https://courses.datatalks.club/ai-dev-tools-2025/homework/hw1


## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public". 

Learning in public is one of the most effective ways to accelerate your growth. Here's why:

1. Accountability: Sharing your progress creates commitment and motivation to continue
2. Feedback: The community can provide valuable suggestions and corrections
3. Networking: You'll connect with like-minded people and potential collaborators
4. Documentation: Your posts become a learning journal you can reference later
5. Opportunities: Employers and clients often discover talent through public learning

Don't worry about being perfect. Everyone starts somewhere, and people love following genuine learning journeys!

### Example post for LinkedIn:

--- 
🚀 Week 1 of AI Dev Tools Zoomcamp by @DataTalksClub complete!

Just built a Django TODO application using AI assistants - without knowing Django beforehand!

Today I learned how to:

- ✅ Set up Django projects and apps
- ✅ Create database models and migrations
- ✅ Implement views and templates
- ✅ Write comprehensive tests with AI help

Here's my repo: <LINK>

Following along with this amazing course - who else is exploring AI development tools? 

You can sign up here: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/

---

### Example post for Twitter/X:

---

🤖 Built a Django app with AI in @Al_Grigor's AI Dev Tools Zoomcamp!

- ✨ TODO app from scratch
- 📝 Models & migrations
- 🎨 Views and templates
- ✅ Tests

My repo: <LINK>

Zero Django knowledge → working app in one session!

Join me: https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/

---

