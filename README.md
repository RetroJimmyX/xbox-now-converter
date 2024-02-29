The purpose of this program is to enable the text copied from the webpage https://www.xbox-now.com/en/deal-list to then be tidied to import to a spreadsheet.

![image](https://github.com/RetroJimmyX/xbox-now-converter/assets/51858595/346a6e5a-c0e0-460a-99c8-26d88d4c96b3)

Steps:
1. Visit https://www.xbox-now.com/en/deal-list in a regular web browser
2. Ensure filters are used and the currency settings to correctly display listings from a desired region.
3. Highlight the bottom listing, hold Shift and highlight the top listing and copy to clipboard.
4. Open up a text file and paste into that text file and save as "try.txt"
5. Execute this Python program (in the same directory as the text file).
6. Save the output to a text file, which can then be imported into spreadsheet software easily.

Notes:
The output values are seperated by ** (not commas)
The website regularly changes its output and formatting so this nuanced script may become obsolete easily
Non-English characters and symbols such as tradmark or regisatered or copyright seem to spit out garbage or crash the program.

When read by line, the file consists of a records with 6-8 lines where each line is a field. An example is below.
The start of each line shows where the data is mapped to.
A * indicates the line may or may not be present and a | divides a field into the options that it may contain

output[0]       The Bard's Tale TrilogyThe Bard's Tale Trilogy

output[4]     * NEW GAME PASS | NEW | GAME PASS

output[3]     * Deal until: 9/17/2799 01:59 UTC | Partly DiscountedUK UK

output[2]       20% (GP)TR Turkey

                11.24 GBP
                
                TR Turkey
                
output[1]       from: 0.64 GBP
                save 94%
