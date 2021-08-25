# pharmvip-pgx

workflow to analysis PGx module.
## Setup

### Dependencies
*   Python 3.8+.
*   [pandas 1.2.4](https://pandas.pydata.org/)
*   BEDTools 2.27+

## Usage 

Create range of selected genes for filter vcf file before run VEP software.

```shell
python PGxgenelist.py GenenameList.txt Pathto/FileGenenameList > filtergene.txt
python PGxgenerange2.py filtergene.txt GRCh38_range_Gene.bed > tmprange.bed
bedtools sort -i tmprange.bed > tmprange_sort.bed
bedtools merge -i tmprange_sort.bed > filterrange.bed  
```
Prepare result of VEP file for lolliplot script.

```shell
python PGx_for_lolliplot.py resultVEP.txt pgx_results_for_lolliplot.txt
python PGx_lolliplot.py pgx_results_for_lolliplot.txt Pathto/PROTEIN_ARCHITECTURE
```
