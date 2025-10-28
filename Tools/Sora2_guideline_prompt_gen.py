# Sora2 Guideline Prompt Generator: This is a tool to generate prompts based on Sora2 guidelines by
# human inputs.

from pathlib import Path

def get_attributes():
    """Extract attributes from the given template."""
    attributes = {}
    attr_path = Path(__file__).with_name("attributions.txt")
    with attr_path.open("r", encoding="utf-8") as file:
        for line in file:
            raw_line = line.strip()
            if not raw_line or ":" not in raw_line:
                continue
            # attribution format: key: value  # Chinese explanation
            key, value = raw_line.split(":", 1)
            # Ignore comments after '#'
            value = value.split("#", 1)[0]
            attributes[key.strip()] = value.strip()
    return attributes

def generate_queries(attr_name):
    """Generate queries based on the extracted attributes."""
    return f"Please enter the detail of {attr_name}:"

def get_user_input():
    """Get user input for Sora2 guideline prompt generation."""
    detailed_attributes = {}
    attributes = get_attributes()
    for key in attributes.keys():
        query = generate_queries(key)
        user_input = input(query)
        detailed_attributes[key] = user_input
    return detailed_attributes

def get_shots_config():
    """Get shots configuration from the user."""
    shots_config = {}
    num_shots = int(input("Enter the number of shots: "))
    for i in range(num_shots):
        print(f"Configuring shot {i + 1}:")
        shot_details = {}
        shot_details['Name'] = input("  Enter shot name: ")
        shot_details['Duration'] = input("  Enter duration (in seconds): ")
        shot_details['Description'] = input("  Enter description: ")
        shot_details['Movement'] = input("  Enter movement details: ")
        shots_config[f'Shot {i + 1}'] = shot_details
    return shots_config

def generate_guideline_prompt():
    """Generate a Sora2 guideline prompt based on user parameters."""
    prompt = "Hello, Sora2. I want to generate a video that satisfies the attributions below:\n"
    prompt_component = get_user_input()
    for key, value in prompt_component.items():
        prompt += f"{key}: {value}\n"
    
    print("Now, let's configure the shots for the video.")
    shots_config = get_shots_config()
    for shot_name, shot_details in shots_config.items():
        prompt += f"{shot_name}:\n"
        for key, value in shot_details.items():
            prompt += f"  {key}: {value}\n"
    print("If you have additional requirements, please specify them now. Otherwise, type 'No'.")
    additional_requirements = input("Additional requirements: ")
    if additional_requirements.lower() != 'no':
        prompt += f"Additional requirements: {additional_requirements}\n"
    return prompt

def main():
    """Main function to run the Sora2 guideline prompt generator."""
    guideline_prompt = generate_guideline_prompt()
    file_name = "../Prompts/sora2_guideline_prompt_1.txt"
    with open(file_name, "w") as file:
        file.write(guideline_prompt)
    print(f"Sora2 guideline prompt saved to {file_name}")
    
if __name__ == "__main__":
    main()