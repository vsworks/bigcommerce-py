## Running with uv (package manager)

You can install the `uv` package via pip:

```bash
pip install uv
```

Then use `uv` to execute your script:

```bash
uv run main.py
```

This will run your `main.py` script within the `uv` task environment.

## Configuration

Credentials for BigCommerce (`client_id`, `client_secret`, `store_hash`) are loaded from the `.secrets.toml` file. Copy the `.secrets.toml.example` to `.secrets.toml` and  update them there to change your API credentials.