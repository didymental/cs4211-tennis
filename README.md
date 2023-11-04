- betting_csv_files folder contains existing MDP_pred.csv (that can be fed into Prof Jiang Kan's betting script)

Steps to perform PCSP generation + generation of CSV file

1. model.txt is the base model to be used. Do not touch the probabilities (e.g. p1_1, p2_13, etc) and do not touch (#define P1_STAMINA = 7; and P2_STAMINA = 7;) as the script relies on this to correctly generate the .pcsp files.
2. `tennis_dataset.csv` (the big 1.9GB one) should be placed in the same folder as the notebook (not uploaded to git)
3. Use jupyter notebook to run the 2nd last cell in generate_pcsp.ipynb, this will generate 579 pcsp files in the `pcsp_files` folder.
4. Use PAT3.Console.Exe on the CLI (probably with a bash/python script) to run the pcsp on all the generated pcsp files. Note that the pcsp file generated is named with this format `2017-12-31_Alison Riske Amritraj_vs_Qiang Wang.pcsp`, and the corresponding output file (from PAT) should be named `2018-01-01_Anett Kontaveit_vs_Heather Watson.pcsp.txt`, basically the same filename as the pcsp file but with added `.txt` extension at the end. The PAT cli will allow you to express the output file.
5. Once all the output files have generated, cd into `generate_csv` folder here and create a folder called `out`, then put all your output files inside.
6. Run `generate_csv.py` and it will create a file called `test.csv` which includes all your betting probabilities. Go to Jiang Kan's betting script (from his Canvas/Google Drive) and replace `MDP_pred.csv` with the contents of `test.csv` Then you can run his betting simulation script and see the results.
