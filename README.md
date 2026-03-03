# Assignment 3: Task Tracker — File I/O

This app is a small personal task tracker — the kind of tool you might build to log your own project work. The display page already works: run the app and visit `/display` to see pre-loaded tasks. Your job is to build the input form so you can add new ones.

The assignment is described below.  For detailed instructional material, be sure to click through https://asbflask.netlify.app/03-forms-file-io/
## Setup

1. Open this project in GitHub Codespaces (or your local environment).
2. Run the app:
   ```
   flask run --debug
   ```
3. Visit `/display` to confirm the pre-loaded tasks appear. Click a project name to see just that project's tasks.

## Assignment Requirements

### Step 1: Draw the system

Run the app and visit `/display`. The table is already working. Before you write any code, draw a diagram — on paper or digitally — that shows how that page gets built.

Your diagram should trace what happens from the moment a browser requests `/display` to the moment it receives a finished HTML page. It needs to include all of these components:

- **`app.py`** — specifically the `display` route
- **`tasks.csv`** — where the data lives
- **`render_template()`** — the hand-off from Python to HTML
- **`base.html`** — the shared page structure
- **`display.html`** — the template that fills it in

Show how these components connect in sequence. Label your arrows. The goal is a drawing that makes it clear what each part does and what order things happen in — not a formal diagram, just one that someone unfamiliar with Flask could follow.

### Step 2: Build the HTML form

Open `templates/input.html`. A `<datalist>` is already set up for project title autocomplete — your job is to build the form that uses it.

Create a `<form>` with `action="/input"` and `method="POST"` containing:

- **project_title** — a text input wired to the datalist: `<input type="text" name="project_title" list="project-suggestions">`
- **title** — a text input
- **description** — a textarea
- **status** — a select dropdown with options: `In Progress`, `Blocked`, `Done`
- **next_steps** — a text input

Add a submit button.

### Step 3: Complete the POST handler

Open `app.py` and complete the POST block inside the `/input` route. You need to:

1. Read each field from `request.form`
2. Generate a datetime stamp: `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`
3. Append a new row to `tasks.csv` using `csv.DictWriter`
4. Redirect to the display page using `redirect(url_for("display"))`

### Step 4: Test it

Submit a task through your form. Check that:
- It appears on `/display`
- The project name is a clickable link that filters to just that project
- The status prompt text in the Next Steps column matches what you selected

### Step 5 (Stretch)

Add a `required` attribute to your form inputs so the browser validates before submitting. Try navigating to `/display/Task+Tracker` directly in the URL bar.

## Hints

- The CSV fieldnames are: `datetime`, `project_title`, `title`, `description`, `status`, `next_steps`
- When opening a file for `csv.DictWriter`, use mode `"a"` (append) and include `newline=""`:
  ```python
  with open("tasks.csv", "a", newline="") as f:
  ```
- Look at the GET-side of `/input` in `app.py` — the CSV is already being read there to build the datalist. Your DictWriter goes in the POST block, which runs only when the form is submitted.
- Every `<input>`, `<textarea>`, and `<select>` **must** have a `name` attribute — that's the key Flask uses in `request.form`.

## What to Submit

Push your completed code to your repository.

