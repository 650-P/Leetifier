from hashlib import md5
import random,argparse


the_leet_book={
    'a':['a','4','4'],
    'e':['e','3','3'],
    'i':['i','1','l','1','l'],
    'l':['l','1','I','1','I'],
    'o':['o','0','0'],
    's':['s','5','5'],
    't':['t','7','7'],
    'z':['z','2','2'],
    'A':['A','4','4'],
    'E':['E','3','3'],
    'I':['I','1','l','1','l'],
    'l':['l','1','I','1','I'],
    'O':['O','0','0'],
    'S':['S','5','5'],
    'T':['T','7','7'],
    'Z':['Z','2','2'],
    '1':['1','I','l','I','l'],
    '2':['2','z','Z','z','Z'],
}



def seed(text:str,times):
    random.seed(int(md5(text.encode()).hexdigest(),16)+times)

def leetify(get_leet:str,times):
    seed(get_leet,times)
    for i in range(len(get_leet)):
        if get_leet[i] in the_leet_book.keys():
            get_leet=get_leet.replace(get_leet[i],random.choice(the_leet_book[get_leet[i]]),1)
    return get_leet

def writeOutput(leeted,output):
    if output is not None:
        output.write('\n'.join(leeted))
    else:
        print('\n'.join(leeted))

def generateLeetifiedStrings(inputStrings,times):
    output=[]
    for i in inputStrings:
        for j in range(times):
            output.append(leetify(i,j))
    return output

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('plaintext',nargs='?', type=str,help='string to leetify')
    parser.add_argument('-i', '--infile',  type=argparse.FileType('r'), help='batch leetify string from input file, one string on one line')
    parser.add_argument('-o', '--outfile' , type=argparse.FileType('w'), help='output file')
    parser.add_argument('-r', '--repeat',type=int,help='leetify the string X times')
    args=parser.parse_args()
    inputStrings=[]
    if args.plaintext is None and args.infile is None:
        print("You need to specify a string or a input file to leetify.")
        exit(0)
    if args.plaintext is not None and args.infile is not None:
        print("You can only input from either command argument or file, not both")
    if args.plaintext is not None:
        inputStrings=[args.plaintext]
    else:
        temp=args.infile.read()
        inputStrings=[i.strip() for i in temp.split("\n")]
    if args.repeat is not None:
        if args.repeat<=0:
            print(f"Hi there, you cannot repeat {args.repeat} times.")
            exit()
    else:
        args.repeat=1

    writeOutput(generateLeetifiedStrings(inputStrings,args.repeat),args.outfile)


if __name__=="__main__":    
    main()

