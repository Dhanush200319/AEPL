#!/usr/bin/env python3
# Script to fix duplicate scripts in services.html

# Read the entire content from the services.html file
with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of the first complete script (3D viewer functionality)
end_of_first_script = content.find("alert('Launching AR View")
if end_of_first_script != -1:
    # Look for the closing of the main 3D viewer function 
    # Find the next structured data section to know where the duplicates start
    next_structured_data = content.find('<!-- Structured Data for SEO -->', end_of_first_script)
    if next_structured_data != -1:
        # Find the end of the first structured data script
        first_structured_data_end = content.find('</script>', next_structured_data) + 9
        # Find the first scripts section
        first_scripts_start = content.find('<!-- Scripts -->', first_structured_data_end)
        if first_scripts_start != -1:
            # Find the end of the first animation script (this is what we want to keep)
            animation_script_start = content.find('<!-- Animation Script -->', first_scripts_start)
            if animation_script_start != -1:
                # Find the end of the first animation script
                first_animation_script_end = content.find('</script>', animation_script_start) + 9
                # Find the second structured data (this indicates the start of duplicates)
                second_structured_data = content.find('<!-- Structured Data for SEO -->', first_animation_script_end)
                if second_structured_data != -1:
                    # We want to keep everything from the beginning until the second structured data start
                    # and then find the footer from the end of the original file
                    final_footer_start = content.rfind('<footer')
                    if final_footer_start != -1:
                        # Get the part to keep (from start to before second duplicate scripts)
                        keep_content = content[:second_structured_data]
                        # Get the footer part from the original file
                        footer_content = content[final_footer_start:]
                        # Combine them
                        fixed_content = keep_content + footer_content
                        
                        # Write the fixed content
                        with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services_fixed.html', 'w', encoding='utf-8') as f:
                            f.write(fixed_content)
                        print("Fixed file created as services_fixed.html")
                        print(f"Original file size: {len(content)} characters")
                        print(f"Fixed file size: {len(fixed_content)} characters")
                    else:
                        print("Could not find footer tag in original file")
                else:
                    print("Could not find second structured data (duplicate marker)")
            else:
                print("Could not find animation script section")
        else:
            print("Could not find scripts section after first structured data")
    else:
        print("Could not find next structured data section")
else:
    print("Could not find 3D viewer script")