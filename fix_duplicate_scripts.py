#!/usr/bin/env python3
import re

# Read the original file
with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original file size:", len(content), "characters")

# Find the end of the first complete 3D viewer functionality 
end_of_3d_functionality = content.find("alert('Launching AR View")
if end_of_3d_functionality != -1:
    # Go back to find the closing brace of the main 3D viewer function
    # Find the line with "}  </script>" after the 3D functionality
    search_start = end_of_3d_functionality
    # Find the end of the 3D viewer function - look for the closing brace
    closing_brace = -1
    for i in range(search_start, len(content)):
        if content[i:i+13] == '            }':
            # Check if the next few characters contain </script>
            if '</script>' in content[i:i+20]:
                closing_brace = i
                break
    
    if closing_brace != -1:
        # Find the end of the first complete script section including the closing tag
        script_end = content.find('</script>', closing_brace) + len('</script>')
        
        # Now, find the first structured data section and its script
        structured_start = content.find("<!-- Structured Data for SEO -->", script_end)
        if structured_start != -1:
            structured_script_end = content.find('</script>', structured_start) + len('</script>')
            
            # Find the first scripts section and animation script
            scripts_header = content.find("<!-- Scripts -->", structured_script_end)
            if scripts_header != -1:
                animation_script_start = content.find("<!-- Animation Script -->", scripts_header)
                if animation_script_start != -1:
                    # Find the closing of the animation script
                    # Look for the next </script> after the animation script starts
                    animation_script_end = content.find('</script>', animation_script_start) + len('</script>')
                    
                    # Now find where the duplicate scripts start - 
                    # look for the next "Mobile navigation functionality" after our content
                    duplicate_start = content.find("Mobile navigation functionality", animation_script_end)
                    
                    if duplicate_start != -1:
                        # Extract the essential content (up to but not including duplicates)
                        essential_content = content[:duplicate_start]
                        
                        # Find the original footer (the last occurrence of <footer in the file)
                        footer_start = content.rfind('<footer')
                        if footer_start != -1:
                            original_footer = content[footer_start:]
                            
                            # Combine the essential content with the original footer
                            fixed_content = essential_content + original_footer
                            
                            # Write the fixed content
                            with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services_optimized.html', 'w', encoding='utf-8') as f:
                                f.write(fixed_content)
                            
                            print("Optimized file created as services_optimized.html")
                            print("Fixed file size:", len(fixed_content), "characters")
                            print("Reduced by:", len(content) - len(fixed_content), "characters")
                            print("Successfully removed duplicate script sections!")
                            print("Duplicate removal was successful!")
                        else:
                            print("Could not find original footer in file")
                    else:
                        print("Could not find duplicate scripts start position")
                else:
                    print("Could not find animation script section")
            else:
                print("Could not find scripts section")
        else:
            print("Could not find structured data section")
    else:
        print("Could not find closing brace of 3D viewer function")
else:
    print("Could not find 3D viewer functionality")
