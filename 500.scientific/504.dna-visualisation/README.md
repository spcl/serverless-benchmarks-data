
**Data**

For input, we use the FASTA file for Bacillus subtilis QB92, as in the original [DNAVisualization](https://github.com/Benjamin-Lee/DNAvisualization.org/) project.

Source: https://www.ncbi.nlm.nih.gov/nuccore/CP003783

Compared to the original file, it has been changed to have 80 characters per line:

```
seqtk seq -l 80 sequence.fasta > bacillus_subtilis.fasta
```

