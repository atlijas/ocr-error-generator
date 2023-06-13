# OCR error generator

This repository contains code to generate a synthetic OCRed error dataset, given a parallel corpus of OCRed texts and their corrected counterparts, as well as a dataset of regular texts, into which the errors will be inserted. The errors are extracted from the parallel corpus, and the regular texts are noised with these errors. The resulting dataset can be used to train a model to correct OCRed texts, especially when data is scarce.

Example of what the data might look like:  
**OCRed text**: `Thc guick brown f0x jump5 ov er the lazg dog`  
**Corrected text**: `The quick brown fox jumps over the lazy dog`  
**Regular text**: `Colorless green ideas sleep furiously`  
**Artificially generated OCRed text**: `Colorlcss g r e e n ideassleep furi0usly`

## Usage
First, the error files need to be generated. This is done by running the `prepare_errors.py` script. It takes the following arguments:
- `--ocr`: Path to the OCRed corpus
- `--corrected`: Path to the corrected corpus (parallel to the OCRed corpus)

The structure might look like this:
```
path
│
└───original
│   │   1.txt
│   │   2.txt
└───corrected
    │   1.txt
    │   2.txt
```

The script assumes the files have the same name in both directories, and that the files are completely parallel, i.e. the first file in the `original/` directory is the OCRed version of the first file in the `corrected/` directory, with every line in the former corresponding to a line in the latter. The script will generate the tsv file `errors/all_replacements.tsv` (see the example in `data/`), which is structured as follows:
```
original_characters<tab>replacement_characters<tab>frequency
e<tab>c<tab><tab>3
rn<tab>m<tab><tab>2
...
```
This file is then used to create a SQLite database, `replacements.db` (see the example in `data/`), with a similar structure.

To populate the regular texts with errors, run the `generate_errors.py` script. It takes the following arguments:
- `--corpus`: Path to the corpus of regular texts, which are to be noised with artifical OCR errors (e.g. `dummy_corpus/corrected`)
- `--output`: A directory where the noised texts will be saved (e.g. `dummy_corpus/original`)
- `--min-error-freq`: The minimum frequency of an error in the error database for it to be considered for insertion
- `--intensity`: The intensity of the noise. This number should be experimentally determined. For more information, take a look at `utils/noise_to_text.py`.

There are three different noise types:
- character replacement
- space insertion (two different types)
  - A space inserted between two characters in a token
  - A space be inserted between every characters in a token
- space deletion