**Indala.py conversion script**
<br />
<br />
This script converts the "Wiegand" hex value recorded by the Indala long-range reader into the correct hex value to be written to an Indala card (via Proxmark) for cloning.
<br />
<br />
Example:

~~~~
SOUTHPLAZA01:indala eric$ ./indala.py 2005b8272e

Converting Wiegand hex value 2005b8272e to Indala format...
Wiegand 26 bit binary value: 01101110000010011100101110
Checksum ( 5 ) is odd. Adding '01' to bytes 30 and 31.

--Candidate 1 (Try this one first)--
Indala binary value: 0b10010000110000111111011001010001101
Indala hex value to write to card: 4861fb28d

--Candidate 2 (This will probably also work)--
Indala binary value: 0b10010000110000111111011001010010101
Indala hex value to write to card: 4861fb295

Alternate Indala values to try if the above values do not work (these are only used in rare Indala configurations):
4861fb295
4861fb29d

SOUTHPLAZA01:indala eric$
~~~~



To write the card with the Proxmark software, you would use this command: 
~~~~
lf indalaclone 4861fb28d
~~~~
