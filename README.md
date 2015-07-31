# pyndianizer
Tool that turns 32bit hex numbers to little endian; to help writing payloads for exploiting

### usage:
`pyndianizer.py 0xbebafeca` ==outputs==> `\xca\xfe\xba\xbe`

### where to:
`echo "{shellcode}$(python pyndianizer.py 0xbaaddead)" | bufferoverflowbinary`
