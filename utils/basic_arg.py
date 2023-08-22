import argparse

def obtain_args():
    parser = argparse.ArgumentParser(description='Train Transformer for BKAI Competition',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--train_lists", type = str, nargs= "+", help = "List of file to the dataset")
    parser.add_argument("--eval_lists",  type = str, nargs= "+", help = "List of evaluation list")

    args = parser.parse_args()

    return args
