import argparse

def obtain_args():
    parser = argparse.ArgumentParser(description='Train Transformer for BKAI Competition',
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--label_train", type = str, nargs= "+", help = "Path to train label file")
    parser.add_argument("--label_eval",  type = str, nargs= "+", help = "Path to eval label file")
    parser.add_argument("--train_folder", type = str, nargs= "+", help = "Path to all image for training")
    parser.add_argument("--eval_folder", type = str,  nargs= "+", help = "Path to the all images for evaluate")
    
    args = parser.parse_args()

    return args
