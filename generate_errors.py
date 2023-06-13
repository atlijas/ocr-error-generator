from utils.noise_to_corpus import noise_corpus
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-c', '--corpus', help='A directory containing the files to be noised')
parser.add_argument('-o', '--output', help='A directory to write the noised files to')
parser.add_argument('-f', '--min-error-freq', help='The minimum frequency of an error to be considered', default=1, type=int)
parser.add_argument('-i','--intensity', help='The intensity of the noise', default=1, type=int)
args = parser.parse_args()


if __name__ == '__main__':
    noise_corpus(args.corpus, args.output, min_error_freq=args.min_error_freq, intensity=args.intensity)