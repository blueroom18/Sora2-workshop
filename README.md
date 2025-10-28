# Sora2-workshop

blueroom's notes and works for Sora2 guideline prompt generation.

## Description

This project provides a Python-based tool to interactively generate detailed guideline prompts for Sora2 video generation. The tool reads predefined attributes from `Tools/attributions.txt` and prompts the user to input details for each attribute, then configures shots and additional requirements to produce a structured prompt file.

## Features

- **Interactive Input Collection**: Prompts users for details on various video attributes like duration, lighting, framing, etc.
- **Shot Configuration**: Allows users to specify multiple shots with names, durations, descriptions, and movements.
- **Output Generation**: Saves the generated prompt to a `.txt` file in the `Prompts/` directory.
- **Modular Design**: Easy to extend with new attributes or configurations.

## Installation

1. Ensure you have Python 3.6+ installed.
2. Clone or download this repository.
3. (Optional) Create a virtual environment:

   ```bash
   python -m venv .venv
   # Activate the virtual environment (Windows: .venv\Scripts\activate)
   ```
4. No additional dependencies are required as the script uses only standard library modules.

## Usage

1. Navigate to the project root directory.
2. Run the script:

   ```bash
   python Tools/Sora2_guideline_prompt_gen.py
   ```

3. Follow the interactive prompts to enter details for each attribute.
4. Configure the number of shots and their details.
5. Optionally add additional requirements.
6. The generated prompt will be saved to `Prompts/sora2_guideline_prompt_1.txt`.

## File Structure

- `README.md`: This file.
- `Prompts/`: Directory containing example prompts and generated outputs.
- `Tools/`: Contains the main script and attribute definitions.
  - `Sora2_guideline_prompt_gen.py`: The main Python script.
  - `attributions.txt`: List of attributes with descriptions.
- `Videos/`: (Presumably for video outputs or examples, currently empty.)

## Contributing

Feel free to submit issues or pull requests for improvements.

## License

[Specify license if applicable, e.g., MIT]
