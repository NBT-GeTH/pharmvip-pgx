# pharmvip-pgx

workflow to analysis PGx module.
## Setup

### Dependencies
*   Python 3.8+.
*   [pandas 1.2.4](https://pandas.pydata.org/)
*   [BEDTools 2.27+](https://github.com/arq5x/bedtools2/releases)

## Usage 

1. Filter VCF file with range of selected genes before run VEP software.
- input : list gene that interested (CPIC2019.txt,FDA2017.txt,KoreanHan2017.txt,PGxGamazon2012.txt,PharmGKBClinical.txt,TruGenome.txt,Drugbank515.txt,PGRNseq2016.txt,PharmGKBVIP66.txt,iPLEXPGx.txt)
- output : output.filtered.vcf.gz

```shell
python PGxgenelist.py ${params.geneList} path/to/pgx_resource > filtergene.txt
python PGxgenerange2.py filtergene.txt GRCh38_range_Gene.bed > tmprange.bed
bedtools sort -i tmprange.bed > tmprange_sort.bed
bedtools merge -i tmprange_sort.bed > filterrange.bed  
tabix -p vcf ${vcfGzFile}
tabix -h -R filterrange.bed  ${vcfGzFile} > ${output}.filtered.vcf
bgzip -c ${output}.filtered.vcf > ${output}.filtered.vcf.gz
```

2. Run VEP software for result annotation and prepare to run lolliplot
- input : output.filtered.vcf.gz filtergene.txt
- output : output.VEPfilter.txt pgx_results_for_lolliplot.txt
```shell
 vep --cache --offline \
            --use_transcript_ref \
            --refseq \
            --species homo_sapiens \
            --assembly GRCh38 \
            --dir_cache ${vepDataCache} \
            --fasta ${referenceFasta_HumanGenome} \
            --fork ${task.cpus} \
            --no_stats \
            --input_file output.filtered.vcf.gz \
            --output_file stdout \
            --tab \
            --variant_class \
            --sift b \
            --polyphen b \
            --humdiv \
            --symbol \
            --uniprot \
            --check_existing \
            --protein \
            --total_length \
            --canonical \
            --biotype \
            --pick \
            --coding_only \
            --no_intergenic \
            --fields "Uploaded_variation,Location,Allele,Gene,Feature,Feature_type,ENSP,SWISSPROT,SYMBOL,CANONICAL,BIOTYPE,Consequence,STRAND,cDNA_position,CDS_position,Protein_position,Amino_acids,Codons,Existing_variation,IMPACT,VARIANT_CLASS,SIFT,PolyPhen" \
            | filter_vep --format tab -filter "SYMBOL in filtergene.txt" --output_file ${output}.VEPfilter.txt
            python PGx_for_lolliplot.py ${output}.VEPfilter.txt pgx_results_for_lolliplot.txt
```
3. Prepare result of VEP file for lolliplot script.
- input : pgx_results_for_lolliplot.txt
- output : folder/Lolliplot

```shell
python PGx_lolliplot.py pgx_results_for_lolliplot.txt path/to/pgx_resource
```
