import daft

print("Hello World script loaded!")
print(f"Daft version: {daft.__version__}")


def main() -> daft.DataFrame:
    """Simple Hello World example that creates and processes a DataFrame."""
    print("main() function called!")
    print("=" * 60)
    print("Daft Hello World Example")
    print("=" * 60)

    # Create a simple DataFrame
    df = daft.from_pydict({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "age": [25, 30, 35, 28, 32],
        "city": ["New York", "San Francisco", "Chicago", "Boston", "Seattle"],
    })

    print("\nSchema:")
    print(df.schema())

    print("\nOriginal data:")
    print(df.collect())

    # Do some simple transformations
    result = df.with_column(
        "greeting", daft.lit("Hello, ").str.concat(df["name"]).str.concat(daft.lit("!"))
    ).select("greeting", "name", "age", "city")

    print("\nTransformed data with greetings:")
    collected = result.collect()
    print(collected)

    print("\nDone!")
    return collected
