from pathlib import Path
import pandas
from argparse import ArgumentParser
from utils.sql.db_setup import FileToSQL
from utils.error_files_setup import write_replacements_to_single_file, create_correct_word_list

parser = ArgumentParser()
parser.add_argument('-o', '--ocr', help='A directory containing the OCR files')
parser.add_argument('-c', '--corrected', help='A directory containing the corrected files')
args = parser.parse_args()


def handle_file(filename):
    file_path = Path(filename)
    if file_path.is_file():
        print(f'> {Path(filename).name} already exists. Overwriting.')
        file_path.unlink()
    else:
        print(f'> Writing to {Path(filename).name}.')



if __name__ == '__main__':
    # correct_words is used to ignore correct words that might appear in the OCR files
    correct_words = create_correct_word_list(args.corrected)
    print('> Setting up files...')
    # Creates a tsv file with the following columns: original, corrected, frequency (without headers)
    write_replacements_to_single_file('errors/all_replacements.tsv',
                                        correct_word_list=correct_words,
                                        ocr_files_path=args.ocr,
                                        corrected_files_path=args.corrected)
    print('> Setting up databases...')
    # This database contains original_string, corrected_string, frequency_of_substitution
    handle_file('errors/replacements.db')
    original_replacement_to_db = FileToSQL(file_to_db='errors/all_replacements.tsv',
                                            db_name='errors/replacements')
    original_replacement_to_db.create_db_orig_corr_freq('REPLACEMENTS',
                                                        'original',
                                                        'replacement',
                                                        'frequency',
                                                        field_separator='\t',
                                                        headers=['original',
                                                                 'replacement',
                                                                 'frequency'])
