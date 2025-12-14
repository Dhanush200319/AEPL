#!/usr/bin/env python3
import re

# Read the original file
with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original file size:", len(content), "characters")

# Find the end of the 3D viewer functionality - find the pattern that ends it
pattern = "Launching AR View"
end_pos = content.find(pattern)
if end_pos != -1:
    # Find the closing braces after this point: first '            }' then '        });' then '    </script>'
    pos_after_alert = end_pos + len(pattern)
    
    # Look for the specific closing pattern
    closing_pos1 = content.find('            }', pos_after_alert)
    if closing_pos1 != -1:
        closing_pos2 = content.find('        });', closing_pos1) 
        if closing_pos2 != -1:
            script_end_pos = content.find('    </script>', closing_pos2) + len('    </script>')
            
            if script_end_pos != -1:
                # Now find the first complete script section (3D + structured data + essential scripts)
                # Find the end of the first structured data script
                structured_start = content.find('<!-- Structured Data for SEO -->', script_end_pos)
                if structured_start != -1:
                    structured_end = content.find('</script>', structured_start) + len('</script>')
                    
                    # Find the first main scripts section
                    main_scripts_start = content.find('<!-- Scripts -->', structured_end)
                    if main_scripts_start != -1:
                        # Find the end of the main scripts + animation script
                        animation_script_start = content.find('<!-- Animation Script -->', main_scripts_start)
                        if animation_script_start != -1:
                            # Find all occurrences of "Mobile navigation functionality" to identify duplicates
                            all_mobile_nav_positions = []
                            start = 0
                            while True:
                                pos = content.find("Mobile navigation functionality", start)
                                if pos == -1:
                                    break
                                all_mobile_nav_positions.append(pos)
                                start = pos + 1

                            if len(all_mobile_nav_positions) > 1:
                                # Take the second occurrence as the start of duplicates
                                next_mobile_nav = all_mobile_nav_positions[1]

                                # Find the original footer to append
                                footer_pos = content.rfind('<footer')
                                if footer_pos != -1:
                                    # Create fixed content: up to the duplicate start + original footer
                                    essential_content = content[:next_mobile_nav]
                                    original_footer = content[footer_pos:]
                                    fixed_content = essential_content + original_footer

                                    # Write the fixed content
                                    with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services_optimized.html', 'w', encoding='utf-8') as f:
                                        f.write(fixed_content)

                                    print("Optimized file created as services_optimized.html")
                                    print("Fixed file size:", len(fixed_content), "characters")
                                    print("Reduced by:", len(content) - len(fixed_content), "characters")
                                    print("Successfully removed duplicate script sections!")
                                else:
                                    print("Could not find original footer")
                            else:
                                print("Could not find duplicate Mobile navigation functionality - only found one instance")
                        else:
                            print("Could not find animation script")
                    else:
                        print("Could not find main scripts section")
                else:
                    print("Could not find structured data section")
            else:
                print("Could not find script end position")
        else:
            print("Could not find closing pattern 2")
    else:
        print("Could not find closing pattern 1")
else:
    print("Could not find alert pattern")