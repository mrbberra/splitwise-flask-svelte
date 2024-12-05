# Easy CSV to Splitwise

## Setup

### Requirements

This repo uses [Python](https://www.python.org/) + [Flask](https://flask.palletsprojects.com/en/stable/) for the server and [PNPM](https://pnpm.io/) + [Svelte](https://svelte.dev/) + [Vite](https://vite.dev/) for the client code. I'd also recommend using [venv](https://docs.python.org/3/library/venv.html) or your preferred virtual environment manager for python.

### Building locally

Set up venv dependencies for the server

```bash
# If you're using venv
python -m venv venv
. ./venv/bin/activate

pip install -r requirements.txt
```

Install dependencies and build the client

```bash
cd app/client
pnpm install
pnpm build
```

Then, run the server from this directory with `flask --app app run`
