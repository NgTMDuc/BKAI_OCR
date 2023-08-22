# print("Hello World!")
from utils.basic_arg import obtain_args
from data_loader.dataset import HandWritttenDataset
# print("Hello World!")

def main(args):
    label_train = args.label_train
    print(label_train)
if __name__ == "__main__":
    args = obtain_args()
    for name, value in args._get_kwargs():
        print('{:16} : {:}'.format(name, value))
    # label_train = args._get_args()
    main(args)