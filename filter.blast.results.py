__author__ = 'Lidia Montiel & Ramiro Logares'

"""

Script to filter the taxonomy given by BLAST after running the Uparse pipeline. I will filter only based on read quality

The input blast files is as following:

# query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, query length, subject length
	0			1			2 				3   		4   			5   	6   		7  		8  		9     10 		11 			12  			13


#######################################################################

== USAGE ==
$ python filter_blastn_uparse_pipeline.py -i input_fle -p 90 (default) -e 0.001 (default) -c 60 (default) -a 200 (default)  -o output_filename

#######################################################################

"""

import argparse


def calculate_coverage(hit):
	"""Calculates the coverage of each hit by dividing the alignment length [3] by the query length [12]"""
	coverage = (float(hit[3]) / float(hit[12]) * 100)
	return coverage


def main(filename, outputfilename, percent_id, evalue, coverage, al_length):
	"""Performs multiple filtering steps"""
	table_file = open(filename, "r")
	output = open(outputfilename, "w")

	# Define variables
	table_line = ""
	table_list = []
	parsed_line = ""

	# Doing a list of lists from the whole file. Each hit is a list.
	for line in table_file:
		table_line = line.split("\t")
		table_list.append(table_line)

	# Filtering hits by  % of identity, alignment length, coverage and evalue.
	filtered_list = []
	for hit in table_list:
		if float(hit[2]) >= percent_id and int(hit[3]) >= al_length:
			if calculate_coverage(hit) >= coverage and float(hit[10]) <= evalue:
				filtered_list.append(hit)

			# Write the final filtered list of best hits to a new file
	for hit in filtered_list:
		parsed_line = hit
		n = 0
		while n < (len(parsed_line) - 1):
			output.write(parsed_line[n] + "\t")
			n += 1
		output.write(parsed_line[n])

	return


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Script to filter blastn results from the uparse pipeline.")

	parser.add_argument("-i", "--input",
						dest="inputfile",
						action="store",
						default=None,
						help="Input blast tab-separated table file")

	parser.add_argument("-p", "--percent",
						dest="percent_id",
						action="store",
						default=90,
						type=int,
						help="Percentage of identity of BLASTn; default 90%")

	parser.add_argument("-o", "--output",
						dest="outputfilename",
						action="store",
						default="filteredblastn",
						help="Output filename")

	parser.add_argument("-e", "--evalue",
						dest="evalue",
						action="store",
						default=0.001,
						type=float,
						help="E-value; default = 0.001")

	parser.add_argument("-c", "--coverage",
						dest="coverage",
						action="store",
						default=60,
						type=int,
						help="Coverage; default = 60")

	parser.add_argument("-a", "--al_length",
						dest="al_length",
						action="store",
						default=200,
						type=int,
						help="Alignment length; default = 200")

	options = parser.parse_args()
	main(options.inputfile, options.outputfilename, options.percent_id, options.evalue, options.coverage, options.al_length)
