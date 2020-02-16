# Blast output filtering
Python script to filter blast results

Script to filter  BLAST results. 

The input blast files is as following:

query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, query length, subject length (Fields 0			1			2 				3   		4   			5   	6   		7  		8  		9     10 		11 			12  			13)

### Usage

$ python filter_blastn_uparse_pipeline.py -i input_fle -p 90 (default) -e 0.001 (default) -c 60 (default) -a 200 (default)  -o output_filename



