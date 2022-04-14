# Author: Christopher Reid
# Course: CSC 110
# Description: This program prompts the user for the name of two files; an 'encrypted' .txt file
#               where each line is arranged in a shuffled order from it's original order. The
#               second file is an adjacent .txt file containing the original 'index' of each line
#               in the encrypted .txt file. This program rearranges the lines of each file to
#               reassemble the lines of the encrypted file to their original sequence.

def decryption(text_lines, index_lines):
    """
    This function accepts two parameters; two lists. The lists contain elements of strings
    provided by the content of files retrieved by the user prompt in main().

    The first list contains the elements of a .txt file where each line is in a rearranged order
    from an original sequence.

    The second list contains the original 'indexes' of the lines in the encrypted file. It acts as
    a key to reassemble the encrypted file lines to their original sequence.
    """
    decrypted_lst = []
    for i in range(len(text_lines)):
        decrypted_lst.append('')

    for i in range(len(text_lines)):
        lst_index = int(index_lines[i]) - 1
        decrypted_lst[lst_index] = text_lines[i]

    decrypted_text = open('decrypted.txt', 'w')
    for line in decrypted_lst:
        decrypted_text.write(line)
    decrypted_text.close()

def main():
    text_file = input('Enter the name of an encrypted text file:\n')
    index_file = input('Enter the name of the encryption index file:\n')

    text = open(text_file, 'r')
    text_lines = text.readlines()
    text.close()

    index = open(index_file, 'r')
    index_lines = index.readlines()
    index.close()

    decryption(text_lines, index_lines)

main()