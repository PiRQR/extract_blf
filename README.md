# extract_blf
extract_blf script can convert .blf log file to .txt or .csv, .dbc file can be imported to get can msg and data
---
1. ARGUMENTS
- (-db) : .dbc file to import for extract can log file
- (-blf) : .blf file to convert
- (-csv) : .csv file to save your blf extract
- (-outfile) : by default, extract will be done in out.txt file but outfile can save the extract in another file
- (-logs) : to display what is happening while extracting blf

2. HOW TO USE EXTRACT BLF
- python extractBLF -h
- python extractBLF -blf BLF_FILE.blf
- python extractBLF -blf BLF_FILE.blf -outfile FILE_TO_SAVE_EXTRACT.txt