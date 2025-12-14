#!/usr/bin/env python3
import re

# Read the original file
with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original file size:", len(content), "characters")

# Find the location of the first complete script block (3D viewer + its related scripts)
# The 3D viewer ends after the alert function and has a specific structure
end_of_3d_functionality = content.find("alert('Launching AR View\\nIn a real implementation, this would activate AR functionality.');")
if end_of_3d_functionality != -1:
    # Find the end of that function block - look for the closing braces
    # First find '            }' after the alert
    first_closing_brace = content.find('            }', end_of_3d_functionality)
    if first_closing_brace != -1:
        # Then find next '        });' that closes the document.addEventListener
        closing_document_event = content.find('        });', first_closing_brace)
        if closing_document_event != -1:
            # Then find the closing </script> tag
            script_close = content.find('</script>', closing_document_event) + len('</script>')
            
            # Now find the first structured data section and script ending
            structured_start = content.find('<!-- Structured Data for SEO -->', script_close)
            if structured_start != -1:
                structured_end = content.find('</script>', structured_start) + len('</script>')
                
                # Find the first <!-- Scripts --> section and its related content
                first_scripts_section = content.find('<!-- Scripts -->', structured_end)
                if first_scripts_section != -1:
                    # Find where the first animation script ends - look for the </script> after <!-- Animation Script -->
                    animation_script_start = content.find('<!-- Animation Script -->', first_scripts_section)
                    if animation_script_start != -1:
                        # Find the </script> that ends the first animation script
                        animation_script_end = content.find('</script>', animation_script_start) + len('</script>')
                        
                        # Now find the second occurrence of the entire script pattern (this will be the duplicate)
                        # Look for the next <!-- Scripts --> after our first animation script end
                        next_scripts_section = content.find('<!-- Scripts -->', animation_script_end)
                        if next_scripts_section != -1:
                            # Find the original footer from the very end of the original file
                            # But first, let's find the real end of the first complete section
                            # Find the next "Mobile navigation functionality" after our first animation script  
                            next_mobile_nav = content.find("Mobile navigation functionality", animation_script_end)
                            
                            # Since we know there are 2 instances, let's find both positions
                            all_mobile_positions = []
                            start_pos = 0
                            while True:
                                pos = content.find("Mobile navigation functionality", start_pos)
                                if pos == -1:
                                    break
                                all_mobile_positions.append(pos)
                                start_pos = pos + 1
                            
                            if len(all_mobile_positions) >= 2:
                                # The second occurrence marks the beginning of duplicate scripts
                                duplicate_start = all_mobile_positions[1]
                                
                                # Find the original footer from the original file
                                original_footer_start = content.rfind('<footer')
                                if original_footer_start != -1:
                                    original_footer = content[original_footer_start:]
                                    
                                    # Create fixed content: up to duplicate start + original footer
                                    fixed_content = content[:duplicate_start] + original_footer
                                    
                                    # Write the fixed content
                                    with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services_fixed_correctly.html', 'w', encoding='utf-8') as f:
                                        f.write(fixed_content)
                                    
                                    print("Corrected file created as services_fixed_correctly.html")
                                    print("Original file size:", len(content), "characters")
                                    print("Fixed file size:", len(fixed_content), "characters")
                                    print("Reduced by:", len(content) - len(fixed_content), "characters")
                                    print("Successfully removed duplicate script sections!")
                                else:
                                    print("Could not find original footer")
                            else:
                                print("Could not find multiple mobile navigation functionality instances")
                        else:
                            print("Could not find next scripts section (duplicate)")
                    else:
                        print("Could not find animation script section")
                else:
                    print("Could not find first scripts section")
            else:
                print("Could not find structured data section")
        else:
            print("Could not find document event closing")
    else:
        print("Could not find first closing brace")
else:
    print("Could not find 3D viewer alert function")