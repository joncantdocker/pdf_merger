# pdf merging tool
import PyPDF2
import os
import argparse

def merge_pdf(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def split_pdf(pdf_list, page, output_path):
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))
        with open(output_path, 'wb') as f:
            pdf_writer.write(f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge PDF files')
    parser.add_argument('--action', type=str, default='merge', help='Action to perform (merge, split)')
    parser.add_argument('pdf_list', type=str, nargs='+', help='List of PDF files to merge')
    parser.add_argument('--page', type=int, default=1, help='Page number to split PDF')
    parser.add_argument('--output', type=str, default='merged.pdf', help='Output PDF file')
    args = parser.parse_args()
    if args.action == 'merge':
        print('Merging PDF')
        merge_pdf(args.pdf_list, args.output)
    elif args.action == 'split':
        print('Splitting PDF')
        split_pdf(args.pdf_list, args.page, args.output)
    else:
        print('Invalid action')