import re

# Read the original file
with open('C:\\Users\\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original file size:", len(content), "characters")

# Find the end of the first complete 3D viewer functionality (around line 3944)
end_of_3d_functionality = content.find("alert('Launching AR View")
if end_of_3d_functionality != -1:
    # Find the closing braces of the function
    end_brace = content.find("            }", end_of_3d_functionality)
    if end_brace != -1:
        # Find the closing </script> tag after the 3D functionality
        script_close = content.find("</script>", end_brace)
        if script_close != -1:
            # Move to end of the script tag
            script_close += len("</script>")
            
            # Find the first structured data section after 3D functionality
            structured_start = content.find("<!-- Structured Data for SEO -->", script_close)
            if structured_start != -1:
                # Find the end of the first structured data script
                structured_end = content.find("</script>", structured_start) + len("</script>")
                
                # Find the first scripts section
                scripts_start = content.find("<!-- Scripts -->", structured_end)
                if scripts_start != -1:
                    # Find the end of the first animation script section
                    animation_script_start = content.find("<!-- Animation Script -->", scripts_start)
                    if animation_script_start != -1:
                        # Find the closing of this first animation script
                        # Look for the corresponding closing </script>
                        script_tag_start = content.find("<script>", animation_script_start)
                        if script_tag_start != -1:
                            # Find the matching closing </script> tag for this animation script
                            # We'll search for the pattern that ends this specific script block
                            next_structured_data = content.find("<!-- Structured Data for SEO -->", animation_script_start + 100)
                            if next_structured_data != -1:
                                # Keep content up to the next structured data (which marks start of duplicates)
                                essential_content = content[:next_structured_data]
                                
                                # Find the original footer from the end of the file
                                original_footer_start = content.rfind("<footer")
                                if original_footer_start != -1:
                                    original_footer = content[original_footer_start:]
                                    
                                    # Combine the essential content with the original footer
                                    fixed_content = essential_content + original_footer
                                    
                                    # Write the fixed content
                                    with open('C:\\Users\Dhanush s v\\Desktop\\Aepl final 1\\Aepl final\\aero 2\\services_clean_fixed.html', 'w', encoding='utf-8') as f:
                                        f.write(fixed_content)
                                    
                                    print("Fixed file created as services_clean_fixed.html")
                                    print("Fixed file size:", len(fixed_content), "characters")
                                    print("Reduced by:", len(content) - len(fixed_content), "characters")
                                    print("Successfully removed duplicate script sections!")
                                else:
                                    print("Could not find original footer")
                            else:
                                print("Could not find next structured data (duplicate marker)")
                        else:
                            print("Could not find script tag start")
                    else:
                        print("Could not find animation script section")
                else:
                    print("Could not find scripts section")
            else:
                print("Could not find structured data section")
        else:
            print("Could not find script closing tag")
    else:
        print("Could not find closing brace")
else:
    print("Could not find 3D viewer functionality")