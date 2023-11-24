CS4211 Final Submission

# Introduction

This project explores the impact of player fatigue on tennis match performance.
Note that `model.txt` contains the base model for our project. We use placeholder probabilities (e.g. `p1_1`, `p1_2`, `p2_1`, ...) which can be filled in dynamically later. Additionally, note that `MDP_pred.csv` comes directly from Prof Jiang Kan's betting script folder, we use this as a source of match (p1/p2) information.

# Instructions

1. First, place the large 1.9GB+ `tennis_dataset.csv` file into the root folder (same folder as `generate_pcsp.ipynb`)
2. Create a folder called `pcsp_files` in the root project folder, if it does not already exist.
3. Open the `generate_pcsp.ipynb` notebook. The last cell will enable you to generate 579 `.pcsp` PAT model files corresponding to each match.
4. Use PAT CLI to generate the 579 `.txt` output files for each of the 579 `.pcsp` models.
5. Create a folder `./generate_csv/out`, and dump all the `.txt` files outputted by PAT there.
6. Run `python3 ./genreate_csv/generate_csv.py`. This will parse all the files in step 5) and produce `test.csv` results file.
7. You may feed `test.csv` results file into Dr Jiang Kan's betting script to see the betting result.
