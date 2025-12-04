#!/bin/bash

echo ">>> Starting the process..."

# Step 1: Run the Python script (this creates the folder)
echo ">>> Running Python script to create folder..."
python3 main-python-program.py

# Step 2: Find the most recently created folder in the current directory
FOLDER_NAME=$(ls -td */ | head -1 | sed 's#/##')

echo ">>> Latest folder detected: $FOLDER_NAME"

# Step 3: Check if the folder exists
if [ -d "$FOLDER_NAME" ]; then
    echo ">>> Folder '$FOLDER_NAME' exists."
    echo ">>> Contents of '$FOLDER_NAME':"
    ls "$FOLDER_NAME"

    # Step 4: Run the inside script
    if [ -f "$FOLDER_NAME/compile_all.sh" ]; then
        echo ">>> Running compile_all.sh inside '$FOLDER_NAME'..."
        chmod +x "$FOLDER_NAME/compile_all.sh"
        bash "$FOLDER_NAME/compile_all.sh"
        echo ">>> See the inside folder and all PDF files have created..... Enjoy 🎉"
    else
        echo "!!! Error: compile_all.sh not found inside $FOLDER_NAME"
        exit 1
    fi
else
    echo "!!! Error: Folder '$FOLDER_NAME' was not found."
    exit 1
fi

echo ">>> Process completed."


