# pyndianizer
Tool that turns hex numbers to little endian; to help writing payloads for exploiting

### usage:
`pyndianizer.py 0xbebafecabebafeca` ==outputs==> `\xca\xfe\xba\xbe\xca\xfe\xba\xbe`

### where to:
`echo "{shellcode}$(python pyndianizer.py 0xbaaddeadfabadaca)" | bufferoverflowbinary`
